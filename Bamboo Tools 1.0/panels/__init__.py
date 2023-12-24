import bpy

from .control_shape_keys_panel import OBJECT_PT_ControlShapeKeysPanel
from .mesh_manipulation_panel import OBJECT_PT_MeshManipulation
from .v1_bone_roll_panel import BAMBOOTOOLS_PT_V1BoneRollPanel
from .credits_panel import BAMBOOTOOLS_PT_CreditsPanel

def register():
    bpy.utils.register_class(OBJECT_PT_ControlShapeKeysPanel)
    bpy.utils.register_class(OBJECT_PT_MeshManipulation)
    bpy.utils.register_class(BAMBOOTOOLS_PT_V1BoneRollPanel)
    bpy.utils.register_class(BAMBOOTOOLS_PT_CreditsPanel)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_ControlShapeKeysPanel)
    bpy.utils.unregister_class(OBJECT_PT_MeshManipulation)
    bpy.utils.unregister_class(BAMBOOTOOLS_PT_V1BoneRollPanel)
    bpy.utils.unregister_class(BAMBOOTOOLS_PT_CreditsPanel)


