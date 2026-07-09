#!/usr/bin/env python3
"""
generate_tracker.py — single source of truth for the 8-month SDET progress tracker.

This script builds tracker/theory/<phase>.md and tracker/automation/<phase>.md
from the WEEKS data below.

USAGE:
    python3 scripts/generate_tracker.py

WARNING:
Re-running this OVERWRITES every file in tracker/theory/ and tracker/automation/,
which erases any checkmarks you've already made. Only re-run this if you're
resetting on purpose or you've edited WEEKS below and accept losing progress
(commit or back up tracker/ first if you're not sure).

Day tags ending in "(both)" mean the task genuinely spans both tracks (e.g. a
full-loop mock interview that includes live coding). Those items are rendered
into BOTH files with a shared-checkpoint note. Checking it off in one file does
not check it off in the other — that's a plain-markdown limitation — so check
both copies when you finish one of these.
"""

import os

PHASES = [
    {"id": 1, "slug": "phase-1-qa-foundations",
     "title": "QA Foundations & Test Strategy, at Architect Level", "weeks": [1, 2, 3]},
    {"id": 2, "slug": "phase-2-api-testing",
     "title": "API Testing at Senior Depth", "weeks": [4, 5, 6, 7, 8]},
    {"id": 3, "slug": "phase-3-js-ts-architecture",
     "title": "Advanced JavaScript/TypeScript for Framework Architecture", "weeks": [9, 10]},
    {"id": 4, "slug": "phase-4-git-capstone",
     "title": "Git, Code Review Discipline, and Q1 Capstone", "weeks": [11, 12]},
    {"id": 5, "slug": "phase-5-playwright-framework",
     "title": "Playwright & Framework Architecture at Depth", "weeks": [13, 14, 15]},
    {"id": 6, "slug": "phase-6-cicd-ownership",
     "title": "CI/CD Ownership at Scale", "weeks": [16, 17, 18]},
    {"id": 7, "slug": "phase-7-performance-ai-systemdesign",
     "title": "Performance, AI-in-QA, and System Design", "weeks": [19, 20, 21, 22, 23, 24]},
    {"id": 8, "slug": "phase-8-interview-machine",
     "title": "Interview Machine + Portfolio + DSA", "weeks": [25, 26, 27, 28, 29, 30, 31, 32]},
]

# category per day: "theory" | "automation" | "both"
WEEKS = {
    1: {"phase": 1, "title": "SDLC/STLC as Decision Frameworks, Not Trivia", "days": [
        ("Mon", "theory", """Study SDLC models (Waterfall, Agile, V-model). Write one paragraph on which model your company actually runs, where it deviates from the textbook version, and why."""),
        ("Tue", "theory", """Study STLC phases. Map them onto your company's real process; identify one gap and how you'd fix it."""),
        ("Wed", "theory", """Study the 7 testing principles. For each, find a real instance where your team violated it — and what it cost."""),
        ("Thu", "theory", """Record a 3-minute answer: "Walk me through how you'd design a test strategy for a new feature with a 2-week deadline." No notes."""),
        ("Fri", "theory", """Study V&V, static vs dynamic testing. Research what "shift-left" means in practice and where your team could shift left today."""),
        ("Sat (2h)", "theory", """Write a full Test Strategy document (scope, risks, entry/exit criteria, environments, tooling, ownership) for a hypothetical checkout feature."""),
        ("Sun (1h)", "theory", """Review. List 5 questions where a mid-level and senior answer differ — draft the senior version of each."""),
    ]},
    2: {"phase": 1, "title": "Test Design Techniques as Tools You Choose Between", "days": [
        ("Mon", "theory", """Equivalence Partitioning on a login form, then argue when EP alone is insufficient."""),
        ("Tue", "theory", """Boundary Value Analysis on an age-eligibility field; combine with EP and compare coverage."""),
        ("Wed", "theory", """Decision Table Testing for a multi-condition discount engine (stacking rules)."""),
        ("Thu", "theory", """State Transition Testing for an order-status workflow, including invalid transitions."""),
        ("Fri", "theory", """Exploratory testing — session-based test management; write how you'd justify its ROI to a skeptical manager."""),
        ("Sat (2h)", "theory", """Apply 3 techniques to one real feature; write a one-paragraph justification of technique selection."""),
        ("Sun (1h)", "theory", """Record a 3-minute answer to "how do you decide which test design technique fits a given feature?" """),
    ]},
    3: {"phase": 1, "title": "Risk, Requirements, and Defect Lifecycle as Strategy Tools", "days": [
        ("Mon", "theory", """Defect lifecycle — severity vs priority, with a real example where they diverge."""),
        ("Tue", "theory", """Risk-based testing — build a real risk matrix for a payment feature; rank coverage by risk score."""),
        ("Wed", "theory", """Requirement analysis — rewrite 3 vague acceptance criteria from real tickets into testable ones."""),
        ("Thu", "theory", """Record: "How do you prioritize testing when you can't test everything before release?" """),
        ("Fri", "theory", """Test strategy vs test plan — identify which your team is actually missing."""),
        ("Sat (2h)", "theory", """Write a risk-based test plan for a payment-gateway feature, including what you're consciously choosing not to test and why."""),
        ("Sun (1h)", "theory", """Consolidate Weeks 1-3 into a "QA Fundamentals — Senior Framing" reference doc."""),
    ]},
    4: {"phase": 2, "title": "HTTP & REST, Including the Parts Junior Candidates Skip", "days": [
        ("Mon", "theory", """HTTP methods deep dive — PUT vs PATCH, including partial-update edge cases."""),
        ("Tue", "theory", """Status codes beyond the common ones — 409, 422, 429, and when each is correct."""),
        ("Wed", "theory", """Headers, content types, cookies, sessions — session-based vs token-based auth in test design."""),
        ("Thu", "theory", """CORS — then explain how you'd test for a CORS misconfiguration deliberately."""),
        ("Fri", "theory", """REST principles — statelessness, idempotency, plus HATEOAS."""),
        ("Sat (2h)", "automation", """Hit every method against a public API in Postman; flag design smells you'd raise in a real API review."""),
        ("Sun (1h)", "theory", """Record: "What makes an API well-designed from a testability standpoint?" """),
    ]},
    5: {"phase": 2, "title": "Postman as a Design Tool, Not Just a Request Sender", "days": [
        ("Mon", "automation", """Collections & environments for multi-environment use."""),
        ("Tue", "automation", """Chaining requests — realistic multi-step flow (create → update → verify → delete)."""),
        ("Wed", "automation", """Scripting — pre-request scripts, pm.test, dynamic variable generation for test data isolation."""),
        ("Thu", "automation", """Assertions — status, body, full JSON schema validation."""),
        ("Fri", "automation", """Auth — Basic, Bearer, OAuth2, plus token refresh flow testing."""),
        ("Sat (2h)", "automation", """Build a full collection: 15+ requests, CRUD + auth + negative cases + token refresh."""),
        ("Sun (1h)", "theory", """Write a README that reads like a design doc: what's covered, what's out of scope, why."""),
    ]},
    6: {"phase": 2, "title": "Automating API Tests: Production-Grade, Not Tutorial-Grade", "days": [
        ("Mon", "automation", """Real test project structure — config layer, fixtures, reusable request builders."""),
        ("Tue", "automation", """Automate GET; add retry logic with backoff for flaky dependencies."""),
        ("Wed", "automation", """Automate POST/PUT/PATCH; add test data cleanup (teardown, not just setup)."""),
        ("Thu", "automation", """Automate DELETE with state verification; think through test isolation for parallel runs."""),
        ("Fri", "automation", """Negative cases: invalid payloads, missing auth, wrong methods, rate-limit triggering."""),
        ("Sat (2h)", "automation", """Convert your Postman collection into this production-grade suite."""),
        ("Sun (1h)", "theory", """Review and push. Write: "if this suite ran with 10x parallel workers, what would break?" """),
    ]},
    7: {"phase": 2, "title": "Schema, Contract Testing (Implemented), and GraphQL", "days": [
        ("Mon", "automation", """JSON Schema validation — implement it fully in your suite."""),
        ("Tue", "automation", """Contract testing — set up Pact (or lightweight equivalent) between a mock consumer and provider."""),
        ("Wed", "automation", """Continue Pact setup — get one real contract test passing."""),
        ("Thu", "theory", """GraphQL — queries, mutations, N+1 query problems in testing."""),
        ("Fri", "automation", """Automate 2-3 GraphQL tests, including one testing query complexity/depth limiting."""),
        ("Sat (2h)", "automation", """Finish and document your Pact contract test."""),
        ("Sun (1h)", "theory", """Review. If Pact setup ran long, flag it for the Week 32 buffer."""),
    ]},
    8: {"phase": 2, "title": "API Test Suite as Infrastructure (Portfolio Project #1)", "days": [
        ("Mon", "automation", """Organize the full suite: config, fixtures, contract tests, GraphQL tests, reporting."""),
        ("Tue", "automation", """Add reporting with historical trend tracking."""),
        ("Wed", "automation", """Add environment config via env variables — no hardcoded URLs."""),
        ("Thu", "theory", """Write the suite README as an architecture doc: decisions, trade-offs, out-of-scope items."""),
        ("Fri", "theory", """Self-review as an auditor: security headers, rate-limit handling, auth edge cases?"""),
        ("Sat (2h)", "automation", """Address 5 gaps found Friday."""),
        ("Sun (1h)", "automation", """Ship v1 to GitHub. Portfolio Project #1."""),
    ]},
    9: {"phase": 3, "title": "JS Fundamentals, Applied to Framework Design", "days": [
        ("Mon", "automation", """Closures — write a test-data factory pattern using closures."""),
        ("Tue", "theory", """Scope & hoisting, `this` — where arrow functions break `this`-dependent patterns."""),
        ("Wed", "theory", """Prototypes — then composition over inheritance and why modern frameworks favor it."""),
        ("Thu", "automation", """Design patterns: Factory, Builder, Singleton — implement a Builder for complex test fixtures."""),
        ("Fri", "theory", """ES6+ refresh: destructuring, spread/rest, module patterns (barrel exports, circular dependency avoidance)."""),
        ("Sat (2h)", "automation", """Refactor part of your API suite to use the Builder pattern."""),
        ("Sun (1h)", "theory", """Record: "How would you architect a test framework so 10 engineers can contribute without stepping on each other?" """),
    ]},
    10: {"phase": 3, "title": "TypeScript & Async Mastery for Scale", "days": [
        ("Mon", "automation", """TypeScript generics — write a generic ApiClient<T> type."""),
        ("Tue", "automation", """Interfaces vs types, utility types (Partial, Pick, Omit) applied to fixture typing."""),
        ("Wed", "theory", """Promises — Promise.all vs Promise.allSettled for parallel test execution."""),
        ("Thu", "theory", """Event loop — microtasks vs macrotasks."""),
        ("Fri", "theory", """Async pitfalls: race conditions, flaky waits, how Promise.allSettled avoids one test blocking others."""),
        ("Sat (2h)", "automation", """Migrate a meaningful chunk of your API suite to TypeScript with generic typing."""),
        ("Sun (1h)", "theory", """Record: "Explain the event loop, and why it matters for writing non-flaky async tests." """),
    ]},
    11: {"phase": 4, "title": "Git and Code Review as a Senior Engineer", "days": [
        ("Mon", "theory", """Branching strategies — git-flow vs trunk-based, which fits a fast-moving test framework team."""),
        ("Tue", "automation", """Merge vs rebase — resolve a deliberately created conflict."""),
        ("Wed", "automation", """Interactive rebase, commit squashing, changelog-quality messages."""),
        ("Thu", "theory", """Code review discipline — review one of your old PRs as if you were a senior reviewer."""),
        ("Fri", "automation", """.gitignore, git stash, cherry-pick, CODEOWNERS files."""),
        ("Sat (2h)", "automation", """Simulate a full PR workflow: branch → commit → rebase → resolve conflict → self-review → merge."""),
        ("Sun (1h)", "theory", """Write "how I review code and expect to be reviewed." """),
    ]},
    12: {"phase": 4, "title": "Q1 Capstone: Consolidation at Senior Depth", "days": [
        ("Mon", "theory", """Revisit every "shaky" flag from Weeks 1-11's Sunday reviews."""),
        ("Tue", "both", """Buffer day #1 — Week 7's Pact setup or any slipped task lands here."""),
        ("Wed", "automation", """Final polish on Portfolio Project #1 — does it read like adoptable infrastructure?"""),
        ("Thu", "theory", """Record a 90-second "what I built and why," pitched at a senior audience."""),
        ("Fri", "theory", """Self-check: can you defend every design decision under pushback?"""),
        ("Sat (2h)", "both", """Full mock self-interview: 10 QA fundamentals questions + defend your project's trade-offs."""),
        ("Sun (1h)", "theory", """Review Phase 5 so Week 13 starts with zero ramp-up."""),
    ]},
    13: {"phase": 5, "title": "Playwright Fundamentals, With Explicit Cypress Comparison", "days": [
        ("Mon", "automation", """Playwright setup, locators, auto-waiting — compare to Cypress's retry-ability model."""),
        ("Tue", "automation", """Network interception in Playwright vs cy.intercept."""),
        ("Wed", "automation", """Multi-tab/multi-context support — the concrete capability gap vs Cypress."""),
        ("Thu", "automation", """Visual testing (screenshot comparison)."""),
        ("Fri", "theory", """Write a one-page "Cypress vs Playwright: when I'd pick which" decision doc."""),
        ("Sat (2h)", "automation", """Port a meaningful chunk of your Cypress suite to Playwright."""),
        ("Sun (1h)", "theory", """Record the decision doc as a 3-minute spoken answer."""),
    ]},
    14: {"phase": 5, "title": "Framework Architecture: Page Object Model, Done Properly", "days": [
        ("Mon", "theory", """POM anti-patterns vs a properly layered POM (locators/actions/assertions separated)."""),
        ("Tue", "automation", """Refactor one page object into separated layers."""),
        ("Wed", "theory", """Test data management: fixtures vs factories vs seeded databases."""),
        ("Thu", "automation", """Implement a data factory for your Playwright suite."""),
        ("Fri", "automation", """Custom commands/fixtures in Cypress and Playwright — build a reusable authenticated-session fixture."""),
        ("Sat (2h)", "automation", """Apply the layered POM refactor to 2-3 more page objects."""),
        ("Sun (1h)", "theory", """Write "why I structure page objects this way." """),
    ]},
    15: {"phase": 5, "title": "Reporting, Flakiness Management, Test Health as a Discipline", "days": [
        ("Mon", "automation", """Reporting with historical trend visibility (Allure or similar)."""),
        ("Tue", "theory", """Flaky test root causes: timing, isolation, environment drift, shared state."""),
        ("Wed", "automation", """Implement a flaky test quarantine strategy — tag, isolate, track separately from the main gate."""),
        ("Thu", "theory", """Test health metrics: flake rate, suite runtime trend, signal-to-noise ratio."""),
        ("Fri", "theory", """Write a one-page "Test Health Dashboard" spec."""),
        ("Sat (2h)", "automation", """Wire up reporting across both Cypress and Playwright suites."""),
        ("Sun (1h)", "theory", """Record: "How do you deal with a flaky test suite the team has stopped trusting?" """),
    ]},
    16: {"phase": 6, "title": "GitHub Actions: Building the Pipeline, Not Just Running It", "days": [
        ("Mon", "theory", """GitHub Actions fundamentals — workflows, jobs, steps, triggers."""),
        ("Tue", "automation", """Build a pipeline: lint → build → test → report, from scratch."""),
        ("Wed", "automation", """Add caching (node_modules, browser binaries); measure actual time saved."""),
        ("Thu", "automation", """Add parallelization/sharding across runners; measure runtime before/after."""),
        ("Fri", "automation", """Add a merge gate — required status checks."""),
        ("Sat (2h)", "automation", """Get your full Cypress + Playwright + API suite running end-to-end in this pipeline."""),
        ("Sun (1h)", "theory", """Write a before/after paragraph with real runtime and cost numbers."""),
    ]},
    17: {"phase": 6, "title": "Docker, Environments, and Pipeline Resilience", "days": [
        ("Mon", "theory", """Docker basics — images, containers, why test environments benefit from them."""),
        ("Tue", "automation", """Containerize your test suite so it runs identically locally and in CI."""),
        ("Wed", "automation", """Environment strategy — secrets/env-variable injection, no hardcoded values."""),
        ("Thu", "automation", """Pipeline resilience — retry logic for genuine infra failures (distinct from flaky tests, which you quarantine)."""),
        ("Fri", "theory", """Jenkins pipeline-as-code conceptually — enough to discuss it if a target company uses it."""),
        ("Sat (2h)", "automation", """Get your containerized suite running inside the Week 16 pipeline."""),
        ("Sun (1h)", "theory", """Record: "Walk me through a CI/CD pipeline you built and the trade-offs you made" (full 3-5 min version)."""),
    ]},
    18: {"phase": 6, "title": "Q2 Capstone: Integrated System + Documentation + Self-Audit", "days": [
        ("Mon", "automation", """Consolidate everything into one coherent repo: Cypress + Playwright + API + contract tests + reporting + pipeline."""),
        ("Tue", "theory", """Write the master README as an architecture document with a simple system diagram."""),
        ("Wed", "theory", """Write 2-3 ADRs — e.g. "Why Playwright + Cypress dual-framework," "Why quarantine over retry for flakiness." """),
        ("Thu", "theory", """Self-audit: could a new hire understand the why, not just the what, from your docs alone?"""),
        ("Fri", "both", """Full mock interview: theory + coding + API design + CI/CD walk-through + one ADR defended under pushback."""),
        ("Sat (2h)", "automation", """Fix whatever Friday's mock exposed."""),
        ("Sun (1h)", "theory", """Review Phase 7 so Week 19 starts with zero ramp-up."""),
    ]},
    19: {"phase": 7, "title": "k6 Performance Testing at Senior Depth", "days": [
        ("Mon", "automation", """k6 basics — scripting in JS, virtual users, staged load."""),
        ("Tue", "theory", """Load testing types: load, stress, spike, soak — know when each applies."""),
        ("Wed", "automation", """Write a k6 script against a real/demo API with ramping VUs."""),
        ("Thu", "theory", """Interpret metrics — p95/p99 latency, error rate, throughput — tied to a hypothetical SLA."""),
        ("Fri", "theory", """JMeter — conceptual literacy only: GUI vs code-based debate, why some enterprises still require it."""),
        ("Sat (2h)", "automation", """Build a full k6 test plan doc + script with a written results interpretation against an SLA."""),
        ("Sun (1h)", "theory", """Record: "How do you decide performance testing strategy and what metrics matter?" """),
    ]},
    20: {"phase": 7, "title": "Performance Integration and Capacity Reasoning", "days": [
        ("Mon", "automation", """Integrate a lightweight k6 smoke-perf check into your CI pipeline."""),
        ("Tue", "theory", """Capacity planning basics — how test results inform scaling decisions."""),
        ("Wed", "theory", """Bottleneck analysis — reading APM/flame-graph data conceptually."""),
        ("Thu", "theory", """Write an ADR: "When do we run full load tests vs lightweight smoke perf checks in CI?" """),
        ("Fri", "automation", """Finalize and push k6 artifacts."""),
        ("Sat (2h)", "automation", """Wire the k6 script into GitHub Actions as a scheduled job."""),
        ("Sun (1h)", "theory", """Record a 3-minute "walk me through a performance test you designed." """),
    ]},
    21: {"phase": 7, "title": "AI in QA: Foundations Applied", "days": [
        ("Mon", "theory", """LLM fundamentals — explainable without jargon."""),
        ("Tue", "theory", """AI Agents & MCP conceptually — what problem they solve in testing workflows."""),
        ("Wed", "automation", """Try a real AI-assisted test generation tool (Playwright AI codegen, Copilot, or similar) on a real feature."""),
        ("Thu", "theory", """Self-healing locators — where they help, where they mislead."""),
        ("Fri", "theory", """Write an honest one-page "AI in my testing workflow" assessment — what helped, what produced garbage."""),
        ("Sat (2h)", "automation", """Use an AI tool to scaffold one test, then refine it by hand; document the diff and why each change was needed."""),
        ("Sun (1h)", "theory", """Record: "Where does AI genuinely help in test automation, and where is it overhyped?" """),
    ]},
    22: {"phase": 7, "title": "AI-Assisted Testing: Practical Build + Flaky Triage", "days": [
        ("Mon", "theory", """Explore MCP servers relevant to QA workflows conceptually."""),
        ("Tue", "automation", """AI-assisted flaky test triage — can an LLM classify "real bug" vs "flaky" from failure logs? Try it."""),
        ("Wed", "automation", """Build a small prompt workflow that takes a failure log and drafts a triage summary."""),
        ("Thu", "theory", """Document limitations found: hallucination risk, need for human review."""),
        ("Fri", "automation", """Consolidate AI-in-QA artifacts into a portfolio piece."""),
        ("Sat (2h)", "automation", """Finalize the AI-assisted triage demo; write its README."""),
        ("Sun (1h)", "theory", """Review the week."""),
    ]},
    23: {"phase": 7, "title": "System Design for Test Infrastructure (Part 1)", "days": [
        ("Mon", "theory", """Test infra architecture basics — runner, orchestration, reporting, environments."""),
        ("Tue", "theory", """Scalability patterns — sharding and parallelization at the infra level, beyond a single pipeline."""),
        ("Wed", "theory", """Environment strategy at scale — ephemeral environments, environment-per-PR."""),
        ("Thu", "theory", """Whiteboard practice (self-recorded): design test infra for a 20-engineer team running 5,000 tests."""),
        ("Fri", "theory", """Test data management at scale — synthetic data, seeding/reset strategies."""),
        ("Sat (2h)", "theory", """Write a full system design doc: "Test Infrastructure for a 20-Engineer Team" — components, trade-offs, scaling plan."""),
        ("Sun (1h)", "theory", """Record yourself presenting the doc as if in a design review."""),
    ]},
    24: {"phase": 7, "title": "System Design (Part 2) + Q3 Capstone", "days": [
        ("Mon", "theory", """Observability for test systems — dashboards, alerting on suite health."""),
        ("Tue", "theory", """Cost optimization for CI/CD at scale — compute cost vs speed trade-offs."""),
        ("Wed", "theory", """Refine your Week 23 doc with observability + cost sections."""),
        ("Thu", "theory", """Mock system design interview — present and defend the doc under pushback."""),
        ("Fri", "automation", """Consolidate Phase 7 artifacts: k6 suite, AI-in-QA demo, system design doc."""),
        ("Sat (2h)", "automation", """Full review and polish of all three artifacts."""),
        ("Sun (1h)", "theory", """Review Phase 8 so Week 25 starts with zero ramp-up."""),
    ]},
    25: {"phase": 8, "title": "DSA: Interview-Relevant Only", "days": [
        ("Mon", "automation", """Arrays & strings — two-pointer and sliding-window patterns at SDET-interview depth."""),
        ("Tue", "automation", """Hashmaps — 2-3 practice problems."""),
        ("Wed", "automation", """Basic recursion + time/space complexity reasoning."""),
        ("Thu", "theory", """Practice explaining your approach out loud while solving — this is the actual skill being tested."""),
        ("Fri", "automation", """2-3 more practice problems, same speak-while-solving format."""),
        ("Sat (2h)", "automation", """Timed practice: 3 problems in 90 minutes, real interview pressure simulation."""),
        ("Sun (1h)", "theory", """Note which DSA area is still shaky for Week 32's buffer."""),
    ]},
    26: {"phase": 8, "title": "Resume + Portfolio Finalization Begins", "days": [
        ("Mon", "theory", """Audit every portfolio project — what's presentation-ready vs needs polish."""),
        ("Tue", "theory", """Rewrite READMEs consistently across all repos — same structure, same voice."""),
        ("Wed", "theory", """Draft resume v1 — impact-first bullets, not tool lists."""),
        ("Thu", "theory", """Get resume feedback (peer, mentor, or a resume-review community)."""),
        ("Fri", "theory", """Revise resume based on feedback."""),
        ("Sat (2h)", "automation", """Polish the 1-2 weakest portfolio repos."""),
        ("Sun (1h)", "theory", """Finalize resume v2."""),
    ]},
    27: {"phase": 8, "title": "Mock Interviews: QA Theory + Automation Coding", "days": [
        ("Mon", "theory", """Mock QA theory interview — STLC, test design, defect lifecycle."""),
        ("Tue", "theory", """Debrief — log every stumble, schedule a redo drill within 48h."""),
        ("Wed", "automation", """Mock automation coding interview — live-code a Cypress or Playwright test from a scenario."""),
        ("Thu", "automation", """Debrief + redo drill."""),
        ("Fri", "theory", """Mock JS/TS interview questions (closures, async, event loop)."""),
        ("Sat (2h)", "both", """Full run: theory + coding combined, timed like a real loop."""),
        ("Sun (1h)", "theory", """Review all debriefs; prioritize weak spots for next week."""),
    ]},
    28: {"phase": 8, "title": "Mock Interviews: API + System Design + CI/CD Walkthrough", "days": [
        ("Mon", "theory", """Mock API testing interview — design a test strategy for a given spec live."""),
        ("Tue", "theory", """Debrief + redo drill."""),
        ("Wed", "theory", """Mock system design discussion — present your Week 23/24 doc, defend under pushback."""),
        ("Thu", "theory", """Debrief + redo drill."""),
        ("Fri", "theory", """Mock "walk me through your CI/CD pipeline" with real Week 16 before/after metrics."""),
        ("Sat (2h)", "theory", """Full run: API + system design combined."""),
        ("Sun (1h)", "theory", """Review."""),
    ]},
    29: {"phase": 8, "title": "Behavioral + Communication Intensive", "days": [
        ("Mon", "theory", """STAR method — draft/refine 3 stories (conflict, failure, leadership without authority)."""),
        ("Tue", "theory", """Draft/refine 3 more (tight deadline, disagreement with a decision, a bug you're proud of catching)."""),
        ("Wed", "theory", """Full mock behavioral interview."""),
        ("Thu", "theory", """Debrief + re-record the weakest 2 stories."""),
        ("Fri", "theory", """Practice explaining any one project in 90 seconds and in 5 minutes, back to back."""),
        ("Sat (2h)", "both", """Full mock behavioral + technical combined loop."""),
        ("Sun (1h)", "theory", """Review remaining weak spots."""),
    ]},
    30: {"phase": 8, "title": "Full-Loop Mock Interviews", "days": [
        ("Mon", "both", """Full loop mock #1: theory + coding + API + behavioral in one extended session, simulating a real onsite."""),
        ("Tue", "theory", """Debrief thoroughly — this is the single most valuable data point in the plan."""),
        ("Wed", "both", """Targeted drilling on whatever broke Monday."""),
        ("Thu", "both", """Full loop mock #2."""),
        ("Fri", "both", """Debrief + drill."""),
        ("Sat (2h)", "both", """Address any remaining structural gaps — actual understanding, not memorization."""),
        ("Sun (1h)", "theory", """Review overall progress against the Final Readiness Checklist."""),
    ]},
    31: {"phase": 8, "title": "Company-Specific Prep + Applications Begin", "days": [
        ("Mon", "theory", """Identify 5-10 realistic target companies."""),
        ("Tue", "theory", """Research each one's stack and interview style; tailor prep notes per company."""),
        ("Wed", "theory", """Company-specific mock #1."""),
        ("Thu", "theory", """Apply to your first batch of target companies."""),
        ("Fri", "theory", """Company-specific mock #2."""),
        ("Sat (2h)", "automation", """Finalize LinkedIn, portfolio links — everything live and consistent."""),
        ("Sun (1h)", "theory", """Review applications sent; plan follow-ups."""),
    ]},
    32: {"phase": 8, "title": "Final Capstone: Readiness Checklist + Buffer", "days": [
        ("Mon", "theory", """Full self-audit against the Final Readiness Checklist — every box should now be checkable."""),
        ("Tue", "both", """Buffer day #2 — close any remaining gap (DSA, a shaky ADR defense, whatever's left)."""),
        ("Wed", "both", """One more full-loop mock interview as a final gut check."""),
        ("Thu", "both", """Debrief, final touch-ups."""),
        ("Fri", "theory", """Final proofread pass on portfolio + resume."""),
        ("Sat (2h)", "theory", """Rest / light review only — new material has negative ROI this close to interviewing."""),
        ("Sun (1h)", "theory", """Reflect on the full 32 weeks; set a maintenance cadence for continued learning afterward."""),
    ]},
}


def render_week(week_num, week, track):
    lines = [f"## Week {week_num:02d} — {week['title']}", ""]
    any_task = False
    for day, cat, task in week["days"]:
        if cat == track or cat == "both":
            any_task = True
            note = " _(🔗 shared checkpoint — also tracked in the other file)_" if cat == "both" else ""
            lines.append(f"- [ ] **{day}** — {task}{note}")
    if not any_task:
        lines.append("_No dedicated tasks this week for this track._")
    lines.append("")
    return "\n".join(lines)


def build_phase_file(phase, track):
    lines = [
        f"# {phase['title']}",
        "",
        f"_Phase {phase['id']} of 8 — {track.title()} Track_",
        "",
        "[⬅ Back to README](../../README.md)",
        "",
        "---",
        "",
    ]
    for wk in phase["weeks"]:
        lines.append(render_week(wk, WEEKS[wk], track))
    return "\n".join(lines)


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for track in ("theory", "automation"):
        out_dir = os.path.join(base, "tracker", track)
        os.makedirs(out_dir, exist_ok=True)
        for phase in PHASES:
            content = build_phase_file(phase, track)
            path = os.path.join(out_dir, f"{phase['slug']}.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"wrote {path}")


if __name__ == "__main__":
    main()
