var exportTargets = {
  geometry: "C:/project/mine_structure/projects/mine_furniture_01/addon/resource_pack/models/entity/unicorn_toilet.geo.json",
  texture: "C:/project/mine_structure/projects/mine_furniture_01/addon/resource_pack/textures/entity/unicorn_toilet/unicorn_toilet_atlas.png",
  animation: "C:/project/mine_structure/projects/mine_furniture_01/addon/resource_pack/animations/unicorn_toilet.animation.json"
};

var exportNotes = [
  "Run this in Blockbench through MCP risky_eval after opening the furniture project.",
  "Export Bedrock Geometry to exportTargets.geometry.",
  "Save texture unicorn_toilet_atlas to exportTargets.texture.",
  "Export animations lid_open, lid_close, flush to exportTargets.animation.",
  "If automated export API is unavailable, use these exact paths in the Blockbench UI export dialogs."
];

({
  exportTargets: exportTargets,
  exportNotes: exportNotes
});
