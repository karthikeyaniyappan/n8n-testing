// Node 5: Format Receipt
// Input: complete order  →  Output: order + receipt text

const results = [];

for (const item of $input.all()) {
  const data = item.json;

  const lines = [
    `--- RECEIPT ${data.order_id} ---`,
    `Item:     ${data.item}`,
    `Qty:      ${data.quantity} x $${data.unit_price.toFixed(2)}`,
    `Subtotal: $${data.subtotal.toFixed(2)}`,
    `Tax (${Math.round(data.tax_rate * 100)}%):    $${data.tax_amount.toFixed(2)}`,
  ];

  if (data.discount_amount > 0) {
    lines.push(
      `Discount (${data.discount_percent}%): -$${data.discount_amount.toFixed(2)}`
    );
  }

  lines.push(`TOTAL:    $${data.final_total.toFixed(2)}`);
  lines.push('------------------------');

  results.push({ json: { ...data, receipt: lines.join('\n') } });
}

return results;
