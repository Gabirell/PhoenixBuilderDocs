# Architectural Decision Records (ADRs)

All major architectural decisions for the Phoenix Ecosystem are documented here as **Architectural Decision Records (ADRs)**. This ensures that the reasoning behind design choices is captured, remaining accessible to future developers and AI assistants.

## ADR Template

Every ADR should be formatted using the following structure:

```markdown
# ADR-[Number]: [Title]

* **Status**: [Draft | Proposed | Accepted | Rejected | Superseded]
* **Date**: YYYY-MM-DD
* **Authors**: [Name]
* **Decisions Superseded**: [ADR-XXX (if applicable)]

## Context & Problem Statement
Provide a clear description of the problem, background context, and the choices we need to make.

## Considered Options
List all potential approaches or alternatives considered.
* **Option 1**: Pros & Cons
* **Option 2**: Pros & Cons

## Decision Outcome
State the chosen option and explain the rationale for the choice.

## Consequences
Describe the impact of this decision (e.g., changes to file formats, new dependencies, complexity trade-offs).
```

## ADR Index

| ADR ID | Title | Status | Date |
|--------|-------|--------|------|
| [ADR-001](001_PhoenixAssetSpecification.md) | File Format Schema for .pbp and .pba | Proposed | 2026-08-07 |
