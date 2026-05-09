import { useState, useRef } from "react";
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
      spaceBetween={14}
      slidesPerView={1.2}
      breakpoints={{
        0:    { slidesPerView: 1.2 },
        480:  { slidesPerView: 1.5 },
        768:  { slidesPerView: 2 },
        1024: { slidesPerView: 3 },
      }}
      style={{ paddingBottom: "8px" }}
    >
      {images.map((img, i) => (
        <SwiperSlide key={i}>
          <div className="image-card">
            <img src={img} alt="" loading="lazy" />
          </div>
        </SwiperSlide>
      ))}
    </Swiper>
  );
}
console.log(data);

function App() {
  const [file, setFile]       = useState(null);
  const [preview, setPreview] = useState(null);
  const [data, setData]       = useState(null);
  const [loading, setLoading] = useState(false);
  const inputRef              = useRef(null);

  const handleFileChange = (e) => {
    const f = e.target.files[0];
    if (!f) return;
    setFile(f);
    setPreview(URL.createObjectURL(f));
    setData(null);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const f = e.dataTransfer.files[0];
    if (!f || !f.type.startsWith("image/")) return;
    setFile(f);
    setPreview(URL.createObjectURL(f));
    setData(null);
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
        { headers: { "Content-Type": "multipart/form-data" } }
      );
      setData(res.data);
    } catch (err) {
      console.log(err.response);
      alert("Error while calling API");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">

      {/* ── HEADER ── */}
      <header className="header">
        <div className="header-inner">
          <span className="header-logo">✦</span>
          <span className="header-title">Punjabi AI Outfit Recommender</span>
        </div>
      </header>

      <main className="main-layout">

        {/* ── LEFT PANEL ── */}
        <aside className="left-panel">
          <p className="panel-label">Upload your shirt</p>

          {/* Drop zone */}
          <div
            className={`upload-zone ${preview ? "has-preview" : ""}`}
            onClick={() => inputRef.current?.click()}
            onDragOver={(e) => e.preventDefault()}
            onDrop={handleDrop}
          >
            {preview ? (
              <img src={preview} alt="preview" className="preview-img" />
            ) : (
              <div className="upload-placeholder">
                <span className="upload-icon">⬆</span>
                <span className="upload-hint">Click or drag an image here</span>
                <span className="upload-sub">JPG, PNG, WEBP</span>
              </div>
            )}
          </div>

          <input
            ref={inputRef}
            type="file"
            accept="image/*"
            onChange={handleFileChange}
            style={{ display: "none" }}
          />

          {preview && (
            <button
              className="change-btn"
              onClick={() => inputRef.current?.click()}
            >
              Change image
            </button>
          )}

          <button
            className="analyze-btn"
            onClick={handleSubmit}
            disabled={!file || loading}
          >
            {loading ? (
              <span className="btn-loading">
                <span className="spinner" />
                Analyzing…
              </span>
            ) : (
              "Recommend Outfit"
            )}
          </button>
        </aside>

        {/* ── RIGHT PANEL ── */}
        <section className="right-panel">
          {!data && !loading && (
            <div className="empty-state">
              <span className="empty-icon">👔</span>
              <p>Upload a shirt to get personalized outfit recommendations</p>
            </div>
          )}

          {loading && (
            <div className="empty-state">
              <span className="empty-icon pulse">✦</span>
              <p>Analysing your outfit…</p>
            </div>
          )}

          {data && (
            <div className="results-grid fade-in">

              {/* PANTS */}
              {data.pant_images &&
                Object.entries(data.pant_images).map(([type, images]) => (
                  <div key={type} className="section-block">
                    <h3 className="section-title">
                      <span className="section-dot" />
                      {type.replace(/_/g, " ").toUpperCase()}
                    </h3>
                    <ImageSlider images={images} />
                  </div>
                ))}

              {/* TURBANS */}
              {data.turban_images &&
                Object.entries(data.turban_images).map(([color, images]) => (
                  <div key={color} className="section-block">
                    <h3 className="section-title">
                      <span className="section-dot turban" />
                      Turban — {color}
                    </h3>
                    <ImageSlider images={images} />
                  </div>
                ))}

              {/* FITTI */}
              {data.fitti_images && data.fitti_images.length > 0 && (
                <div className="section-block">
                  <h3 className="section-title">
                    <span className="section-dot fitti" />
                    Fitti — {data.fitti_color}
                  </h3>
                  <ImageSlider images={data.fitti_images} />
                </div>
              )}
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
