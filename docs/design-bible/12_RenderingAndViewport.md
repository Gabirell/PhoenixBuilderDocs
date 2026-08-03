# Phoenix Builder Design Bible
## 12_RenderingAndViewport.md

Version: 2.0.0
Status: Draft

---

# Rendering and Viewport

The viewport is not merely a renderer.

It is the user's architectural workspace.

Its purpose is to communicate spatial relationships clearly while remaining fast enough for very large projects.

The viewport should prioritize understanding over visual effects.

---

# Philosophy

Beautiful rendering is valuable.

Understanding architecture is essential.

Whenever realism conflicts with clarity, clarity wins.

Phoenix Builder is an authoring tool, not a game engine.

---

# The Viewport as a Workspace

The viewport should answer three questions immediately.

• What am I looking at?

• What is selected?

• What can I do next?

Users should never wonder where they are or what is editable.

---

# Navigation

Navigation should feel natural regardless of project size.

Supported controls include:

Orbit

Pan

Zoom

Focus Selection

Frame Building

Frame Room

Frame Floor

Frame Project

Navigation should remain fluid even for large scenes.

---

# Camera Modes

Phoenix Builder supports multiple camera modes.

Perspective

Orthographic

Isometric

Top

Front

Back

Left

Right

Section View

Interior View

Every mode exists for a different architectural task.

---

# Isometric Mode

Isometric mode is a first-class citizen.

Many games created with Phoenix Builder will ultimately render isometric assets.

The viewport should therefore provide an accurate isometric preview.

Users should be able to preview:

SpriteKit exports.

Layer ordering.

Roof visibility.

Wall transparency.

Shadow direction.

This allows game-ready assets to be validated before export.

---

# Visual Layers

Every architectural category can be shown or hidden independently.

Examples

Roofs

Floors

Walls

Doors

Windows

Furniture

Vegetation

Collision

Sockets

Helpers

Terrain

Lighting

Navigation

Selection

Users should be able to isolate exactly the information they need.

---

# Cutaway Views

Understanding interiors is critical.

The viewport supports several cutaway modes.

Roof Hidden

Upper Floors Hidden

Section Plane

Room Isolation

Selected Floor Only

Interior Preview

Cutaway operations never modify the building.

They only change visualization.

---

# Transparency

Objects may become transparent automatically when they obstruct editing.

Examples

Roof fades while editing interiors.

Upper floors fade while editing lower levels.

Walls fade while placing furniture.

Transparency should feel smooth and unobtrusive.

---

# Grid System

The viewport includes a configurable architectural grid.

Supported modes include:

Square Grid

Isometric Grid

Metric Grid

Imperial Grid

Adaptive Grid

Snap Grid

The grid assists placement without restricting creativity.

---

# Construction Overlays

The viewport may display semantic overlays.

Examples

Construction Grammar

Surface Regions

Sockets

Building Groups

Material Regions

Structural Elements

Collision

Navigation

Lighting

These overlays help users understand the building rather than the geometry.

---

# Surface Preview

Selecting an architectural element opens the Surface Preview panel.

This panel displays:

Surface DNA

Material Family

Surface Recipe

Trim Template

Decal Layers

Weathering

Damage

Paint

Users edit appearance without leaving the viewport.

---

# Performance Modes

The viewport automatically adapts to project size.

Quality Mode

Highest visual fidelity.

Balanced Mode

Default authoring mode.

Performance Mode

Optimized for extremely large projects.

Users may switch modes manually.

---

# Preview Accuracy

The viewport aims to match exported results.

Previews should accurately represent:

Materials

Lighting response

Transparency

Layer order

SpriteKit slicing

Export Profiles

Minor differences may exist depending on the destination engine, but architectural intent should remain identical.

---

# Debug Visualization

Advanced users may enable diagnostic overlays.

Examples

Socket Normals

Construction Grammar

Bounding Volumes

LOD Levels

Collision Shapes

Surface Regions

Building DNA

Procedural Dependencies

Validation Warnings

Debug information should never interfere with standard workflows.

---

# Multi-Viewport (Future)

Future versions may support multiple synchronized viewports.

Examples

Perspective + Top

Exterior + Interior

Isometric + Sprite Preview

Wireframe + Shaded

Orthographic + Perspective

Multiple views improve precision during complex projects.

---

# Rendering Independence

The viewport is an editor.

It is not responsible for defining exported visuals.

Rendering exists only to assist architectural authoring.

Export Profiles remain responsible for generating runtime assets.

---

# Relationship to Phoenix Engine

Phoenix Builder previews architecture.

Phoenix Engine renders gameplay.

Although both applications may eventually share rendering technology, their objectives remain distinct.

Builder prioritizes editing.

Engine prioritizes simulation.

---

# Guiding Principle

The viewport should disappear from the user's mind.

Users should feel as though they are manipulating architecture directly rather than controlling a camera inside a 3D scene.

---

End of File
