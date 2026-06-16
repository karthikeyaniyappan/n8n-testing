# Node 1: Generate Order
# Input:  cycle number from previous loop (Node 6) or empty on first run
# Output: a single order object passed to Node 2

import random
import string
from datetime import datetime, timezone

ITEMS = ["Coffee Mug", "Notebook", "USB Cable", "Desk Lamp", "Water Bottle"]

results = []

for item in _items:
    payload = item["json"]
    # Loop-back from webhook wraps body; manual start uses root fields.
    if isinstance(payload.get("body"), dict):
        state = payload["body"]
    else:
        state = payload

    cycle = int(state.get("cycle", 0))

    order = {
        "cycle": cycle,
        "order_id": "ORD-" + "".join(random.choices(string.digits, k=5)),
        "item": random.choice(ITEMS),
        "quantity": random.randint(1, 5),
        "unit_price": round(random.uniform(5.0, 50.0), 2),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    results.append({"json": order})

return results
