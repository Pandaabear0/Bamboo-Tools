bl_info = {
    "name": "Bamboo Tools",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import math
import mathutils

# Operator for the Small preset
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

# Operator for the Thicker preset
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
        
# Operator to sett all shapekeys to 0
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
        
#Operator for T to A pose
class POSE_OT_TtoA(bpy.types.Operator):
    """Rotate from T to A pose"""
    bl_idname = "pose.rotate_ttoa"
    bl_label = "Rotate T to A"

# Check if the active object is an armature
    def execute(self, context):
        if context.active_object.type != 'ARMATURE':
            self.report({'ERROR'}, "Please select an armature.")
            return {'CANCELLED'}
        
        # Create a dictionary with selected bones and their respective values
        bone_rotations = {
            "Left shoulder": 10.7,
            "Right shoulder": -10.7,
            "Left arm": 29.54,
            "Right arm": -29.54,
        }

        # Ensure pose mode is set
        bpy.ops.object.mode_set(mode='POSE')

      # Go through dictionary and check if key matches with armature's bones
        for bone_name, rotation_deg in bone_rotations.items():
            bone = context.active_object.pose.bones.get(bone_name)
            if bone:
                # Ensure Euler rotations
                if bone.rotation_mode not in {'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'}:
                    bone.rotation_mode = 'XYZ'  
                    
                # Apply the rotation around the Y-axis in radians
                bone.rotation_euler[2] += math.radians(rotation_deg)
            else:
                self.report({'ERROR'}, f"Bone '{bone_name}' not found.")
                
        #Update scene and return to object mode
        context.view_layer.update()
        bpy.ops.object.mode_set(mode= 'OBJECT')

        return {'FINISHED'}
    
# Operator for A to T pose    
class POSE_OT_AtoT(bpy.types.Operator):
    """Rotate from A to T pose"""
    bl_idname = "pose.rotate_atot"
    bl_label = "Rotate A to T"

# Check if the active object is an armature
    def execute(self, context):
        if context.active_object.type != 'ARMATURE':
            self.report({'ERROR'}, "Please select an armature.")
            return {'CANCELLED'}
        
        # Create a dictionary with selected bones and their respective values
        bone_rotations = {
            "Left shoulder": -10.7,
            "Right shoulder": 10.7,
            "Left arm": -29.54,
            "Right arm": 29.54,
        }

        # Ensure pose mode is set
        bpy.ops.object.mode_set(mode='POSE')

        # Go through dictrionary and check if key matches with armature's bones
        for bone_name, rotation_deg in bone_rotations.items():
            bone = context.active_object.pose.bones.get(bone_name)
            if bone:
                # Ensure Euler rotations
                if bone.rotation_mode not in {'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'}:
                    bone.rotation_mode = 'XYZ' 
                    
                # Apply the rotation around the Y-axis in radians
                bone.rotation_euler[2] += math.radians(rotation_deg)
            else:
                self.report({'ERROR'}, f"Bone '{bone_name}' not found.")
        
        #Update scene and return to object mode
        context.view_layer.update()
        bpy.ops.object.mode_set(mode= 'OBJECT')

        return {'FINISHED'}
    
#Operator to adjust boneroll of the armature to global +Y axis
class ARMATURE_OT_RecalculateBoneRoll(bpy.types.Operator):
    """Recalculate Bone Roll to Global +Y Axis"""
    bl_idname = "armature.recalculate_bone_roll"
    bl_label = "Recalculate Bone Roll"

    def execute(self, context):
        obj = context.active_object
        if obj and obj.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='EDIT')
            for bone in obj.data.edit_bones:
                # Align roll to the Global +Y axis
                bone.align_roll(mathutils.Vector([0, 1, 0]))
                
            #Return to object mode
            bpy.ops.object.mode_set(mode='OBJECT') 
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Active object is not an armature.")
            return {'CANCELLED'}
    
# Panel for operators
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
        
#Panel for V1 base assets conversion.
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

#Panel for credits :)
class BAMBOOTOOLS_PT_CreditsPanel(bpy.types.Panel):
    bl_label = "Credits"
    bl_idname = "BAMBOOTOOLS_PT_credits"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Bamboo Tools'

    def draw(self, context):
        layout = self.layout
        text_box = layout.box()
        text_box.label(text="Created by Pandaabear.")
        text_box.label(text="Written by MapleYuudachi")
        text_box.label(text="Pandaabear's discord:")
        text_box.label(text="discord.gg/Xt6mgjK")
        text_box.label(text="MapleYuudachi's discord:")
        text_box.label(text="discord.gg/kGmNWCtW9D")

    
def register():
    bpy.utils.register_class(OBJECT_OT_SetSmallPresetButton)
    bpy.utils.register_class(OBJECT_OT_SetThickerPresetButton)
    bpy.utils.register_class(POSE_OT_TtoA)
    bpy.utils.register_class(OBJECT_PT_ControlShapeKeysPanel)
    bpy.utils.register_class(POSE_OT_AtoT)
    bpy.utils.register_class(OBJECT_OT_ResetAllShapeKeys)
    bpy.utils.register_class(ARMATURE_OT_RecalculateBoneRoll)
    bpy.utils.register_class(BAMBOOTOOLS_PT_V1BoneRollPanel)
    bpy.utils.register_class(BAMBOOTOOLS_PT_CreditsPanel)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_SetSmallPresetButton)
    bpy.utils.unregister_class(OBJECT_OT_SetThickerPresetButton)
    bpy.utils.unregister_class(POSE_OT_TtoA)
    bpy.utils.unregister_class(OBJECT_PT_ControlShapeKeysPanel)
    bpy.utils.unregister_class(POSE_OT_AtoT)
    bpy.utils.unregister_class(OBJECT_OT_ResetAllShapeKeys)
    bpy.utils.unregister_class(ARMATURE_OT_RecalculateBoneRoll)
    bpy.utils.unregister_class(BAMBOOTOOLS_PT_V1BoneRollPanel)
    bpy.utils.unregister_class(BAMBOOTOOLS_PT_CreditsPanel)


if __name__ == "__main__":
    register()