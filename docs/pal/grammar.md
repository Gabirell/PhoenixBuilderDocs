# Chapter 3: Grammar & Inheritance

To keep the platform flexible and avoid writing unique code for hundreds of different objects, PAL uses a **hierarchical grammar**. Elements are organized into an inheritance tree. 

When Phoenix Builder needs to evaluate rules or apply styles, it query-checks classes at any node in the inheritance tree.

---

## The PAL Inheritance Hierarchy

Below is the foundational inheritance map for PAL element classes:

```
                            PAL Element
                                 │
     ┌───────────────────────────┼───────────────────────────┐
     ▼                           ▼                           ▼
Structural Element            Opening                      Trim
     │                           │                           │
     ├─ VerticalStructure        ├─ Door                     ├─ Baseboard
     │    └─ Wall                ├─ Window                   ├─ Chair Rail
     │    └─ Column              ├─ Arch                     ├─ Cornice
     │    └─ Buttress            └─ Gate                     ├─ Coving
     │                                                       ├─ Ledge
     ├─ HorizontalStructure                                  ├─ Window Sill
     │    └─ Foundation                                      └─ Door Surround
     │    └─ Floor
     │    └─ Ceiling
     │
     └─ SlopedStructure
          └─ RoofPlane
          └─ Stair
```

---

## How Inheritance Simplifies Development

### 1. Polymorphic Sockets
Instead of configuring a socket on a wall to only accept a single window file like `window_gothic_lancet_01`, the socket defines its constraint as `allowed_classes: ["Window"]`. 
Because `GothicLancetWindow` inherits from `Window`, it is automatically accepted by the socket. If the user later imports a `ModernCasementWindow`, it will work without modifying the wall's socket constraints.

### 2. High-Level Style Overrides
Style Families can apply overrides at any level of the inheritance hierarchy.
* If a style mapping defines:
  ```json
  "VerticalStructure": { "surface_recipe": "recipe_weathered_brick" }
  ```
  Both `Wall` and `Column` elements inherit this brick recipe.
* If the style family then adds a specific child override:
  ```json
  "Column": { "surface_recipe": "recipe_polished_marble" }
  ```
  The column will override its parent style and render as marble, while walls remain brick.

### 3. Shared Behaviors
All elements inheriting from `Opening` share the capability to detect host intersections and declare boolean cutout boundaries. All elements inheriting from `Trim` share the capability to swept-extrude along parent borders.
