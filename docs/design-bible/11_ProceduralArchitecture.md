# Phoenix Builder Design Bible
## 11_ProceduralArchitecture.md

Version: 2.0.0
Status: Draft

---

# Procedural Architecture

Procedural generation in Phoenix Builder exists to accelerate creativity.

It does not replace the designer.

Instead, it proposes architectural solutions that remain completely editable.

Every generated result can be modified manually.

Nothing is permanent.

Nothing is hidden.

Nothing depends on artificial intelligence.

---

# Philosophy

Phoenix Builder generates architecture using explicit rules.

Every decision is deterministic.

Every result can be reproduced.

Every variation can be regenerated.

Users should always understand why something was generated.

---

# Deterministic Generation

Every procedural system depends on:

• Building DNA

• Construction Grammar

• Building Kit

• Surface DNA

• Parameters

• Random Seeds

Given identical inputs, the software always generates identical outputs.

This guarantees reproducibility across platforms and over time.

---

# Procedural Scope

Procedural generation may operate at several levels.

## Component Level

Generate:

• Window spacing

• Column repetition

• Roof beams

• Railings

• Roof tiles

• Floor supports

---

## Room Level

Generate:

• Interior walls

• Corridors

• Ceiling beams

• Door placement

• Lighting suggestions

---

## Building Level

Generate:

• Roofs

• Staircases

• Foundations

• Balconies

• Chimneys

• Gutters

• Courtyards

---

## Template Level

Generate:

• Houses

• Churches

• Warehouses

• Shops

• Schools

• Castles

• Factories

---

## District Level (Future)

Generate:

• Streets

• Sidewalks

• Building lots

• Parks

• Plazas

• Rivers

• Bridges

---

# Generation Workflow

Every procedural operation follows the same sequence.

Architecture

↓

Construction Grammar

↓

Building Rules

↓

Constraints

↓

Random Seeds

↓

Validation

↓

Preview

↓

User Approval

↓

Generation

The user remains in control throughout the process.

---

# Architectural Rules

Rules define architectural logic.

Examples

A church should contain:

• Nave

• Entrance

• Sanctuary

Optional:

• Bell Tower

• Side Aisles

• Buttresses

• Transept

Different architectural styles may implement these rules differently while preserving the same functional structure.

---

# Rule Modules

Rules are grouped into reusable modules.

Examples

Residential Rules

Commercial Rules

Industrial Rules

Religious Rules

Military Rules

Fantasy Rules

Science Fiction Rules

Rule modules allow Building Kits to share procedural behavior.

---

# Constraints

Procedural generation respects explicit constraints.

Examples

Maximum height

Minimum room size

Door accessibility

Roof angle

Window spacing

Wall thickness

Budget limits

Gameplay restrictions

Constraints are never ignored.

If conflicting constraints exist, the user is notified.

---

# Randomization

Randomness exists only where appropriate.

Every procedural subsystem owns its own seed.

Examples

Building Seed

Roof Seed

Window Seed

Material Seed

Decoration Seed

Vegetation Seed

Changing one seed should never affect unrelated systems.

---

# Controlled Randomness

Every procedural feature supports three modes.

Manual

The user defines everything.

Assisted

Phoenix Builder proposes sensible defaults while allowing immediate editing.

Automatic

The system generates complete solutions using deterministic rules.

Switching between modes never destroys information.

---

# Architectural Suggestions

Construction Grammar continuously evaluates the project.

When opportunities are detected, Phoenix Builder may suggest improvements.

Examples

Missing gutters

Add roof overhang?

Generate support columns?

Align windows?

Complete balcony railing?

Generate interior staircase?

Suggestions remain optional.

The software assists rather than interrupts.

---

# Live Preview

Every procedural operation generates a preview before committing changes.

The preview communicates:

Geometry

Affected areas

New elements

Removed elements

Warnings

Estimated performance impact

Users always know what will happen before accepting.

---

# Progressive Generation

Generation should occur incrementally.

Only affected areas are regenerated.

Changing a single window should not regenerate the entire building.

Incremental regeneration improves responsiveness on large projects.

---

# Architectural Styles

Procedural generation is style-independent.

The same template may produce:

Victorian

Modern

Mediterranean

Japanese

Industrial

Sci-Fi

Fantasy

Style affects implementation rather than architectural intent.

---

# Procedural Decoration

Decorative elements are generated using semantic rules.

Examples

Street lamps near entrances.

Drainpipes below roof edges.

Signs near commercial buildings.

Air conditioners on modern structures.

Vines on abandoned buildings.

The user can remove or edit every generated decoration.

---

# Expansion System

Building Kits may introduce additional procedural rules.

Examples

Japanese Kit

• Tatami layout

• Sliding doors

• Engawa generation

Medieval Kit

• Timber framing

• Stone foundations

• Wooden shutters

Sci-Fi Kit

• Energy conduits

• Modular panels

• Ventilation systems

Each kit extends Phoenix Builder without modifying the core engine.

---

# Performance

Procedural generation should remain interactive.

The engine should:

Cache previous results.

Reuse unchanged components.

Evaluate dependencies.

Perform heavy calculations asynchronously whenever possible.

Maintain deterministic output regardless of execution order.

---

# Future Possibilities

Future versions may support:

Multi-building generation.

District templates.

Village templates.

Castle complexes.

Road networks.

Infrastructure generation.

Historical evolution.

Seasonal adaptation.

Disaster variants.

These systems should build upon the same procedural architecture rather than introducing separate workflows.

---

# Relationship to Phoenix Forge

Phoenix Forge provides the intelligent assets that procedural systems consume.

A Building Kit authored in Phoenix Forge automatically becomes available for procedural generation inside Phoenix Builder.

This guarantees that custom assets participate in procedural workflows exactly like native assets.

---

# Relationship to Phoenix Engine

Phoenix Builder generates architectural data.

Phoenix Engine simulates what happens after construction.

The Builder decides how a city is built.

The Engine decides how the city lives.

---

# Guiding Principle

Procedural generation should eliminate repetitive work.

It should never eliminate creative decisions.

Every generated building remains fully understandable, fully editable and fully reproducible.

---

End of File
