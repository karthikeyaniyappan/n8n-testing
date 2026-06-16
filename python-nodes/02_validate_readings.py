# Node 2: Validate Readings
# Checks schema, sensor types, and value ranges before downstream processing.

REQUIRED_FIELDS = ["sensor_id", "sensor_type", "raw_value", "unit", "timestamp"]
VALID_TYPES = {"temperature", "humidity", "pressure", "voltage"}
VALUE_RANGES = {
    "temperature": (-50, 150),
    "humidity": (0, 100),
    "pressure": (800, 1200),
    "voltage": (0, 500),
}

results = []

for item in _items:
    data = item["json"]
    readings = data.get("readings", [])
    validated = []
    errors = []

    for index, reading in enumerate(readings):
        missing = [field for field in REQUIRED_FIELDS if field not in reading]
        if missing:
            errors.append({"index": index, "error": f"Missing fields: {missing}"})
            continue

        sensor_type = reading["sensor_type"]
        if sensor_type not in VALID_TYPES:
            errors.append(
                {"index": index, "error": f"Invalid sensor_type: {sensor_type}"}
            )
            continue

        low, high = VALUE_RANGES[sensor_type]
        value = reading["raw_value"]
        if not isinstance(value, (int, float)) or value < low or value > high:
            errors.append(
                {
                    "index": index,
                    "error": f"Value {value} out of range [{low}, {high}]",
                }
            )
            continue

        validated.append({**reading, "valid": True})

    results.append(
        {
            "json": {
                "cycle": data.get("cycle", 0),
                "running": data.get("running", True),
                "stage": "validated",
                "readings": validated,
                "validation_errors": errors,
                "validation_passed": len(errors) == 0,
                "valid_count": len(validated),
                "generated_at": data.get("generated_at"),
            }
        }
    )

return results
