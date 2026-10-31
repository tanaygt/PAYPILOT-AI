# Devpost submission draft

## Project title
PAYPILOT AI — Your AI Purchasing Agent. Your Money, Your Rules.

## Elevator pitch
PayPilot turns plain-English procurement briefs into budget-aware, approval-ready purchase plans, then routes human-approved orders through PayPal Sandbox.

## About
Small teams lose time translating needs into product lists and lose control when automation hides the spend decision. PayPilot combines catalogue-grounded AI recommendations, server-side price validation, and an explicit human approval gate. The product never claims a payment succeeded from a browser event; only a verified PayPal capture becomes a transaction.

This MVP is a working local prototype. The planning journey, deterministic fallback, server-side PayPal Sandbox order creation, validation, responsive UI, and transaction persistence are implemented. A full Sandbox capture requires a buyer account and an approval in the browser; no payment is simulated.

## Built with
React, TypeScript, Vite, Express, Zod, Groq API adapter, PayPal Orders API v2, JSON persistence, Lucide React, CSS responsive layout.

## Current limitations
The demo is local rather than hosted. The seeded catalogue is demonstration data, not live supplier inventory. Groq and PayPal require the submitter's own credentials. A public GitHub repository is available; the YouTube video must be uploaded by the submitter as Public or Unlisted.
