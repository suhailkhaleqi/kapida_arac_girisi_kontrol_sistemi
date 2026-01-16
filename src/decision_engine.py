
import pandas as pd

def decide_access(plate, vehicle_type, db_path):
    db = pd.read_csv(db_path)
    authorized = set(db["plate"])

    if plate is None:
        return False, "Plate could not be read"

    if plate not in authorized:
        return False, "Unauthorized plate"

    if vehicle_type == "truck":
        return False, "Truck access denied"

    return True, "Access granted"
