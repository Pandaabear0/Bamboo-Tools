import bpy
import math
import mathutils

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
    