import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose

def extract_shirt_region(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_pose.Pose(static_image_mode=True) as pose:
        results = pose.process(image_rgb)

        if not results.pose_landmarks:
            return None

        h, w, _ = image.shape

        landmarks = results.pose_landmarks.landmark

        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
        right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]

        x1 = int(min(left_shoulder.x, right_shoulder.x) * w)
        x2 = int(max(left_shoulder.x, right_shoulder.x) * w)
        y1 = int(min(left_shoulder.y, right_shoulder.y) * h)
        y2 = int(max(left_hip.y, right_hip.y) * h)

        margin_x = int(0.05 * w)
        margin_y = int(0.05 * h)

        x1 = max(0, x1 - margin_x)
        x2 = min(w, x2 + margin_x)
        y1 = max(0, y1 - margin_y)
        y2 = min(h, y2 + margin_y)

        shirt_crop = image[y1:y2, x1:x2]

        if shirt_crop.size == 0:
            return None

        return shirt_crop
