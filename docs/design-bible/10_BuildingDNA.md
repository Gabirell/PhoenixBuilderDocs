# Phoenix Builder Design Bible
## 10_BuildingDNA.md

Version: 2.0.0
Status: Draft

---

# Building DNA

Every project created in Phoenix Builder is fundamentally described by a deterministic architectural document called **Building DNA**.

Building DNA is the canonical representation of a building.

Everything else is generated from it.

Geometry.

Textures.

Sprites.

Meshes.

Collision.

Navigation.

Lighting.

Export data.

These are all products of Building DNA.

---

# Philosophy

Traditional software stores geometry.

Phoenix Builder stores architecture.

Geometry becomes a visualization of architectural intent.

This distinction makes buildings:

• Deterministic

• Editable

• Portable

• Engine Independent

---

# Canonical Representation

A building should always be reconstructable from Building DNA alone.

Deleting every generated mesh should never destroy the project.

Rebuilding should always produce identical results when using:

• identical Building Kits

• identical Surface DNA

• identical random seed

---

# Building DNA Contains

Building Identity

↓

Building Hierarchy

↓

Construction Grammar

↓

Rooms

↓

Floors

↓

Connections

↓

Openings

↓

Building Kit References

↓

Asset References

↓

Surface DNA References

↓

Procedural Rules

↓

Random Seeds

↓

Export Metadata

---

# What Building DNA Does NOT Store

Building DNA intentionally avoids storing implementation data.

It should not directly contain:

• triangle meshes

• UV coordinates

• baked textures

• vertex buffers

• renderer state

• SceneKit nodes

• Blender objects

Those belong to generated outputs.

---

# Building Identity

Each building possesses a unique identity.

Examples:

Building Name

Identifier

Version

Author

Creation Date

Revision

Tags

Description

Preferred Export Profiles

---

# Spatial Hierarchy

Buildings are organized hierarchically.

Example

Building

↓

Wing

↓

Floor

↓

Room

↓

Wall

↓

Opening

↓

Window

Every element understands its parent and children.

---

# Architectural Relationships

Relationships are stored semantically.

Example

Door

connects

Room A

↓

Room B

instead of

Mesh 214

attached to

Mesh 387

Meaning is always preferred over geometry.

---

# Building Grammar

Construction Grammar defines architectural validity.

Building DNA references grammar rather than duplicating rules.

This allows grammar improvements without modifying existing projects.

---

# Surface DNA

Building DNA references Surface DNA.

The same building may therefore produce:

Modern

Victorian

Industrial

Ruined

Snow Covered

Japanese

Sci-Fi

without changing structure.

---

# Parametric Values

Building DNA stores parameters rather than results whenever possible.

Examples

Roof Pitch

Floor Height

Wall Thickness

Window Spacing

Column Radius

Stair Width

Changing a parameter regenerates affected geometry.

---

# Random Seeds

Every procedural subsystem stores its own seed.

Example

Building Seed

Roof Seed

Window Seed

Material Seed

Decal Seed

Vegetation Seed

This allows selective randomization.

Changing windows does not alter roofs.

---

# Variants

Variants are lightweight modifications.

Examples

Door Handle

Window Frame

Cornice

Roof Ornament

Balcony Type

Variants never duplicate entire buildings.

---

# Templates

Templates are partially completed Building DNA.

Examples

Church Template

Warehouse Template

Apartment Template

Townhouse Template

Users customize templates rather than rebuilding common structures.

---

# Groups

Groups are semantic collections.

Examples

Entrance

Tower

Roof

Basement

Garden

North Wing

Groups simplify editing while preserving hierarchy.

---

# Constraints

Building DNA also stores architectural constraints.

Examples

Maximum Floors

Roof Type

Required Stair Access

Door Clearance

Accessibility Rules

Minimum Room Size

These constraints assist procedural generation and validation.

---

# Export Independence

Building DNA is intentionally renderer-independent.

The same Building DNA may generate:

SpriteKit layers

Phoenix Engine scene

Unity prefab

Godot scene

Unreal actors

glTF

USD

Future formats

without modification.

---

# Serialization

Building DNA should remain:

Human-readable

Versioned

Diff-friendly

Merge-friendly

Future-proof

Whenever possible, it should be stored as structured text rather than binary data.

---

# Version Compatibility

Each Building DNA file contains:

DNA Version

Surface DNA Version

Construction Grammar Version

Asset Kit Version

Export Profile Version

Independent versioning allows long-term compatibility.

---

# Live Regeneration

Whenever Building DNA changes, Phoenix Builder regenerates only affected systems.

Examples

Move wall

↓

Regenerate nearby trims

↓

Recalculate sockets

↓

Refresh collision

↓

Update previews

No unnecessary work should occur.

---

# Collaboration

Because Building DNA stores architecture instead of meshes, it is ideal for version control.

Teams should be able to:

Compare revisions

Review architectural changes

Merge compatible edits

Track design history

This makes Git a natural companion to Phoenix Builder projects.

---

# Relationship to the Phoenix Ecosystem

Building DNA is the bridge between the Phoenix applications.

Phoenix Forge creates intelligent assets.

Phoenix Builder creates Building DNA.

Phoenix Engine consumes Building DNA through exported runtime assets.

Each application contributes to the same architectural language while maintaining a distinct responsibility.

---

# Guiding Principle

Building DNA should describe **what the building is**, never **how a renderer chooses to display it**.

If a renderer changes, Building DNA should remain unchanged.

Architecture is permanent.

Rendering is transient.

---

End of File
