# Unicorn Dining Set Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two independent unicorn-themed furniture entities: `mine_structure:unicorn_dining_table` and `mine_structure:unicorn_chair`.

**Architecture:** Follow the existing `unicorn_toilet` content pattern. Each furniture item gets behavior entity JSON, client entity JSON, geometry JSON, a 64x64 texture atlas, render controller, content document, resource map, and registry entries. Static first version only; seating or advanced interactions are deferred.

**Tech Stack:** Minecraft Bedrock add-on JSON, Python validation/generation helpers, PNG texture generation via Pillow, PowerShell packaging.

---

### Task 1: Validation First

**Files:**
- Modify: `projects/mine_furniture_01/validate_unicorn_toilet_resources.py`

- [ ] Extend validation to check all three required furniture IDs: `unicorn_toilet`, `unicorn_dining_table`, and `unicorn_chair`.
- [ ] Run `python projects/mine_furniture_01/validate_unicorn_toilet_resources.py`.
- [ ] Expected before implementation: FAIL for missing dining table and chair files.

### Task 2: Register Content

**Files:**
- Modify: `projects/mine_furniture_01/content/README.md`
- Modify: `projects/mine_furniture_01/content/furniture/README.md`
- Create: `projects/mine_furniture_01/content/furniture/unicorn_dining_table.md`
- Create: `projects/mine_furniture_01/content/furniture/unicorn_dining_table.resources.json`
- Create: `projects/mine_furniture_01/content/furniture/unicorn_chair.md`
- Create: `projects/mine_furniture_01/content/furniture/unicorn_chair.resources.json`

- [ ] Add both furniture IDs to registries.
- [ ] Add docs with source documents, add-on files, and first-version static behavior goals.

### Task 3: Add Bedrock Entity Resources

**Files:**
- Create behavior entities under `addon/behavior_pack/entities/`.
- Create client entities under `addon/resource_pack/entity/`.
- Create render controllers under `addon/resource_pack/render_controllers/`.
- Create geometry files under `addon/resource_pack/models/entity/`.
- Create texture folders and PNG atlases under `addon/resource_pack/textures/entity/`.

- [ ] Dining table geometry: table top, four legs, horn centerpiece, rainbow runner.
- [ ] Chair geometry: seat, four legs, backrest, ears, horn, rainbow mane.
- [ ] Use static entities with summonable behavior.
- [ ] Use 64x64 texture atlases and `entity_alphatest`.

### Task 4: Verify and Package

**Files:**
- Modify: `projects/mine_furniture_01/README.md`
- Modify: `projects/mine_furniture_01/PROJECT_CONTEXT.md`
- Modify: `PROJECTS.md`
- Create: `dist/mine_furniture_01-<timestamp>/...`

- [ ] Run validation script and JSON parsing.
- [ ] Package updated behavior/resource packs into `.mcaddon`.
- [ ] Document latest package path and remaining manual Minecraft test.
