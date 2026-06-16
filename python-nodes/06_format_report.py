# Node 6: Format Report
# Builds a human-readable report and prepares the payload for the next loop.

from datetime import datetime, timezone

results = []

for item in _items:
    data = item["json"]
    cycle = int(data.get("cycle", 0))
    anomaly_count = data.get("anomaly_count", 0)
    severity_counts = data.get("severity_counts", {})

    if severity_counts.get("critical", 0) > 0:
        status = "CRITICAL"
    elif anomaly_count > 0:
        status = "DEGRADED"
    else:
        status = "HEALTHY"

    report_lines = [
        f"=== Sensor Pipeline Report | Cycle {cycle} ===",
        f"Status: {status}",
        f"Anomalies: {anomaly_count}",
        f"Severity: {severity_counts}",
    ]

    for sensor_type, aggregate in data.get("aggregates_by_type", {}).items():
        report_lines.append(
            "  "
            + f"{sensor_type}: avg={aggregate['avg']} "
            + f"min={aggregate['min']} max={aggregate['max']} "
            + f"(n={aggregate['count']})"
        )

    report_text = "\n".join(report_lines)

    results.append(
        {
            "json": {
                "cycle": cycle,
                "running": data.get("running", True),
                "stage": "complete",
                "status": status,
                "report": report_text,
                "summary": {
                    "cycle": cycle,
                    "status": status,
                    "anomaly_count": anomaly_count,
                    "severity_counts": severity_counts,
                    "aggregates_by_type": data.get("aggregates_by_type", {}),
                },
                "completed_at": datetime.now(timezone.utc).isoformat(),
                "next_cycle": cycle + 1,
                "loop_payload": {
                    "cycle": cycle + 1,
                    "running": True,
                },
            }
        }
    )

return results
