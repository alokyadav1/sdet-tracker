# API Testing at Senior Depth

_Phase 2 of 8 — Automation Track_

[⬅ Back to README](../../README.md)

---

## Week 04 — HTTP & REST, Including the Parts Junior Candidates Skip

- [ ] **Sat (2h)** — Hit every method against a public API in Postman; flag design smells you'd raise in a real API review.

## Week 05 — Postman as a Design Tool, Not Just a Request Sender

- [ ] **Mon** — Collections & environments for multi-environment use.
- [ ] **Tue** — Chaining requests — realistic multi-step flow (create → update → verify → delete).
- [ ] **Wed** — Scripting — pre-request scripts, pm.test, dynamic variable generation for test data isolation.
- [ ] **Thu** — Assertions — status, body, full JSON schema validation.
- [ ] **Fri** — Auth — Basic, Bearer, OAuth2, plus token refresh flow testing.
- [ ] **Sat (2h)** — Build a full collection: 15+ requests, CRUD + auth + negative cases + token refresh.

## Week 06 — Automating API Tests: Production-Grade, Not Tutorial-Grade

- [ ] **Mon** — Real test project structure — config layer, fixtures, reusable request builders.
- [ ] **Tue** — Automate GET; add retry logic with backoff for flaky dependencies.
- [ ] **Wed** — Automate POST/PUT/PATCH; add test data cleanup (teardown, not just setup).
- [ ] **Thu** — Automate DELETE with state verification; think through test isolation for parallel runs.
- [ ] **Fri** — Negative cases: invalid payloads, missing auth, wrong methods, rate-limit triggering.
- [ ] **Sat (2h)** — Convert your Postman collection into this production-grade suite.

## Week 07 — Schema, Contract Testing (Implemented), and GraphQL

- [ ] **Mon** — JSON Schema validation — implement it fully in your suite.
- [ ] **Tue** — Contract testing — set up Pact (or lightweight equivalent) between a mock consumer and provider.
- [ ] **Wed** — Continue Pact setup — get one real contract test passing.
- [ ] **Fri** — Automate 2-3 GraphQL tests, including one testing query complexity/depth limiting.
- [ ] **Sat (2h)** — Finish and document your Pact contract test.

## Week 08 — API Test Suite as Infrastructure (Portfolio Project #1)

- [ ] **Mon** — Organize the full suite: config, fixtures, contract tests, GraphQL tests, reporting.
- [ ] **Tue** — Add reporting with historical trend tracking.
- [ ] **Wed** — Add environment config via env variables — no hardcoded URLs.
- [ ] **Sat (2h)** — Address 5 gaps found Friday.
- [ ] **Sun (1h)** — Ship v1 to GitHub. Portfolio Project #1.
