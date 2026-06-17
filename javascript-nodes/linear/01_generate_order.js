// Node 1: Generate Order
// Input:  cycle from Node 6 loop or Manual Start
// Output: order object passed to Node 2

const ITEMS = ['Coffee Mug', 'Notebook', 'USB Cable', 'Desk Lamp', 'Water Bottle'];
const results = [];

for (const item of $input.all()) {
  const payload = item.json;
  const state =
    payload.body && typeof payload.body === 'object' ? payload.body : payload;
  const cycle = Number(state.cycle ?? 0);

  results.push({
    json: {
      cycle,
      order_id: 'ORD-' + String(Math.floor(10000 + Math.random() * 90000)),
      item: ITEMS[Math.floor(Math.random() * ITEMS.length)],
      quantity: Math.floor(Math.random() * 5) + 1,
      unit_price: Math.round((5 + Math.random() * 45) * 100) / 100,
      created_at: new Date().toISOString(),
    },
  });
}

return results;
