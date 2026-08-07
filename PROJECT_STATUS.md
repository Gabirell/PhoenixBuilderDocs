# Phoenix Ecosystem - Project Status

## Current Version
- **Ecosystem Specs & Docs**: v2.0.0
- **Phoenix Builder**: v0.1.0 (Conceptual Design Phase)

## Current Sprint
- **Sprint Name**: Core Specifications & Architectural Foundation

## Current Milestone
- **Milestone 0**: Foundation Complete (Scaffolding, ADRs, Docs Portal Setup)

## Current Goal
- Establish the **Phoenix SDK** contracts and specifications as the core shared interface of the ecosystem.

## Current Focus
1. Restructuring documentation layout to be Ecosystem-centric.
2. Splitting file format decisions into modular ADRs (Philosophy, Primitive, Building Asset).
3. Defining the detailed format specifications for `.pbp` and `.pba` structures in `docs/specifications/`.

## Completed
- [x] Create core repo structure and workspace
- [x] Configure MkDocs Material & automatic deployment
- [x] Establish `AI_CONTEXT.md` and `AGENTS.md` rules
- [x] Define step-by-step assistant engineering process

## Blocked
- None

## Known Risks
- **Long-term SDK Drift**: If Forge, Builder, or Engine modify their asset interpretation independently, the ecosystem breaks. Mitigation: Enforce strict adherence to schemas in `docs/specifications/` and the "Golden Rule" in `AGENTS.md`.

## Next Milestone
- **Milestone 1: Phoenix SDK Alpha**: Finalized specifications for `.pbp` and `.pba` and their validation schemas.

## Recent Decisions
- **ADR-001 (Proposed)**: Decided on a Hybrid Package structure (JSON for metadata, glTF/USD for binary meshes) to separate geometry from metadata.

## Upcoming ADRs
- **ADR-002**: `.pbp` (Parametric Primitive) schema specifications.
- **ADR-003**: `.pba` (Building Asset) socket and metadata integration structure.
