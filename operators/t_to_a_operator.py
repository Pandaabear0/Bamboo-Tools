import bpy
import math

class POSE_OT_TtoA(bpy.types.Operator):
    """Rotate from T to A pose"""
    bl_idname = "pose.rotate_ttoa"
    bl_label = "Rotate T to A"

    def execute(self, context):
        if context.active_object.type != 'ARMATURE':
            self.report({'ERROR'}, "Please select an armature.")
            return {'CANCELLED'}

        bone_rotations = {
            "Left shoulder": 10.7,
            "Right shoulder": -10.7,
            "Left arm": 29.54,
            "Right arm": -29.54,
        }

        bpy.ops.object.mode_set(mode='POSE')

        for bone_name, rotation_deg in bone_rotations.items():
            bone = context.active_object.pose.bones.get(bone_name)
            if bone:
                if bone.rotation_mode not in {'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'}:
                    bone.rotation_mode = 'XYZ'
                bone.rotation_euler[2] += math.radians(rotation_deg)
            else:
                self.report({'ERROR'}, f"Bone '{bone_name}' not found.")

        context.view_layer.update()
        
        # Save the original object
        original_obj = context.active_object

        # 1: Create a temporary copy of the original object
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.duplicate(linked=False)
        temp_obj = context.active_object  # This is now the temporary copy
        
        # 2: Apply the base shape key
        if temp_obj.data.shape_keys:
            temp_obj.shape_key_add(name='Basis', from_mix=False)

        # 3: Apply the armature modifier
        for modifier in temp_obj.modifiers:
            if modifier.type == 'ARMATURE':
                bpy.ops.object.modifier_apply(modifier=modifier.name)

        # 4: Transfer all the shape keys
        if original_obj.data.shape_keys:
            for key_block in original_obj.data.shape_keys.key_blocks:
                temp_obj.shape_key_add(name=key_block.name, from_mix=False)
                temp_obj.data.shape_keys.key_blocks[key_block.name].value = key_block.value
