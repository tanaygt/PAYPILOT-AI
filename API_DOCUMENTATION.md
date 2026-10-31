# API documentation

- `GET /api/health` — liveness.
- `GET /api/catalogue` — seeded catalogue.
- `POST /api/agent/plan` body `{message}` — returns a purchase plan.
- `GET /api/paypal/config` — credential availability; never returns secrets.
- `POST /api/paypal/create-order` body `{lines, budget}` — revalidates and creates a PayPal order.
- `POST /api/paypal/capture-order` body `{orderID}` — verifies completed capture and persists it.
- `GET /api/transactions` — verified transaction history.
