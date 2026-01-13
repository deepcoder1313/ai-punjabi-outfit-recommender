from tensorflow.keras.models import load_model

MODEL_PATH = "models/shirt_type_model.keras"

# Load model once when server starts
shirt_model = load_model(MODEL_PATH)

print("✅ Shirt type model loaded successfully")
