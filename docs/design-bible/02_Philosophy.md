# Phoenix Builder Design Bible
## 02_Philosophy.md

Version: 1.0.0
Status: Draft

# Philosophy

Phoenix Builder is a procedural architectural assembler built upon intelligent assets.

Its purpose is not to create geometry.

Its purpose is to assemble architecture.

## Core Beliefs

### Architecture First

Users think about buildings, not polygons.

### Progressive Complexity

Phoenix Builder grows with the user.

Level 1: Builder
- Assemble buildings quickly.

Level 2: Variant Editor
- Customize architectural recipes.
- No mesh editing.

Level 3: Specialist Workflow
- Blender + Phoenix SDK.
- Unlimited artistic freedom.

## Non-Destructive Design

Every operation must remain editable.

Nothing should permanently destroy information.

## Deterministic Generation

Every generated building is reproducible from:

- Building Kit
- Rules
- Parameters
- Seed

## Separation of Responsibilities

Blender creates geometry.

Phoenix Builder creates architecture.

Game engines execute the result.

## Intelligent Assets

Every asset carries semantic meaning.

A wall knows it is a wall.

A roof knows it is a roof.

A door knows how it connects.

## Construction Grammar

Architecture is assembled through meaning rather than raw meshes.

The same construction grammar applies whether an asset comes from:
- Phoenix Builder
- Variant Editor
- Blender + Phoenix SDK

## Simplicity

The most common workflow should require the fewest clicks.

Power should emerge through intelligent defaults rather than complex interfaces.

## Guiding Question

Whenever a feature is proposed ask:

"Does this help users design architecture instead of managing geometry?"

If yes, it belongs in Phoenix Builder.

If not, it probably belongs somewhere else.

---

End of File
