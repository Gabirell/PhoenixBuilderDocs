# Phoenix Builder Design Bible
## 04_Interface.md

Version: 2.0.0
Status: Draft

---

# Interface

The interface is the physical expression of Phoenix Builder's philosophy.

Users should feel they are assembling architecture rather than operating modelling software.

Every panel, tool and interaction exists to support architectural thinking.

The interface must remain clean, predictable and scalable as the project grows.

---

# Design Goals

The interface should satisfy four primary goals.

## 1. Discoverability

New users should immediately understand how to begin.

The software should encourage experimentation.

---

## 2. Speed

Experienced users should spend almost all their time inside the viewport.

Mouse movement should be minimized.

Frequently used tools should always remain visible.

---

## 3. Progressive Complexity

The interface exposes deeper functionality only when required.

Builder Mode remains simple.

Variant Mode introduces customization.

Specialist workflows belong to Blender.

---

## 4. Architectural Thinking

The user manipulates:

• Buildings

• Rooms

• Walls

• Roofs

• Doors

• Windows

• Floors

Never polygons.

---

# Workspace Layout

The default workspace consists of six major areas.

```text
+---------------------------------------------------------------+
| Toolbar                                                       |
+---------------------------------------------------------------+

+---------+--------------------------------------+--------------+
|         |                                      |              |
| Library |                                      | Inspector    |
|         |                                      |              |
|         |                                      |              |
|---------|          3D Viewport                 |--------------|
|Hierarchy|                                      | Properties   |
|         |                                      | Variants     |
+---------+--------------------------------------+--------------+

|                 Trim Template Editor                          |
+---------------------------------------------------------------+

| Status Bar                                                    |
+---------------------------------------------------------------+
```

Every panel can be hidden, resized or detached in future versions.

---

# Left Panel

The left panel contains two tabs.

## Asset Library

The Asset Library contains every reusable architectural asset.

Assets are organized by:

- Building Kits
- Categories
- Favorites
- Recent Assets
- Search Results

Categories include:

- Walls
- Doors
- Windows
- Roofs
- Floors
- Foundations
- Columns
- Railings
- Stairs
- Decoration
- Utilities

---

## Hierarchy

The Hierarchy displays every object inside the current project.

Objects can be:

- Selected
- Grouped
- Renamed
- Hidden
- Locked
- Duplicated

Future versions will support folders and layers.

---

# Center

## 3D Viewport

The viewport is the primary workspace.

Everything should be possible directly from the viewport.

Users should rarely need dialogs.

---

Supported interactions:

Click

Select.

Shift Click

Multi-selection.

Double Click

Edit.

Drag

Move.

Scroll

Zoom.

Right Mouse

Orbit.

Middle Mouse

Pan.

---

# Ghost Placement

Dragging an asset displays a transparent preview.

The preview indicates:

Valid placement

Invalid placement

Snap targets

Collision

Building alignment

Nothing is committed until released.

---

# Smart Snapping

Phoenix Builder supports several snapping systems.

Priority:

1. Construction Grammar

↓

2. Sockets

↓

3. Bounding Faces

↓

4. Grid

↓

5. Free Placement

This allows intelligent placement without requiring perfect precision.

---

# Builder Toolbar

The toolbar contains only the most frequently used actions.

New

Open

Save

Undo

Redo

Selection

Move

Rotate

Mirror

Duplicate

Delete

Builder Mode

Variant Mode

Export

Search

Command Palette

---

# Right Panel

The Inspector changes depending on the current selection.

---

## Nothing Selected

Shows:

Project Information

Building Kit

Building Style

Export Profile

Project Statistics

---

## One Object

Shows:

Asset

Position

Rotation

Scale

Sockets

Trim Template

Construction Grammar

Surface Recipe

Metadata

Variants

---

## Multiple Objects

Shows:

Selection Count

Group Transform

Group Rotation

Distribution

Alignment

Grouping

---

# Bottom Panel

## Trim Template Editor

This is one of Phoenix Builder's defining features.

Instead of editing UV coordinates, users edit semantic trim assignments.

Example:

Wall Selected

↓

Bottom Trim

Main Surface

Window Border

Top Cornice

Damage Layer

Weathering Layer

Decal Layer

Every section is represented visually.

Changing one region immediately updates the viewport.

---

# Variant Mode

When activated, the Inspector changes.

Instead of mesh parameters, users edit architectural definitions.

Example

Door

↓

Frame

↓

Leaf

↓

Panels

↓

Handle

↓

Threshold

↓

Construction Grammar

↓

Mesh Generator

The mesh updates automatically.

---

# Surface Recipe Preview

Every selected object displays its complete material stack.

Example

Brick

↓

Paint

↓

Dirt

↓

Leaks

↓

Moss

↓

Snow

↓

Decals

Each layer can be enabled, disabled or reordered.

---

# Building Templates

Projects may optionally begin with templates.

Examples

Small House

Church

Apartment

Warehouse

Castle

Factory

Templates define architectural layout rather than appearance.

Style remains independent.

---

# Command Palette

Every function should be searchable.

Press

⌘K

Search:

Create Wall

Duplicate Room

Apply Victorian Style

Export SpriteKit

Create Variant

Everything should be discoverable.

---

# Search Everywhere

Search should include:

Assets

Variants

Building Kits

Commands

Materials

Styles

Projects

Documentation

---

# Future Workspace Modes

Builder

Default.

Variant

Asset customization.

District

Future city planning.

Presentation

Client visualization.

Debug

Construction Grammar visualization.

---

# Interface Principles

The interface should satisfy these rules.

• No floating modal dialogs whenever possible.

• Everything updates live.

• Undo always works.

• Every operation remains editable.

• Most workflows require drag-and-drop.

• Users manipulate architecture instead of geometry.

---

# Success Metric

A first-time user should be capable of assembling a recognizable building within ten minutes.

An experienced user should be capable of building an entire neighborhood without opening Blender.

Whenever Blender is opened, it should be because the user genuinely wants to create a new asset, not because Phoenix Builder failed to provide the necessary architectural tools.

---

End of File
