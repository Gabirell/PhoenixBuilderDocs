# Phoenix Ecosystem - Project Status

## Current Version
- **Ecosystem Specs & Docs**: v2.1.0
- **Phoenix Builder**: v0.1.0 (Conceptual Design Phase)

## Current Sprint
- **Sprint Name**: Core Specifications & Architectural Foundation

## Current Milestone
- **Milestone 0**: Foundation Complete (Scaffolding, ADRs, Docs Portal Setup)

## Current Goal
- Establish the **Phoenix Architectural Language (PAL)** as the core shared semantic ontology of the ecosystem.

## Current Focus
1. Restructuring documentation layout to be Ecosystem-centric.
2. Defining the PAL core semantic classes (Walls, Doors, Windows, Cornices) in `docs/specifications/pal_ontology.md`.
3. Creating ADR-004 to document the transition from a technical SDK API to a semantic architectural ontology.

## Completed
- [x] Create core repo structure and workspace
- [x] Configure MkDocs Material & automatic deployment
- [x] Establish `AI_CONTEXT.md` and `AGENTS.md` rules
- [x] Define step-by-step assistant engineering process
- [x] Initial draft of primitive (.pbp) and building asset (.pba) file structures

## Blocked
- None

## Known Risks
- **Ecosystem Schema Drift**: If Forge, Builder, or Engine interpret architectural semantics differently, asset validation fails. Mitigation: Define the exact ontology in the PAL Specification and enforce it via the Golden Rule process.

## Next Milestone
- **Milestone 1: PAL Alpha**: Finalized specifications for `.pbp`, `.pba`, and the complete PAL Ontology dictionary.

## Recent Decisions
- **ADR-001 (Proposed)**: Decided on a Hybrid Package structure (JSON for metadata, glTF/USD for binary meshes) to separate geometry from metadata.
- **ADR-002 (Proposed)**: Parametric Primitive Architecture (.pbp) represented as pure mathematical JSON data.
- **ADR-003 (Proposed)**: Building Asset Architecture (.pba) represented as a folder bundle matching GLTF/USD with metadata.

## Upcoming ADRs
- **ADR-004**: Phoenix Architectural Language (PAL) Core Ontology.
