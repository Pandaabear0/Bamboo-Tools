import bpy

class OBJECT_OT_ResetAllShapeKeys(bpy.types.Operator):
    """Set all shapekeys to 0"""
    bl_idname = "object.reset_all_shape_keys"
    bl_label = "Reset All Shape Keys"
    
#Go through all shapekeys in object and set value to 0
    def execute(self, context):
        obj = context.active_object
        if obj and obj.type == 'MESH' and obj.data.shape_keys:
            key_blocks = obj.data.shape_keys.key_blocks
            for key_block in key_blocks:
                key_block.value = 0.0
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Ensure you select a mesh before choosing a preset.")
            return {'CANCELLED'}
        