// Node 3: Add Tax
// Input: order + subtotal  →  Output: order + tax fields

const TAX_RATE = 0.08;
const results = [];

for (const item of $input.all()) {
  const data = item.json;
  const tax_amount = Math.round(data.subtotal * TAX_RATE * 100) / 100;

  results.push({
    json: {
      ...data,
      tax_rate: TAX_RATE,
      tax_amount,
      total_before_discount: Math.round((data.subtotal + tax_amount) * 100) / 100,
    },
  });
}

return results;
