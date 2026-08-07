# PHX-SPEC-002: Phoenix Building Asset Specification (`.pba`)

* **Status**: Draft (Proposed)
* **File Extension**: `.pba` (Folder/Bundle format)
* **Format**: Folder bundle containing JSON metadata and binary 3D geometry files.

> [!NOTE]
> For **Milestone 1: First House**, we use a simplified version of this format. See [PHX-MVP-001](PHX-MVP-001_FirstHouse.md) for the exact MVP schema properties.

---

## 1. Directory Structure

A `.pba` asset is packaged on disk as a folder. The directory naming convention is `[AssetID].pba/` and must contain the following files at its root:

```text
[AssetID].pba/
├── metadata.json           # Mandatory: Semantic and attachment definitions
├── mesh.glb                # Mandatory: Binary glTF containing meshes, bones, and default materials
└── icon.png                # Optional: Thumbnail for the asset library viewport
```

For macOS/iOS-focused deployment, a `mesh.usdz` file may also be included to support native SceneKit/RealityKit performance.

---

## 2. Metadata Schema (`metadata.json`)

The `metadata.json` file inside the bundle is structured as follows:

```json
{
  "$schema": "https://phoenix.sdk/schemas/building_asset.schema.json",
  "format_version": "1.0.0",
  "asset_id": "string (matches folder name)",
  "display_name": "string (user-facing title)",
  "semantic_class": "string (door | window | column_cap | trim | prop | ornament)",
  "geometry": {
    "source_file": "mesh.glb",
    "bounding_box": {
      "min": { "x": -0.5, "y": 0.0, "z": -0.1 },
      "max": { "x": 0.5, "y": 2.0, "z": 0.1 }
    }
  },
  "attachment_connectors": [
    {
      "connector_id": "string (e.g., base_snapper)",
      "type": "string (must match a primitive socket type)",
      "offset_transform": {
        "position": { "x": 0.0, "y": 0.0, "z": 0.0 },
        "rotation": { "x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0 }
      }
    }
  ],
  "material_interfaces": [
    {
      "submesh_node_name": "string (name of mesh node in GLB)",
      "material_slot": "string (semantic slot name for swapping)",
      "default_recipe_id": "string (fallback Surface Recipe)"
    }
  ],
  "variations": [
    {
      "variant_id": "string (e.g., clean | damaged)",
      "mesh_node_override": "string (name of alternative submesh node in GLB)"
    }
  ],
  "lods": [
    {
      "lod_level": 0,
      "max_distance": 10.0,
      "mesh_node_name": "string (high-poly node name)"
    },
    {
      "lod_level": 1,
      "max_distance": 50.0,
      "mesh_node_name": "string (low-poly node name)"
    }
  ]
}
```

---

## 3. Detailed Component Specifications

### 3.1. Geometry Reference & Bounds
* **`source_file`**: Refers to the physical mesh asset inside the bundle.
* **`bounding_box`**: Defines the physical bounds in meters relative to the asset origin. The editor (Builder) uses this boundary to perform collision detection, occlusion queries, and calculate boolean cutouts in primitives.

### 3.2. Attachment Connectors
Connectors are the counterpart to a primitive's **Sockets**:
* **`type`**: Must match a socket `type` in the target `.pbp` primitive (e.g. `door_opening`).
* **`offset_transform`**: Local offset from the asset's origin. For instance, a door might align its origin at the bottom-center, while a window might align its origin at the center.

### 3.3. Material Interfaces
This list maps raw mesh nodes inside the binary file to logical material slots. This is crucial for **Level 2 (Variant Creator)** workflows:
* **`submesh_node_name`**: The exact string matching the named object node inside the Blender scene/GLB hierarchy.
* **`material_slot`**: A semantic name (e.g., `frame_wood`, `window_glass`). Builder and Engine use this slot to swap textures programmatically using **Surface Recipes**, bypassing the raw textures compiled inside the `.glb`.

### 3.4. Variations & LODs
* **`variations`**: Rather than shipping separate `.pba` packages for different object states (e.g., active vs. broken door), artists are encouraged to author all mesh variations inside a single `.glb` file. The `variations` block instructs the loader which mesh node to render based on the current state.
* **`lods`**: Maps camera distance to specific model nodes in the `.glb` file, ensuring seamless lod-swapping at runtime in Phoenix Engine.
