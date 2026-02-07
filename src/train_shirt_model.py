import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model

IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 10

# -----------------------------
# Data Augmentation
# -----------------------------
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=15,
    zoom_range=0.2,
    width_shift_range=0.1,
    height_shift_range=0.1,
    brightness_range=[0.7, 1.3],
    horizontal_flip=True,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    "data/shirt_types",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training"
)

val_data = datagen.flow_from_directory(
    "data/shirt_types",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation"
)

# -----------------------------
# Model
# -----------------------------
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)
x = Dropout(0.4)(x)
output = Dense(train_data.num_classes, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=output)

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# -----------------------------
# Training
# -----------------------------
model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS
)

# -----------------------------
# Save Model
# -----------------------------
model.save("models/shirt_type_model.keras")

print("✅ Training completed and model saved")
from src.predict_shirt_type import predict_shirt_type
import os

TEST_DIR = "data/test_images"

for category in os.listdir(TEST_DIR):
    folder_path = os.path.join(TEST_DIR, category)

    print(f"\n🔍 Testing category: {category}")

    for img in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img)
        prediction = predict_shirt_type(img_path)

        print(f"Image: {img}  →  Predicted: {prediction}")
