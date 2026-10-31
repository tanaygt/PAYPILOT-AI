# Testing

Build/type check: `npm run build`.

Manual acceptance matrix: valid request and invalid request are covered by the planner UI/API; budget exceeded and invalid quantity are rejected server-side; missing products are ignored by AI output and rejected by PayPal validation; missing AI credentials use safe deterministic fallback; missing PayPal credentials are visibly blocked; duplicate capture prevention requires a durable idempotency store before production. Live sandbox capture is blocked until credentials are supplied.
