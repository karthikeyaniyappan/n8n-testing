# Node 4: Detect Anomalies
# Flags outliers in the current batch using z-score analysis.

import math

results = []

for item in _items:
    data = item["json"]
    readings = data.get("readings", [])

    values = [reading["normalized_value"] for reading in readings]
    count = len(values)

    if count == 0:
        mean = 0.0
        std = 0.0
    else:
        mean = sum(values) / count
        variance = sum((value - mean) ** 2 for value in values) / count
        std = math.sqrt(variance) if variance > 0 else 0.0

    flagged = []
    anomaly_count = 0

    for reading in readings:
        value = reading["normalized_value"]
        if std > 0:
            z_score = abs((value - mean) / std)
        else:
            z_score = 0.0

        is_anomaly = z_score > 1.5
        if is_anomaly:
            anomaly_count += 1

        if z_score > 2.5:
            severity = "critical"
        elif is_anomaly:
            severity = "warning"
        else:
            severity = "normal"

        flagged.append(
            {
                **reading,
                "z_score": round(z_score, 4),
                "is_anomaly": is_anomaly,
                "severity": severity,
            }
        )

    results.append(
        {
            "json": {
                "cycle": data.get("cycle", 0),
                "running": data.get("running", True),
                "stage": "anomaly_checked",
                "validation_passed": data.get("validation_passed", False),
                "valid_count": data.get("valid_count", 0),
                "readings": flagged,
                "batch_stats": {
                    "mean": round(mean, 4),
                    "std": round(std, 4),
                    "count": count,
                },
                "anomaly_count": anomaly_count,
            }
        }
    )

return results
