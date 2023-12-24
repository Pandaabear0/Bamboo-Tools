import bpy
from ..operators.small_preset_operator import OBJECT_OT_SetSmallPresetButton
from ..operators.thicker_preset_operator import OBJECT_OT_SetThickerPresetButton
from ..operators.reset_shape_keys_operator import OBJECT_OT_ResetAllShapeKeys
from ..operators.t_to_a_operator import POSE_OT_TtoA
from ..operators.a_to_t_operator import POSE_OT_AtoT

class OBJECT_PT_ControlShapeKeysPanel(bpy.types.Panel):
    """Creates a Panel to control shape keys with presets"""
    bl_label = "Bamboo Tools"
    bl_idname = "OBJECT_PT_control_shape_keys_presets"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Bamboo Tools'

    def draw(self, context):
        layout = self.layout
            
        # Preset Buttons
        layout.operator(OBJECT_OT_SetSmallPresetButton.bl_idname, text='"Smol" Preset')
        layout.operator(OBJECT_OT_SetThickerPresetButton.bl_idname, text='"Thicc" Preset')
        layout.operator(OBJECT_OT_ResetAllShapeKeys.bl_idname, text="Default Preset")

        # Pose buttons
        layout.separator()
        layout.operator(POSE_OT_TtoA.bl_idname, text="Change from T to A pose")
        layout.operator(POSE_OT_AtoT.bl_idname, text="Change from A to T pose")
        