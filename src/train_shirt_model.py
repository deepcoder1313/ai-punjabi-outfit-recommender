# =========================
# 1. IMPORT LIBRARIES
# =========================
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model

# =========================
# 2. BASIC SETTINGS
# =========================
IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 8

# =========================
# 3. DATA AUGMENTATION (IMPORTANT)
# =========================
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=15,
    zoom_range=0.1,
    horizontal_flip=True,
    validation_split=0.2
)

# =========================
# 4. TRAIN DATA
# =========================
train_data = train_datagen.flow_from_directory(
    "data/shirt_types",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training"
)

# =========================
# 5. VALIDATION DATA
# =========================
val_data = train_datagen.flow_from_directory(
    "data/shirt_types",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation"
)
# =========================
# 6. LOAD PRETRAINED MODEL
# =========================
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)
# =========================
# 7. FREEZE BASE MODEL
# =========================
base_model.trainable = False

# =========================
# 8. BUILD CUSTOM HEAD
# =========================
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)
x = Dropout(0.3)(x)
output = Dense(train_data.num_classes, activation="softmax")(x)

# =========================
# 9. FINAL MODEL
# =========================
model = Model(inputs=base_model.input, outputs=output)

# =========================
# 10. COMPILE MODEL
# =========================
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
# =========================
# 11. TRAIN MODEL
# =========================
model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS
)

# =========================
# 12. SAVE MODEL
# =========================
model.save("models/shirt_type_model.keras")
print("✅ Model retrained and saved successfully")
