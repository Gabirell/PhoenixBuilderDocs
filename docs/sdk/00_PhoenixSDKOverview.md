# Phoenix SDK Overview

The **Phoenix SDK** is the shared core of the entire Phoenix Ecosystem. It represents the shared interface, contracts, data schemas, and mathematical specifications that ensure compatibility between the creation, assembly, and execution stages of game development.

Instead of treating applications as silos, the Phoenix Ecosystem positions all tools (Forge, Builder, Engine) as co-equal implementors of the Phoenix SDK.

```
                 PHOENIX ECOSYSTEM
                         │
        ┌────────────────┼────────────────┐
        │                │                │
    Phoenix          Phoenix          Phoenix
     Forge           Builder          Engine
 (Asset Authoring)  (Assembly)       (Runtime)
        │                │                │
        └────────────────┼────────────────┘
                         │
                    Phoenix SDK
                         │
             Shared Specifications & Data
             - File Formats (.pba, .pbp)
             - Sockets & Snapping Grammar
             - Surface Recipes & Style DNA
```

---

## Shared Specifications

* **[PHX-SPEC-001 (Primitives)](../specifications/pbp_format.md)**: Specifications for parametric, mathematical components.
* **[PHX-SPEC-002 (Building Assets)](../specifications/pba_format.md)**: Specifications for artist-authored models combined with JSON metadata.

---

## Core Pillars of the SDK

### 1. File Formats (.pbp and .pba)
Enforces a clean separation between pure parametric metadata (`.pbp`) and detailed artist-authored geometry packaged with socket connectors (`.pba`).

### 2. Sockets & Construction Grammar
Defines how primitives and building assets interact. This schema governs how elements connect, align, and validate their bounds relative to surrounding architectural blocks.

### 3. Surface System
Decouples visual properties (textures, materials, shaders) from geometry. The SDK defines **Surface Recipes** and **Style Families** that allow instant variations without modifying structural geometry.

### 4. Deterministic DNA
Ensures that all procedural algorithms remain entirely seed-based and non-destructive. The identical source file must result in the exact same rendered geometry and configuration in both the editor (Builder) and the game client (Engine).
