# Phoenix Ecosystem - Project Status

## Project Versioning
- **MkDocs Documentation**: v2.0.0
- **Phoenix Builder**: v0.1.0 (Conceptual & Design Phase)

## Current Sprint
- **Sprint Goal**: Documentation, Core Architecture Specification & ADR Foundation.
- **Current Objective**: Establish the **Phoenix Asset Specification** (`.pbp` and `.pba` formats) and the Architectural Decision Record (ADR) framework.

## Current Priorities
1. **Phoenix Asset Specification**: Draft the file format specifications for `.pbp` (Phoenix Primitive) and `.pba` (Phoenix Building Asset) schemas.
2. **ADR Framework**: Define and set up the `docs/adr/` structure for documenting architectural choices.
3. **GitHub Deployment**: Ensure automation of MkDocs publishing to GitHub Pages on commit to `main`.

## Status of Key Components

### 🏛 Phoenix Builder (macOS App)
- **Status**: Design & Architecture
- [x] Design Bible Draft
- [x] AI Context and Workspace Rules alignment
- [ ] Asset Spec Draft
- [ ] Core UI Mockups
- [ ] SceneKit Viewport Prototyping

### 🔥 Phoenix Forge (Blender Add-on)
- **Status**: Planning
- [ ] Semantic Asset Exporter Specifications
- [ ] Metadata / Socket Editor Design

### 🎮 Phoenix Engine (Swift) & HowNotToDie (Validation)
- **Status**: Planning
- [ ] Specification of Asset Consumer Layer

## Next Milestones
- **v0.2.0**: Finalized Asset Specification and ADR-001 (File Formats & Data Model approval).
- **v0.3.0**: Automatic build/deploy CI/CD workflow & initial UI wireframes.
