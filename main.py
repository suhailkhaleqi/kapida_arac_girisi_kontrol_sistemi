
from src.detect_vehicle import detect_and_crop
from src.plate_ocr import read_plate
from src.vlm_description import describe_vehicle
from src.decision_engine import decide_access

IMAGE_PATH = "input_images/car_unplash.jpg"
MODEL_PATH = "models/yolov8n.pt"
DB_PATH = "data/authorized_plates.csv"

vehicle_crop, vehicle_class = detect_and_crop(IMAGE_PATH, MODEL_PATH)

plate = read_plate(vehicle_crop)
description = describe_vehicle(vehicle_crop)

access, reason = decide_access(plate, vehicle_class, DB_PATH)

print("Vehicle type:", vehicle_class)
print("Plate:", plate)
print("VLM description:", description)
print("Decision:", reason)
