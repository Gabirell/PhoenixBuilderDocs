# ADR-001: File Format Schema for .pbp and .pba

* **Status**: Proposed
* **Date**: 2026-08-07
* **Authors**: Antigravity (AI Architect) & Gabriel Netto
* **Decisions Superseded**: None

---

## Context & Problem Statement

The Phoenix Ecosystem requires a standard, robust, and platform-agnostic file format specification for architectural assets. These formats must bridge three distinct tools:
1. **🔥 Phoenix Forge** (Blender Add-on): Generates and exports the files.
2. **🏛 Phoenix Builder** (macOS App): Reads, instantiates, and procedurally modifies/assembles them.
3. **🎮 Phoenix Engine** (Swift Game Engine): Consumes the finalized, exported assets for real-time runtime rendering.

We need to specify two distinct formats:
- **`.pbp` (Phoenix Primitive)**: For parametric, procedurally generated components (walls, roofs, foundations, etc.).
- **`.pba` (Phoenix Building Asset)**: For static, artist-authored components (doors, windows, columns, trims) which attach to primitives.

The file schemas must support the **Three Levels of Editability** (Assembler, Variant Creator, Specialist) and enforce the **Surface System** (separating appearance/material from geometry).

---

## Considered Options

### Option 1: Binary Formats (e.g., Protocol Buffers, FlatBuffers, or custom binary)
* **Pros**: Extremely fast parsing, small file size on disk, easy integration in Swift/C++.
* **Cons**: Hard to inspect manually (requires tools to read), difficult for a developer to edit with a simple text editor, harder to manage version diffs in Git.

### Option 2: Pure Text JSON / YAML
* **Pros**: Human-readable, native Git diffing, easy to parse in any language, self-documenting.
* **Cons**: Slow parser overhead for large arrays of data, larger file footprint (though negligible for metadata-only structures).

### Option 3: Hybrid Package (Recommended)
* **`.pbp`** as pure JSON/YAML (since it's strictly parametric definitions, vectors, and metadata).
* **`.pba`** as a compressed bundle/archive (or a JSON metadata file referring to a standard `.gltf` / `.glb` or `.usdz` file for raw geometry).
* **Pros**: Clean separation of lightweight metadata from heavy mesh/texture data. Uses industry-standard glTF/USD for geometry, making Blender and Swift integrations trivial.
* **Cons**: Requires reading multi-file archives or references.

---

## Decision Outcome

We propose **Option 3: Hybrid Package (JSON Metadata + Industry-Standard Geometry)**.

1. **`.pbp` (Phoenix Primitive)**: Pure JSON. It does not store raw mesh data; it only stores the mathematical parameters, footprint curves, height/thickness constraints, and surface recipe tags.
2. **`.pba` (Phoenix Building Asset)**: A directory or package wrapper containing:
   - `metadata.json`: Defines semantic tags, socket arrays, LOD references, and material slots.
   - `mesh.glb` (or `mesh.usdz`): The actual 3D geometry authored by the artist.

---

## Proposed Schema Specifications

### 1. `.pbp` (Phoenix Primitive) Schema
Below is the proposed JSON schema for a procedural wall or floor primitive:

```json
{
  "format_version": "1.0.0",
  "asset_type": "primitive",
  "semantic_class": "wall", 
  "id": "wall_plaster_01",
  "display_name": "Standard Plaster Wall",
  "parameters": {
    "thickness": 0.2,
    "height": 3.0,
    "alignment": "center",
    "footprint": {
      "type": "polyline",
      "points": [
        {"x": 0.0, "y": 0.0, "z": 0.0},
        {"x": 4.0, "y": 0.0, "z": 0.0}
      ]
    }
  },
  "surface_slots": [
    {
      "id": "interior_face",
      "default_recipe": "recipe_plaster_white_01"
    },
    {
      "id": "exterior_face",
      "default_recipe": "recipe_brick_red_01"
    }
  ],
  "sockets": [
    {
      "id": "door_socket_01",
      "type": "door_opening",
      "transform": {
        "position": {"x": 2.0, "y": 0.0, "z": 0.0},
        "rotation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0}
      },
      "constraints": {
        "allowed_classes": ["door"],
        "max_width": 1.2,
        "max_height": 2.2
      }
    }
  ]
}
```

### 2. `.pba` (Phoenix Building Asset) Schema
Below is the proposed JSON structure for the `metadata.json` accompanying an artist-authored asset (e.g., a window):

```json
{
  "format_version": "1.0.0",
  "asset_type": "building_asset",
  "semantic_class": "window",
  "id": "window_gothic_double",
  "display_name": "Gothic Double Window",
  "geometry": {
    "source": "mesh.glb",
    "bounds": {
      "min": {"x": -0.6, "y": 0.0, "z": -0.1},
      "max": {"x": 0.6, "y": 1.8, "z": 0.1}
    }
  },
  "variants": [
    {
      "id": "pristine",
      "mesh_node": "window_mesh_clean"
    },
    {
      "id": "damaged",
      "mesh_node": "window_mesh_broken"
    }
  ],
  "sockets": [
    {
      "id": "attachment_point",
      "type": "window_mount",
      "transform": {
        "position": {"x": 0.0, "y": 0.0, "z": 0.0},
        "rotation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0}
      }
    }
  ],
  "material_slots": [
    {
      "slot_name": "frame_material",
      "default_texture_set": "wood_oak_dark",
      "swappable": true
    },
    {
      "slot_name": "glass_material",
      "default_texture_set": "glass_clear",
      "swappable": true
    }
  ]
}
```

---

## Consequences

* **Interoperability**: Standard tools can open `.glb` or `.usdz` meshes directly, meaning artists do not need specialized viewers just to inspect the visual part of the asset.
* **Deterministic Assembly**: Primitives can calculate exact intersections using coordinate vectors, while sockets enforce clear constraints on what assets can snap to them.
* **Ease of Editing**: Level 2 creators (Variant Creators) can simply duplicate a `.pba` folder, tweak `metadata.json` (e.g. modify the `default_texture_set` or scale limits), and register it as a new variant without modifying or duplicating the heavy 3D geometry asset (`mesh.glb`).
* **Source Control Friendly**: Both schemas represent metadata in readable JSON, making history diffs highly legible and easy to merge.
