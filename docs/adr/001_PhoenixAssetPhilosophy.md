# ADR-001: Phoenix Asset Philosophy (Primitive vs. Building Asset)

* **Status**: Proposed
* **Date**: 2026-08-07
* **Authors**: Antigravity & Gabriel Netto
* **Decisions Superseded**: None

---

## Context & Problem Statement

In the Phoenix Ecosystem, we must define how architectural structures are constructed and represented. In general game development:
* Levels are typically built of monolithic meshes or static prefabs.
* Mesh modification requires modeling tools.
* Procedural systems are often black boxes, making manual adjustments or variant swaps difficult.

To build an easy-to-use, non-destructive architectural editor (Phoenix Builder) that solo developers and indie studios can maintain, we need to decide on the core classification of our assets.

---

## Considered Options

### Option 1: Monolithic Procedural Generation (Pure Grammar/Code)
* All walls, windows, doors, and roofs are generated on the fly through code.
* **Pros**: Infinitely flexible, tiny disk footprint.
* **Cons**: Extremely hard for artists to author custom stylized details (like ornate Gothic windows or complex gargoyles). Everything must be parameterized mathematically.

### Option 2: Pure Prefab Kitbashing (Static Meshes)
* All buildings are assembled by placing pre-made modular meshes (e.g. wall tiles, door tiles).
* **Pros**: Simple asset authoring in Blender/Maya.
* **Cons**: No procedural flexibility. Changing a wall length or height requires stretching the mesh (which stretches textures) or creating new unique models, breaking the "architecture, not geometry" rule.

### Option 3: Bipartite Asset System (Parametric Primitives + Artist-Authored Assets)
* Split the ecosystem into two categories:
  1. **Phoenix Primitives (`.pbp`)**: Mathematical, parametric skeletons (walls, floors, roofs) whose geometry is generated procedurally by the engine/editor.
  2. **Phoenix Building Assets (`.pba`)**: Static 3D meshes (doors, windows, furniture, trims) authored in Blender, decorated with metadata, that socket into the primitives.
* **Pros**: Combines procedural flexibility for skeletons (walls can grow, shrink, and join dynamically without texture stretching) with infinite artistic expression for detailed fixtures.
* **Cons**: Requires managing two distinct formats and building a layout/snapping engine (sockets) to merge them.

---

## Decision Outcome

We chose **Option 3: Bipartite Asset System**. 

By dividing the world into **Parametric Primitives (`.pbp`)** and **Building Assets (`.pba`)**, we establish the core foundation for our **Three Levels of Editability**:
* **Level 1 (Assembler)**: Instantiates primitives and snaps assets to sockets.
* **Level 2 (Variant Creator)**: Swaps surface recipes on primitives or mesh variations on building assets.
* **Level 3 (Specialist)**: Authors custom `.pba` files in Blender via Phoenix Forge.

---

## Consequences

* **Clear Separation of Concerns**: Primitives manage layout, boundaries, and construction grammar. Building Assets handle decorative details and architectural articulation.
* **Stable Contracts**: The interfaces (sockets, attachment rules) between `.pbp` and `.pba` are defined at the SDK level, allowing tools to evolve independently.
* **Texture Integrity**: Primitives can use seamless tiled materials based on surface recipes, while building assets use custom UV sets or trims, avoiding texture stretching.
