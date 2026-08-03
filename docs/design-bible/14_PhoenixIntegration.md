# Phoenix Builder Design Bible
## 14_PhoenixIntegration.md

Version: 2.0.0
Status: Draft

---

# Phoenix Integration

Phoenix Builder is one application within the larger Phoenix Ecosystem.

Each Phoenix application has a single responsibility.

Together they create a complete, open and deterministic pipeline for building games.

---

# The Phoenix Ecosystem

The ecosystem consists of three primary applications.

🔥 Phoenix Forge

Creates intelligent assets.

↓

🏛 Phoenix Builder

Creates intelligent architecture.

↓

🎮 Phoenix Engine

Creates living worlds.

Each application communicates through open formats and shared concepts rather than tightly coupled code.

---

# Single Responsibility

Every Phoenix application exists to solve one problem exceptionally well.

Phoenix Forge

Asset authoring.

Phoenix Builder

Architectural authoring.

Phoenix Engine

Simulation and gameplay.

Whenever a feature is proposed, it should first answer:

"Which application owns this responsibility?"

If the answer is unclear, the feature probably needs to be redesigned.

---

# Shared Language

Although each application performs different tasks, they all speak the same architectural language.

Examples

Building DNA

Surface DNA

Construction Grammar

Material Families

Building Kits

Style Families

Semantic Assets

This shared vocabulary eliminates translation between applications.

---

# Shared Identity

Every exported building keeps its identity.

Example

Church_01

remains

Church_01

inside every application.

This allows references, gameplay systems and future updates to remain synchronized.

---

# Shared Metadata

Metadata should never be discarded.

Examples

Building Type

Room Names

Wall Types

Door Categories

Surface Regions

Accessibility

Gameplay Tags

Everything authored in Builder should remain available to the Engine whenever practical.

---

# Runtime Awareness

Phoenix Engine should understand architecture rather than static meshes.

Instead of asking

"What mesh was clicked?"

the Engine should know

"The player clicked the north entrance door of the church."

This semantic understanding enables richer gameplay while simplifying game logic.

---

# Surface Awareness

Surface DNA may optionally be preserved.

Examples

Burned Wall

Broken Window

Wet Roof

Snow Covered Surface

These states can influence gameplay, weather systems and visual effects.

The Engine is free to use or ignore this information depending on the project.

---

# Intelligent Exports

Export Profiles decide how much information each runtime receives.

SpriteKit

Receives optimized layered sprites and gameplay metadata.

Phoenix Engine

Receives the richest semantic representation.

Other engines receive the most appropriate subset supported by their capabilities.

---

# Shared Versioning

Every exported project stores independent version numbers.

Building DNA Version

Surface DNA Version

Grammar Version

Asset Version

Export Version

Independent versioning improves compatibility across long-lived projects.

---

# Deterministic Pipeline

Every stage of the Phoenix Ecosystem remains deterministic.

Forge

Creates deterministic assets.

Builder

Creates deterministic architecture.

Engine

Simulates deterministic worlds whenever requested.

This philosophy simplifies debugging, collaboration and procedural generation.

---

# Open Standards

The ecosystem should favor open technologies whenever possible.

Examples

glTF

PNG

JSON

SVG

USD (future)

Avoiding proprietary formats protects projects over the long term.

---

# Live Workflow (Future)

Future versions of the ecosystem may communicate directly.

Example

Artist edits a window inside Phoenix Forge.

↓

Builder detects the updated asset.

↓

Building regenerates automatically.

↓

Phoenix Engine refreshes the running scene.

This creates a seamless authoring experience while preserving the independence of each application.

---

# Shared Libraries

Applications may reference common libraries.

Examples

Material Vault

Building Kits

Surface Recipes

Templates

Style Families

These resources should never be duplicated unnecessarily.

---

# Community Ecosystem

The Phoenix Ecosystem is designed to encourage sharing.

Users should be able to publish:

Building Kits

Material Vaults

Surface Recipes

Templates

Export Profiles

Phoenix Forge Assets

Community contributions should integrate naturally with official content.

---

# Backward Compatibility

Compatibility should be maintained whenever possible.

When changes become unavoidable, migration tools should accompany new versions.

Users should never fear updating the ecosystem.

---

# Long-Term Vision

The Phoenix Ecosystem aims to become a complete workflow for game world creation.

Forge creates reusable knowledge.

Builder organizes that knowledge into architecture.

Engine transforms architecture into interactive experiences.

Each application strengthens the others without becoming dependent upon them.

---

# Guiding Principle

The Phoenix Ecosystem is not a collection of applications.

It is a collection of responsibilities.

Each tool performs one responsibility exceptionally well.

Together they provide a coherent and extensible platform for creating games.

---

End of File
