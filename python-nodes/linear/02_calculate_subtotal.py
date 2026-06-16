# Node 2: Calculate Subtotal
# Input: order from Node 1  →  Output: order + subtotal

results = []

for item in _items:
    data = item["json"]
    subtotal = round(data["quantity"] * data["unit_price"], 2)
    results.append({"json": {**data, "subtotal": subtotal}})

return results
