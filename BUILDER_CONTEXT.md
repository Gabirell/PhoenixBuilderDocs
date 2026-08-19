# PHOENIX ECOSYSTEM — MASTER CONTEXT & WORKING INSTRUCTIONS

## 1. PROJECT VISION
Phoenix is an **architectural creation ecosystem** where users can create, assemble, edit parametrically, reuse, and share architectural pieces. 
> **Users must be able to CREATE, not merely BUY or DOWNLOAD.**
Must serve both Beginners (easy, visual) and Professionals (precise, parametric, scriptable).

## 2. ANTI-FIVE-YEAR RULE
Phoenix must evolve through **small, working vertical slices**.
DEFINE A SMALL PIECE → IMPLEMENT IT → SEE IT → EXPERIMENT WITH IT → LEARN WHAT IS MISSING → UPDATE ARCHITECTURE → IMPLEMENT THE NEXT PIECE

## 3. PHOENIX ARCHITECTURAL LANGUAGE (PAL)
> **Design architecture, not geometry.**
Semantic definitions (Wall, Door, Window) rather than just meshes.

## 4. PAL CORE PRINCIPLES
1. Engine agnostic of gameplay.
2. Composition over inheritance.
3. Performance measured, not assumed.
4. Evolution without rupture.
5. Growth by extension.
6. Semantic architecture separated from baked geometry.
7. Documentation and implementation evolve together.

## 5. GOLDEN RULE
> **No AI assistant may introduce a feature that changes the philosophy of Phoenix Builder without first proposing a Design Bible update.**
Do not silently introduce large architectural systems. Keep implementations simple for the current vertical slice.

## 6. .PBP AND .PBA CONCEPT
- **.pbp (Phoenix Primitive)**: Parametric representation describing semantic properties (points, dimensions) instead of baked meshes.
- **.pba (Phoenix Building Asset)**: Compiled asset packages (future MVP).

## 7. CURRENT IMPLEMENTATION ENVIRONMENT
- **Xcode, Swift, macOS, SceneKit / SwiftUI**.
The Builder implementation is in Xcode, not Blender.

## 8. PHX-MVP-001: FIRST HOUSE
Initial PAL scope restricted to 5 classes: Wall, Floor, Roof, Door, Window.
Currently Implemented (Steps 1-5):
- Swift PAL model (Wall).
- .pbp export.
- Wall rendering in SceneKit Builder.
- Editable Wall parameters (Length, Height, Thickness).
- Multiple Walls & Room Assembly (Endpoint-to-Endpoint connections).

## 9. IMMEDIATE NEXT ACTION: STEP 6 — TRANSFORM & CONNECT
The next vertical slice to implement in Phoenix Builder:
### Phase A: Viewport stability
Fix grid disappearance, camera clipping, Z-fighting. (zNear=0.1, zFar=1000.0). Safe minimum bounds.
### Phase B: 3D Axis Transform Gizmo
Visual handles for X (red), Y (green), Z (blue) to constrain movement. Configurable ON/OFF toggle. Applied only to Wall for now.
### Phase C: Endpoint-only Snap Preview
Basic endpoint-to-endpoint coincidence detection. Glowing preview when dragging near a valid target. Snap on release. NOT a semantic system (no host relations yet).

**CRITICAL STOP CONDITION**: After Step 6, stop and test manually. Build a small building to identify real friction before planning Step 7.

## 10. AI ASSISTANT WORKFLOW
1. Read AGENTS.md, AI_CONTEXT.md, PAL specs.
2. Propose implementation plan before changes.
3. Keep changes narrowly scoped.
4. Run tests and verify visually.
5. Do NOT rewrite architecture unnecessarily or add speculative systems.
