# Phoenix Architectural Language (PAL) Specifications

This directory contains the concrete technical specifications of the **Phoenix Architectural Language (PAL)**. While ADRs explain **why** architectural decisions were made, the specifications document **how** those concepts are implemented.

These specifications represent the shared contract between all tools in the ecosystem:
* **🔥 Phoenix Forge** (Blender Add-on) must export geometry and metadata conforming exactly to these specifications.
* **🏛 Phoenix Builder** (macOS App) must load, modify, and combine files following these rules.
* **🎮 Phoenix Engine** (Swift Game Engine) must read the exported outputs of Builder according to these structures.

## Active Specifications

| Spec ID | Name | Format | Status | Target Component |
|---|---|---|---|---|
| [PHX-MVP-001](PHX-MVP-001_FirstHouse.md) | Milestone 1: "First House" Specification | Mixed | Proposed | MVP End-to-End Slice |
| [PHX-SPEC-001](pbp_format.md) | Phoenix Primitive Specification | `.pbp` (JSON) | Draft | Primitives & Grammar |
| [PHX-SPEC-002](pba_format.md) | Phoenix Building Asset Specification | `.pba` (Hybrid GLTF/USD + JSON) | Draft | Asset Libraries & Snapping |
| [PHX-SPEC-003](pal_ontology.md) | PAL Core Ontology | Markdown | Draft | Semantic Dictionary |
