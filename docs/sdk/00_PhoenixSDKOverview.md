# Phoenix Architectural Language (PAL) Overview

The **Phoenix Architectural Language (PAL)** is the shared core of the entire Phoenix Ecosystem. It represents the shared semantic ontology, specifications, and data contracts that ensure compatibility between the creation (Forge), assembly (Builder), and execution (Engine) stages of game development.

Instead of treating applications as isolated tools, the Phoenix Ecosystem positions all tools as co-equal implementors of PAL.

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
         Phoenix Architectural Language (PAL)
                         │
             Shared Specifications & Data
             - Core Ontology (Wall, Door, Cornice...)
             - File Formats (.pba, .pbp)
             - Sockets & Snapping Grammar
             - Surface Recipes & Style DNA
```

---

## Active Specifications

* **[PHX-SPEC-001 (Primitives)](../specifications/pbp_format.md)**: Specifications for parametric, mathematical components.
* **[PHX-SPEC-002 (Building Assets)](../specifications/pba_format.md)**: Specifications for artist-authored models combined with JSON metadata.
* **[PHX-SPEC-003 (PAL Ontology)](../specifications/pal_ontology.md)**: The core dictionary of semantic architectural classes.

---

## Core Pillars of PAL

### 1. Semantic Ontology (Classes & Relationships)
Establishes first-class elements (e.g. Wall, Window, Cornice) with defined snapping connectors and hosts. This allows the editor to reason about architecture instead of raw polygon files.

### 2. File Formats (.pbp and .pba)
Enforces a clean separation between pure parametric metadata (`.pbp`) and detailed artist-authored geometry packaged with socket connectors (`.pba`).

### 3. Sockets & Construction Grammar
Defines how elements connect, align, and validate their boundaries. Sockets enforce structural sanity (e.g. windows must snap onto walls or roof planes).

### 4. Surface System & Style Families
Decouples visual properties (materials, textures) from geometry. Defines **Surface Recipes** and **Style Families** that allow complete visual transformations (e.g., Cottage to Gothic) without modifying structural layouts.
