# Node 1: Generate Sensor Data
# Simulates a batch of IoT sensor readings for the current pipeline cycle.

import random
from datetime import datetime, timezone

SENSOR_TYPES = ["temperature", "humidity", "pressure", "voltage"]
UNITS = {
    "temperature": "C",
    "humidity": "%",
    "pressure": "hPa",
    "voltage": "V",
}

results = []

for item in _items:
    payload = item["json"]
    # Webhook POST bodies arrive under "body"; manual start uses root fields.
    if isinstance(payload.get("body"), dict):
        state = payload["body"]
    else:
        state = payload

    cycle = int(state.get("cycle", 0))

    readings = []
    for index in range(5):
        sensor_type = SENSOR_TYPES[index % len(SENSOR_TYPES)]
        readings.append(
            {
                "sensor_id": f"SNR-{sensor_type[:3].upper()}-{index + 1:02d}",
                "sensor_type": sensor_type,
                "raw_value": round(random.uniform(10, 100), 2),
                "unit": UNITS[sensor_type],
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        )

    results.append(
        {
            "json": {
                "cycle": cycle,
                "running": state.get("running", True),
                "stage": "generated",
                "readings": readings,
                "generated_at": datetime.now(timezone.utc).isoformat(),
            }
        }
    )

return results
