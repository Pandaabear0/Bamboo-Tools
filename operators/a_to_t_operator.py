import bpy
import math

class POSE_OT_AtoT(bpy.types.Operator):
    """Rotate from A to T pose"""
    bl_idname = "pose.rotate_atot"
    bl_label = "Rotate A to T"

#Check if the active object is an armature
    def execute(self, context):
        if context.active_object.type != 'ARMATURE':
            self.report({'ERROR'}, "Please select an armature.")
            return {'CANCELLED'}

#Create a dictionary with selected bones and their respective values
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

#Apply the rotation around the Y-axis in radians
                bone.rotation_euler[2] += math.radians(rotation_deg)
            else:
                self.report({'ERROR'}, f"Bone '{bone_name}' not found.")

        #Update scene and return to object mode
        context.view_layer.update()
        bpy.ops.object.mode_set(mode= 'OBJECT')

        return {'FINISHED'}
