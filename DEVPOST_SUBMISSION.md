# Devpost submission checklist

## Project title

PAYPILOT AI — Your AI Purchasing Agent. Your Money, Your Rules.

## Headline

Controlled agentic commerce for small teams: AI prepares a purchase, humans authorize the money, and PayPal verifies the result.

## About the project

Small businesses often turn a simple purchasing need into a manual process: compare products, check the budget, get approval, and then pay. PayPilot AI compresses that workflow into a transparent, reviewable journey.

The user describes a request such as “I need two monitors and one office chair. My total budget is $600.” The server matches the request against a seeded catalogue, calculates the total, explains the recommendation, and shows the budget status. The user then reviews every item and explicitly approves the PayPal Sandbox checkout. AI never independently authorizes or captures money.

The MVP demonstrates controlled agentic commerce rather than an autonomous black box. Prices come from the server catalogue, purchase lines are validated again before PayPal order creation, and a transaction is recorded only after a completed PayPal capture response is verified by the server.

## Built with

React, TypeScript, Vite, Node.js, Express, Zod, Groq API, PayPal Orders API v2, AG Grid Community, JSON persistence, Lucide React, responsive CSS.

## What is implemented

- Natural-language procurement planning with Groq and a deterministic fallback.
- Seeded monitors, chairs, keyboards, laptops, desks, and accessories catalogue.
- Server-side quantity, availability, budget, and price validation.
- Human approval screen with itemized totals and budget status.
- PayPal Sandbox server-side order creation and capture verification code.
- Transaction history for verified captures.
- Responsive dashboard and mobile layout.
- Rate limiting, secret-safe `.env` configuration, documentation, and MIT license.

## Honest limitations

- The catalogue is seeded demonstration data, not live inventory.
- Live Sandbox capture requires a PayPal Sandbox buyer account and browser approval.
- The app is currently a local demo; no hosted URL is claimed.
- The YouTube demo video must be uploaded as Public or Unlisted by the submitter.

## Links to add in Devpost

- GitHub: https://github.com/tanaygt/PAYPILOT-AI
- Demo: paste the final YouTube URL after upload.
