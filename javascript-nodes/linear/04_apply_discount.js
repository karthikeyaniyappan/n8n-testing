// Node 4: Apply Discount
// Input: order + tax  →  Output: order + discount + final_total

const DISCOUNT_THRESHOLD = 40.0;
const DISCOUNT_PERCENT = 10;
const results = [];

for (const item of $input.all()) {
  const data = item.json;
  const total_before = data.total_before_discount;

  let discount_percent = 0;
  let discount_amount = 0;

  if (total_before >= DISCOUNT_THRESHOLD) {
    discount_percent = DISCOUNT_PERCENT;
    discount_amount =
      Math.round(total_before * (discount_percent / 100) * 100) / 100;
  }

  results.push({
    json: {
      ...data,
      discount_percent,
      discount_amount,
      final_total: Math.round((total_before - discount_amount) * 100) / 100,
    },
  });
}

return results;
