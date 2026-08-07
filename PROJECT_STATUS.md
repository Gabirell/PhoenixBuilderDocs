# Phoenix Ecosystem - Project Status

## Current Version
- **Ecosystem Specs & Docs**: v2.3.0
- **Phoenix Builder**: v0.1.0 (Conceptual Design Phase)

## Current Sprint
- **Sprint Name**: Milestone 1: "First House" (MVP Vertical Slice)

## Current Milestone
- **Milestone 1**: First House (Export a primitive skeleton and static assets from Forge, assemble a cottage in Builder, load and walk through it in How Not To Die).

## Current Goal
- Compile a single beautiful, customizable house in Builder and test walk inside it in the game client (How Not To Die) within the next two weeks.

## Current Focus
1. Creating the `PRODUCT_ROADMAP.md` double-track tracker.
2. Rewriting `15_Roadmap.md` in the Design Bible to align with the Phoenix Spiral.
3. Specifying the MVP metadata boundaries for the 5 core PAL classes: Wall, Floor, Roof, Door, Window.

## PAL Class MVP Checklist

| PAL Class | Primitive Schema | Builder Snapping | Game Engine Load | How Not To Die Integration | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Wall** | [x] | [ ] | [ ] | [ ] | In Progress |
| **Floor** | [x] | [ ] | [ ] | [ ] | Planned |
| **Roof** | [ ] | [ ] | [ ] | [ ] | Planned |
| **Door** | [ ] | [ ] | [ ] | [ ] | Planned |
| **Window** | [ ] | [ ] | [ ] | [ ] | Planned |

## Completed
- [x] Create core repo structure and workspace
- [x] Configure MkDocs Material & automatic deployment
- [x] Establish `AI_CONTEXT.md` and `AGENTS.md` rules
- [x] Define step-by-step assistant engineering process
- [x] Rebrand SDK to PAL
- [x] ADR-004: Phoenix Architectural Language (PAL) Ontology
- [x] Formulate PAL Core Ontology 7 Chapters

## Blocked
- None

## Known Risks
- **Scope Creep**: Getting distracted by complex trimming or procedural decay algorithms before achieving the "First House" walkthrough. Mitigation: Rely strictly on the "Now / Next / Later" boundaries of `PRODUCT_ROADMAP.md`.

## Next Milestone
- **Milestone 2**: Trim Profiles & Surface Recipes (Procedural moldings and style family swaps on the same cottage mesh).

## Recent Decisions
- **ADR-004**: Transitioned from code-level SDK to the Phoenix Architectural Language (PAL) semantic ontology.
