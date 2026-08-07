# Roadmap & The Phoenix Spiral

This chapter details the development strategy of the Phoenix Ecosystem. To prevent the project from becoming a purely theoretical architecture exercise, development is structured around a **Double-Track Model** known as **The Phoenix Spiral**.

---

## 1. The Double-Track Philosophy

Development is split into two synchronized tracks:

* **Track A: The Phoenix Vision (Long-term)**: Outlines the ultimate dream of the platform. A complete pipeline where artists author semantic assets in Blender (Forge), assemble them into buildings using style families (Builder), and deploy them dynamically to the custom runtime (Engine) and community marketplace (Atlas).
* **Track B: The Phoenix Playground (Immediate)**: Asks one pragmatic question: *"What can I use next month in my actual game?"* Every development cycle must produce a tangible asset, primitive, or tool that immediately upgrades the validation game (*How Not To Die*).

```
   TRACK A: THE VISION (Design)               TRACK B: THE PLAYGROUND (Validation)
   
       [ Phoenix Forge Exporter ] ────────────► Exposes basic class assignment
                   │                                         │
                   ▼                                         ▼
       [ PAL Ontology Specifications ] ───────► Concretizes active MVP classes
                   │                                         │
                   ▼                                         ▼
       [ Phoenix Builder Assembly ] ──────────► Generates rectangular cottage layouts
                   │                                         │
                   ▼                                         ▼
       [ Target Engine Exporters ] ───────────► Compiles collisions and navigation
                   │                                         │
                   ▼                                         ▼
       [ Phoenix Swift Engine ] ──────────────► Player navigates inside the house
```

### The Gold Integration Rules
1. **The Bi-Weekly Rule**: Every two weeks, the Phoenix pipeline must compile a new capability that manifests directly inside *How Not To Die*.
2. **The Development Rule**: Every proposed feature must satisfy the three-way validator:
   - Does this improve **Phoenix Builder**?
   - Does this improve **Phoenix Engine**?
   - Can I immediately use it in **How Not To Die**?
   *If any answer is "No", the feature is deferred to the LATER backlog.*

---

## 2. Re-defining Milestones: The Vertical Slices

Instead of completing 100% of Builder before starting Engine integration, development is organized into **Vertical Slices** (Milestones). Each slice matures the entire pipeline (Forge -> Builder -> Engine -> Game) for a specific set of PAL elements.

```
       Milestone 3+ (Districts)
            ▲
            │
       Milestone 2 (Trims & Surfaces)
            ▲
            │
       Milestone 1 (First House MVP)
            ▲
            │
       Milestone 0 (Scaffolding Complete)
```

### Milestone 1: "First House" (The MVP Slice)
The objective of this milestone is simply: **Build one customizable, beautiful cottage, export it, and walk around inside it in How Not To Die.**
* **PAL Classes Active**: `Wall`, `Floor`, `Roof`, `Door`, `Window`.
* **Forge Deliverables**: Expose a panel in Blender to label meshes with these 5 PAL classes and export the `.pba` folder bundles and `.pbp` primitives.
* **Builder Deliverables**: Viewport logic to draw a footprint, extrude the walls, snap the floor/roof, and insert doors/windows.
* **Engine & Game Deliverables**: Load the compiled house, calculate SceneKit collisions, and place loot spawners inside the cabin in *How Not To Die*.

### Milestone 2: Trim Templates & Surface Recipes
The objective of this milestone is to support visual styles and moldings without modifying core geometry blueprints.
* **PAL Classes Active**: `Baseboard`, `Cornice`, `Coving` (Trims).
* **Forge Deliverables**: Profile curve path tools and Trim template schemas.
* **Builder Deliverables**: A Bézier profile editor to draw custom moldings; support for Style Families and Surface Recipe material swapping.
* **Engine & Game Deliverables**: Auto-mitering of corners at runtime and path-aligned UV mapping. *How Not To Die* gains diverse log cabins, brick houses, and plaster structures sharing identical blueprints.

### Milestone 3: Advanced Ontology & Decay
The objective of this milestone is to support organic variations, decay, and damage parameters.
* **PAL Classes Active**: Sockets, damage variants, and decay values.
* **Builder Deliverables**: Decay multipliers (e.g. 50% broken window meshes, collapsed roof sections, procedural moss propagation).
* **Game Deliverables**: *How Not To Die* gains ruined shelters, abandoned villages, and weathered environments.

---

## 3. The Lifecycle of a PAL Class

PAL classes are not frozen; they mature along with the platform. A class undergoes four lifecycle stages as it winds through the spiral:

1. **Specified**: The schema boundaries are defined in `docs/specifications/`.
2. **Exporter Ready**: Phoenix Forge can assign and export the class from Blender.
3. **Builder Ready**: Phoenix Builder can snap, align, and manipulate the class.
4. **Engine Ready**: Phoenix Engine compiles the geometry, handles navigation colliders, and presents it in the active game.

By treating the roadmap as a spiral, the project remains highly agile, producing immediate creative value for game development while preserving the long-term integrity of the architectural platform.
