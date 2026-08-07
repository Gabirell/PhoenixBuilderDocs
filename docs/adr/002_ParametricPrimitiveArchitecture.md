# ADR-002: Parametric Primitive Architecture (.pbp)

* **Status**: Proposed
* **Date**: 2026-08-07
* **Authors**: Antigravity & Gabriel Netto
* **Decisions Superseded**: None

---

## Context & Problem Statement

Phoenix Primitives (`.pbp`) represent walls, floors, roofs, columns, and foundations. We must decide how to store and manage their geometry and structural information. 

Should a primitive contain compiled vertex/index arrays representing the 3D mesh, or should it store purely mathematical and structural parameters that are evaluated at runtime?

---

## Considered Options

### Option 1: Baked Geometry (Vertex/Polygon data inside the file)
* The file contains the actual 3D mesh vertices, normals, and UVs generated at the time of creation.
* **Pros**: Rapid loading in the viewport since no procedural generation is needed on load.
* **Cons**: Destructive. If the user changes a wall length or height, we must recalculate, modify, and re-serialize the raw mesh. Version diffs in Git will show huge binary/numeric changes. It violates the core rule: "Design architecture, not geometry."

### Option 2: Parameterized Definition (Pure JSON/YAML metadata)
* The file stores coordinates, polylines, thickness, height, and references to surface styles. The geometry is compiled dynamically in-memory when loaded in Phoenix Builder or Phoenix Engine.
* **Pros**:
  - Non-destructive: editing a wall is as simple as updating a vector point or a height float.
  - Tiny file size: files are lightweight text representations.
  - Dynamic adaptation: we can automatically adjust LODs, UV mappings, and texture repetitions based on runtime size.
  - Interactive: dynamic operations like cutting openings for doors or windows are calculated cleanly by subtracting bounding shapes from the primitive definition.
* **Cons**:
  - Requires writing robust geometry generators (tesselation, extrusion) in both the macOS builder application and the Swift game engine.
  - Minor performance overhead on initial scene load to construct the meshes.

---

## Decision Outcome

We chose **Option 2: Parameterized Definition (Pure JSON)**.

Primitives will be stored as lightweight, human-readable JSON files that define the mathematical parameters and structural intent.

---

## Consequences

* **Dynamic Extrusion and UV Generation**: The editor (Phoenix Builder) and runtime (Phoenix Engine) must share a common triangulation/extrusion codebase (part of the Phoenix SDK) to ensure that the identical `.pbp` compiles to the exact same 3D mesh in both tools.
* **Dynamic Boolean Openings**: Sockets and opening requests (from doors and windows) are evaluated on the fly. The primitive recalculates its geometric mesh by carving out the opening bounding box, preserving non-destructive editing.
* **Level 2 Editability**: Users can open a `.pbp` in a text editor and tweak thickness, default heights, or change surface recipe IDs directly.
