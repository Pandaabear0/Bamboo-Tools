import bpy

class OBJECT_OT_SetSmallPresetButton(bpy.types.Operator):
    """Set Shape Keys for Small Preset"""
    bl_idname = "object.set_small_preset_button"
    bl_label = "Small Preset"

# Check if object is mesh and create dictionary with shapekey values
    def execute(self, context):
        obj = context.active_object
        if obj and obj.type == 'MESH' and obj.data.shape_keys:
            key_blocks = obj.data.shape_keys.key_blocks
            presets = {
                "Alternative Booba 1": 1.0,
                "Belly (Flatten)": 0.164,
                "Back Thigh Reduction": 0.304,
                "Leg (Thin)": 0.573,
                "Hip( Smaller)": 0.702
            }
            # Check if dictionary key matches with mesh and apply given value
            for key, value in presets.items():
                if key in key_blocks:
                    key_blocks[key].value = value
                else:
                    self.report({'ERROR'}, f"Shape key not found: {key} Have you edited any shapekeys?")
                    return {'CANCELLED'}
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Ensure you select a mesh before choosing a preset.")
            return {'CANCELLED'}

