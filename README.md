# PAYPILOT AI

Your AI Purchasing Agent. Your Money, Your Rules.

PayPilot turns a natural-language procurement brief into a server-validated purchase plan. A human reviews every line item and budget status before any PayPal Sandbox order is created. The seeded catalogue is demonstration data, not live supplier inventory.

## Run locally

1. Install Node 20+.
2. `npm install`
3. Copy `.env.example` to `.env` and optionally add a fresh `GROQ_API_KEY`, `PAYPAL_CLIENT_ID`, and `PAYPAL_CLIENT_SECRET`.
4. `npm run dev`
5. Open http://localhost:5173

Without AI credentials, the full planning journey works in deterministic demo mode. Without PayPal credentials, payment safely reports that credentials are missing. No payment is simulated.

## Architecture

Vite/React frontend with AG Grid transaction management; Express/TypeScript API; Zod request validation; server-side catalogue and PayPal Orders API v2 adapter; JSON persistence for verified transactions. See [ARCHITECTURE.md](ARCHITECTURE.md), [SECURITY.md](SECURITY.md), and [API_DOCUMENTATION.md](API_DOCUMENTATION.md).

## Verification

`npm run build` checks the production bundle. `npm test` runs the test suite. PayPal sandbox success requires credentials and a sandbox buyer account. See [TESTING.md](TESTING.md).

## Hackathon status

Implemented: AI adapter with validated catalogue matching and safe fallback, human approval UI, budget enforcement, genuine server-side PayPal create/capture integration, transaction persistence, responsive dashboard, and documentation. Not included: hosted deployment, public repository, and demo video; these require external accounts/authorization.
