# Architecture

The browser calls the Express API. The API owns catalogue prices, validates request shapes with Zod, calls Groq only with a server-side key, and recalculates totals before creating PayPal orders. PayPal capture responses are verified on the server before a transaction is written to `paypilot-data.json`.
