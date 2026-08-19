# 🌲 Phoenix Ecosystem — Sprites & Sprints Tree 🗺️

**Current Date / Time:** August 12, 2026  
**Active Work:** `Sprint 5 — Observation, Balancing & MetricTracker`  
**Active AI Model:** `⚡ Gemini 2.5 Flash` (with `ChatGPT` Architect & `DeepSeek` Fallback)

---

## 🎨 1. Sprite & Asset Tree (`SpriteGenerator.swift`)

How Not To Die currently utilizes a procedural vector-rasterization engine in [SpriteGenerator.swift](file:///Users/gabrielnetto/Documents/Programaciones/PhoenixEcosystem/PhoenixGAMES/HowNotToDie/HowToNotDie/HowToNotDie/03_Game/05_Gameplay/SpriteGenerator.swift) to create crisp, lightweight isometric 2D assets on the fly:

```
SpriteGenerator (Shared Singleton)
│
├── 👤 Characters & Entities
│   ├── .player
│   │   ├── Isometric Diamond Body (Ruby Red #D32F2F)
│   │   ├── Elliptical Head (Amber Orange #FF9800)
│   │   └── High-Contrast White Silhouette Stroke
│   │
│   └── 🧟 .zombie
│       ├── Decayed Organic Torso (Moss Green #8BC34A)
│       ├── Dual-Point Red Eye Emissive Nodes (#F44336)
│       └── Dark Shaded Outline
│
├── 🌲 Nature & Environment
│   ├── 🌲 .tree
│   │   ├── Isometric Cylindrical Trunk (Timber Brown #795548)
│   │   └── 3-Layered Overlapping Foliage Canopy (Forest Greens)
│   │
│   ├── 🪵 .treeStump
│   │   ├── Truncated Wood Core (Sienna #A1887F)
│   │   └── Concentric Growth Rings
│   │
│   ├── 🪨 .rock
│   │   ├── 6-Point Shaded Isometric Polyhedron
│   │   ├── Specular Facet Highlights
│   │   └── Ground Ambient Occlusion Base
│   │
│   ├── 🪨 .rockDestroyed
│   │   └── 3-Fragment Scavengeable Rubble Cluster
│   │
│   └── 💧 .water
│       ├── Layered Deep-Blue Ellipses (#1976D2)
│       └── Dynamic White Ripple Rings
│
├── 🔥 Fire & Light
│   ├── 🪵 .campfire
│   │   ├── Cross-Stacked Timber Logs
│   │   └── Charcoal Base Ash Pile
│   │
│   └── 🔥 .campfireBurning
│       ├── Charcoal Bed with Amber Embers
│       └── Dual-Tone Layered Triangle Flame Geometry (Yellow/Orange)
│
└── 🎒 Items & Pickups
    ├── 🪵 .woodPickup (16x16 Log Resource Token)
    └── 💎 .stonePickup (16x16 Polyhedral Mineral Token)
```

---

## 🗺️ 2. Sprints & Milestones Progression Tree

```
PHOENIX ECOSYSTEM & HOW NOT TO DIE ROADMAP
│
├── ✅ SPRINT 1: Movement & Virtual Controls (COMPLETED)
│   ├── 8-direction virtual joystick input
│   ├── SpriteKit character physics body
│   └── Camera tracking and viewport constraints
│
├── ✅ SPRINT 2: Persistence & Time System (COMPLETED)
│   ├── SaveSystem.swift with JSON world serialization
│   └── WorldClock.swift with simulation acceleration (1x, 2x, 5x)
│
├── ✅ SPRINT 3: Game Feel & Lighting (COMPLETED)
│   ├── SafeAreaHUD.swift adaptive layout
│   └── Dynamic day/night ambient color grading
│
├── ✅ SPRINT 4: Procedural Foundations & Nodes (COMPLETED)
│   ├── SpriteGenerator.swift procedural textures
│   └── Interactive ResourceNode.swift (Trees, Rocks, Water, Fire)
│
├── 🏗️ SPRINT 5: [CURRENT ACTIVE SPRINT] Observation & Balancing
│   │   Status: GEMINI CODING / ARCHITECT REVIEW
│   ├── 📄 MetricTracker.swift (Records births, deaths, starvation, thirst)
│   ├── 📄 GameplayManager.swift (Simulation tick listener)
│   ├── 📄 CitizenWithSleep.swift (Health, hunger, rest state machine)
│   └── 📊 Resource Heat Map & Collapse Cause Analytics
│
├── 📋 SPRINT 6: PAL Abstraction Layer (BACKLOG)
│   ├── Dynamic Entity Mapping between PhoenixEngine and GameScene
│   └── KnowledgeGraph Derivations without state duplication
│
└── 📋 SPRINT 7: Milestone 1 "First House" Assembly (PLANNED)
    ├── Core 5 PAL Classes: Wall, Floor, Roof, Door, Window
    ├── Forge Exporter add-on
    └── In-game walkable cabin validation in HowNotToDie
```
