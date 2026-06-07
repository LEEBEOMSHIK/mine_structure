"""Package skin_pack/ into dist/ as a .mcpack (zip). Excludes preview_*.png."""
import datetime
import os
import zipfile

PROJECT = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.join(PROJECT, "skin_pack")
REPO_ROOT = os.path.normpath(os.path.join(PROJECT, "..", ".."))
DIST = os.path.join(REPO_ROOT, "dist")


def main():
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = os.path.join(DIST, "mine_skins_01-" + stamp)
    os.makedirs(out_dir, exist_ok=True)
    mcpack = os.path.join(out_dir, "unicorn_pastel_girls.mcpack")
    with zipfile.ZipFile(mcpack, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _dirs, files in os.walk(PACK):
            for name in files:
                if name.startswith("preview_"):
                    continue
                full = os.path.join(root, name)
                rel = os.path.relpath(full, PACK)
                zf.write(full, rel)
    print("wrote %s (%d bytes)" % (os.path.relpath(mcpack, REPO_ROOT), os.path.getsize(mcpack)))


if __name__ == "__main__":
    main()
