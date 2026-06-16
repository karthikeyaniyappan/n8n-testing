# Node 4: Apply Discount
# Input: order + tax  →  Output: order + discount + final_total

DISCOUNT_THRESHOLD = 40.0
DISCOUNT_PERCENT = 10

results = []

for item in _items:
    data = item["json"]
    total_before = data["total_before_discount"]

    if total_before >= DISCOUNT_THRESHOLD:
        discount_percent = DISCOUNT_PERCENT
        discount_amount = round(total_before * (discount_percent / 100), 2)
    else:
        discount_percent = 0
        discount_amount = 0.0

    results.append(
        {
            "json": {
                **data,
                "discount_percent": discount_percent,
                "discount_amount": discount_amount,
                "final_total": round(total_before - discount_amount, 2),
            }
        }
    )

return results
