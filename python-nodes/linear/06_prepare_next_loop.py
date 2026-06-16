# Node 6: Prepare Next Loop
# Input:  order + receipt from Node 5
# Output: summary + loop_payload sent back to Node 1 via webhook

results = []

for item in _items:
    data = item["json"]
    cycle = int(data.get("cycle", 0))
    next_cycle = cycle + 1

    results.append(
        {
            "json": {
                "cycle": cycle,
                "next_cycle": next_cycle,
                "last_order_id": data.get("order_id"),
                "last_final_total": data.get("final_total"),
                "last_receipt": data.get("receipt"),
                "stage": "loop_ready",
                # This payload becomes the input for Node 1 on the next run.
                "loop_payload": {
                    "cycle": next_cycle,
                    "running": True,
                },
            }
        }
    )

return results
