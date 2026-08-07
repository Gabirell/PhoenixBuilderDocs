# Chapter 4: Core Foundational Classes

This chapter defines the **25 foundational architectural concepts** in the PAL core dictionary. These classes represent the semantic primitives from which any building is assembled.

> [!IMPORTANT]
> For **Milestone 1: First House**, we only implement the 5 core classes: `Wall`, `Floor`, `Roof`, `Door`, and `Window`. All other classes are currently deferred to the LATER backlog (Anti-Five-Year Shield).

---

## 1. Vertical Structures

### 1.1. `Wall`
* **Representation**: Parametric Primitive (`.pbp`).
* **Semantic Role**: The primary vertical structural partition. Manages height, thickness, and footprint coordinates.

### 1.2. `Column`
* **Representation**: Building Asset (`.pba`) or Parametric (`.pbp`).
* **Semantic Role**: A vertical support shaft transferring load downwards. Snaps between floors or bases.

### 1.3. `Buttress`
* **Representation**: Building Asset (`.pba`).
* **Semantic Role**: An exterior lateral support pier reinforcing walls (highly prominent in Gothic and classical architecture).

### 1.4. `Pillar`
* **Representation**: Building Asset (`.pba`).
* **Semantic Role**: A heavy square or rectangular vertical structural support.

### 1.5. `Arch`
* **Representation**: Building Asset (`.pba`).
* **Semantic Role**: A curved structure spanning an opening, serving both structural and decorative purposes.

---

## 2. Horizontal Structures

### 2.1. `Foundation`
* **Representation**: Parametric Primitive (`.pbp`).
* **Semantic Role**: The load-bearing base resting on the terrain. Adapts downward to meet sloped ground.

### 2.2. `Floor`
* **Representation**: Parametric Primitive (`.pbp`).
* **Semantic Role**: The horizontal walkable surface of a room.

### 2.3. `Ceiling`
* **Representation**: Parametric Primitive (`.pbp`) or automatically generated under-face of a floor.
* **Semantic Role**: The overhead interior surface of a room.

### 2.4. `Balcony`
* **Representation**: Building Asset (`.pba`).
* **Semantic Role**: An elevated platform projecting from an exterior wall, requiring structural brackets and handrails.

### 2.5. `Porch`
* **Representation**: Composite structure.
* **Semantic Role**: A covered shelter projecting from the entrance of a building.

---

## 3. Sloped Structures & Roofs

### 3.1. `RoofPlane`
* **Representation**: Parametric Primitive (`.pbp`).
* **Semantic Role**: A sloped surface protecting the top of the structure. Manages slope pitch.

### 3.2. `RoofRidge`
* **Representation**: Trim Line.
* **Semantic Role**: The horizontal intersection line at the peak of two sloped roof planes.

### 3.3. `RoofValley`
* **Representation**: Trim Line.
* **Semantic Role**: The sloped concave intersection line where two roof planes meet.

### 3.4. `RoofHip`
* **Representation**: Trim Line.
* **Semantic Role**: The sloped convex intersection line extending from the ridge to the eaves.

### 3.5. `Eave`
* **Representation**: Trim Line.
* **Semantic Role**: The bottom overhanging edge of a roof plane.

### 3.6. `Gutter`
* **Representation**: Trim Sweep (`.pba` profile).
* **Semantic Role**: A channel running along the eaves to collect rainwater.

### 3.7. `DrainPipe`
* **Representation**: Building Asset (`.pba`) or swept curve.
* **Semantic Role**: A vertical pipe conveying water from gutters to the ground.

### 3.8. `Chimney`
* **Representation**: Building Asset (`.pba`).
* **Semantic Role**: A vertical brick/stone flue venting smoke from hearths.

---

## 4. Openings

### 4.1. `Door`
* **Representation**: Building Asset (`.pba`).
* **Semantic Role**: A swappable barrier blocking or allowing movement through a wall. Requires hinge and clearance metadata.

### 4.2. `Window`
* **Representation**: Building Asset (`.pba`).
* **Semantic Role**: An aperture in a wall or roof plane designed to admit light and air.

### 4.3. `Gate`
* **Representation**: Building Asset (`.pba`).
* **Semantic Role**: A large exterior double-leaf opening barrier (used in courtyards or fortresses).

---

## 5. Trims & Moldings

### 5.1. `Baseboard`
* **Representation**: Trim Sweep.
* **Semantic Role**: A decorative molding running along the bottom interior edge of walls.

### 5.2. `Cornice`
* **Representation**: Trim Sweep.
* **Semantic Role**: An ornamental molding crown running along the top exterior edge of walls.

### 5.3. `Coving`
* **Representation**: Trim Sweep.
* **Semantic Role**: An ornamental concave profile transitioning between interior walls and ceilings.

### 5.4. `Ledge`
* **Representation**: Trim Sweep or Building Asset (`.pba`).
* **Semantic Role**: A horizontal stone or wood projection forming a shelf along a wall facade.

### 5.5. `Molding`
* **Representation**: Trim Sweep.
* **Semantic Role**: General linear profile sweep applied to panel joints or boundaries.

---

## 6. Circulation

### 6.1. `Stair`
* **Representation**: Parametric Primitive (`.pbp`) or static `.pba`.
* **Semantic Role**: A series of steps allowing vertical transit.

### 6.2. `Landing`
* **Representation**: Horizontal platform.
* **Semantic Role**: An intermediate flat platform between stair flights.

### 6.3. `Handrail`
* **Representation**: Trim Sweep or modular `.pba`.
* **Semantic Role**: A protective barrier and grip running along stairs and balconies.
