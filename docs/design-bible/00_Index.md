{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
{\info
{\author Gabriel Netto}
{\*\company gabrielnetto.com}
{\*\copyright gabrielnetto.com}}\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Phoenix Builder Design Bible\
## 00_Index.md\
\
Version: 1.0.0  \
Status: Living Document  \
Author: Phoenix Project  \
Revision: 0\
\
---\
\
# Phoenix Builder\
\
> **Assemble once. Export anywhere.**\
\
Phoenix Builder is a deterministic architectural asset authoring system designed for game development.\
\
It is **not** a modelling package.\
\
It is **not** a CAD application.\
\
It is **not** a level editor.\
\
Its purpose is to assemble reusable modular architecture from carefully prepared building kits and export optimized assets for multiple game engines and rendering pipelines.\
\
---\
\
# Purpose of this Design Bible\
\
This document defines the philosophy, architecture, workflows, constraints, terminology and long-term direction of Phoenix Builder.\
\
Every major decision in the project should be consistent with this document.\
\
Whenever uncertainty exists, this document has priority over individual implementation ideas.\
\
---\
\
# Core Philosophy\
\
Phoenix Builder exists because there is a gap between:\
\
\'95 Blender (asset creation)\
\
and\
\
\'95 Game Engines (asset consumption)\
\
Blender is excellent for creating modular pieces.\
\
Game engines are excellent for rendering and gameplay.\
\
Neither is optimized for assembling hundreds of reusable game-ready buildings quickly.\
\
Phoenix Builder fills that gap.\
\
---\
\
# Fundamental Principles\
\
## Principle 01\
\
Assembler, never modeller.\
\
If a proposed feature transforms Phoenix Builder into a general-purpose modelling package, reject it.\
\
Geometry creation belongs in Blender.\
\
Phoenix Builder assembles.\
\
---\
\
## Principle 02\
\
Everything remains editable.\
\
No operation should permanently destroy information.\
\
Generated buildings remain manually editable.\
\
Procedural generation never creates locked assets.\
\
---\
\
## Principle 03\
\
Reuse before duplication.\
\
Meshes are never duplicated unnecessarily.\
\
Buildings store references to reusable assets.\
\
---\
\
## Principle 04\
\
Deterministic generation.\
\
Every procedural result must be reproducible from:\
\
\'95 Seed\
\
\'95 Rules\
\
\'95 Parameters\
\
Identical inputs must always generate identical outputs.\
\
---\
\
## Principle 05\
\
Export is a product.\
\
Exporting is not an afterthought.\
\
Every export profile should produce assets immediately usable by its target engine.\
\
---\
\
## Principle 06\
\
Artists work with architecture.\
\
The software internally uses:\
\
\'95 meshes\
\
\'95 trim sheets\
\
\'95 sockets\
\
\'95 metadata\
\
The user should primarily think about:\
\
\'95 walls\
\
\'95 roofs\
\
\'95 windows\
\
\'95 buildings\
\
---\
\
## Principle 07\
\
Simple beats powerful.\
\
A feature that solves 90% of use cases with one click is preferable to one that solves 100% but requires twenty settings.\
\
---\
\
## Principle 08\
\
Performance begins during authoring.\
\
Optimization is not something done by the game.\
\
Optimization begins while assembling the building.\
\
---\
\
# The Asset Pipeline\
\
```text\
Blender\
      \uc0\u9474 \
      \uc0\u9474 \
      \uc0\u9660 \
Phoenix Builder\
      \uc0\u9474 \
      \uc0\u9500 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9488 \
      \uc0\u9474             \u9474 \
      \uc0\u9660             \u9660 \
\
SpriteKit      Phoenix Engine\
\
PNG Layers     glTF\
\
Metadata        Metadata\
\
Collision       Collision\
\
Atlases         Materials\
```\
\
Phoenix Builder is the bridge between asset creation and runtime.\
\
---\
\
# The Golden Rule\
\
Every decision must answer one question.\
\
> Does this make building game-ready architecture faster?\
\
If the answer is no, the feature should be questioned.\
\
---\
\
# Project Scope\
\
Phoenix Builder focuses on modular architecture.\
\
Supported examples include:\
\
\'95 Houses\
\
\'95 Shops\
\
\'95 Apartments\
\
\'95 Warehouses\
\
\'95 Factories\
\
\'95 Garages\
\
\'95 Castles\
\
\'95 Sci-Fi Structures\
\
Future versions may support cities.\
\
The first versions will not.\
\
---\
\
# Out of Scope\
\
Phoenix Builder intentionally does not replace Blender.\
\
It will not include:\
\
\'95 Sculpting\
\
\'95 Retopology\
\
\'95 UV Editing\
\
\'95 Animation\
\
\'95 Character Modelling\
\
\'95 Video Editing\
\
\'95 Particle Editing\
\
\'95 Physics Simulation\
\
\'95 General Mesh Editing\
\
---\
\
# Long-Term Vision\
\
Phoenix Builder should become the central architectural authoring tool used before exporting to game engines.\
\
One building should produce:\
\
\'95 SpriteKit assets\
\
\'95 Phoenix Engine assets\
\
\'95 Unity assets\
\
\'95 Godot assets\
\
\'95 Unreal assets\
\
without rebuilding the structure.\
\
---\
\
# Documentation Structure\
\
01_Vision.md\
\
Defines why Phoenix Builder exists.\
\
---\
\
02_Philosophy.md\
\
Defines the core principles that guide every decision.\
\
---\
\
03_UserExperience.md\
\
Explains how the software should feel.\
\
---\
\
04_Interface.md\
\
Describes every window, panel and interaction.\
\
---\
\
05_BuildingWorkflow.md\
\
Complete building workflow from empty project to export.\
\
---\
\
06_TrimSheets.md\
\
Complete trim sheet philosophy and implementation.\
\
---\
\
07_SurfaceRecipes.md\
\
Materials, decals, procedural weathering and style system.\
\
---\
\
08_AssemblyEngine.md\
\
Snapping, sockets, placement and reusable modular systems.\
\
---\
\
09_BuildingDNA.md\
\
The deterministic description of every building.\
\
---\
\
10_ProceduralRules.md\
\
Rule-based procedural generation.\
\
No AI.\
\
---\
\
11_Rendering.md\
\
Viewport architecture and rendering philosophy.\
\
---\
\
12_ExportProfiles.md\
\
SpriteKit, Phoenix Engine and future exporters.\
\
---\
\
13_PhoenixIntegration.md\
\
Shared asset pipeline with Phoenix Engine.\
\
---\
\
14_Roadmap.md\
\
Development milestones.\
\
---\
\
15_DecisionLog.md\
\
Permanent architectural decisions.\
\
---\
\
# Living Document\
\
This Design Bible is expected to evolve alongside Phoenix Builder.\
\
New chapters may be added.\
\
Existing chapters may be revised.\
\
Architectural decisions should never be silently changed.\
\
Every important change must be documented.\
\
---\
\
End of File}
