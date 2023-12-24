import bpy
from ..operators.recalculate_bone_roll_operator import ARMATURE_OT_RecalculateBoneRoll

class BAMBOOTOOLS_PT_V1BoneRollPanel(bpy.types.Panel):
    bl_label = "V1 Asset conversion"
    bl_idname = "BAMBOOTOOLS_PT_v1_bone_roll"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Bamboo Tools'

    def draw(self, context):
        layout = self.layout
        layout.label(text="FOR v1 ASSETS WITH RIG ONLY! This section is for assets made for Female Base v1, and helps with conversion.")
        layout.operator(ARMATURE_OT_RecalculateBoneRoll.bl_idname, text="Recalculate Bone Roll")
