import os
from predict_shirt_type import predict_shirt_type

TEST_DIR = "data/raw_images"

for class_name in os.listdir(TEST_DIR):
    class_path = os.path.join(TEST_DIR, class_name)

    if not os.path.isdir(class_path):
        continue

    print(f"\n🔍 Testing class: {class_name}")

    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)

        pred = predict_shirt_type(img_path)
        print(f"{img_name} → {pred}")
