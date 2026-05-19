import streamlit as st
import os

from src.color_extraction import extract_dominant_color
from src.color_matching import match_colors
from src.predict_shirt_type import predict_shirt_type
from src.pant_recommendation import recommend_pants
from src.turban_recommendation import recommend_turban_and_fitti
from src.fitti_color_mapping import rgb_to_fitti_color
from src.fitti_recommendation import recommend_fitti
from src.turban_images import (
    get_primary_turban_images,
    get_fitti_images
)
from src.pant_images import get_pant_images


# =========================
# HELPER FUNCTION
# =========================
def get_shirt_color_category(rgb):
    avg = sum(rgb) / 3
    if avg > 220:
        return "white"
    elif avg < 90:
        return "dark"
    elif avg > 170:
        return "light"
    else:
        return "pastel"


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Punjabi Outfit Recommendation",
    page_icon="🧢",
    layout="wide"
)

# =========================
# DARK UI
# =========================
st.markdown("""
<style>
.stApp { background-color: #0f172a; }
.block-container { padding-top: 2rem; }
h1, h2, h3 { color: #e5e7eb; }
p, span, div { color: #cbd5e1; }
img { border-radius: 12px; }
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("🧢 AI Punjabi Outfit & Turban Recommendation")
st.caption("Shirt image → Punjabi turban → FITTI balance → Pant style")

st.divider()

# =========================
# LAYOUT
# =========================
left_col, right_col = st.columns([1, 2])

# =========================
# LEFT — INPUT
# =========================
with left_col:
    st.subheader("📤 Upload Shirt Image")

    uploaded_file = st.file_uploader(
        "Choose a shirt image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        os.makedirs("data/raw_images", exist_ok=True)
        image_path = os.path.join("data/raw_images", uploaded_file.name)

        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image(image_path, width=320, caption="Uploaded Shirt")

# =========================
# RIGHT — OUTPUT
# =========================
with right_col:
    st.subheader("🧠 AI Recommendation Output")

    if uploaded_file:
        with st.spinner("Analyzing full Punjabi outfit styling..."):

            # -------- SHIRT COLORS --------
            dominant_rgb, secondary_rgb = extract_dominant_color(image_path)
            shirt_colors = match_colors(dominant_rgb)

            # -------- SHIRT TYPE --------
            shirt_type = predict_shirt_type(image_path)
            shirt_type = shirt_type.lower().replace(" ", "_")

            # -------- SHIRT COLOR CATEGORY --------
            shirt_color_category = get_shirt_color_category(dominant_rgb)

            # -------- TURBAN PRIMARY --------
            turban_result = recommend_turban_and_fitti(
                 secondary_rgb=secondary_rgb
                
            )

            if turban_result.get("turban_colors"):
                primary_turban_color = turban_result["turban_colors"][0]
            else:
                primary_turban_color = "Maroon"  # safe Punjabi fallback

            # -------- FITTI FROM SHIRT --------
            shirt_fitti_color = rgb_to_fitti_color(secondary_rgb)

            final_fitti = recommend_fitti(
                shirt_fitti_color=shirt_fitti_color,
                primary_turban_color=primary_turban_color
            )

            # -------- PANT RECOMMENDATION --------
            pant_types, pant_colors, pant_images = recommend_pants(
            shirt_type,
                  shirt_colors
                           )

            # -------- IMAGES --------
            primary_images = get_primary_turban_images(primary_turban_color)
            fitti_images = get_fitti_images(final_fitti["fitti_color"])
            pant_images = get_pant_images(pant_types, pant_colors)

        # =========================
        # SHIRT SECTION
        # =========================
        st.markdown("### 👕 Shirt Analysis")
        st.write("**Shirt Type:**", shirt_type.replace("_", " ").title())
        st.write("**Shirt Main Colors:**", ", ".join(shirt_colors))

        # =========================
        # PRIMARY TURBAN SECTION
        # =========================
        st.markdown("### 🧢 Primary Turban")
        st.write(f"**Primary Color:** {primary_turban_color}")

        if primary_images:
            cols = st.columns(len(primary_images))
            for i, img in enumerate(primary_images):
                cols[i].image(img, width=220)
        else:
            st.info("No primary turban images found.")

        # =========================
        # FITTI SECTION
        # =========================
        st.markdown("### 🎯 FITTI (Balance Near Face)")

        st.markdown(
            f"""
            <div style="
                background-color:#111827;
                padding:12px;
                border-radius:12px;
                border-left:6px solid #22c55e;
                margin-bottom:12px;
            ">
                <b>Fitti Color:</b> {final_fitti['fitti_color']}<br>
                <small>{final_fitti['reason']}</small>
            </div>
            """,
            unsafe_allow_html=True
        )

        if fitti_images:
            cols = st.columns(len(fitti_images))
            for i, img in enumerate(fitti_images):
                cols[i].image(img, width=180)
        else:
            st.info("No FITTI images found.")

        # =========================
        # PANT SECTION (IMAGES ADDED)
        # =========================
        st.markdown("### 👖 Pant Recommendation")

        st.write("**Pant Types:**")
        for p in pant_types:
            st.write("•", p.replace("_", " ").title())

        st.write("**Pant Colors:**")
        for c in pant_colors:
            st.write("•", c.title())

        if pant_images:
            st.markdown("**Recommended Pant Styles:**")
            cols = st.columns(len(pant_images))
            for i, img in enumerate(pant_images):
                cols[i].image(img, width=200)
        else:
            st.info("No pant images found. Please check pant_styles folder.")

    else:
        st.info("Upload a shirt image to see AI recommendations.")
