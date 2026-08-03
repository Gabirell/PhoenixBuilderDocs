# Phoenix Builder Design Bible
## 16_DecisionLog.md

Version: 2.0.0
Status: Living Document

---

# Decision Log

The Decision Log records every significant architectural decision made during the development of Phoenix Builder.

Its purpose is not only historical.

It explains *why* a decision was made, what alternatives were considered, and what consequences are expected.

Future changes should extend this log rather than silently replacing previous decisions.

---

# Format

Every decision receives:

Decision ID

Date

Status

Author

Summary

Context

Decision

Alternatives Considered

Consequences

---

# PB-001

## Phoenix Builder is an Architectural Assembler

Status

Accepted

---

### Context

General-purpose modelling applications already exist.

Attempting to compete with Blender would dramatically increase project scope.

---

### Decision

Phoenix Builder assembles architecture.

Geometry creation belongs to Phoenix Forge (Blender).

---

### Consequences

The application remains focused, simpler to maintain and easier to learn.

---

# PB-002

## Intelligent Assets

Status

Accepted

---

### Context

Meshes alone cannot support procedural architecture.

---

### Decision

Every asset carries semantic metadata describing its architectural role.

Examples:

Wall

Window

Door

Cornice

Roof

Foundation

---

### Consequences

Procedural generation becomes deterministic and meaningful.

---

# PB-003

## Everything is Editable

Status

Accepted

---

### Decision

No procedural operation permanently destroys user work.

Generated content can always be edited manually.

---

### Consequences

Users remain in control of every project.

---

# PB-004

## Three Levels of Editing

Status

Accepted

---

### Decision

Phoenix Builder supports three editing workflows.

Simple

Variant

Specialist (Phoenix Forge)

---

### Context

Most users should never need Blender.

Advanced users should never feel limited.

---

### Consequences

The application scales naturally from indie developers to technical artists.

---

# PB-005

## Progressive Complexity

Status

Accepted

---

### Decision

Simple workflows expose only essential controls.

Advanced controls appear only when requested.

---

### Consequences

The interface remains approachable while retaining professional capabilities.

---

# PB-006

## Building DNA

Status

Accepted

---

### Decision

Projects store architectural intent rather than meshes.

Geometry is generated from Building DNA.

---

### Consequences

Buildings become deterministic, portable and engine independent.

---

# PB-007

## Surface DNA

Status

Accepted

---

### Decision

Appearance remains independent from structure.

---

### Consequences

Entire projects can change architectural style without rebuilding geometry.

---

# PB-008

## Phoenix Forge

Status

Accepted

---

### Decision

Asset creation is handled by a dedicated Blender add-on named Phoenix Forge.

---

### Consequences

Phoenix Builder remains focused exclusively on architectural assembly.

---

# PB-009

## Export Profiles

Status

Accepted

---

### Decision

Users choose project goals instead of technical formats.

Examples:

Mobile 2D

Mobile 3D

PC

Console

Presentation

Prototype

---

### Consequences

Phoenix Builder handles optimization automatically.

---

# PB-010

## One-Person Rule

Status

Accepted

---

### Context

The Phoenix Ecosystem is designed to be developed and maintained primarily by a single developer.

---

### Decision

Every architectural decision must consider long-term maintainability by one person.

Complexity is introduced only when it clearly provides lasting value.

---

### Consequences

Features should be modular.

Documentation must stay synchronized.

Automation should reduce repetitive work.

The ecosystem grows incrementally through stable milestones.

---

# PB-011

## Architectural X-Ray

Status

Accepted

---

### Decision

Buildings can unfold visually to reveal interiors.

Animations include roof lifting, wall fading, floor separation and semantic overlays.

A Performance Mode disables animations and heavy visual effects.

---

### Consequences

The feature improves usability without preventing use on lower-end hardware.

---

# PB-012

## Shared Phoenix SDK

Status

Proposed

---

### Context

Forge, Builder and Engine all use the same architectural concepts.

---

### Proposal

Create a shared Phoenix SDK containing common data structures and serialization.

---

### Expected Benefits

One implementation.

Consistent file formats.

Simpler maintenance.

Cleaner ecosystem.

---

# Maintaining the Decision Log

Every major architectural change should create a new decision entry.

Existing accepted decisions should never be rewritten.

If a decision changes, a new entry should explain why.

This preserves the evolution of the project and provides historical context for future development.

---

# Guiding Principle

A good decision is one whose reasoning is still understandable years later.

The Decision Log exists to preserve that reasoning.

---

End of File
