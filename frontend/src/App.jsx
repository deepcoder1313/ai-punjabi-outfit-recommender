import { useState } from "react";
import axios from "axios";

import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation } from "swiper/modules";

import "swiper/css";
import "swiper/css/navigation";
import "./App.css";


function ImageSlider({ images }) {
  if (!images || images.length === 0) return null;

  return (
    <Swiper
      modules={[Navigation]}
      navigation
      spaceBetween={16}
      slidesPerView={3}
      breakpoints={{
        0: { slidesPerView: 1.2 },
        640: { slidesPerView: 2.2 },
        1024: { slidesPerView: 3.2 }
      }}
      style={{ paddingBottom: "12px" }}
    >
      {images.map((img, i) => (
        <SwiperSlide key={i}>
          <div className="image-card">
            <img src={img} alt="" />
          </div>
        </SwiperSlide>
      ))}
    </Swiper>
  );
}


function App() {

  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);


  const handleFileChange = (e) => {
    const f = e.target.files[0];
    if (!f) return;

    setFile(f);
    setPreview(URL.createObjectURL(f));
  };


  const handleSubmit = async () => {

    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const res = await axios.post(
  "https://ai-punjabi-outfit-recommender-4.onrender.com/recommend-outfit",
  formData,
  {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  }
);
      setData(res.data);

    } catch (err) {
  console.log(err.response); // 🔥 important
  alert("Error while calling API");
}
    finally {
      setLoading(false);
    }
  };


  return (
    <div className="app-container">

      {/* ---------------- HEADER ---------------- */}
      <div className="header">
        Punjabi AI Outfit Recommender
      </div>


      <div className="main-layout">

        {/* ---------------- LEFT PANEL ---------------- */}
        <div className="left-panel">

          <h3>Upload your shirt</h3>

          <input
            type="file"
            accept="image/*"
            onChange={handleFileChange}
          />

          {preview && (
            <div className="preview-box">
              <img src={preview} alt="preview" />
            </div>
          )}

          <button
            className="analyze-btn"
            onClick={handleSubmit}
            disabled={!file || loading}
          >
            {loading ? "Analyzing..." : "Recommend outfit"}
          </button>

        </div>


        {/* ---------------- RIGHT PANEL ---------------- */}
        <div className="right-panel">

          {!data && (
            <div className="empty-text">
              Upload an image to see recommendations
            </div>
          )}

          {data && (

            <>
              {/* ---------------- PANTS ---------------- */}
              {data.pant_images &&
                Object.entries(data.pant_images).map(([type, images]) => (
                  <div key={type} className="section-block">
                    <div className="section-title">
                      {type.toUpperCase()}
                    </div>
                    <ImageSlider images={images} />
                  </div>
                ))}


              {/* ---------------- TURBANS ---------------- */}
              {data.turban_images &&
                Object.entries(data.turban_images).map(([color, images]) => (
                  <div key={color} className="section-block">
                    <div className="section-title">
                      Turban – {color}
                    </div>
                    <ImageSlider images={images} />
                  </div>
                ))}


              {/* ---------------- FITTI ---------------- */}
              {data.fitti_images && data.fitti_images.length > 0 && (
                <div className="section-block">
                  <div className="section-title">
                    Fitti – {data.fitti_color}
                  </div>

                  <ImageSlider images={data.fitti_images} />
                </div>
              )}
            </>
          )}

        </div>
      </div>
    </div>
  );
}

export default App;
