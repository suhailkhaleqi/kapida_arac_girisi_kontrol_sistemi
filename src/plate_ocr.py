
import cv2
import easyocr

def read_plate(vehicle_crop):
    """
    Extract plate region heuristically and apply OCR
    """
    h, w, _ = vehicle_crop.shape

    plate_candidate = vehicle_crop[
        int(h*0.6):int(h*0.9),
        int(w*0.25):int(w*0.75)
    ]

    gray = cv2.cvtColor(plate_candidate, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    reader = easyocr.Reader(['en'], gpu=True)
    results = reader.readtext(
        gray,
        allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
        detail=0
    )

    if len(results) == 0:
        return None

    return results[0]
