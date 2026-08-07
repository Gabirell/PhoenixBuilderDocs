# ADR-004: Phoenix Architectural Language (PAL) Ontology

* **Status**: Proposed
* **Date**: 2026-08-07
* **Authors**: Antigravity & Gabriel Netto
* **Decisions Superseded**: None (Refines SDK definition to PAL)

---

## Context & Problem Statement

To bind **Phoenix Forge** (Blender), **Phoenix Builder** (standalone editor), and **Phoenix Engine** (Swift) into a unified platform, they must share a common understanding of what assets are. 

Standard modular kits and game editors classify assets using arbitrary mesh file names (e.g. `gothic_wall_left_v3.fbx`), naming conventions, or folder structures. This presents several problems for procedural tools:
1. **No Semantic Rules**: The system has no way of knowing that a mesh represents a "door" and requires a "wall host" to be placed, or that a "cornice" must align along the top edges of a "wall".
2. **Fragile Snapping**: Snapping relies on mathematical bounding boxes rather than structural alignment rules.
3. **Rigid Styles**: Changing the visual style of a building (e.g., swapping a cottage window for a gothic window) requires manually replacing each mesh instance rather than updating a styling grammar.

We need a unified, platform-agnostic way to define the rules, relationships, and capabilities of every architectural component.

---

## Considered Options

### Option 1: Code-Level API (Traditional SDK approach)
* We write a Swift library (for Builder/Engine) and a Python library (for Forge/Blender) containing shared functions and data structures.
* **Pros**: Safe types, autocomplete support in IDEs, direct runtime execution.
* **Cons**: Language locking. If we expand to support Unity (C#) or Godot (C++/GDScript), we must port the entire SDK logic. It mixes software implementation details with pure architectural concepts.

### Option 2: Mesh Tags and Naming Conventions
* We establish naming rules for mesh nodes in Blender (e.g. prefixing sockets with `SOCK_` or meshes with `WALL_`).
* **Pros**: Simple, zero file-format changes.
* **Cons**: Unstructured, highly error-prone, and cannot enforce complex rules (like "a window cannot float in mid-air").

### Option 3: Semantic Ontology - Phoenix Architectural Language (PAL)
* We establish a formal specification dictionary detailing every architectural class (Wall, Door, Window, Column, Cornice) as a semantic concept. 
* Every class in PAL defines:
  - **Inputs & Hosts**: What other classes it attaches to.
  - **Sockets**: What slots it provides for child elements.
  - **Behavior Constraints**: Snapping, clearance volumes, and navigation behaviors.
* **Pros**:
  - **Style Independence**: Enables style-swapping at the ontological level (swapping a Victorian Door for a Gothic Door of the same semantic class without altering geometry anchors).
  - **Tool-Agnostic**: Defines the *intent* of architecture. Python (Blender), Swift (Builder/Engine), and C# (Unity/Godot) simply implement validators matching this shared ontology.
  - **True Architecture**: Users design buildings using architectural constructs instead of raw meshes.
* **Cons**: Requires documenting and maintaining an extensive class dictionary.

---

## Decision Outcome

We chose **Option 3: Semantic Ontology (PAL)**.

We will establish the **Phoenix Architectural Language (PAL)** specifications. PAL will be the single canonical index of all architectural classes. Forge, Builder, and Engine will conform to this dictionary.

---

## Consequences

* **Ontological Validation**: Phoenix Forge will read the PAL dictionary to validate exported `.pba` packages (e.g., checking that a door has a valid hinge socket and clearance metadata).
* **Semantic Swapping**: Phoenix Builder can procedurally replace elements (e.g., "Replace all baseboard trims") because Baseboard is a first-class class, not an arbitrary filename.
* **Unified Platform Contract**: Future extensions (like District Builder or new game engines) implement PAL specifications rather than low-level layout code.
