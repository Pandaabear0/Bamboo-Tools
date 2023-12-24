import bpy

from .small_preset_operator import OBJECT_OT_SetSmallPresetButton
from .thicker_preset_operator import OBJECT_OT_SetThickerPresetButton
from .reset_shape_keys_operator import OBJECT_OT_ResetAllShapeKeys
from .t_to_a_operator import POSE_OT_TtoA
from .a_to_t_operator import POSE_OT_AtoT
from .recalculate_bone_roll_operator import ARMATURE_OT_RecalculateBoneRoll
from .nsfw_mesh_high_attach_operator import OBJECT_OT_NsfwMeshHighAttach
from .nsfw_mesh_low_attach_operator import OBJECT_OT_NsfwMeshLowAttach
from .sfw_mesh_high_attach_operator import OBJECT_OT_SfwMeshHighAttach
from .sfw_mesh_low_attach_operator import OBJECT_OT_SfwMeshLowAttach
from .discord_operator import OpenURL

def register():
    bpy.utils.register_class(OBJECT_OT_SetSmallPresetButton)
    bpy.utils.register_class(OBJECT_OT_SetThickerPresetButton)
    bpy.utils.register_class(OBJECT_OT_ResetAllShapeKeys)
    bpy.utils.register_class(POSE_OT_TtoA)
    bpy.utils.register_class(POSE_OT_AtoT)
    bpy.utils.register_class(ARMATURE_OT_RecalculateBoneRoll)
    bpy.utils.register_class(OBJECT_OT_NsfwMeshHighAttach)
    bpy.utils.register_class(OBJECT_OT_NsfwMeshLowAttach)
    bpy.utils.register_class(OBJECT_OT_SfwMeshHighAttach)
    bpy.utils.register_class(OBJECT_OT_SfwMeshLowAttach)
    bpy.utils.register_class(OpenURL)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_SetSmallPresetButton)
    bpy.utils.unregister_class(OBJECT_OT_SetThickerPresetButton)
    bpy.utils.unregister_class(OBJECT_OT_ResetAllShapeKeys)
    bpy.utils.unregister_class(POSE_OT_TtoA)
    bpy.utils.unregister_class(POSE_OT_AtoT)
    bpy.utils.unregister_class(ARMATURE_OT_RecalculateBoneRoll)
    bpy.utils.unregister_class(OBJECT_OT_NsfwMeshHighAttach)
    bpy.utils.unregister_class(OBJECT_OT_NsfwMeshLowAttach)
    bpy.utils.unregister_class(OBJECT_OT_SfwMeshHighAttach)
    bpy.utils.unregister_class(OBJECT_OT_SfwMeshLowAttach)
    bpy.utils.unregister_class(OpenURL)