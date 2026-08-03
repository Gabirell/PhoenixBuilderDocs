# Phoenix Builder Design Bible
## 15_Roadmap.md

Version: 2.0.0
Status: Living Document

---

# Roadmap

Phoenix Builder is a long-term project.

Its development philosophy is based on steady evolution rather than large rewrites.

Every release should improve an already usable application.

No milestone should exist only as preparation for a future milestone.

Every version should solve real problems for real developers.

---

# Core Development Principles

Development follows seven principles.

## 1

Always shippable.

At the end of every milestone, Phoenix Builder should remain stable and usable.

---

## 2

One-person sustainable.

Every feature must be maintainable by a single developer.

Complexity is added only when it clearly improves the user experience.

---

## 3

Architecture before features.

Strong foundations reduce future work.

Features built on poor architecture become technical debt.

---

## 4

Documentation evolves together with code.

Every important architectural decision updates:

Design Bible

Decision Log

Roadmap

Architecture Documentation

Developer Notes

---

## 5

Performance is a feature.

Fast interaction is never postponed until the end.

---

## 6

Determinism everywhere.

Projects should always be reproducible.

---

## 7

Progressive Complexity.

Simple users remain productive.

Advanced users remain unrestricted.

---

# Phase 1

## Foundation

Goal

Create a reliable architectural editor.

Features

• Document-based application

• Scene management

• Asset Library

• Hierarchy

• Inspector

• SceneKit viewport

• Camera

• Selection

• Undo / Redo

• Basic snapping

• Saving projects

Deliverable

A user can manually assemble simple buildings.

Status

Current Phase

---

# Phase 2

## Intelligent Assembly

Goal

Replace simple placement with semantic construction.

Features

Construction Grammar

Sockets

Semantic Assets

Automatic wall joining

Automatic corners

Door insertion

Window insertion

Roof generation

Foundation generation

Live validation

Result

Building architecture instead of placing boxes.

---

# Phase 3

## Surface System

Goal

Separate appearance from geometry.

Features

Surface DNA

Surface Recipes

Style Families

Material Vault

Trim Templates

Automatic UV assignment

Decal Layers

Weathering

Damage

Result

One building.

Infinite appearances.

---

# Phase 4

## Building Templates

Goal

Buildings become reusable architectural assets.

Features

Building Templates

Building DNA

Template Library

Parameterized buildings

Building presets

Building inheritance

Template editing

Random variation

Result

Create one church.

Generate hundreds of churches.

---

# Phase 5

## Procedural Architecture

Goal

Automate repetitive architectural work.

Features

Rule engine

Seeds

Constraint system

Building generators

Room generators

Roof generators

Facade generators

Decoration generators

Validation

Result

Procedural buildings that remain fully editable.

---

# Phase 6

## Phoenix Forge

Goal

Complete asset creation workflow.

Features

Blender Add-on

Asset exporter

Metadata editor

Socket editor

Trim authoring

Asset validation

LOD authoring

Collision authoring

Preview exporter

Result

Artists create intelligent assets.

Builder assembles them.

---

# Phase 7

## Export Profiles

Goal

Support multiple engines.

Profiles

Phoenix Engine

SpriteKit

Unity

Godot

Unreal

glTF

Features

Automatic optimization

Texture atlases

Sprite slicing

LOD generation

Collision generation

Metadata export

Result

Build once.

Export anywhere.

---

# Phase 8

## Community Ecosystem

Goal

Make Phoenix Builder expandable.

Features

Community Building Kits

Style Libraries

Surface Recipes

Export Profiles

Plugin API

Template Marketplace

Documentation Portal

Result

Community content becomes first-class.

---

# Phase 9

## District Builder

Goal

Expand from buildings to neighborhoods.

Features

Street generation

Building lots

Sidewalks

Parks

Vegetation

Utility networks

District Templates

Road grammar

Result

Entire neighborhoods become procedural.

---

# Phase 10

## City Builder

Future Vision

Procedural cities.

Historical evolution.

District interaction.

Infrastructure.

Traffic.

Population support.

This phase belongs to the long-term future.

It is intentionally outside the initial scope.

---

# Continuous Improvement

Certain areas evolve continuously.

Performance

User Interface

Documentation

Accessibility

Localization

Asset Libraries

Developer Experience

Testing

None of these wait for major releases.

---

# Success Metrics

Progress is not measured by lines of code.

Instead, Phoenix Builder should continuously improve:

Time required to create a building.

Number of reusable assets.

Export quality.

Editor responsiveness.

Documentation quality.

User satisfaction.

Community contributions.

Maintainability.

---

# The Friday Night Test

Every milestone should pass one simple test.

Imagine returning to the project after two months away.

Within thirty minutes you should understand:

Where development stopped.

What was completed.

What comes next.

Why previous decisions were made.

If this is not possible, documentation has failed.

---

# Long-Term Vision

Phoenix Builder should become the fastest way to create game-ready architecture.

Not because it automates creativity.

Because it removes unnecessary work.

Artists create architecture.

Phoenix Builder handles repetition.

---

# Final Milestone

The project reaches maturity when a single developer can:

Create intelligent assets inside Phoenix Forge.

Assemble an entire town inside Phoenix Builder.

Export directly into Phoenix Engine.

Begin designing gameplay immediately.

Without manually rebuilding or optimizing content.

---

# Guiding Principle

The roadmap is a compass.

Not a contract.

The destination remains constant.

The path may evolve as Phoenix Builder grows.

---

End of File
