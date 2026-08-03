# Phoenix Builder Design Bible
## 06_ArchitecturalSurfaceSystem.md

Version: 2.0.0
Status: Draft

---

# Architectural Surface System

One of Phoenix Builder's defining ideas is the complete separation between:

Architecture

and

Appearance.

Buildings define architecture.

Surfaces define appearance.

This separation allows the same building to become:

• Medieval

• Victorian

• Japanese

• Sci-Fi

• Industrial

without rebuilding geometry.

---

# Surface Philosophy

Traditional workflows usually assign materials directly to meshes.

Phoenix Builder does not.

Instead it assigns architectural meaning.

For example:

Wall

↓

Bottom Edge

Main Surface

Corners

Window Frames

Top Cornice

Weather Layer

Damage Layer

Instead of thinking about UV islands, users think about architectural parts.

---

# Architectural Regions

Every intelligent asset contains semantic regions.

Example:

Wall

• Foundation

• Main Surface

• Window Area

• Door Area

• Trim

• Cornice

• Side Edge

• Bottom Edge

• Top Edge

These regions become the targets for every future operation.

---

# Surface Layers

Each region supports multiple independent layers.

Example:

Brick

↓

Paint

↓

Dust

↓

Leaks

↓

Moss

↓

Snow

↓

Graffiti

↓

Bullet Holes

↓

Posters

↓

Decals

Each layer remains editable.

No layer permanently alters another.

---

# Surface Recipes

A Surface Recipe defines the complete appearance of a region.

Example

Old Painted Brick

Brick Material

↓

White Paint

↓

Edge Wear

↓

Rain Leaks

↓

Moss

↓

Dust

↓

Small Cracks

↓

AO Enhancement

↓

Micro Decals

Instead of manually creating every material, users simply apply a recipe.

---

# Trim Templates

Trim Sheets remain extremely important.

However, Phoenix Builder treats them as implementation details.

A Trim Template defines:

• Trim Regions

• UV Rules

• Scaling Rules

• Orientation

• Rotation Constraints

• Seam Rules

Users rarely interact directly with UV coordinates.

---

# Intelligent Trim Assignment

When a wall is placed, Phoenix Builder automatically decides:

Which trim should be used.

Which orientation fits.

Whether mirroring is allowed.

Whether stretching is acceptable.

Whether repeating is preferable.

Users may override every decision.

---

# Tileable Materials

Large surfaces rarely require unique textures.

Instead they use:

Tileable PBR Materials.

These may include:

Brick

Stone

Concrete

Wood

Tiles

Metal

Plaster

Everything is controlled by Surface Recipes.

---

# Decal System

Variation should come primarily from decals instead of geometry.

Examples:

Cracks

Leaks

Dirt

Graffiti

Water Damage

Bullet Holes

Broken Plaster

Rust

Paint Peeling

Decals dramatically increase visual variety while keeping geometry lightweight.

---

# Smart Decal Placement

Phoenix Builder can suggest decal locations.

Examples:

Leaks appear below roofs.

Dirt appears near ground level.

Rust appears beneath metal.

Moss grows in humid areas.

The user remains in complete control.

---

# Material Families

Instead of assigning individual materials, users select Material Families.

Example

Victorian Brick

contains

Several Bricks

Several Mortars

Paint Variants

Age Variants

Weather Variants

This allows large buildings to remain visually consistent.

---

# Style Families

Style Families combine:

Surface Recipes

Trim Templates

Decal Libraries

Color Palettes

Material Families

Window Styles

Door Styles

Roof Profiles

Changing style should require one click.

---

# Texture Optimization

Phoenix Builder always prefers efficient rendering.

Possible implementations include:

Trim Sheets

Texture Atlases

Tileable PBRs

Shared Materials

Texture Arrays

Virtual Textures

Sprite Atlases

The implementation depends on the Export Profile.

Users should not need to understand the underlying optimization.

---

# Mobile Optimization

SpriteKit and mobile exports prioritize:

Small texture memory

Few draw calls

Shared atlases

Minimal overdraw

Layer reuse

Decals over geometry

These optimizations happen automatically.

---

# SpriteKit Rendering

For SpriteKit exports, Surface Recipes become layered sprites.

Typical output:

Roof

Upper Walls

Interior Walls

Floors

Props

Shadow Layer

Collision Layer

Interaction Layer

The same building can later be exported as full 3D geometry.

---

# Future Rendering

Future versions may support:

Virtual Materials

Nanite-friendly meshes

Runtime weather

Runtime aging

Seasonal variations

Snow accumulation

Wet surfaces

All without changing Building DNA.

---

# Architectural Independence

Perhaps the most important principle:

Buildings describe architecture.

Surfaces describe appearance.

Neither should depend on the other.

---

# Guiding Principle

A user should never think:

"I need a different mesh."

Instead they should think:

"I need a different architectural surface."

Phoenix Builder decides the most efficient implementation.

---

End of File
