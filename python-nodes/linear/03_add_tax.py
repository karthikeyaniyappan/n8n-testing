# Node 3: Add Tax
# Input: order + subtotal  →  Output: order + tax fields

TAX_RATE = 0.08

results = []

for item in _items:
    data = item["json"]
    tax_amount = round(data["subtotal"] * TAX_RATE, 2)
    results.append(
        {
            "json": {
                **data,
                "tax_rate": TAX_RATE,
                "tax_amount": tax_amount,
                "total_before_discount": round(data["subtotal"] + tax_amount, 2),
            }
        }
    )

return results
