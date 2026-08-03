# Phoenix Builder Design Bible
## 00_Index.md

Version: 2.0.0
Status: Living Document
Author: Phoenix Project (Gabriel Netto)
Site: gabrielnetto.com
Revision: 2

---

# Phoenix Builder

> **Design architecture. Not geometry.**

Phoenix Builder is a **procedural architectural assembler built upon intelligent assets**, designed to create game-ready buildings quickly, consistently and non-destructively.

It is not a modelling package.

It is not a CAD application.

It is not a level editor.

Instead, Phoenix Builder occupies the space between asset creation and game engines, allowing artists and developers to assemble architecture from intelligent building kits while automatically handling appearance, optimization and export.

The software exists to let creators think like architects instead of 3D modellers.

---

# The Phoenix Ecosystem

Phoenix Builder is one application inside the Phoenix Ecosystem.

Each application has a single responsibility.

```text
🔥 Phoenix Forge
Create Intelligent Assets
(Blender Add-on)

        │

        ▼

🏛 Phoenix Builder
Assemble Intelligent Architecture

        │

        ▼

🎮 Phoenix Engine
Simulate Living Worlds
```

Every application speaks the same language.

Building DNA.

Surface DNA.

Construction Grammar.

Material Families.

Style Families.

Semantic Assets.

The ecosystem grows through specialization rather than duplication.

---

# The Phoenix Philosophy

Phoenix follows several fundamental principles.

Architecture instead of geometry.

Progressive Complexity.

Deterministic generation.

Everything remains editable.

Reuse before duplication.

Build once. Export anywhere.

Open standards before proprietary formats.

Documentation grows together with code.

One developer should be capable of understanding and maintaining the entire ecosystem.

These principles are explained throughout this Design Bible.

---

# Purpose of this Design Bible

The Design Bible defines the long-term vision of Phoenix Builder.

It documents:

• Philosophy

• User Experience

• Interface

• Asset Architecture

• Procedural Systems

• Rendering

• Export Pipeline

• Roadmap

• Architectural Decisions

Every important implementation should be consistent with this document.

When implementation and documentation disagree, documentation should be updated before code evolves.

---

# Vision

Phoenix Builder is not another modelling application.

It is an architectural authoring platform.

Users create:

• Buildings

• Building Kits

• Surface Libraries

• Architectural Templates

• Style Families

rather than meshes.

Geometry becomes an implementation detail.

Architecture becomes the design language.

---

# Long-Term Goal

Phoenix Builder should become the fastest way to create reusable architecture for games.

A single project should be capable of producing:

• SpriteKit Assets

• Phoenix Engine Assets

• Unity Prefabs

• Godot Scenes

• Unreal Actors

• glTF

• USD (future)

without rebuilding anything.

---

# Core Technologies

Phoenix Builder is built around several core systems.

• Intelligent Assets

• Construction Grammar

• Building DNA

• Surface DNA

• Surface Recipes

• Style Families

• Trim Templates

• Material Vault

• Semantic Metadata

• Deterministic Procedural Generation

These systems work together to create editable architecture instead of static geometry.

---

# Editing Philosophy

Phoenix Builder adapts to different kinds of creators.

Three editing levels are available.

## Simple

Fast building assembly.

Minimal decisions.

Ideal for indie developers and rapid prototyping.

---

## Variant

Customize existing intelligent assets.

Create new architectural styles.

Modify trims, materials and appearance.

No external tools required.

---

## Specialist

Create entirely new intelligent assets using Phoenix Forge.

Professional workflow.

Unlimited artistic freedom.

---

# Progressive Complexity

Complexity should appear only when requested.

Beginners should feel productive immediately.

Experts should never feel limited.

This philosophy guides every user interface decision throughout the Phoenix Ecosystem.

---

# One-Person Sustainability

Phoenix Builder is intentionally designed around solo development.

Every subsystem should remain:

Understandable.

Documented.

Modular.

Replaceable.

Maintainable.

If a future feature dramatically increases long-term complexity without equivalent value, it should be reconsidered.

---

# Asset Pipeline

```text
Blender

↓

Phoenix Forge

↓

Intelligent Assets

↓

Building Kits

↓

Building Templates

↓

Phoenix Builder

↓

Export Profiles

↓

Phoenix Engine
Unity
Godot
Unreal
SpriteKit
```

Each application performs one responsibility exceptionally well.

---

# Documentation Structure

## 01_Manifesto.md

Why Phoenix exists.

The philosophy behind the ecosystem.

---

## 02_Philosophy.md

Fundamental architectural principles.

---

## 03_UserExperience.md

How Phoenix Builder should feel.

Interaction philosophy.

Progressive Complexity.

---

## 04_Interface.md

Complete UI specification.

Panels.

Editors.

Viewport.

Navigation.

---

## 05_BuildingWorkflow.md

From an empty project to a finished building.

The complete architectural workflow.

---

## 06_TrimTemplates.md

Semantic Trim Templates.

Trim philosophy.

Trim editing.

Trim libraries.

---

## 07_SurfaceRecipes.md

Surface DNA.

Material Vault.

Style Families.

Weathering.

Decals.

Damage.

Procedural appearance.

---

## 08_ConstructionGrammar.md

Architectural semantics.

Sockets.

Construction roles.

Automatic assembly.

---

## 09_AssetArchitecture.md

Phoenix Primitives.

Phoenix Building Assets.

Phoenix Forge.

Asset metadata.

Intelligent Assets.

---

## 10_BuildingDNA.md

Parametric architectural description.

Building Templates.

Deterministic buildings.

---

## 11_ProceduralArchitecture.md

Rule-based generation.

Seeds.

Constraints.

Templates.

Architectural Profiles.

---

## 12_RenderingAndViewport.md

Viewport philosophy.

Architectural X-Ray.

Performance modes.

Preview system.

Visualization.

---

## 13_ExportProfiles.md

Build once.

Export anywhere.

Optimization.

SpriteKit.

Phoenix Engine.

Unity.

Godot.

Unreal.

---

## 14_PhoenixIntegration.md

Shared ecosystem.

Phoenix SDK.

Shared metadata.

Future live workflows.

---

## 15_Roadmap.md

Long-term development plan.

Milestones.

Solo development strategy.

---

## 16_DecisionLog.md

Permanent architectural decisions.

Historical reasoning.

Future evolution.

---

# Companion Documents

Outside this Design Bible, the project also maintains:

• README (Manifesto)

• Architecture Documentation

• Decision Log

• Developer Journal

• Changelog

• API Documentation

• Coding Guidelines

• Phoenix SDK Documentation (future)

These documents evolve together.

---

# Living Documentation

Phoenix Builder is expected to evolve for many years.

The documentation should evolve with it.

Architectural decisions are never silently changed.

Every important change should leave a trace.

The documentation is as important as the source code.

---

# Final Principle

Whenever a new feature is proposed, ask four questions.

1.

Does it help users design architecture instead of geometry?

2.

Does it respect Progressive Complexity?

3.

Can one developer reasonably maintain it?

4.

Will it still make sense ten years from now?

If the answer to any question is "no", the feature should be reconsidered.

---

End of File
