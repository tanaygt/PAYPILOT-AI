# Security notes

Secrets are server-only and excluded by `.gitignore`. Inputs are bounded and validated with Zod; API rate limiting is enabled. Prices are looked up from the server catalogue for every order. Over-limit carts and unavailable products are rejected. Capture is only considered successful when the PayPal response is `COMPLETED` with a capture record. Production hardening should add authentication, CSRF protection, a durable database, and idempotency keys.
