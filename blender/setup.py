"""
CB400SF Blender初期セットアップスクリプト
実行: blender --background --python setup.py
出力: blender/cb400sf_main.blend
"""

import bpy
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR  # blender/ がプロジェクトルート相当
BLEND_PATH = os.path.join(SCRIPT_DIR, "cb400sf_main.blend")

REF_SIDE   = os.path.join(SCRIPT_DIR, "references", "photos", "detail", "cb400sf-199.jpg")
REF_FRONT  = os.path.join(SCRIPT_DIR, "references", "photos", "detail", "cb400sf-057.jpg")
REF_BLUEPRINT = os.path.join(SCRIPT_DIR, "references", "blueprint", "cb400sf_2018_blueprint.jpg")


# ------------------------------------------------------------------ #
# 1. デフォルトオブジェクトを全削除
# ------------------------------------------------------------------ #
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

# デフォルトコレクションの中身も消す
for col in bpy.data.collections:
    bpy.data.collections.remove(col)


# ------------------------------------------------------------------ #
# 2. シーン単位設定（Metric / Millimeters）
# ------------------------------------------------------------------ #
scene = bpy.context.scene
scene.unit_settings.system       = "METRIC"
scene.unit_settings.length_unit  = "MILLIMETERS"
scene.unit_settings.scale_length = 0.001   # 1 Blender unit = 1 mm


# ------------------------------------------------------------------ #
# 3. コレクション構成を作成
# ------------------------------------------------------------------ #
root = bpy.data.collections.new("CB400SF")
scene.collection.children.link(root)

collection_names = [
    "_REFERENCE",
    "Frame",
    "Engine",
    "Body",
    "Suspension",
    "Wheels",
    "Electrical",
]

cols = {}
for name in collection_names:
    col = bpy.data.collections.new(name)
    root.children.link(col)
    cols[name] = col

# _REFERENCE はレンダリングに映らないよう除外
cols["_REFERENCE"].hide_render = True


# ------------------------------------------------------------------ #
# 4. リファレンス画像を配置
# ------------------------------------------------------------------ #
def add_reference_image(filepath, name, location, rotation_euler, size=2000):
    """リファレンス画像エンプティを作成して _REFERENCE コレクションへ追加"""
    if not os.path.exists(filepath):
        print(f"[WARNING] リファレンス画像が見つかりません: {filepath}")
        return None

    bpy.ops.object.empty_add(type="IMAGE", location=location)
    obj = bpy.context.active_object
    obj.name = name

    img = bpy.data.images.load(filepath)
    obj.data = img
    obj.empty_image_depth   = "DEFAULT"
    obj.empty_image_side    = "FRONT"
    obj.empty_display_size  = size
    obj.rotation_euler      = rotation_euler

    # デフォルトのコレクションから外して _REFERENCE へ移動
    for c in obj.users_collection:
        c.objects.unlink(obj)
    cols["_REFERENCE"].objects.link(obj)

    return obj

import math

# 右側面図（YZ平面）
add_reference_image(
    filepath       = REF_BLUEPRINT,
    name           = "REF_side_right",
    location       = (0, 0, 755),
    rotation_euler = (math.radians(90), 0, math.radians(90)),
    size           = 2080,
)

# 正面図（XZ平面）
add_reference_image(
    filepath       = REF_BLUEPRINT,
    name           = "REF_front",
    location       = (0, -1500, 755),
    rotation_euler = (math.radians(90), 0, 0),
    size           = 2080,
)

# 上面図（XY平面）
add_reference_image(
    filepath       = REF_BLUEPRINT,
    name           = "REF_top",
    location       = (0, 0, 1500),
    rotation_euler = (0, 0, 0),
    size           = 2080,
)


# ------------------------------------------------------------------ #
# 5. 計測用エンプティを配置（スケール確認用）
# ------------------------------------------------------------------ #
def add_measure_empty(name, location, col_name="_REFERENCE"):
    bpy.ops.object.empty_add(type="PLAIN_AXES", location=location)
    obj = bpy.context.active_object
    obj.name = name
    obj.empty_display_size = 50
    for c in obj.users_collection:
        c.objects.unlink(obj)
    cols[col_name].objects.link(obj)

# ホイールベース両端（前輪・後輪の接地点）
add_measure_empty("MEASURE_wheel_front",  (0,    0,    0))
add_measure_empty("MEASURE_wheel_rear",   (0, 1410,    0))   # ホイールベース1410mm
add_measure_empty("MEASURE_height_top",   (0,    0, 1080))   # 全高1080mm
add_measure_empty("MEASURE_width_half",   (372,  0,  755))   # 全幅745mm の半分


# ------------------------------------------------------------------ #
# 6. カメラ設定（右側面ビュー）
# ------------------------------------------------------------------ #
bpy.ops.object.camera_add(
    location       = (0, -4000, 755),
    rotation       = (math.radians(90), 0, 0),
)
cam_obj = bpy.context.active_object
cam_obj.name = "Camera_side"
cam_obj.data.lens       = 100      # 望遠気味（歪み少ない）
# scale_length=0.001（1unit=1mm）のため clip をmm単位で設定
cam_obj.data.clip_start = 10       # 10mm
cam_obj.data.clip_end   = 100000   # 100,000mm = 100m
scene.camera = cam_obj

for c in cam_obj.users_collection:
    c.objects.unlink(cam_obj)
scene.collection.objects.link(cam_obj)


# ------------------------------------------------------------------ #
# 7. スタジオライト（3点ライト）
# ------------------------------------------------------------------ #
lights = [
    ("Light_key",   "AREA",  (-2000, -3000, 3000), 500000),
    ("Light_fill",  "AREA",  ( 2000, -2000, 2000), 200000),
    ("Light_back",  "AREA",  (    0,  3000, 2000), 300000),
]

for lname, ltype, loc, energy in lights:
    bpy.ops.object.light_add(type=ltype, location=loc)
    lobj = bpy.context.active_object
    lobj.name = lname
    lobj.data.energy = energy
    for c in lobj.users_collection:
        c.objects.unlink(lobj)
    scene.collection.objects.link(lobj)


# ------------------------------------------------------------------ #
# 8. レンダリング設定（Cycles）
# ------------------------------------------------------------------ #
scene.render.engine          = "CYCLES"
scene.render.resolution_x   = 1920
scene.render.resolution_y   = 1080
scene.render.filepath        = os.path.join(SCRIPT_DIR, "render", "wip", "wip_")
scene.render.image_settings.file_format = "PNG"

# Cycles サンプル数
scene.cycles.samples         = 128
scene.cycles.preview_samples = 32


# ------------------------------------------------------------------ #
# 9. ビューポートクリップを自動設定するテキストブロックを埋め込む
#    use_module=True にするとファイルを開いたとき自動実行される
# ------------------------------------------------------------------ #
script_name = "auto_viewport_clip.py"
if script_name in bpy.data.texts:
    bpy.data.texts.remove(bpy.data.texts[script_name])

text = bpy.data.texts.new(script_name)
text.use_module = True
text.write(
    "import bpy\n"
    "\n"
    "def _set_clip(dummy=None):\n"
    "    for window in bpy.context.window_manager.windows:\n"
    "        for area in window.screen.areas:\n"
    "            if area.type == 'VIEW_3D':\n"
    "                for space in area.spaces:\n"
    "                    if space.type == 'VIEW_3D':\n"
    "                        space.clip_start = 1\n"
    "                        space.clip_end   = 100000\n"
    "\n"
    "if _set_clip not in bpy.app.handlers.load_post:\n"
    "    bpy.app.handlers.load_post.append(_set_clip)\n"
    "_set_clip()\n"
)


# ------------------------------------------------------------------ #
# 10. .blend ファイルを保存
# ------------------------------------------------------------------ #
bpy.ops.wm.save_as_mainfile(filepath=BLEND_PATH)
print(f"\n✅ 保存完了: {BLEND_PATH}\n")
