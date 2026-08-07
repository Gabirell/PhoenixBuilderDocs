# Chapter 6: The PAL Style System

The surface appearance and static details of a building are completely independent of its structural geometry. PAL enforces this separation through the **Style System**.

---

## 1. Decoupling Geometry from Style

A building footprint, height, and partition layout represent the building's **Skeletal DNA**. The visual presentation (wood type, stone masonry style, door models, coving moldings) represents the building's **Style Family**.

Because PAL coordinates are semantic, you can change the visual theme of an entire city block in a single click:
* The core structural coordinates of the walls, floors, and openings remain identical.
* The editor swaps the visual assets and surface textures mapping to those semantic classes.

---

## 2. Style Family Mapping Schema

A Style Family is a JSON definition file that acts as a lookup dictionary. When Builder compiles a scene, it queries the active Style Family to resolve what assets to instantiate for each class.

Example mapping structure:

```json
{
  "style_family_id": "nordic_stave_01",
  "display_name": "Nordic Stave Wood",
  "mappings": {
    "Wall": {
      "interior_face": "recipe_pine_planks_clean",
      "exterior_face": "recipe_pine_shingles_weathered"
    },
    "Door": {
      "default_asset": "door_pine_heavy_01"
    },
    "Cornice": {
      "profile_template": "profile_carved_dragon_edge",
      "surface_recipe": "recipe_dark_pine_tar"
    },
    "Baseboard": {
      "profile_template": "profile_simple_chamfer_01",
      "surface_recipe": "recipe_pine_planks_clean"
    }
  }
}
```

---

## 3. Style Variations & Organic Randomization

To prevent procedural cities from looking repetitive, PAL support **Organic Style Variation Rules**. A Style Family mapping can map a semantic class to an array of choices instead of a single asset.

* **Material Swapping Rules**: A mapping for a brick wall can list multiple compatible brick texture recipes (e.g. `recipe_brick_clean_01`, `recipe_brick_mossy_01`). The compiler will randomly apply these recipes to individual wall panels based on a seed value, ensuring natural variation.
* **Asset Variation Rules**: A window opening style mapping can list multiple window models with varying decay rates or pane divisions, distributing them across the building footprint while preserving the same structural anchors.
