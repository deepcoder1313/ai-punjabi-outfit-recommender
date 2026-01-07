import streamlit as st
import os

from src.color_extraction import extract_dominant_color
from src.color_matching import match_colors
from src.predict_shirt_type import predict_shirt_type
from src.pant_recommendation import recommend_pants
from src.celebrity_recommendation import recommend_celebrity_outfits


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Outfit Recommendation",
    page_icon="👔",
    layout="wide"
)

# =========================
# DARK PROFESSIONAL UI (CSS)
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f172a;
    }

    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3 {
        color: #e5e7eb;
        font-weight: 600;
    }

    p, li, span, div {
        color: #cbd5e1;
        font-size: 15px;
    }

    section[data-testid="stFileUploader"] {
        background-color: #111827;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #1f2933;
    }

    img {
        border-radius: 12px;
    }

    .stAlert {
        background-color: #111827;
        border-radius: 10px;
        border: 1px solid #1f2933;
    }

    button {
        background-color: #1f2937 !important;
        color: #e5e7eb !important;
        border-radius: 8px !important;
        border: 1px solid #374151 !important;
    }

    hr {
        border-top: 1px solid #1f2937;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# TITLE
# =========================
st.title("👔 AI Outfit Recommendation System")
st.caption("Upload a shirt image on the left and get outfit recommendations on the right")

st.divider()

# =========================
# MAIN LAYOUT
# =========================
left_col, right_col = st.columns([1, 2])


# =========================
# LEFT SIDE — INPUT
# =========================
with left_col:
    st.subheader("📤 Input")

    uploaded_file = st.file_uploader(
        "Upload a shirt image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image_path = os.path.join("data/raw_images", uploaded_file.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image(image_path, width=350, caption="Uploaded Image")


# =========================
# RIGHT SIDE — OUTPUT
# =========================
with right_col:
    st.subheader("🧠 AI Output")

    if uploaded_file:

        with st.spinner("Analyzing outfit..."):

            # Color extraction
            dominant_rgb = extract_dominant_color(image_path)
            shirt_colors = match_colors(dominant_rgb)

            # Shirt type prediction
            shirt_type = predict_shirt_type(image_path)

            # Pant recommendation
            pant_types, pant_colors = recommend_pants(shirt_type, shirt_colors)

        st.markdown("### 👕 Shirt Analysis")
        st.write("**Shirt Type:**", shirt_type.replace("_", " ").title())
        st.write("**Matching Colors:**", ", ".join(shirt_colors))

        st.markdown("### 👖 Pant Recommendation")

        st.write("**Pant Types:**")
        for pant in pant_types:
            st.write("•", pant.replace("_", " ").title())

        st.write("**Pant Colors:**")
        for color in pant_colors:
            st.write("•", color.title())

        st.markdown("### 🔥 Celebrity Outfit Inspiration")

        celeb_images = recommend_celebrity_outfits(pant_types, pant_colors)

        if celeb_images:
            cols = st.columns(3)
            for i, img in enumerate(celeb_images):
                cols[i % 3].image(img, width=220)
        else:
            st.info("No celebrity inspiration available yet.")

    else:
        st.info("Upload an image to see recommendations.")
