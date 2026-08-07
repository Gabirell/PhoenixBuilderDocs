# Chapter 5: Host & Socket Rules

In PAL, assets do not float arbitrarily in space. They exist within a structured hierarchy of **Hosts** and **Sockets**. This grammar prevents placement errors and automates snapping logic.

---

## 1. Host Relationships

A **Host** is a structural element (typically a parametric primitive like `Wall` or `RoofPlane`) that owns the local coordinate system and coordinate boundaries for other elements.

* **Openings require a Host**: A `Door` or `Window` cannot exist in mid-air. It must declare a `Wall` or `RoofPlane` host. 
* **Trims require a Host**: A `Baseboard` or `Cornice` attaches to a `Wall` boundary line.
* **Child Offset Propagation**: If a host is moved, resized, or rotated, all hosted elements automatically recalculate their absolute world positions based on their relative coordinates on the host.

---

## 2. Sockets & Connector Docking

Sockets are defined attachment points with semantic constraints. Docking occurs when a Building Asset (`.pba`) matching a connector is snapped into a primitive's (`.pbp`) socket.

```
      [ Wall Primitive ]  ──────► Sockets: "WindowOpening" (Type: Window)
             │
             ▼ Snaps
      [ Window Asset ]    ──────► Connectors: "FrameSnapper" (Type: Window)
```

### Semantic Constraints
Every socket defines an `allowed_classes` array.
* A socket of type `door_mount` will reject any asset that is not of class `Door` or its descendants.
* Sockets can also enforce physical constraints (e.g., maximum width and height limits).

---

## 3. Clearance Volumes

To prevent doors, windows, and drawers from clipping into columns, furniture, or walls, PAL defines **Clearance Volumes** in asset metadata.

* **Sweep Volumes**: A `Door` asset must declare its swing radius and angle (e.g., 90 degrees or 180 degrees).
* **Validation Checks**: When a door is snapped into a wall opening, Phoenix Builder checks if any static geometry collides with the door's sweep volume. If clipping is detected, the editor displays a validation warning (or blocks placement).

---

## 4. Trim Sweeps and Miter Generation

Trims are linear profiles (Trim Templates) swept along parent lines.

* **Path Definition**: Sockets on walls can define paths (e.g. the bottom profile line of a wall).
* **Auto-Mitering**: When two walls meet at an angle, the hosted trims (Baseboard, Cornice) must automatically calculate miter cuts. Instead of generating square ends, the geometry engine cuts the trim profiles at exactly half the wall-intersection angle to ensure a seamless seam.
