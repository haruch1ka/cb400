bl_info = {
    "name": "Flip View Y",
    "author": "user",
    "version": (1, 0),
    "blender": (5, 0, 0),
    "location": "3D View, Shift + Numpad 9",
    "description": "視点のY成分だけ反転する（X・Zは維持）",
    "category": "3D View",
}

import bpy
import math


class VIEW3D_OT_flip_view_y(bpy.types.Operator):
    """視点のY成分だけ反転する（X・Zは維持）"""
    bl_idname = "view3d.flip_view_y"
    bl_label = "Flip View Y"

    def execute(self, context):
        rv3d = context.region_data
        eul = rv3d.view_rotation.to_euler('XYZ')
        # 方位角のみ π - θ にすると視線方向のYだけが反転する
        eul.z = math.pi - eul.z
        rv3d.view_rotation = eul.to_quaternion()
        return {'FINISHED'}


addon_keymaps = []


def register():
    bpy.utils.register_class(VIEW3D_OT_flip_view_y)
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="3D View", space_type='VIEW_3D')
        kmi = km.keymap_items.new("view3d.flip_view_y", 'NUMPAD_9', 'PRESS', shift=True)
        addon_keymaps.append((km, kmi))


def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(VIEW3D_OT_flip_view_y)
