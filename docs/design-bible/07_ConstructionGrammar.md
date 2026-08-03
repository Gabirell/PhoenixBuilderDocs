# Phoenix Builder Design Bible
## 07_ConstructionGrammar.md

Version: 2.0.0
Status: Draft

---

# Construction Grammar

Construction Grammar is the semantic language of Phoenix Builder.

It describes **what every architectural element is**, **what it does**, and **how it relates to every other element**.

Unlike traditional 3D software, Phoenix Builder does not assemble buildings from meshes.

It assembles buildings from meaning.

Meshes are only one possible representation.

---

# The Core Principle

Traditional software asks:

> "Which mesh should I place here?"

Phoenix Builder asks:

> "What architectural role belongs here?"

The software then chooses the most appropriate asset to fulfill that role.

---

# Architectural Roles

Every intelligent asset has one or more architectural roles.

Examples include:

- Exterior Wall
- Interior Wall
- Foundation
- Floor
- Ceiling
- Roof
- Column
- Beam
- Door
- Window
- Stair
- Balcony
- Railing
- Chimney
- Elevator
- Decoration

Roles define purpose, not appearance.

---

# Hierarchical Grammar

Construction Grammar is hierarchical.

```
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
```

Every level inherits information from the level above.

---

# Parent–Child Relationships

Each architectural object understands its relationship with neighboring objects.

For example:

A roof belongs to a building.

A window belongs to a wall.

A doorknob belongs to a door.

A gutter belongs to a roof edge.

Changing a parent automatically updates its children whenever possible.

---

# Semantic Connections

Connections are more than sockets.

Each connection also defines architectural intent.

Examples:

Door → Wall

Window → Exterior Wall

Balcony → Exterior Wall

Chimney → Roof

Stair → Floor

These rules prevent invalid constructions while reducing user effort.

---

# Intelligent Placement

When dragging an asset into the scene, Phoenix Builder evaluates:

1. Construction Grammar
2. Sockets
3. Building Rules
4. Physical Constraints
5. User Intent

Only then is the placement suggested.

---

# Building Intelligence

Construction Grammar allows buildings to behave intelligently.

Examples:

Removing a wall updates connected openings.

Changing roof pitch adjusts gutters.

Adding another floor extends staircases.

Changing floor height updates doors.

Moving a room relocates connected windows.

The user edits architecture rather than geometry.

---

# Grammar Layers

Construction Grammar operates on several levels.

## Structural Grammar

Defines load-bearing relationships.

Examples:

- Foundations support walls.
- Walls support roofs.
- Columns support beams.

---

## Spatial Grammar

Defines organization.

Examples:

- Rooms belong to floors.
- Floors belong to buildings.
- Hallways connect rooms.

---

## Functional Grammar

Defines purpose.

Examples:

- Doors provide access.
- Windows provide light.
- Roofs provide protection.

---

## Visual Grammar

Defines appearance rules.

Examples:

- Cornices align horizontally.
- Windows repeat rhythmically.
- Roof tiles follow slope direction.

---

# Rule Evaluation

Rules should never feel restrictive.

Instead they act as intelligent assistants.

The software should explain *why* a placement is invalid and suggest valid alternatives whenever possible.

---

# Building Templates

Templates are nothing more than predefined Construction Grammar.

For example:

A church template defines:

- Nave
- Aisles
- Tower
- Entrance
- Sanctuary

A medieval kit and a modern kit may share the same grammar while producing entirely different architecture.

---

# Variants

Variants modify implementation while preserving grammar.

A wooden window and a steel window perform the same architectural role.

Only their realization changes.

---

# Blender Integration

Assets created in Blender must preserve Construction Grammar through PBS metadata.

This allows custom assets to participate in every intelligent workflow exactly like native assets.

---

# Future Possibilities

Construction Grammar enables features such as:

- Automatic stairs
- Automatic foundations
- Automatic roof generation
- Automatic trim assignment
- Automatic structural validation
- Automatic accessibility rules
- Automatic LOD generation
- Procedural city generation

These are consequences of semantic understanding rather than isolated features.

---

# Guiding Principle

Geometry answers:

> "How is this object built?"

Construction Grammar answers:

> "Why does this object exist?"

Phoenix Builder always prioritizes the second question.

---

End of File
