# Chapter 1: Introduction to PAL

Welcome to the **Phoenix Architectural Language (PAL)** documentation. PAL is the shared semantic ontology, grammar, and interface contract at the very center of the Phoenix Ecosystem.

Instead of treating asset creation (Forge), assembly (Builder), and execution (Engine) as isolated tools, the Phoenix platform positions all components as co-equal implementors of PAL.

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

## Why a Shared Language?

Most game engines and procedural tools communicate using raw, unstructured geometry data (e.g. static `.fbx` or `.obj` meshes with arbitrary tag suffixes). This creates several points of friction:
1. **Mesh Blindness**: The editor and engine have no understanding of what a mesh represents. A wall mesh is treated the same as a chair mesh.
2. **Fragile Snapping**: Snapping relies on bounding box collisions rather than structural logic (e.g. windows aligning inside wall openings).
3. **Rigid Styles**: Swapping the theme of a building requires manually replacing individual meshes.

PAL solves these problems by defining a **semantic domain model**. Every asset in the database is bound to an architectural concept. When an artist exports a Gothic Window from Blender, it is tagged as a `Window` class of type `Lancet` under the PAL ontology.

Because the system understands the *intent* of the architecture, Builder can snap it automatically, check its clearance volume, apply damage logic, and swap its entire visual style family seamlessly without altering the core structural geometry.

---

## Navigating the PAL Chapters

* [**Chapter 2: Philosophy**](philosophy.md): Explains the "Design architecture, not geometry" mindset.
* [**Chapter 3: Grammar & Inheritance**](grammar.md): Outlines the semantic class inheritance structure.
* [**Chapter 4: Core Ontology**](ontology.md): Lists the 25 foundational architectural concepts.
* [**Chapter 5: Host & Socket Rules**](rules.md): Defines how components dock and interact.
* [**Chapter 6: Style System**](style_system.md): Details procedural style family swapping.
* [**Chapter 7: Constraints & Validation**](constraints.md): Outlines bounds, clearance volumes, and metadata validation rules.
