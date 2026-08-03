# Phoenix Builder Design Bible
## 05_BuildingWorkflow.md

Version: 2.0.0
Status: Draft

---

# Building Workflow

Phoenix Builder is designed around a simple idea:

> Buildings should be assembled, not modeled.

Instead of asking users to manipulate vertices, edges and polygons, Phoenix Builder asks them to make architectural decisions.

Every workflow should reinforce this philosophy.

---

# The Architectural Pipeline

Every project follows the same general workflow.

```text
Project

↓

Choose Building Kit

↓

Choose Building Template (optional)

↓

Block Out Architecture

↓

Refine Structure

↓

Apply Style

↓

Customize Variants (optional)

↓

Decorate

↓

Validate

↓

Export
```

Each stage solves a different problem.

The user is never required to think about UVs, topology or mesh optimization.

---

# Step 1 — Create Project

Every building starts with a new project.

The project stores:

- Building Kit
- Style Family
- Surface Recipes
- Variants
- Export Profiles
- Procedural Seed
- Building DNA

Nothing else is required.

---

# Step 2 — Choose a Building Kit

A Building Kit defines the available architectural vocabulary.

Examples:

- Medieval
- Victorian
- Japanese
- Modern
- Industrial
- Sci-Fi
- Fantasy

A Building Kit contains:

- Walls
- Floors
- Roofs
- Windows
- Doors
- Foundations
- Stairs
- Columns
- Decorations

Every component already understands its architectural role.

---

# Step 3 — Choose a Building Template (Optional)

Templates provide an architectural starting point.

Examples:

- Small House
- Church
- Castle
- Apartment
- Warehouse
- Factory
- School
- Shop

Templates define relationships rather than appearance.

A church built from a medieval kit and one built from a sci-fi kit share the same architectural intent but completely different aesthetics.

---

# Step 4 — Block Out the Building

This is Builder Mode.

The user assembles architecture using drag-and-drop.

The process should feel similar to assembling LEGO bricks rather than modeling.

The user decides:

- Room sizes
- Wall placement
- Roof layout
- Floor arrangement
- Openings
- Vertical circulation

Smart snapping and Construction Grammar assist every placement.

---

# Step 5 — Refine the Structure

Once the basic building exists, the user refines it.

Examples:

- Add balconies
- Add porches
- Add towers
- Extend wings
- Create courtyards
- Split floors
- Add elevators
- Insert staircases

The building remains completely editable.

---

# Step 6 — Apply an Architectural Style

Structure and appearance remain independent.

The user applies a Style Family.

Examples:

- Victorian
- Art Deco
- Gothic
- Japanese
- Brutalist
- Mediterranean
- Cyberpunk

Changing style never changes architectural structure.

Only appearance.

---

# Step 7 — Apply Surface Recipes

Surface Recipes define material layering.

Examples:

Brick

↓

Paint

↓

Weathering

↓

Leaks

↓

Moss

↓

Decals

↓

Dust

Every layer remains editable.

---

# Step 8 — Create Variants (Optional)

Some projects require custom components.

Instead of editing meshes, Phoenix Builder edits architectural definitions.

Examples:

Door

↓

Frame Width

↓

Panels

↓

Handle

↓

Arch

↓

Threshold

↓

Generate

The resulting component behaves exactly like every other intelligent asset.

---

# Step 9 — Specialist Workflow (Optional)

When completely original geometry is required:

Open Blender.

The Phoenix SDK automatically preserves:

- Construction Grammar
- Sockets
- Metadata
- Trim Mapping
- LOD
- Collision
- PBS compatibility

After export, the new asset immediately becomes available inside the current Building Kit.

---

# Step 10 — Decoration

Decorative elements complete the building.

Examples:

- Signs
- Lamps
- Gutters
- Pipes
- Air Conditioners
- Awnings
- Flowers
- Antennas
- Satellite Dishes

Decoration should remain lightweight.

Whenever possible, decals and Surface Recipes are preferred over additional geometry.

---

# Step 11 — Validation

Before export, Phoenix Builder validates the project.

Checks include:

- Missing sockets
- Invalid references
- Broken variants
- Missing textures
- Export compatibility
- PBS compliance

Errors should be descriptive and actionable.

---

# Step 12 — Export

Export is treated as a product.

Users choose an Export Profile.

Examples:

- SpriteKit
- Phoenix Engine
- Unity
- Godot
- Unreal
- glTF

Every profile optimizes assets specifically for its target platform.

---

# SpriteKit Workflow

SpriteKit deserves special attention.

Instead of exporting interactive meshes, Phoenix Builder may export layered sprite assets.

Examples:

- Exterior
- Roof
- Upper Walls
- Interior Walls
- Floor
- Decoration
- Shadows
- Collision Masks

This allows 2D games such as *How Not To Die* to benefit from the same architectural workflow while rendering efficient layered sprites.

The same building can later be exported as full 3D geometry without rebuilding it.

---

# Building DNA

Every exported building contains a deterministic Building DNA.

The Building DNA stores:

- Building Kit
- Template
- Variants
- Style
- Surface Recipes
- Procedural Seed
- Construction Grammar

Given identical inputs, Phoenix Builder must always reproduce the exact same building.

---

# Future Workflow

Future versions may introduce District Mode.

```text
District

↓

Road Network

↓

Plots

↓

Buildings

↓

Infrastructure

↓

Vegetation

↓

Export
```

District Mode expands the workflow but never replaces the building-centric philosophy.

---

# Workflow Principles

Every workflow inside Phoenix Builder should satisfy these principles:

- Start with architectural intent.
- Remain non-destructive.
- Prefer intelligent defaults.
- Keep buildings editable.
- Separate structure from appearance.
- Prefer reuse over duplication.
- Automate technical work.
- Preserve artistic freedom.

---

# Success Metric

The ideal workflow allows a solo indie developer to create a complete, game-ready building in minutes while still allowing experienced artists to produce highly customized architecture without leaving the Phoenix ecosystem more than necessary.

If users spend more time making architectural decisions than solving technical problems, Phoenix Builder has achieved its purpose.

---

End of File
