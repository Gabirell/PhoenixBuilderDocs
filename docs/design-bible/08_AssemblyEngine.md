# Phoenix Builder Design Bible
## 08_AssemblyEngine.md

Version: 2.0.0
Status: Draft

---

# Assembly Engine

The Assembly Engine is the heart of Phoenix Builder.

While the viewport displays geometry, the Assembly Engine understands architecture.

It is responsible for turning architectural intent into valid, editable buildings.

The user never assembles meshes.

The user assembles architecture.

---

# Responsibilities

The Assembly Engine is responsible for:

• Smart Placement

• Intelligent Snapping

• Construction Grammar

• Socket Resolution

• Terrain Adaptation

• Automatic Structural Helpers

• Building Validation

• Multi-object Editing

• Procedural Assembly

• Building DNA generation

---

# Smart Placement

When the user drags an object into the scene the engine evaluates:

Construction Grammar

↓

Sockets

↓

Bounding Faces

↓

Collision

↓

Terrain

↓

Grid

↓

Free Placement

Every placement receives a confidence score.

The best solution is presented to the user.

---

# Smart Sockets

Sockets are no longer simple connection points.

Each socket contains semantic information.

Example

Door Socket

Knows:

• accepts doors

• accepts arches

• accepts gates

• rejects windows

• rejects chimneys

---

Each socket stores:

• Position

• Rotation

• Normal

• Size

• Priority

• Grammar Type

• Connection Rules

• Mirror Rules

• Scale Rules

---

# Connection Rules

Connections are evaluated by meaning.

Instead of

```
Socket A

↓

Socket B
```

the engine evaluates

```
Exterior Wall

↓

Door Opening

↓

Door

↓

Threshold
```

The geometry follows automatically.

---

# Multi-Level Snapping

Snapping occurs in several passes.

Priority 1

Construction Grammar

Priority 2

Semantic Socket

Priority 3

Geometry Socket

Priority 4

Bounding Box

Priority 5

Grid

Priority 6

Free Placement

This greatly reduces incorrect snapping.

---

# Ghost Preview

Every dragged object displays a live preview.

The preview communicates:

Green

Valid.

Yellow

Valid but requires adjustment.

Orange

Will generate helper geometry.

Red

Invalid.

---

# Automatic Helpers

The Assembly Engine automatically creates helper elements when appropriate.

Examples

Wall floating above terrain

↓

Foundation extension

---

Door above terrain

↓

Automatic staircase

---

Building on a hill

↓

Foundation adapts

---

Roof gap

↓

Automatic trim

---

Window inside roof

↓

Suggest relocation

---

Helper geometry always remains editable.

---

# Terrain Adaptation

Terrain adaptation is deterministic.

Possible strategies:

Foundation Extension

Wall Extension

Terrain Cut

Terrain Fill

Automatic Steps

Retaining Wall

The user chooses the preferred strategy.

---

# Building Integrity

The engine constantly validates the building.

Examples

Missing roof

Floating floor

Disconnected wall

Unsupported balcony

Broken stair

Missing collision

Every issue receives:

Severity

Explanation

Suggested Fix

Automatic Fix (when possible)

---

# Group Assembly

Groups behave like architectural units.

Examples

Room

Wing

Floor

Tower

Courtyard

Groups may be:

Moved

Duplicated

Mirrored

Rotated

Saved as templates

Groups preserve internal relationships.

---

# Procedural Assistance

Procedural generation never replaces the user.

Instead it assists.

Examples

Generate roof

Generate windows

Generate support columns

Generate balconies

Generate fences

Generate sidewalks

Generate vegetation

Every generated result remains editable.

---

# Rule Engine

Every decision comes from explicit rules.

Example

Church

↓

Nave

↓

Tower

↓

Roof

↓

Entrance

↓

Windows

↓

Decoration

Changing the seed changes the solution.

The rules remain identical.

---

# Undo Philosophy

Every Assembly Engine operation is reversible.

Automatic operations are simply commands.

They can always be undone.

---

# Performance

Large projects should remain interactive.

The Assembly Engine should:

Reuse references

Cache evaluations

Evaluate incrementally

Avoid duplicate geometry

Batch updates

Delay expensive calculations until necessary

---

# Future Expansion

The Assembly Engine should eventually support:

District Assembly

Road Networks

Terrain Blocks

City Infrastructure

Procedural Rivers

Bridges

Railways

Vegetation Rules

Without changing its underlying architecture.

---

# Guiding Principle

The Assembly Engine exists to reduce technical work.

It should never reduce creative freedom.

Whenever possible it should propose rather than impose.

The user always has the final decision.

---

End of File
