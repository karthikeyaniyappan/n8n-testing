// Node 2: Calculate Subtotal
// Input: order from Node 1  →  Output: order + subtotal

const results = [];

for (const item of $input.all()) {
  const data = item.json;
  const subtotal = Math.round(data.quantity * data.unit_price * 100) / 100;
  results.push({ json: { ...data, subtotal } });
}

return results;
