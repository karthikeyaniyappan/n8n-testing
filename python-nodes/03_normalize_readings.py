# Node 3: Normalize Readings
# Applies per-sensor calibration offsets and scaling factors.

NORMALIZATION = {
    "temperature": {"offset": 0, "scale": 1.0},
    "humidity": {"offset": 0, "scale": 1.0},
    "pressure": {"offset": 900, "scale": 0.1},
    "voltage": {"offset": 0, "scale": 0.01},
}

results = []

for item in _items:
    data = item["json"]
    normalized = []

    for reading in data.get("readings", []):
        config = NORMALIZATION[reading["sensor_type"]]
        raw_value = reading["raw_value"]
        normalized_value = round((raw_value - config["offset"]) * config["scale"], 4)
        normalized.append(
            {
                **reading,
                "normalized_value": normalized_value,
                "calibration_applied": True,
            }
        )

    results.append(
        {
            "json": {
                "cycle": data.get("cycle", 0),
                "running": data.get("running", True),
                "stage": "normalized",
                "validation_passed": data.get("validation_passed", False),
                "valid_count": data.get("valid_count", 0),
                "validation_errors": data.get("validation_errors", []),
                "readings": normalized,
            }
        }
    )

return results
