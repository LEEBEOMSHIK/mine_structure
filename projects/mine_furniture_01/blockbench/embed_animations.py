"""Embed the add-on Bedrock animations into the matching .bbmodel files so they
appear in Blockbench's Animate tab (the runtime files live in
resource_pack/animations/*.animation.json and are NOT stored inside .bbmodel by
default, so the Animate tab shows nothing).

For each blockbench/<sid>.bbmodel that has resource_pack/animations/<sid>.animation.json,
convert each Bedrock animation to Blockbench's internal animation format (mapping
bone names to the model's group UUIDs) and write it into the .bbmodel "animations".

Re-run this after regenerating a model (the generators reset animations to []).
"""
import json
import os
import uuid

HERE = os.path.dirname(__file__)
RP_ANIM = os.path.normpath(os.path.join(HERE, "..", "addon", "resource_pack", "animations"))


def uid():
    return str(uuid.uuid4())


def loop_value(loop):
    if loop is True:
        return "loop"
    if loop == "hold_on_last_frame":
        return "hold_on_last_frame"
    return "once"


def as_xyz(value):
    """Bedrock channel value -> {x,y,z} strings. number -> uniform (scale)."""
    if isinstance(value, (int, float)):
        return {"x": str(value), "y": str(value), "z": str(value)}
    if isinstance(value, list):
        v = [str(c) for c in (list(value) + [0, 0, 0])[:3]]
        return {"x": v[0], "y": v[1], "z": v[2]}
    if isinstance(value, str):
        return {"x": value, "y": value, "z": value}
    return {"x": "0", "y": "0", "z": "0"}


def keyframes_for(channel, value):
    """value can be a constant (number/list) or a dict {time: value}."""
    frames = []
    if isinstance(value, dict) and not {"x", "y", "z"} & set(value):
        items = sorted(value.items(), key=lambda kv: float(kv[0]))
        for t, v in items:
            frames.append((float(t), v))
    else:
        frames.append((0.0, value))
    out = []
    for t, v in frames:
        out.append({
            "channel": channel,
            "data_points": [as_xyz(v)],
            "uuid": uid(),
            "time": t,
            "color": -1,
            "interpolation": "linear",
            "bezier_linked": True,
        })
    return out


def convert(anim_name, anim, name_to_uuid):
    animators = {}
    for bone_name, channels in anim.get("bones", {}).items():
        guid = name_to_uuid.get(bone_name)
        if not guid:
            continue
        keyframes = []
        for channel in ("rotation", "position", "scale"):
            if channel in channels:
                keyframes.extend(keyframes_for(channel, channels[channel]))
        if keyframes:
            animators[guid] = {"name": bone_name, "type": "bone", "keyframes": keyframes}
    length = anim.get("animation_length")
    if length is None:
        times = [kf["time"] for a in animators.values() for kf in a["keyframes"]]
        length = max(times) if times else 0.0
    return {
        "uuid": uid(), "name": anim_name, "loop": loop_value(anim.get("loop")),
        "override": False, "length": length, "snapping": 24, "selected": False,
        "saved": True, "path": "", "anim_time_update": "", "blend_weight": "",
        "start_delay": "", "loop_delay": "", "animators": animators,
    }


def process(bbmodel_path, sid):
    anim_path = os.path.join(RP_ANIM, sid + ".animation.json")
    if not os.path.isfile(anim_path):
        return None
    with open(bbmodel_path, encoding="utf-8") as fh:
        model = json.load(fh)
    name_to_uuid = {g.get("name"): g.get("uuid") for g in model.get("groups", []) if isinstance(g, dict)}
    anims = json.load(open(anim_path, encoding="utf-8")).get("animations", {})
    converted = [convert(name, body, name_to_uuid) for name, body in anims.items()]
    model["animations"] = converted
    with open(bbmodel_path, "w", encoding="utf-8") as fh:
        json.dump(model, fh, ensure_ascii=False, separators=(",", ":"))
    return len(converted)


def main():
    count = 0
    for fname in sorted(os.listdir(HERE)):
        if not fname.endswith(".bbmodel"):
            continue
        sid = fname[:-len(".bbmodel")]
        n = process(os.path.join(HERE, fname), sid)
        if n:
            print(f"embedded {n} animation(s) into {fname}")
            count += 1
    print(f"done: {count} model(s) updated")


if __name__ == "__main__":
    main()
