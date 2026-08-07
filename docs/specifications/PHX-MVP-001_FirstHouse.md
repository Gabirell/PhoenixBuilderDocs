# PHX-MVP-001: Milestone 1 — "First House" Specification

* **Status**: Proposed
* **Ecosystem Version**: v0.1.0-MVP
* **Primary Target**: Walk around a custom, assembled house in the validation game *How Not To Die*.

---

## 1. The MVP Scope (Five PAL Classes)

To establish the pipeline, we restrict the ecosystem to exactly five foundational PAL classes. Anything not listed here belongs to the **LATER Backlog (Anti-Five-Year Shield 🛡️)**.

1. `Wall` (Structural Vertical)
2. `Floor` (Structural Horizontal)
3. `Roof` (Structural Sloped)
4. `Door` (Opening Barrier)
5. `Window` (Opening Aperture)

---

## 2. Minimal Data Specifications

### 2.1. `.pbp` (Phoenix Primitive)
For **Wall**, **Floor**, and **Roof** primitives, the data structure stores only basic coordinate bounds and dimensions:

```json
{
  "pal_class": "Wall | Floor | Roof",
  "id": "string",
  "points": [
    { "x": 0.0, "y": 0.0, "z": 0.0 },
    { "x": 4.0, "y": 0.0, "z": 0.0 }
  ],
  "height": 3.0,
  "thickness": 0.2,
  "material_override": "string (hardcoded diffuse texture path/name)"
}
```

### 2.2. `.pba` (Phoenix Building Asset)
For **Door** and **Window** assets, the directory package contains:
* `mesh.glb`: The raw 3D mesh.
* `metadata.json`:
  ```json
  {
    "pal_class": "Door | Window",
    "id": "string",
    "mesh_reference": "mesh.glb",
    "bounds": {
      "width": 1.0,
      "height": 2.0,
      "depth": 0.2
    },
    "connector": {
      "offset_position": { "x": 0.0, "y": 0.0, "z": 0.0 }
    }
  }
  ```

---

## 3. Tool-by-Tool MVP Responsibilities

### 3.1. 🔥 Phoenix Forge (Blender Add-on)
* **UI**: A simple dropdown panel in Blender to assign one of the five PAL classes to the active object.
* **Metadata Exporter**: A button that writes the `metadata.json` and exports the selected mesh node as `mesh.glb` into a named `[AssetID].pba/` directory.

### 3.2. 🏛 Phoenix Builder (macOS App)
* **Footprint Input**: Draw a simple 2D footprint (4 points) on a horizontal grid.
* **Auto-Extrusion**: Instantiates 4 `Wall` primitives based on the footprint, 1 `Floor` primitive, and 1 `Roof` primitive spanning the walls.
* **Fixture Placement**: Drag a `.pba` asset (Door or Window) and place it on a wall. Builder slices a simple rectangular opening in the wall primitive mesh and positions the asset at that location.
* **File Output**: Saves the house configuration as a single `.json` scene file.

### 3.3. 🎮 Phoenix Engine & How Not To Die (Swift Integration)
* **Loader**: Swift structures deserialize the Builder house `.json` scene.
* **Mesh Compiler**: Programmatically extrudes the 3D meshes for Walls, Floors, and Roofs, placing the Door and Window `.glb` assets in their respective holes.
* **Colliders**: Generates SceneKit/Physics body boxes from Wall and Floor dimensions.
* **Walkthrough**: The character in *How Not To Die* can collide with the walls, walk through the open doors, and seek shelter inside the house.

---

## 4. The Anti-Five-Year Shield (LATER Backlog) 🛡️

The following features are **explicitly postponed** to future milestones:

* **Trims & Miters**: No baseboards, cornices, mitering calculations, or curve extrusion profiles.
* **Surface Recipes & Style Families**: No dynamic material lookup tables or multi-material slots. Visual styling is limited to single hardcoded diffuse texture files.
* **Decay & Damage**: No moss, weathering, or procedural damage parameters.
* **Complex Sockets**: No generic allowed-classes matching. Snapping is restricted to simple coordinate insertion points on wall segments.
