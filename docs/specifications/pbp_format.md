# PHX-SPEC-001: Phoenix Primitive Specification (`.pbp`)

* **Status**: Draft (Proposed)
* **File Extension**: `.pbp`
* **Format**: UTF-8 Encoded JSON

---

## 1. Overview
Phoenix Primitives (`.pbp`) are mathematical, parametric representations of foundational architectural components (walls, floors, columns, stairs, roofs). They do not store explicit mesh vertices or triangles; instead, they define coordinate footprints and numeric extrusion/generation rules. 

Both **Phoenix Builder** and **Phoenix Engine** must implement the geometry generation code that compiles a `.pbp` definition into a renderable 3D mesh at runtime.

---

## 2. JSON Schema

A `.pbp` file contains a single JSON root object with the following primary fields:

```json
{
  "$schema": "https://phoenix.sdk/schemas/primitive.schema.json",
  "format_version": "1.0.0",
  "asset_id": "string (unique identifier)",
  "display_name": "string (user-facing name)",
  "semantic_class": "string (wall | floor | column | roof | foundation | stairs)",
  "geometry": {
    "type": "string (extrusion | footprint_polygon | parametric_shape)",
    "control_points": [
      { "x": 0.0, "y": 0.0, "z": 0.0 }
    ],
    "parameters": {
      "thickness": 0.2,
      "height": 3.0,
      "pitch_degrees": 45.0,
      "subdivisions": 1
    }
  },
  "surface_slots": [
    {
      "slot_id": "string (e.g., interior_face)",
      "recipe_id": "string (reference to Surface Recipe)",
      "uv_transform": {
        "scale": { "u": 1.0, "v": 1.0 },
        "offset": { "u": 0.0, "v": 0.0 },
        "rotation_degrees": 0.0
      }
    }
  ],
  "sockets": [
    {
      "socket_id": "string (unique key within this primitive)",
      "type": "string (e.g., door_mount, window_frame, pillar_corner)",
      "transform": {
        "position": { "x": 2.0, "y": 0.0, "z": 0.0 },
        "rotation": { "x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0 }
      },
      "constraints": {
        "allowed_classes": ["string"],
        "max_dimensions": { "width": 1.2, "height": 2.2, "depth": 0.5 }
      }
    }
  ]
}
```

---

## 3. Detailed Field Specifications

### 3.1. `semantic_class`
Enforces the architectural classification. Builder uses this to determine construction rules (e.g., walls can join other walls, foundations snap beneath floors):
* `wall`: Extruded along a polyline.
* `floor`: Planar horizontal polygon.
* `column`: Vertically extruded single-point profile.
* `roof`: Sloped planar or multi-pitched geometry.
* `foundation`: Heavy base extruded downwards from floor footprint.

### 3.2. `geometry`
* **`control_points`**: Local coordinate vectors (in meters) representing the skeleton of the primitive. For a straight `wall`, this requires at least 2 points (Start, End). For a `floor`, it represents the outline path (minimum 3 points).
* **`parameters`**:
  * `thickness`: Width of walls/floors (in meters).
  * `height`: Vertical height of walls/columns (in meters).
  * `pitch_degrees`: Pitch of roof planes.

### 3.3. `surface_slots`
Decouples geometry from texture mapping. Rather than hardcoding UV coordinates, the geometry generator must project texture coordinates dynamically onto the generated faces.
* **`slot_id`**: Labels semantic faces (e.g., `exterior_face`, `interior_face`, `left_cut`, `right_cut`).
* **`recipe_id`**: Points to a Surface Recipe (e.g. `recipe_brick_dirty_02`). The renderer queries the recipe to select textures (base, normal, roughness) for this slot.
* **`uv_transform`**: Tiling configurations. Since primitives change size, UV scaling is typically recalculated programmatically relative to physical size (world-space mapping) to prevent stretching.

### 3.4. `sockets`
Sockets define coordinates where static objects (`.pba` assets) can snap onto a primitive.
* **`type`**: Matches target connection tags. A door socket will only allow `.pba` files whose metadata identifies them as `door`.
* **`transform`**: Sockets are defined relative to the primitive's local coordinate system. When a wall changes length, socket positions must scale proportionally or snap to predefined anchors (e.g., start, center, end) using interpolation rules.
* **`constraints`**: Prevents oversized objects from clipping geometry. A door socket on a thin partition wall will reject heavy gate assets.
