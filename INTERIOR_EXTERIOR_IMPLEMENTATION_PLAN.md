# Interior & Exterior Procedural Phase — Implementation Plan

Status: Proposal / Planning (not implemented)
Author: Claude, at Gabriel's request
Date: 2026-10-02
Scope: How to add a big "Interior and Exterior" building/furnishing phase to Phoenix Builder — procedural placement of walls, furniture, facades, etc. — **without breaking anything already built.**

This document does not implement anything. It is the output of reading, in full:

- `PROCEDURAL PHOENIX BUILDER CHATGPT.rtf` (3,178 lines — two ChatGPT conversations: the "JSON cascade" idea, and a full concrete schema design)
- `3D Performance & Loading Time Optimization Guide.rtf` (1,086 lines — mostly Unreal/Houdini-specific; final section translated for "Phoenix Builder")
- The entire `docs/design-bible/` (16 chapters) relevant to this topic: `01_Vision`, `02_Philosophy`, `04_Interface`, `05_BuildingWorkflow`, `06_ArchitecturalSurfaceSystem`, `07_ConstructionGrammar`, `08_AssemblyEngine`, `09_AssetEcosystem`, `10_BuildingDNA`, `11_ProceduralArchitecture`, `12_RenderingAndViewport`, `14_PhoenixIntegration`, `15_Roadmap`
- `docs/specifications/` (`pbp_format.md`, `pba_format.md`, `pal_ontology.md`, `README.md`)
- `docs/pal/` (`grammar.md`, `constraints.md`, `rules.md`, `style_system.md`)
- A full audit of the current Phoenix Builder Swift codebase (every system this plan touches)

Where this plan says "the canon," it means the design-bible + specs above — the project's own, already-authored, already-accepted source of truth. Where it says "today" or "current code," it means what is actually implemented right now, verified by reading the source, not assumed.

---

## 1. The single most important finding, up front

**"Interior" and "Exterior" do not exist anywhere in the canon as an editor phase, a sidebar section, or a workflow stage.** Every occurrence of those exact words across all 16 design-bible chapters is a **SpriteKit 2D sprite-export layer name** (`Exterior`, `Interior Walls`, alongside `Roof`, `Upper Walls`, `Floor`, `Decoration`, `Shadows`, `Collision Masks` — see `05_BuildingWorkflow.md` and `06_ArchitecturalSurfaceSystem.md`). It is not a 3D authoring concept anywhere in the existing plan.

This isn't a contradiction of your request — it just means one of two things, and **I need you to tell me which one** before real implementation starts (Section 10 has the concrete question):

- **(a)** You want to introduce a genuinely new editorial concept the canon hasn't named yet: two organizing phases — "Interior" (rooms, furniture, interior walls, interior materials) and "Exterior" (facade, exterior walls, roof dressing, eventually landscaping/site) — sitting alongside or replacing today's Rooms → Walls → Furniture → Roof pipeline.
- **(b)** You're using "interior/exterior" loosely to mean "the stuff inside the building and the stuff outside it," and what you actually want is the **procedural rule/grammar system** (Construction Grammar, Resolution, Budgets, Seeds — Chapters 7, 8, 10, 11) applied to walls and furniture, without necessarily renaming or restructuring the sidebar.

This plan is written to support either answer, because the underlying engineering work (Section 6 onward) is the same either way — only the UI framing (Section 9) changes.

---

## 2. What already exists vs. what's aspirational

This table is the plan's foundation. Nothing below was guessed — it comes from reading the actual Swift source.

| Concept (canon name) | Canon chapter | Status in current code |
|---|---|---|
| Building DNA (semantic, renderer-independent scene data) | `10_BuildingDNA` | **Already satisfied in spirit.** `BuildingScene`/`RoomPlacement`/`PhoenixPrimitive`/`FurniturePlacement` are pure semantic data (positions, floor index, `palClass` string, dimensions) — SceneKit geometry is generated fresh from them on every render, never stored. This is exactly what Chapter 10 asks for. |
| PAL roles (`Wall`, `Door`, `Window`, `Roof`, `Stair`, `Elevator`, `Fireplace`, …) | `07_ConstructionGrammar`, `pal_ontology.md` | **Implemented.** `palClass` strings match the canon's role list almost exactly. |
| Random seed, deterministic generation | `11_ProceduralArchitecture`, `10_BuildingDNA` | **Stored but 100% unused.** `BuildingScene.randomSeed: UInt64` exists with an empty `didSet` and a literal `// Future: Regenerate procedural variations` comment. Nothing reads it. |
| Per-subsystem seeds (Building/Roof/Window/Material/Decal/Vegetation Seed) | `10_BuildingDNA`, `11_ProceduralArchitecture` | Not implemented — no hashing chain exists. |
| Kit system (`AssetKit`: id, name, tags, author, version) | `09_AssetEcosystem` | **Implemented**, but pure metadata grouping. No resolution logic, no "pick a piece by style" query. |
| Socket system (`SnapSocket: {id, position, normal, type}`) | `08_AssemblyEngine`, `pal/rules.md` | **Implemented, narrower than canon.** Canon wants Position, Rotation, Normal, Size, Priority, Grammar Type, Connection Rules, Mirror Rules, Scale Rules. |
| Semantic asset rules (allowed rooms, tags-as-vocabulary, placement probability) | RTF §6, `09_AssetEcosystem` | **Does not exist at all.** Confirmed zero fields anywhere in `AssetDefinition`. Fully greenfield. |
| Procedural furniture/object placement of any kind | RTF §1–2, `07_ConstructionGrammar` | **Does not exist.** `FurniturePlacement` → `BuildingElement` conversion is 100% manual, one item at a time, via `ConvertFurnitureTo3DCommand`. |
| Resolution / LOD tiers (R0–R4, block/shell/facade/modular/hero) | RTF §9–11, `08_AssemblyEngine` | **Does not exist in the app**, but is already **formally specified at the file-format level**: `pba_format.md`'s `lods: [{lod_level, max_distance, mesh_node_name}]`. This is the one concrete, already-agreed LOD spec — see Section 7. |
| Budget system (triangle/material/draw-call budgets, cascading, priority-based degradation) | RTF §13–14, §27–28 | Does not exist. Fully greenfield, but well-specified in the RTF. |
| Construction Grammar (Structural/Spatial/Functional/Visual layers) | `07_ConstructionGrammar` | Does not exist as a formal system. Scattered partial equivalents exist (the `floor` field, room↔floor geometric matching, `floorsMissingStairs`). |
| Style Family (swap a building's whole look in one click) | `06_ArchitecturalSurfaceSystem`, `pal/style_system.md` | Does not exist. `TrimSheetMaterialManager` + the Materials sidebar section are a narrow, real starting point. |
| "Wing" (Building → Wing → Floor → Room hierarchy level) | `07_ConstructionGrammar` | Named in canon, zero implementation, zero spec. |
| Phoenix Template (`.pbt`, reusable building assemblies) | `09_AssetEcosystem` | Named in canon, **no format spec exists yet** (only `.pbp`/`.pba`/ontology have specs). |
| Terrain adaptation (foundation extension, terrain cut/fill) | `08_AssemblyEngine` | Zero terrain concept exists anywhere in the app. |
| Validate (overlap, missing entrance, missing stairs, obstructed door) | `pal/constraints.md`, `08_AssemblyEngine` | **Implemented and real** (this session's own work) — already matches the canon's "Builder Scene Validation" and "Reachability Check" almost exactly. A good model for how procedural validation should be surfaced. |
| SceneKit-specific performance strategy | `12_RenderingAndViewport` | **Not specified anywhere** — that chapter stays at UX-philosophy level (named modes like Quality/Balanced/Performance, no mechanism). The Unreal/Houdini RTF's mechanisms (HLSL masking, Houdini HDAs, UE auto-instancing) are not portable. The `.pba` `lods` field remains the only concrete target (Section 7). |
| "Upper floors fade while editing lower levels," "walls fade while placing furniture" | `12_RenderingAndViewport` | **Already built**, this session — `AdjacentFloorGhostOverlay`, `phaseVisibility`, `WallContextOverlay`. Confirms current direction is already tracking the canon closely. |

**Conclusion of this section:** the data-model foundation (Building DNA, PAL roles, Commands/Undo) is sound and the canon itself says so implicitly — nothing here argues for a rewrite. The gap is entirely in a semantic layer that doesn't exist yet: tags-as-vocabulary, rules, budgets, resolution, seeding. That layer is additive by construction.

---

## 3. The one principle every later decision should be checked against

From `10_BuildingDNA.md` and `14_PhoenixIntegration.md`, restated for this plan:

> **Intent vs. Representation.** The data says *"this is a bedroom, it needs a bed."* It should never need to say *"place Bed_03.usdc at (1.234, 0, 4.532)."* The same intent should be resolvable into a hero room (real bed + mattress + pillows + props), a game-ready room (one optimized mesh), or a background silhouette (one box) — and still be semantically the same bedroom underneath.

Practically, for this codebase, that means:

- `RoomPlacement`, `PhoenixPrimitive`, `FurniturePlacement` stay as they are — they already **are** the intent layer.
- New rule/budget/resolution data attaches to assets and rooms as **additive, optional metadata**, not a replacement for the existing structs.
- Procedural generation produces more `FurniturePlacement`/`PhoenixPrimitive` instances through the **existing Command system** — it does not invent a parallel pipeline that bypasses undo, persistence, or the 2D/3D views.

---

## 4. Guiding constraints (how "don't break what exists" actually gets enforced)

1. **Every new field on an existing `Codable` struct is added with `decodeIfPresent(...) ?? <default>`**, exactly like `scaleCorrection`, `upAxis`, `floor`, `allFloorsVisibility` were added this session. Old `.phoenix` files keep loading. This is already a proven, repeated pattern in this codebase — reuse it, don't reinvent it.
2. **No existing `Command` type's behavior changes.** New behavior = new `Command` types (`ApplyRoomRuleCommand`, `GenerateFacadeCommand`, etc.), following the bulk-add/bulk-remove, fully-undoable shape already established this session (`AddFloorCommand`, `AddRoomPrimitiveCommand`, `SwapFloorsCommand`).
3. **No existing sidebar section is removed or repurposed.** New capability is additive: either a new action inside an existing section (e.g., a "Fill Procedurally" button inside Furniture) or a genuinely new section, never a silent behavior change to Rooms/Walls/Roof/Furniture as they work today.
4. **Procedural output is always a normal, editable, deletable instance of something that already exists.** A generated bed is a `FurniturePlacement` the user can drag, resize, or delete exactly like a manually placed one — never a special "generated" object type with different rules.
5. **Nothing runs automatically on open/save.** Procedural generation is always an explicit user action ("Fill Room," "Apply Style," "Generate Facade") — matching the canon's "Live Preview → User Approval → Generation" workflow (`11_ProceduralArchitecture.md`) and this app's existing confirmation-dialog pattern (the floor-duplicate prompt from this session).
6. **The rule engine is NOT built first.** Per the RTF's own explicit instruction (RTF Part B, §34) and the canon's phased rollout: data contracts first, engine later. This plan's phases follow that order.

---

## 5. Proposed data model additions (all additive)

### 5.1 `AssetDefinition` — new optional fields

```swift
// All new, all optional with safe defaults via decodeIfPresent — exact
// precedent: scaleCorrection/upAxis added earlier this session.
public struct AssetDefinition {
    // existing fields unchanged: id, name, category, meshPath, thumbnailPath,
    // dimensions, sockets, materials, kitID, tags, upAxis, scaleCorrection

    /// Rooms this asset makes semantic sense in — "living_room", "bedroom",
    /// "kitchen", etc. Empty = no restriction (today's behavior, unchanged).
    public var allowedRooms: [String] = []

    /// How strongly a rule engine should prefer this asset when several
    /// candidates share the same tags — not a hard requirement.
    public var placementWeight: Float = 1.0

    /// Per-instance LOD table, directly matching the already-specified
    /// pba_format.md `lods` field — {distance, meshNodeName}. Empty = no
    /// LOD, render at full detail always (today's behavior, unchanged).
    public var lods: [AssetLOD] = []

    /// Loose, author-facing classification — "seating", "surface",
    /// "storage" — the RTF's "tags over hardcoded IDs" idea. Distinct from
    /// `tags` (free-form search tags already in use) so existing tag-based
    /// search/filtering is untouched.
    public var constructionRole: String? = nil
}

public struct AssetLOD: Codable {
    public let maxDistance: Float
    public let meshNodeName: String  // or a separate meshPath for a swap-file approach
}
```

**Why additive, not a rewrite:** `AssetCategory`, `SnapSocket`, `materials`, `sockets` all keep their current meaning. Nothing that reads `AssetDefinition` today needs to change to keep working.

### 5.2 `SnapSocket` — optional richer fields

Canon (`08_AssemblyEngine.md`) wants Priority, Grammar Type, Connection Rules, Mirror Rules, Scale Rules on top of today's `{id, position, normal, type}`. Add them as optional:

```swift
public struct SnapSocket {
    // existing: id, position, normal, type (unchanged)
    public var priority: Int = 0
    public var connectionRules: [String] = []   // e.g. ["accepts:door","accepts:window"]
    public var mirrorable: Bool = true
    public var allowedScaleRange: ClosedRange<Float>? = nil
}
```

Nothing that reads a socket's `type`/`position`/`normal` today breaks.

### 5.3 A new, separate rule/grammar layer (new files, zero edits to existing types)

This is the "JSON cascade" / Construction Grammar, implemented as **new Swift types in new files**, not folded into `PhoenixPrimitive`/`RoomPlacement`:

```
CoreRulesPhoenixRule.swift         — the rule/grammar types
CoreRulesPhoenixConstraint.swift   — keepClear, minimumDistance, etc.
CoreRulesPhoenixBudget.swift       — triangle/material/draw-call budgets
CoreRulesRelationshipVocabulary.swift — the ON/INSIDE/ALONG_WALL/etc. enums
```

Using the canon's own vocabulary (not reinventing new terms), concretely:

```swift
/// A placement rule: "put X in relation to Y." Matches the RTF's own
/// example shape and 07_ConstructionGrammar's role-based framing.
public struct PhoenixRule: Codable, Identifiable {
    public let id: String
    public let when: RuleCondition          // e.g. roomType == .bedroom
    public let place: [PlacementDirective]
}

public struct PlacementDirective: Codable {
    public let constructionRole: String     // "seating", "sleeping_surface" — not a hardcoded asset id
    public let relationship: SpatialRelationship
    public let parent: String?              // relationship target, by role or id
    public let countRange: ClosedRange<Int>
    public let probability: Double
    public let importance: RuleImportance   // critical/required/preferred/optional/decorative
}

/// Canon vocabulary, 06/07/08 + RTF §4 — kept as the literal terms already
/// agreed on, not invented fresh.
public enum SpatialRelationship: String, Codable {
    case alongWall, centerOfRoom, corner, doorSide, windowSide
    case against, near, inside, onTop, under
    case grid, line, radial, around, scatter, cluster
}

public enum RuleImportance: String, Codable {
    case critical, required, preferred, optional, decorative
}
```

**Why separate files, why not touch `RoomPlacement`:** a `PhoenixRule` never needs to be attached to a specific `RoomPlacement` instance — it's evaluated against one (by `roomType`), producing new `FurniturePlacement`s through a `Command`. `RoomPlacement` itself needs zero new fields for this to work.

### 5.4 Resolution / LOD — use SceneKit's own native API, not a custom system

The codebase audit found **zero existing LOD/instancing code**, but SceneKit has had native LOD support since day one: `SCNLevelOfDetail` + `SCNNode.levelsOfDetail`. This maps directly onto the already-specified `pba_format.md` `lods` field:

```swift
// In ModelImporter / ViewportSceneKitView's mesh-loading path:
if !asset.lods.isEmpty {
    let levels = asset.lods.map { lod in
        SCNLevelOfDetail(geometry: loadGeometry(lod.meshNodeName), worldSpaceDistance: CGFloat(lod.maxDistance))
    }
    node.levelsOfDetail = levels
}
```

This is additive at the call site: an asset with no `lods` entries (every asset today) behaves exactly as it does now. One with `lods` populated gets free, engine-native LOD switching with no new rendering infrastructure. This directly answers the Unreal/Houdini guide's R0–R4 ambition using a mechanism that actually exists in our stack, rather than porting Unreal-specific tricks (HLSL masking, Houdini HDAs) that have no SceneKit equivalent.

### 5.5 Seeds — wire up what's already there

`BuildingScene.randomSeed` already exists and does nothing. Per `10_BuildingDNA.md`'s six named seeds (Building/Roof/Window/Material/Decal/Vegetation — `11_ProceduralArchitecture.md` calls the fifth one "Decoration Seed," a minor canon inconsistency, not worth resolving now), add a pure hashing helper:

```swift
/// Deterministic, hierarchical seeding — RTF §16, 10_BuildingDNA. IDs, not
/// sequential counters, so adding one lamp never reshuffles anything else.
public enum PhoenixSeed {
    public static func derive(from worldSeed: UInt64, entityID: String, ruleID: String) -> UInt64 {
        var hasher = Hasher()
        hasher.combine(worldSeed)
        hasher.combine(entityID)
        hasher.combine(ruleID)
        return UInt64(bitPattern: Int64(hasher.finalize()))
    }
}
```

`randomSeed` keeps its current meaning (the whole-scene seed); this just finally gives it something to seed.

---

## 6. Proposed new Commands (procedural output flows through the existing system)

Following the exact shape of `AddFloorCommand`/`AddRoomPrimitiveCommand` (bulk-add a pre-built list, one atomic undo step):

```swift
/// Evaluates a room's applicable PhoenixRules against the asset library and
/// produces FurniturePlacements — built by the caller (so redo re-adds the
/// same instances, not regenerated ones), executed as one undo step.
public struct ApplyRoomRulesCommand: Command {
    public let roomID: String
    public let furniture: [FurniturePlacement]   // pre-resolved by the rule engine
    public func execute(on scene: BuildingScene) { for item in furniture { scene.addFurniture(item) } }
    public func undo(on scene: BuildingScene)    { for item in furniture { scene.removeFurniture(withID: item.id) } }
}
```

Same shape for a future `GenerateFacadeCommand` (produces `PhoenixPrimitive`s: windows, trims) once Exterior work starts. **No new Command type touches `rooms`/`primitives`/`furniture` in a way existing Commands don't already — this is purely "more of the same kind of bulk add."**

---

## 7. Where the actual rule *evaluation* logic lives (kept separate from Commands)

A new, pure, stateless `RuleEngine` type (new file, e.g. `CoreRulesRuleEngine.swift`) that:

1. Takes a `RoomPlacement` + the active `[PhoenixRule]` set + `AssetLibrary` + a derived seed.
2. Filters `AssetLibrary` candidates by `constructionRole`/`allowedRooms`/tags (never a hardcoded asset ID — RTF §6).
3. Resolves `SpatialRelationship` into actual (x, z) coordinates using the room's existing geometry (`RoomPlacement.minX/maxX/minZ/maxZ`, already present).
4. Checks `PhoenixConstraint`s (door clearance, walkable path width) against the room's existing walls/openings (`PhoenixPrimitive.openingOffset`/`openingWidth`, already present).
5. Returns a plain `[FurniturePlacement]` — never touches `BuildingScene` directly.

The UI then shows these as a **preview** (ghost/ semi-transparent, matching the already-built `AdjacentFloorGhostOverlay` visual language) before the user confirms, at which point they're wrapped in `ApplyRoomRulesCommand` and executed. This mirrors `11_ProceduralArchitecture.md`'s explicit workflow: *Rules → Constraints → Seed → Validation → Preview → User Approval → Generation.*

This keeps the engine 100% decoupled from `BuildingScene`/SwiftUI — testable in isolation (matching this session's own established pattern of testing Commands directly against a bare `BuildingScene()`, no UI).

---

## 8. Budgets — minimal first version

Full budget cascading (City → District → Block → Building → Floor → Room, RTF §26–28) is explicitly out of scope until District-level work exists (Section 11). A useful, small, real first step:

```swift
public struct PhoenixBudget: Codable {
    public var maxFurnitureItems: Int? = nil
    public var maxTriangles: Int? = nil
}
```

Attached optionally to a room-rule evaluation call (not stored on `RoomPlacement`). The `RuleEngine` drops `decorative` → `optional` → `preferred` importance items first when a budget would be exceeded, per `08_AssemblyEngine.md`'s stated priority-based degradation. This is enough to prove the concept without inventing a budget-propagation system nothing yet needs.

---

## 9. UI: where this actually surfaces (needs your decision — see Section 10)

Two concrete options, both compatible with everything above:

**Option A — enhance what exists (lowest risk, fastest to ship something real):**
Add a "Fill Procedurally" button inside the existing Furniture section's inspector (next to the room list), and an "Apply Style" action inside Materials. No sidebar restructuring. "Interior" stays the informal name for "what Furniture + Materials already do," "Exterior" becomes a new, genuinely new section for facade/exterior-wall work (since nothing like it exists today) under the Build group, alongside Rooms/Walls/Roof.

**Option B — the literal reading (bigger, matches your wording exactly):**
Two new top-level sidebar sections, "Interior" and "Exterior," each a thin wrapper that routes to the *existing* Furniture/Materials/Walls work for now, with the new procedural actions (Fill Room, Apply Style, Generate Facade) living inside them. This is mostly a routing/relabeling change plus the new buttons from Option A — it does not require moving or rewriting the underlying 2D/3D canvases.

Both options reuse 100% of the engineering in Sections 5–8. The difference is purely how many sidebar entries change and how much user-facing renaming happens — genuinely a product decision, not an engineering one, which is why Section 10 asks it explicitly rather than this plan picking for you.

---

## 10. Questions that need your answer before implementation starts

1. **Option A or B above** (enhance existing sections vs. new top-level Interior/Exterior sections)?
2. Should "Exterior" scope include facade/cladding only (closest to what you've described — "walls, furniture, etc"), or also start reaching toward the canon's District/landscaping future (`15_Roadmap.md` Milestone 3+)? Recommendation: facade/cladding only for now — District is explicitly a later milestone in the canon's own roadmap.
3. Should procedural furniture-fill start with a small, hand-authored rule set for just 2–3 room types (Bedroom, Living Room, Kitchen — enough to prove the pipeline end-to-end), or do you already have a specific rule set in mind from the RTF conversations to start from?
4. Is Facade3D (your separate project, referenced extensively in the RTF) meant to be integrated as part of this work, or is that a later, separate integration? This plan assumes **later** — Facade3D's "resolution engine" role (RTF §10) is a bigger, separate piece of work than the Interior/Exterior UI ask.

---

## 11. Phased rollout

Directly adapting the RTF's own author-endorsed Phase 1–7 (RTF Part B §34), translated into concrete milestones for this specific Interior/Exterior request:

| Phase | Deliverable | Risk to existing code |
|---|---|---|
| **1. Data contracts** | Add the additive fields from Section 5 (`AssetDefinition`, `SnapSocket`) and the new rule/budget/seed types as new files. No behavior changes anywhere yet. | None — purely additive, Codable-safe. |
| **2. Make current assets conform** | Backfill `constructionRole`/`allowedRooms` on existing library assets (manual tagging pass, or a one-time migration script). | None — existing assets without these fields keep working exactly as today. |
| **3. Rule engine (pure, isolated)** | `RuleEngine` + `PhoenixRule` evaluation, unit-tested against a bare `BuildingScene()` exactly like this session's `FloorManagementTests`. No UI yet. | None — new, isolated code path. |
| **4. One real UI entry point** | "Fill Room Procedurally" button (Furniture section or new Interior section per Section 10's answer) → preview → `ApplyRoomRulesCommand`. | Low — one new button, one new Command, reuses existing FurnitureLayoutView canvas to show results (they're just normal `FurniturePlacement`s). |
| **5. Exterior/facade pass** | New section (per Section 10) for facade dressing — window-grid generation on exterior walls, trim assignment — as `GenerateFacadeCommand` producing ordinary `PhoenixPrimitive`s. | Low — same bulk-Command pattern, new primitives render through the existing wall-rendering path untouched. |
| **6. Resolution/LOD** | Wire `SCNLevelOfDetail` from `AssetLOD` (Section 5.4) for any asset that has LOD data. | None for assets without LOD data (100% of today's library). |
| **7. Seeds & regenerate** | Wire `PhoenixSeed.derive` into the rule engine so "regenerate with new seed" is a real, reproducible action. | None — purely additive on top of Phase 3's engine. |

Each phase ships something real and independently useful — matching `11_ProceduralArchitecture.md`'s "progressive generation" principle and the Roadmap's "Bi-Weekly Rule" (every cycle produces a usable capability, not just scaffolding).

---

## 12. Explicit non-goals for now

Mirroring the RTF's own instruction ("I would NOT implement the entire rule engine now") and the canon's own phased roadmap:

- **No full City/District/Street/Lot hierarchy.** `15_Roadmap.md` already places this at "Milestone 3+," explicitly later than trims/surfaces (Milestone 2) and even later than the MVP (Milestone 1, roughly where the app is today).
- **No `.pbt` Template format.** Named in canon, zero spec exists; inventing one now would be designing a format in a vacuum.
- **No "Wing" hierarchy level.** Named once in `07_ConstructionGrammar.md`, never specified further, no current need.
- **No terrain adaptation.** Zero terrain concept exists anywhere in the app; out of scope for an Interior/Exterior furnishing pass.
- **No full budget cascade (City→District→Block→Building→Floor→Room).** Section 8's minimal per-room budget is enough until District-level work actually exists.
- **No confidence-scored/color-coded ghost placement preview** (Green/Yellow/Orange/Red from `08_AssemblyEngine.md`) in the first pass — a plain preview-then-commit (matching the existing floor-duplicate confirmation dialog pattern) is enough to start; the richer preview is a nice-to-have for a later phase.
- **No Facade3D integration** in this pass (see Question 4).

---

## 13. Summary

The foundation this needs (semantic data model, deterministic seeding concept, Command/undo architecture, PAL role vocabulary) already exists or is already specified at the file-format level — this is genuinely additive work, not a rewrite. The biggest real risk isn't technical, it's scope: the canon describes a multi-year vision (full city generation, multi-engine export, Blender round-tripping). This plan deliberately carves out the smallest slice that (a) is real and shippable, (b) matches what you asked for — walls, furniture, procedural fill — and (c) doesn't block any of the bigger vision later, since every data-model choice here is additive and nothing forecloses District/Template/Terrain work down the line.

The open questions in Section 10 are the only blockers to starting Phase 1.
