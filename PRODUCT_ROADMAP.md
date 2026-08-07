# Phoenix Ecosystem - Product Roadmap

This document maps the evolution of the Phoenix Ecosystem using a **Double-Track Development Model** (The Phoenix Spiral). We synchronize long-term architectural design with immediate game validation.

---

## The Double-Track Framework

```
   TRACK A: VISION (Platform)                 TRACK B: PLAYGROUND (Game Validation)
   
      Forge Exporter Add-on                      Bi-weekly content releases
              │                                             │
              ▼                                             ▼
      PAL Semantic Schema ──────────────────────► Playable inside How Not To Die
              │                                             │
              ▼                                             ▼
      Builder Scene Editor                        Player walking & interaction
```

### The Gold Rules:
1. **The Bi-Weekly Rule**: Every two weeks, the Phoenix pipeline must produce something new and tangible that can be loaded and walked around inside *How Not To Die*.
2. **The Three Questions**: Before building a feature, it must satisfy:
   - Does this improve **Phoenix Builder**? (Yes)
   - Does this improve **Phoenix Engine**? (Yes)
   - Can I use this immediately inside **How Not To Die**? (Yes)
   *If any answer is "No", the feature is deferred to LATER.*

---

## Roadmap Index (NOW / NEXT / LATER)

### 1. NOW: Milestone 1 — "First House" (The MVP House)
* **Goal**: Build one beautiful, customizable house in Builder, export it, and walk around it in *How Not To Die*.
* **PAL Scope**: Concretize the first 5 core classes: `Wall`, `Floor`, `Roof`, `Door`, `Window`.
* **Track Deliverables**:
  - **Forge**: Basic Python panel to assign these 5 PAL classes to meshes and export `.pba`/`.pbp`.
  - **Builder**: Simple viewport interface to draw rectangles, automatically generate 4 walls, snap a roof/floor, and insert door/window assets.
  - **Engine**: Parser logic to load the house, apply SceneKit colliders, and support character locomotion.
  - **Game**: *How Not To Die* integrates these cabins as lootable shelters.

### 2. NEXT: Milestone 2 — Trim Templates & Surface Recipes
* **Goal**: Enable visual variation and procedural moldings on the same house layout without altering core geometry.
* **PAL Scope**: Integrate `Baseboard`, `Cornice`, `Coving` (Trims) and material slot mappings.
* **Track Deliverables**:
  - **Forge**: Expose profile curve paths and trim templates.
  - **Builder**: Build the Bézier profile editor to generate moldings dynamically; implement Style Family mapping and Surface Recipe swapping.
  - **Engine**: Dynamic miter-joint mesh compilation and texture coordinates alignment.
  - **Game**: *How Not To Die* gains diverse cottage layouts (e.g. Stone Cottage, Log Cabin, Plaster Hut) sharing identical blueprints.

### 3. LATER: Milestone 3+ — Advanced Ontology & Scale
* **Goal**: Transition from individual houses to procedural districts.
* **PAL Scope**: Columns, Chimneys, Balconies, damage variations, decay filters, and room-partitioning grammar.
* **Track Deliverables**:
  - **Forge**: LOD validation and collision bounding-box editors.
  - **Builder**: Building footprint DNA curves, room generators, and automatic window distribution.
  - **Engine**: Large-scale spatial partitioning and mesh merging for optimal rendering.
  - **Game**: *How Not To Die* gains entire procedurally generated villages and cities.
