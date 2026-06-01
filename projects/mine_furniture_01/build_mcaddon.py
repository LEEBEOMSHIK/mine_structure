"""Package the add-on into dist/ as .mcpack files and a combined .mcaddon.

Run from the project root:
  python build_mcaddon.py
"""
import os
import time
import zipfile

PROJECT = os.path.dirname(os.path.abspath(__file__))
ADDON = os.path.join(PROJECT, "addon")
REPO_ROOT = os.path.normpath(os.path.join(PROJECT, "..", ".."))
DIST = os.path.join(REPO_ROOT, "dist")

BP = os.path.join(ADDON, "behavior_pack")
RP = os.path.join(ADDON, "resource_pack")


def zip_dir(zf, src_dir, arc_prefix):
    for root, _dirs, files in os.walk(src_dir):
        for name in files:
            full = os.path.join(root, name)
            rel = os.path.relpath(full, src_dir)
            zf.write(full, os.path.join(arc_prefix, rel))


def main():
    stamp = time.strftime("%Y%m%d-%H%M%S")
    out_dir = os.path.join(DIST, f"mine_furniture_01-{stamp}")
    os.makedirs(out_dir, exist_ok=True)

    bp_pack = os.path.join(out_dir, "mine_furniture_01_behavior_pack.mcpack")
    rp_pack = os.path.join(out_dir, "mine_furniture_01_resource_pack.mcpack")
    addon = os.path.join(out_dir, "mine_furniture_01.mcaddon")

    with zipfile.ZipFile(bp_pack, "w", zipfile.ZIP_DEFLATED) as zf:
        zip_dir(zf, BP, "")
    with zipfile.ZipFile(rp_pack, "w", zipfile.ZIP_DEFLATED) as zf:
        zip_dir(zf, RP, "")
    with zipfile.ZipFile(addon, "w", zipfile.ZIP_DEFLATED) as zf:
        zip_dir(zf, BP, "behavior_pack")
        zip_dir(zf, RP, "resource_pack")

    for path in (bp_pack, rp_pack, addon):
        print(f"wrote {os.path.relpath(path, REPO_ROOT)} ({os.path.getsize(path)} bytes)")


if __name__ == "__main__":
    main()
