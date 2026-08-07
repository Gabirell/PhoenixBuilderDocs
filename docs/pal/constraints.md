# Chapter 7: Constraints & Validation

To ensure that assets authored in Blender work immediately in the editor and render without crashing the game client, PAL defines a strict **Validation Contract**.

---

## 1. Forge Exporter Validation (Blender)

When a specialist (Level 3) exports a building asset (`.pba`) using the **Phoenix Forge** Blender Add-on, the exporter reads the PAL dictionary schemas to run local validation checks:

* **Semantic Schema Check**: Verifies that the `metadata.json` generated has all mandatory fields for its declared `semantic_class`.
* **Socket Nomenclature**: Checks that Blender socket helper objects match PAL naming conventions and positions (e.g., checking that a door frame has matching hinge coordinates).
* **Material Slot Verification**: Confirms that every submesh node in the exported `.glb` matches the named slots in `material_interfaces`.

If any check fails, the exporter blocks the export and highlights the invalid parameters inside Blender.

---

## 2. Builder Scene Validation (Compilation)

When a level designer (Level 1) or variant creator (Level 2) arranges assets in **Phoenix Builder**, the editor runs compilation validation passes to prevent logical errors:

* **Host Integrity Check**: Ensures all child objects (`Openings`, `Trims`, `Fixtures`) reside within their host boundaries. If a window is dragged completely off a wall, it fails validation.
* **Clearance Collision check**: Verifies that door swing volumes and window apertures are not blocked by columns, furniture, or structural wall joins.
* **Socket Matching**: Prevents the user from snapping incompatible connectors (e.g., attempting to snap a ceiling ornament into a floor socket).

Failed validations display as warning markers inside the viewport hierarchy, ensuring errors are resolved before exporting the final scene.

---

## 3. Platform Interoperability

Because these constraints are defined in **PAL Specifications** (rather than locked inside Builder's Swift code or Forge's Python script), any developer can write custom parser validators. 

This ensures that whether a level is loaded inside the custom Swift **Phoenix Engine** or exported to **Unity/Godot**, it behaves identically, avoiding runtime asset parsing errors.
