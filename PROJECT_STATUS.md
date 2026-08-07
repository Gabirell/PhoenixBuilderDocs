# Phoenix Ecosystem - Project Status

## Current Version
- **Ecosystem Specs & Docs**: v2.2.0
- **Phoenix Builder**: v0.1.0 (Conceptual Design Phase)

## Current Sprint
- **Sprint Name**: Core Specifications & Architectural Foundation

## Current Milestone
- **Milestone 0**: Foundation Complete (Scaffolding, ADRs, Docs Portal Setup)

## Current Goal
- Establish the **Phoenix Architectural Language (PAL)** as the core shared semantic ontology of the ecosystem.

## Current Focus
1. Creating the dedicated **PAL** directory (`docs/pal/`) and documenting the 7 core chapters (Philosophy, Grammar, Core Ontology, Sockets, Style System, Constraints).
2. Refining navigation layout inside `mkdocs.yml` to make PAL a top-level section.
3. Preparing auto-deploy pipeline verification.

## Completed
- [x] Create core repo structure and workspace
- [x] Configure MkDocs Material & automatic deployment
- [x] Establish `AI_CONTEXT.md` and `AGENTS.md` rules
- [x] Define step-by-step assistant engineering process
- [x] Rebrand SDK to PAL
- [x] ADR-004: Phoenix Architectural Language (PAL) Ontology

## Blocked
- None

## Known Risks
- **Ontology Alignment**: Ensuring Blender python exporter and Swift compiler interpret PAL classes (like Miters, Sweeps, Clearances) identically. Mitigation: Document precise structural rules in `docs/pal/rules.md`.

## Next Milestone
- **Milestone 1: PAL Alpha**: Finalized specifications for `.pbp`, `.pba`, and the complete PAL Ontology dictionary.

## Recent Decisions
- **ADR-004 (Proposed)**: Transitioned from code-level SDK to the Phoenix Architectural Language (PAL) semantic ontology.

## Upcoming ADRs
- **ADR-005**: Trim and Decorative Sweep Semantics.
