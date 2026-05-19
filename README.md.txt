# Punjabi AI Outfit Recommender 👔✨

An AI-powered fashion recommendation system that suggests:

- Matching pants 👖
- Turban recommendations 🧢
- Punjabi outfit combinations 🇮🇳

based on the uploaded shirt image using Computer Vision and Machine Learning.

---

# 🔥 Features

✅ Upload shirt image  
✅ Detect dominant shirt colors  
✅ Predict shirt type using AI  
✅ Recommend matching pants  
✅ Recommend matching turbans  
✅ Responsive frontend UI  
✅ FastAPI backend API  
✅ React + Vite frontend  
✅ Mobile responsive support  

---

# 🛠️ Tech Stack

## Frontend
- React.js
- Vite
- Swiper.js
- Axios
- CSS3

## Backend
- FastAPI
- Python
- OpenCV
- NumPy
- Pillow

## Deployment
- Netlify (Frontend)
- Render (Backend)

---

# 📂 Project Structure

```bash
outfit_color_ai/
│
├── app/
│   ├── main.py
│   └── api/
│       └── routes/
│           └── recommend.py
│
├── src/
│   ├── color_extraction.py
│   ├── color_matching.py
│   ├── predict_shirt_type.py
│   ├── pant_recommendation.py
│   └── turban_recommendation.py
│
├── data/
│   ├── pant_images/
│   ├── turban_images/
│   └── fitti_images/
│
├── frontend/
│
└── requirements.txt

⚙️ Installation

1️⃣ Clone Repository
git clone https://github.com/your-username/your-repo-name.git
cd outfit_color_ai

2️⃣ Create Virtual Environment
python -m venv venv

Windows
venv\Scripts\activate

3️⃣ Install Backend Dependencies
pip install -r requirements.txt

🚀 Run Backend

From root folder:

uvicorn app.main:app --reload

🚀 Run Frontend

Go to frontend folder:

cd frontend
npm install
npm run dev

🧠 AI Workflow
Upload shirt image
Extract dominant colors
Detect shirt type
Match suitable pant colors
Recommend turban combinations
Display outfit suggestions

👨‍💻 Developer

Sandeep Singh

B.Tech AI & ML Student
Passionate about AI, Computer Vision, and Full Stack Development.

# 🔗 Connect With Me

## GitHub
[GitHub Profile](https://github.com/deepcoder1313)

## LinkedIn
[LinkedIn Profile](https://www.linkedin.com/in/sandeep-singh-781671357/)