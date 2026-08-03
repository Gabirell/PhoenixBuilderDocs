# Phoenix Builder Design Bible
## 09_AssetEcosystem.md

Version: 2.0.0
Status: Draft

---

# Asset Ecosystem

Phoenix Builder does not manipulate meshes.

It manipulates intelligent architectural assets.

Every asset carries geometry, metadata, semantic meaning and behavioral rules.

Geometry is only one part of an asset.

The asset itself is much richer.

---

# Asset Philosophy

Traditional software stores:

Mesh

↓

Material

↓

Done

Phoenix Builder stores:

Geometry

↓

Construction Grammar

↓

Surface DNA

↓

Building Roles

↓

Sockets

↓

Variants

↓

Metadata

↓

Export Rules

↓

Dependencies

An asset is a complete architectural component.

---

# Asset Types

Phoenix Builder recognizes three primary asset types.

---

## Phoenix Primitive (.pbp)

Procedural assets generated entirely by Phoenix Builder.

Examples:

- Straight Walls
- Floors
- Foundations
- Flat Roof Sections
- Columns
- Basic Stairs
- Sidewalks

These remain fully parametric.

They are regenerated whenever their parameters change.

---

## Phoenix Building Asset (.pba)

Custom authored assets.

Created externally, usually with Blender and the Phoenix SDK.

Examples:

- Decorative doors
- Gothic windows
- Spiral staircases
- Bell towers
- Sculptures
- Domes
- Chimneys
- Balconies

These preserve artistic freedom while participating fully in the semantic system.

---

## Phoenix Template (.pbt)

Templates are reusable architectural assemblies.

Examples:

- Small House
- Warehouse
- Church
- Castle Tower
- Apartment Floor
- Shop Front

Templates store relationships rather than geometry.

---

# Building Kits

Building Kits organize compatible assets.

Example:

Victorian Kit

Contains:

Walls

Doors

Windows

Roofs

Columns

Railings

Trim

Decoration

Surface Recipes

Style Families

Construction Grammar Rules

Everything required to create Victorian architecture.

---

# Categories

Every asset belongs to one or more categories.

Examples:

Wall

Door

Window

Roof

Foundation

Column

Decoration

Utility

Furniture

Infrastructure

Categories simplify searching and procedural generation.

---

# Asset Metadata

Each asset stores semantic information.

Examples:

Identifier

Display Name

Author

Version

Tags

Building Kit

Category

Supported Styles

Construction Roles

Surface Regions

Recommended Materials

LOD Information

Collision Rules

Export Rules

License

Dependencies

Metadata should be editable.

---

# Sockets

Sockets define how assets connect.

Each socket includes:

Position

Rotation

Normal

Connection Type

Priority

Allowed Roles

Mirror Rules

Scaling Rules

Sockets are semantic rather than purely geometric.

---

# Variants

An asset may expose procedural parameters.

Example:

Door

Width

Height

Frame Style

Handle Type

Panel Count

Arch Type

Threshold

Changing parameters regenerates the geometry.

---

# Asset Lifecycle

Every asset follows the same lifecycle.

Concept

↓

Modeling

↓

PBS Export

↓

Validation

↓

Import

↓

Building Kit

↓

Assembly

↓

Export

↓

Game Engine

The lifecycle remains deterministic.

---

# Blender Integration

Blender is the preferred environment for authoring custom assets.

The Phoenix SDK exports assets directly into PBS format.

The SDK automatically embeds:

Construction Grammar

Sockets

Metadata

Trim Mapping

Surface Regions

Collision

LOD Information

This minimizes manual work.

---

# Material References

Assets do not store textures directly.

Instead they reference Material Families.

This allows appearance to evolve independently from geometry.

---

# Preview Generation

Every asset automatically generates previews.

Examples:

Thumbnail

Orthographic Views

Isometric View

Wireframe

Surface Regions

Socket Overlay

Construction Grammar Overlay

These previews improve browsing and search.

---

# Validation

Before an asset becomes available, Phoenix Builder validates:

Missing metadata

Invalid sockets

Broken grammar

Missing dependencies

Unsupported export features

Invalid variants

Only validated assets become part of Building Kits.

---

# Asset Packages

Assets may be distributed as packages.

Examples:

Victorian Essentials

Modern Commercial

Japanese Architecture

Industrial Expansion

Fantasy Fortress

Each package contains compatible Building Kits, Materials and Templates.

---

# Future Marketplace

Although Phoenix Builder is open source, users should be able to share Building Kits through repositories.

Repositories may contain:

Assets

Surface Recipes

Style Families

Building Templates

Variants

Material Vaults

This encourages community growth while preserving compatibility.

---

# Guiding Principle

Every asset should answer three questions:

What am I?

What can I connect to?

How should I behave?

If those questions are answered, the geometry becomes only one possible representation of the asset.

---

End of File
