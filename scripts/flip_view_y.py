"""
Flip View Y — ビューポートを反転表示するBlenderアドオン

トップビュー等でモデルの対称性・シルエットを確認するために、
3Dビューポートの表示を鏡像反転させる。

使い方:
    3Dビューポートのヘッダー「ビュー」メニュー > Flip View
    または F3 検索で「Flip View」

注意:
    反転はビュー行列への一時的な操作のため、視点を回転（オービット）すると
    元の表示に戻る。もう一度実行しても元に戻せる。
"""

import bpy
from mathutils import Matrix

bl_info = {
    "name": "Flip View Y",
    "author": "kantoku project",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "3Dビューポート > ビューメニュー > Flip View",
    "description": "ビューポートを鏡像反転して対称性チェックを行う",
    "category": "3D View",
}


class VIEW3D_OT_flip_view(bpy.types.Operator):
    """ビューポートを鏡像反転する（再実行で元に戻る）"""

    bl_idname = "view3d.flip_view"
    bl_label = "Flip View"
    bl_options = {"REGISTER"}

    axis: bpy.props.EnumProperty(
        name="反転軸",
        description="画面上のどの軸を中心に反転するか",
        items=[
            ("Y", "Y軸（左右反転）", "画面の縦軸を中心に左右を反転"),
            ("X", "X軸（上下反転）", "画面の横軸を中心に上下を反転"),
        ],
        default="Y",
    )

    @classmethod
    def poll(cls, context):
        return context.area is not None and context.area.type == "VIEW_3D"

    def execute(self, context):
        rv3d = context.region_data
        if rv3d is None:
            self.report({"WARNING"}, "3Dビューポート上で実行してください")
            return {"CANCELLED"}

        # ビュー空間で先頭から掛けることで画面基準の反転になる
        # Y軸反転 = 画面X座標を negate / X軸反転 = 画面Y座標を negate
        mirror_axis = (1.0, 0.0, 0.0) if self.axis == "Y" else (0.0, 1.0, 0.0)
        rv3d.view_matrix = Matrix.Scale(-1.0, 4, mirror_axis) @ rv3d.view_matrix

        return {"FINISHED"}


def draw_menu(self, context):
    self.layout.separator()
    self.layout.operator(VIEW3D_OT_flip_view.bl_idname, text="Flip View（左右反転）").axis = "Y"
    self.layout.operator(VIEW3D_OT_flip_view.bl_idname, text="Flip View（上下反転）").axis = "X"


def register():
    bpy.utils.register_class(VIEW3D_OT_flip_view)
    bpy.types.VIEW3D_MT_view.append(draw_menu)


def unregister():
    bpy.types.VIEW3D_MT_view.remove(draw_menu)
    bpy.utils.unregister_class(VIEW3D_OT_flip_view)


if __name__ == "__main__":
    register()
