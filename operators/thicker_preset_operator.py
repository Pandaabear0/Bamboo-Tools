import bpy

class OBJECT_OT_SetThickerPresetButton(bpy.types.Operator):
    """Set Shape Keys for Thicker Preset"""
    bl_idname = "object.set_thicker_preset_button"
    bl_label = "Thicker Preset"
       
# Check if object is mesh and create dictionary with shapekey values
    def execute(self, context):
        obj = context.active_object
        if obj and obj.type == 'MESH' and obj.data.shape_keys:
            key_blocks = obj.data.shape_keys.key_blocks
            presets = {
                "Back Thigh Reduction": 0.409,
                "Bigger Butt": 0.643,
                "Belly (Out)": 0.386
            }
            #Check if dictrionary key matches with mesh and apply given values
            for key, value in presets.items():
                if key in key_blocks:
                    key_blocks[key].value = value
                else:
                    self.report({'ERROR'}, f"Shape key not found,: {key} Have you edited any shapekeys?")
                    return {'CANCELLED'}
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Ensure you select a mesh before choosing a preset.")
            return {'CANCELLED'}
   