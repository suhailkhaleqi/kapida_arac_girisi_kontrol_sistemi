
from ultralytics import YOLO
import cv2

def detect_and_crop(image_path, model_path):
    """
    Detect vehicle using YOLO and return:
    - cropped vehicle image
    - vehicle class name
    """
    model = YOLO(model_path)
    results = model(image_path)

    box = results[0].boxes.xyxy[0].cpu().numpy().astype(int)
    class_id = int(results[0].boxes.cls[0].item())
    vehicle_class = model.names[class_id]

    img = cv2.imread(image_path)
    x1, y1, x2, y2 = box
    vehicle_crop = img[y1:y2, x1:x2]

    return vehicle_crop, vehicle_class
