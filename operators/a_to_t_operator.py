import bpy
import math

class POSE_OT_AtoT(bpy.types.Operator):
    """Rotate from A to T pose and manage shape keys by duplicating and restoring"""
    bl_idname = "pose.rotate_atot"
    bl_label = "Rotate A to T and Restore Shape Keys"

    def execute(self, context):
        obj = context.active_object
        
        # Check if the active object is an armature
        if obj.type != 'ARMATURE':
            self.report({'ERROR'}, "Please select an armature.")
            return {'CANCELLED'}

        # Ensure the armature's related mesh is selected and has shape keys
        if obj.children:
            mesh_obj = obj.children[0]  # Assuming the mesh is the first child
            if mesh_obj.type == 'MESH' and mesh_obj.data.shape_keys:
                # Duplicate the mesh object for shape keys backup
                bpy.ops.object.select_all(action='DESELECT')
                mesh_obj.select_set(True)
                context.view_layer.objects.active = mesh_obj
                bpy.ops.object.duplicate(linked=False, mode='TRANSLATION')
                duplicate_mesh_obj = context.active_object
            else:
                self.report({'ERROR'}, "Related mesh object does not have shape keys.")
                return {'CANCELLED'}
        else:
            self.report({'ERROR'}, "Armature does not have a related mesh object.")
            return {'CANCELLED'}
        
        # Perform bone rotations as previously defined
        self.rotate_bones(context, obj)
        
        # Apply the armature modifier and pose
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        mesh_obj.select_set(True)  # Select both the armature and the mesh
        context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.modifier_apply(modifier="Armature")
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.armature_apply(selected=False)
        bpy.ops.object.mode_set(mode='OBJECT')

        # Restore shape keys from the duplicate to the original mesh
        self.restore_shape_keys(mesh_obj, duplicate_mesh_obj)

        # Optionally delete the duplicated mesh object
        bpy.data.objects.remove(duplicate_mesh_obj)

        return {'FINISHED'}

    def rotate_bones(self, context, armature_obj):
        bone_rotations = {
            "Left shoulder": -10.7,
            "Right shoulder": 10.7,
            "Left arm": -29.54,
            "Right arm": 29.54,
        }
        
        bpy.ops.object.mode_set(mode='POSE')
        for bone_name, rotation_deg in bone_rotations.items():
            bone = armature_obj.pose.bones.get(bone_name)
            if bone:
                if bone.rotation_mode not in {'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'}:
                    bone.rotation_mode = 'XYZ'
                bone.rotation_euler[2] += math.radians(rotation_deg)
            else:
                self.report({'ERROR'}, f"Bone '{bone_name}' not found.")
        context.view_layer.update()
        bpy.ops.object.mode_set(mode='OBJECT')

    def restore_shape_keys(self, original_mesh_obj, duplicate_mesh_obj):
        # Make sure the original mesh is active and in object mode
        bpy.ops.object.select_all(action='DESELECT')
        original_mesh_obj.select_set(True)
        bpy.context.view_layer.objects.active = original_mesh_obj
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Join as shapes to copy the shape keys from the duplicate to the original mesh
        duplicate_mesh_obj.select_set(True)  # Select the duplicate (which has the shape keys)
        bpy.ops.object.join_shapes()
        original_mesh_obj.select_set(False)  # Deselect to avoid accidental operations
