import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load trained model
model = tf.keras.models.load_model("models/shirt_type_model.h5")

# IMPORTANT: class order must match training folders
class_names = [
    "casual_shirt",
    "formal_shirt",
    "hoodie",
    "oversized_tshirt",
    "t_shirt"
]

def predict_shirt_type(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    predictions = model.predict(img)
    predicted_index = np.argmax(predictions)

    return class_names[predicted_index]
