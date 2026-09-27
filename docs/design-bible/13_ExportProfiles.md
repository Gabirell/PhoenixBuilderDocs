# Phoenix Builder Design Bible
## 13_ExportProfiles.md

Version: 2.0.0
Status: Draft

---

# Export Profiles

Exporting is not the end of the workflow.

It is one of the primary responsibilities of Phoenix Builder.

Every export should produce assets that are immediately usable by the target engine without requiring additional manual work.

The same Building DNA should support multiple export targets.

---

# Philosophy

Users design architecture once.

Phoenix Builder adapts it to different runtime environments.

The exported representation changes.

The architectural intent remains identical.

---

# Export Independence

Building DNA is independent from rendering technology.

A project should be exportable to multiple formats without rebuilding or modifying the architecture.

Examples include:

• Phoenix Engine

• SpriteKit

• Unity

• Godot

• Unreal Engine

• Defold

• Roblox

• glTF

• USD (future)

---

# Export Profiles

Each destination is represented by an Export Profile.

An Export Profile defines:

Geometry strategy

Material strategy

Texture strategy

Collision generation

LOD rules

Metadata

Naming conventions

Folder structure

Optimization settings

---

# Phoenix Engine Profile

The Phoenix Engine profile preserves the richest possible data.

Exports include:

Complete geometry

Material references

Surface DNA

Building metadata

Collision

Navigation

Sockets

Construction Grammar references

Building hierarchy

Semantic groups

This profile prioritizes flexibility and runtime interaction.

---

# SpriteKit Profile

The SpriteKit profile is optimized for 2D isometric games.

Instead of exporting meshes, Phoenix Builder generates layered sprites.

Typical outputs include:

Roof layer

Upper walls

Lower walls

Floors

Interior props

Exterior props

Shadow layer

Collision mask

Selection mask

Interaction mask

Every layer is aligned and ready for immediate use.

---

# Roblox Profile

Roblox does not consume glTF, USD, or a running-scene format directly the way Unity or Godot do.

The Roblox profile therefore works differently from the others:

Geometry exports as FBX/OBJ MeshParts, one per Building DNA piece where practical, respecting Roblox's per-mesh triangle budget.

World-space coordinates are rescaled by a stud conversion factor (Roblox's stud is not a meter; a fixed, documented ratio is applied on export).

Surface Recipes map onto Roblox SurfaceAppearance (Color, Normal, Roughness, Metalness maps) wherever the target supports it, falling back to baked textures otherwise.

Collision exports as a fidelity setting per MeshPart (Default, Box, Precise) rather than a separate custom collision asset, matching how Roblox itself models collision.

Publishing is the real difference from every other profile: Roblox requires assets to be brought in through Roblox Studio or the Open Cloud API, not read directly from a folder at runtime. The Roblox profile packages everything Studio/Open Cloud expects, but the last step is unavoidably manual (or scripted against Roblox's own API) rather than instant, unlike Phoenix Engine, Unity, or Godot exports.

Architectural metadata (room identifiers, Construction Grammar references) is preserved as Attributes on the corresponding instances, so Roblox-side scripts can still reason about the building semantically.

---

# Multi-Layer Rendering

Buildings may be exported as multiple independent visibility layers.

Examples:

Roof

Upper floor

Current floor

Basement

Decoration

Vegetation

Effects

These layers allow games to reveal interiors dynamically without requiring additional authoring.

---

# Geometry Optimization

Each Export Profile chooses the most appropriate optimization strategy.

Possible techniques include:

Mesh instancing

Trim Sheets

Texture atlases

Material batching

Shared meshes

Procedural primitives

Sprite atlases

Geometry merging

LOD generation

The user should not need to understand the implementation.

---

# Material Baking

Surface DNA is translated into engine-specific materials.

Examples:

PBR materials

Baked textures

Layered sprites

Virtual textures

Tileable materials

The same Surface DNA may therefore generate different outputs depending on the Export Profile.

---

# Collision Generation

Collision can be exported independently.

Supported collision types include:

Simple boxes

Convex hulls

Detailed meshes

Navigation volumes

Interaction areas

Custom collision assets

Profiles decide the most suitable representation.

---

# Metadata

Architectural metadata remains available after export.

Examples:

Building identifier

Room identifiers

Construction Grammar

Asset references

Surface regions

Interaction tags

Gameplay categories

This allows game logic to interact with architecture semantically.

---

# Export Presets

Users may create reusable presets.

Examples:

Mobile Low-End

Mobile High-End

PC

Console

Prototype

Presentation

Every preset stores the complete export configuration.

---

# Validation

Before exporting, Phoenix Builder validates:

Missing assets

Broken references

Unsupported materials

Invalid collisions

Missing metadata

Performance warnings

Potential export issues are reported before files are generated.

---

# Batch Export

Multiple buildings may be exported simultaneously.

Examples:

Entire village

Apartment complex

Industrial district

Castle

Building Kit samples

Batch export ensures consistent output across large projects.

---

# Incremental Export

Only modified assets should be regenerated whenever possible.

If one wall changes, Phoenix Builder should avoid rebuilding unrelated buildings.

Incremental export dramatically reduces iteration time.

---

# Open Formats

Whenever practical, Phoenix Builder should favor open standards.

Examples include:

glTF

USD (future)

PNG

JSON

SVG

These formats improve interoperability and long-term accessibility.

---

# Future Cloud Export

Future versions may support direct publishing to online repositories.

Examples:

Phoenix Vault

Git repositories

Package registries

Community Building Kits

Export architecture should remain compatible with these future workflows.

---

# Relationship to Phoenix Forge

Phoenix Forge provides the intelligent assets used during export.

Asset metadata created in Forge remains available throughout the export pipeline.

---

# Relationship to Phoenix Engine

Phoenix Engine is capable of consuming the richest export profile.

However, Phoenix Builder should never become dependent on a single runtime.

Supporting multiple engines strengthens the openness of the ecosystem.

---

# Guiding Principle

Exporting should feel invisible.

The user should spend their time designing architecture.

Phoenix Builder should handle the technical complexity of delivering optimized assets for every supported platform.

---

End of File
