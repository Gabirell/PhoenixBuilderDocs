# ADR-003: Building Asset Architecture (.pba)

* **Status**: Proposed
* **Date**: 2026-08-07
* **Authors**: Antigravity & Gabriel Netto
* **Decisions Superseded**: None

---

## Context & Problem Statement

Phoenix Building Assets (`.pba`) represent static, artist-authored modules (doors, windows, cornices, columns) exported from Blender via Phoenix Forge. 

Unlike primitives, these assets contain custom, non-parametric 3D meshes and UV coordinates. We must decide how to package these assets so that:
1. They are easy to author in Blender.
2. They are lightweight to parse in Phoenix Builder and Phoenix Engine.
3. They support metadata (sockets, LODs, variants, and swappable materials) without reinventing 3D geometry file formats.

---

## Considered Options

### Option 1: Custom Binary Format (Mesh data + Metadata merged)
* We write a custom exporter that packages vertex data and socket metadata into a single custom binary file format.
* **Pros**: A single file on disk, fast parsing if optimized.
* **Cons**: Massive development overhead (writing and maintaining custom importers/exporters in Blender/Python and Swift). Standard engines/viewers cannot open them.

### Option 2: Pure Metadata File referencing External Standard Meshes
* The `.pba` is a pure metadata file (JSON) that points to a standard file path on disk (e.g. `mesh.gltf` or `mesh.fbx`).
* **Pros**: Simple, completely decoupling metadata from mesh.
* **Cons**: Splitting the asset into disconnected files makes distribution, versioning, and drag-and-drop operations in a library manager complex and prone to broken references.

### Option 3: Hybrid Package Directory / Archive (Recommended)
* A `.pba` is a directory (or compressed package) containing a standard `metadata.json` file and an industry-standard geometry file (e.g., `mesh.glb` or `mesh.usdz`).
* **Pros**:
  - Leverages industry standards (`.glb` / `.usdz`) for fast rendering, animation, and texture support.
  - Keeps metadata human-readable and separate from binary mesh data.
  - Level 2 creators can duplicate the `.pba` and only edit `metadata.json` to create new variations (e.g. changing scale constraints or default material sets) while pointing to the same heavy geometry file, saving disk space and source control footprint.
  - Highly portable: can be moved as a single folder or a zipped `.pba` bundle.
* **Cons**: Requires reading a folder structure or extracting an archive.

---

## Decision Outcome

We chose **Option 3: Hybrid Package Directory / Archive**.

Every `.pba` asset is represented on disk as a folder (named `[AssetID].pba/`) or a packaged bundle containing:
1. `metadata.json`: Defines socket attachments, swappable material tags, variation models, and LOD nodes.
2. `mesh.glb` (or `mesh.usdz`): The physical geometry asset exported from Blender via Phoenix Forge.

---

## Consequences

* **Standard Geometry Pipe**: Phoenix Forge (Blender) uses standard glTF export libraries under the hood, injecting semantic node names into the mesh before exporting, which are then mapped in `metadata.json`.
* **Zero-Geometry Variants (Level 2)**: To create a variant (e.g., a "Rusted Window"), a creator does not need to duplicate the heavy `.glb` mesh. They can create a new `.pba` configuration that shares the original mesh file via file reference, overriding only the default material recipes.
* **Platform Portability**: Using `.glb` (glTF binary) provides maximum portability across Windows/Linux/Web, while `.usdz` can be generated dynamically or packaged alongside for native macOS/iOS rendering performance inside SceneKit/Metal.
