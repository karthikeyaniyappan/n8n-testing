# Node 5: Aggregate Metrics
# Computes per-sensor-type statistics and severity breakdowns.

from collections import defaultdict

results = []

for item in _items:
    data = item["json"]
    readings = data.get("readings", [])

    by_type = defaultdict(list)
    for reading in readings:
        by_type[reading["sensor_type"]].append(reading["normalized_value"])

    aggregates = {}
    for sensor_type, values in by_type.items():
        aggregates[sensor_type] = {
            "count": len(values),
            "min": round(min(values), 4),
            "max": round(max(values), 4),
            "avg": round(sum(values) / len(values), 4),
        }

    severity_counts = {"normal": 0, "warning": 0, "critical": 0}
    for reading in readings:
        severity = reading.get("severity", "normal")
        severity_counts[severity] = severity_counts.get(severity, 0) + 1

    results.append(
        {
            "json": {
                "cycle": data.get("cycle", 0),
                "running": data.get("running", True),
                "stage": "aggregated",
                "aggregates_by_type": aggregates,
                "severity_counts": severity_counts,
                "anomaly_count": data.get("anomaly_count", 0),
                "batch_stats": data.get("batch_stats", {}),
                "readings": readings,
            }
        }
    )

return results
