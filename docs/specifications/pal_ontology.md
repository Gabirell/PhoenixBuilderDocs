# PHX-SPEC-003: Phoenix Architectural Language (PAL) Core Ontology

* **Status**: Draft (Proposed)
* **Target Version**: 1.0.0
* **Format**: Specification Document

> [!NOTE]
> For **Milestone 1: First House**, we only implement a subset of 5 classes (Wall, Floor, Roof, Door, Window) using a simplified schema. See [PHX-MVP-001](PHX-MVP-001_FirstHouse.md) for details.

---

## 1. Introduction

The **Phoenix Architectural Language (PAL)** is the unified semantic dictionary of the Phoenix Ecosystem. Rather than thinking of architectural assets as arbitrary 3D meshes or polygons, all components are classified under first-class architectural concepts. 

This shared vocabulary allows **Phoenix Forge** (Blender) to validate exported metadata, **Phoenix Builder** to perform style family swaps (e.g. Victorian vs. Gothic) and auto-align assets, and **Phoenix Engine** to understand structural relationships at runtime.

---

## 2. The PAL Ontology Taxonomy

Every element in a scene belongs to one of four semantic super-classes:

```
                            PAL ELEMENT
                                 │
         ┌───────────────┬───────┴───────┬──────────────┐
         ▼               ▼               ▼              ▼
    Structural       Openings          Trims        Fixtures
   (Skeletons)      (Cut-outs)     (Transitions)  (Attachments)
```

1. **Structural Elements**: Forms the bounding geometry of the structure. Usually represented as parametric primitives (`.pbp`).
2. **Openings**: Intersect with Structural elements, modifying their physical geometry (punching holes).
3. **Trims & Moldings**: Linear decorative pieces extruded or swept along primitive edges or borders.
4. **Fixtures & Elements**: Individual detailed objects snapped onto defined sockets.

---

## 3. Element Specifications

### 3.1. Structural Elements

#### Class: `Wall`
* **Representation**: Typically a Parametric Primitive (`.pbp`).
* **Placement Rules**: Must start and end at horizontal coordinates. Can snap vertically onto a `Foundation` or `Floor`.
* **Standard Sockets**:
  * `exterior_baseboard` / `interior_baseboard`: Runs along the bottom edge.
  * `coving`: Runs along the top interior edge.
  * `cornice`: Runs along the top exterior edge.
  * `opening_mount`: Generic socket accommodating `Door` or `Window` openings.
* **Capabilities**:
  * **Auto-Join**: Detects neighboring walls within snap distance and merges intersections (butt joints or miter joints).
  * **Boolean Cutouts**: Subtracts the bounding volume of host openings from its geometry.

#### Class: `Floor` / `Ceiling`
* **Representation**: Parametric footprint polygon.
* **Placement Rules**: Must lie on a horizontal plane.
* **Standard Sockets**:
  * `column_socket`: Grid intersections for vertical columns.
  * `stairwell`: Subtracts geometry to allow stair passage.

#### Class: `RoofPlane`
* **Representation**: Parametric sloped plane.
* **Standard Sockets**:
  * `ridge_socket`: Top horizontal intersection.
  * `valley_socket`: Concave slope intersection.
  * `gutter_socket`: Bottom eave edge.

---

### 3.2. Structural Openings

#### Class: `Door`
* **Representation**: Artist-authored Building Asset (`.pba`).
* **Placement Rules**: Requires a `DoorOpening` socket on a `Wall` primitive. Cannot exist floating.
* **Required Sockets (in asset)**:
  * `hinge`: Coordinates for rotational pivot.
  * `handle`: Interaction anchor.
* **Capabilities**:
  * **Clearance Volume**: Defines a sweeping bounding box constraint. Builder checks this area against surrounding meshes to ensure the door can open without clipping objects.
  * **Interaction Metadata**: Exposes properties like `locked`, `swing_angle`, and `open_direction` (left, right, dual) to the engine.

#### Class: `Window`
* **Representation**: Artist-authored Building Asset (`.pba`).
* **Placement Rules**: Requires a `WindowOpening` socket on a `Wall` or `RoofPlane`.
* **Standard Sockets**:
  * `shutter`: Mounts for shutters on left/right edges.
  * `flowerbox`: Mounts at the bottom exterior ledge.
* **Capabilities**:
  * **Aperture Scaling**: Can adapt to host opening sizes through standard scaling constraints defined in the asset's metadata.

---

### 3.3. Trims & Moldings

#### Class: `Cornice` / `Baseboard`
* **Representation**: Profile curve template swept along a line.
* **Placement Rules**: Attaches along the top exterior edges (`Cornice`) or bottom edges (`Baseboard`) of a `Wall`.
* **Capabilities**:
  * **Corner Mitering**: Automatically calculates 45-degree angle joints at wall intersections.
  * **Texture Alignment**: Forces UV mapping along the direction of the sweep to ensure wood grain or stone patterns align correctly.

---

### 3.4. Fixtures & Appendages

#### Class: `Column` / `Pillar`
* **Representation**: Parametric or static `.pba`.
* **Placement Rules**: Instantiates between a Floor socket and a Ceiling socket.
* **Standard Sockets**:
  * `cap`: Structural intersection at top.
  * `base`: Intersection at bottom.

---

## 4. The Style System & Semantic Swapping

Because elements are categorized semantically, a **Style Family** (e.g. `gothic_medieval` or `deco_high_society`) consists of a collection of recipes and `.pba` mappings:

```json
{
  "style_family_id": "gothic_stone_01",
  "mappings": {
    "Wall": {
      "default_surface_recipe": "recipe_rough_stone_slate"
    },
    "Window": {
      "default_asset": "window_gothic_arched_double"
    },
    "Cornice": {
      "profile_template": "profile_gothic_cove_01",
      "surface_recipe": "recipe_weathered_granite"
    }
  }
}
```

When a user instructs Builder to **"Apply Style: gothic_stone_01"**, Builder iterates through the ontology nodes of the building and replaces assets based on these semantic map rules, leaving the building's layout, socket attachments, and structural dimensions untouched.
