# Node 5: Format Receipt
# Input: complete order  →  Output: order + printable receipt text

results = []

for item in _items:
    data = item["json"]

    lines = [
        f"--- RECEIPT {data['order_id']} ---",
        f"Item:     {data['item']}",
        f"Qty:      {data['quantity']} x ${data['unit_price']:.2f}",
        f"Subtotal: ${data['subtotal']:.2f}",
        f"Tax ({int(data['tax_rate'] * 100)}%):    ${data['tax_amount']:.2f}",
    ]

    if data["discount_amount"] > 0:
        lines.append(
            f"Discount ({data['discount_percent']}%): -${data['discount_amount']:.2f}"
        )

    lines.append(f"TOTAL:    ${data['final_total']:.2f}")
    lines.append("------------------------")

    results.append({"json": {**data, "receipt": "\n".join(lines)}})

return results
