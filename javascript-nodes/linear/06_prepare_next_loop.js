// Node 6: Prepare Next Loop
// Input: order + receipt from Node 5  →  Output: loop_payload for Node 1

const results = [];

for (const item of $input.all()) {
  const data = item.json;
  const cycle = Number(data.cycle ?? 0);
  const next_cycle = cycle + 1;

  results.push({
    json: {
      cycle,
      next_cycle,
      last_order_id: data.order_id,
      last_final_total: data.final_total,
      last_receipt: data.receipt,
      stage: 'loop_ready',
      loop_payload: {
        cycle: next_cycle,
        running: true,
      },
    },
  });
}

return results;
