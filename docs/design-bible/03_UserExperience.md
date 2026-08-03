# Phoenix Builder Design Bible
## 03_UserExperience.md

Version: 1.0.0  
Status: Draft

---

# User Experience

Phoenix Builder is designed around one central idea:

> The software should feel like assembling architecture, not operating a 3D editor.

The interface must remain approachable for beginners while exposing professional capabilities for experienced users.

The user should never feel overwhelmed.

Instead, the application gradually reveals additional functionality as projects become more complex.

---

# Design Principles

## Progressive Complexity

Phoenix Builder is divided into three creation levels.

### Level 1 — Builder

The default experience.

Users assemble complete buildings by dragging intelligent assets into the scene.

Typical users:

- Indie developers
- Level designers
- SpriteKit developers
- Rapid prototyping

No modelling knowledge is required.

---

### Level 2 — Variant Editor

Users customize existing architectural assets.

Instead of editing meshes, they edit architectural definitions.

Examples:

- Door style
- Window proportions
- Cornice profile
- Stair dimensions
- Roof pitch
- Column type

Geometry is regenerated automatically.

---

### Level 3 — Specialist Workflow

When complete artistic freedom is required, Phoenix Builder connects directly to Blender through the Phoenix SDK.

Artists create entirely new assets while preserving:

- Construction Grammar
- Metadata
- Sockets
- Trim Mapping
- PBS compatibility

---

# The Golden Rule

The interface should expose only the controls necessary for the current task.

Users should discover features naturally rather than being confronted with hundreds of options.

---

# Architectural Thinking

Phoenix Builder encourages users to think in architectural concepts.

Instead of manipulating polygons, they manipulate:

- Rooms
- Walls
- Floors
- Roofs
- Windows
- Doors
- Styles
- Surface Recipes
- Building Kits

The software translates these concepts into optimized geometry.

---

# Immediate Feedback

Every action should produce immediate visual feedback.

Examples:

- Ghost previews while dragging
- Live snapping visualization
- Surface highlighting
- Automatic dimension updates
- Real-time style previews

The user should always understand what will happen before committing an action.

---

# Non-Destructive Editing

Nothing should permanently destroy information.

Every operation must remain editable.

Buildings remain editable after:

- Style changes
- Variant changes
- Procedural generation
- Export profile changes

---

# Consistency

Every editor follows the same interaction principles.

Examples:

- Selection behaves identically everywhere.
- Drag-and-drop behaves consistently.
- Inspector panels share the same layout.
- Keyboard shortcuts remain predictable.

Learning one part of Phoenix Builder should make every other part easier to understand.

---

# Speed

The application should minimize repetitive work.

Users should spend time designing architecture rather than performing technical operations.

Whenever possible:

- One click is better than three.
- Automatic defaults are better than mandatory configuration.
- Smart suggestions are better than lengthy dialogs.

---

# Discoverability

Advanced functionality should remain available without cluttering the interface.

Examples:

- Context menus
- Expandable inspectors
- Optional advanced panels
- Search-driven commands
- Command Palette

Power users should become faster over time without beginners feeling intimidated.

---

# Accessibility

Phoenix Builder should remain comfortable during long design sessions.

The interface should support:

- Light and dark appearance
- Adjustable UI scale
- Keyboard navigation
- Mouse-first workflows
- Trackpad gestures
- Future pen input

---

# Error Prevention

The software should prevent mistakes whenever possible.

Examples:

- Invalid placements are previewed before confirmation.
- Snapping suggests valid connections.
- Missing assets generate clear warnings.
- Broken references are automatically detected.

---

# The Ideal Experience

A new user should be able to create a recognizable building within minutes.

An experienced user should be able to assemble complex architecture significantly faster than with traditional modelling workflows.

The interface should always reinforce the philosophy of Phoenix Builder:

> Design architecture instead of managing geometry.

---

End of File
