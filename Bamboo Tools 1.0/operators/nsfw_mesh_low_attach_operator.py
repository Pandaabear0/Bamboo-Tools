import bpy
import os

class OBJECT_OT_NsfwMeshLowAttach(bpy.types.Operator):
    bl_idname = "low_poly_nsfw.attach"
    bl_label = "Attach low poly nsfw mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        # Save a reference to the active object before importing
        active_obj = bpy.context.active_object

        # Check if the object has a mesh
        if active_obj and active_obj.type == 'MESH':
            mesh = active_obj.data

            # Check if the "SFW" vertex group exists
            sfw_group = active_obj.vertex_groups.get("SFW")

            if sfw_group:
                # Deselect all objects and select the current object
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = active_obj
                active_obj.select_set(True)

                # Deselect all faces first
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='DESELECT')
                bpy.ops.object.mode_set(mode='OBJECT')

                # Select faces in the "SFW" group
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.object.vertex_group_set_active(group="SFW")
                bpy.ops.object.vertex_group_select()
                bpy.ops.object.mode_set(mode='OBJECT')

                # Delete only the selected faces
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.delete(type='FACE')
                bpy.ops.object.mode_set(mode='OBJECT')
            else:
                print("Vertex group 'SFW' not found.")
                self.report({'ERROR'}, "Vertex group SFW not found.")
                return {'CANCELLED'}
        else:
            print("Active object is not a mesh.")
            self.report({'ERROR'}, "Active object is not a mesh")
            return {'CANCELLED'}
        
        # Get the directory where this script file is located
        script_file = os.path.realpath(__file__)
        script_dir = os.path.dirname(script_file)

        # Get the directory above the script directory
        parent_dir = os.path.dirname(script_dir)

        # Define the path to the FBX file 
        file_path = os.path.join(parent_dir, "low_vagina.fbx")

        # Import the FBX file
        try:
            bpy.ops.import_scene.fbx(filepath=file_path)
        except Exception as e:
            self.report({'ERROR'}, "Failed to import FBX: {}".format(str(e)))
            return {'CANCELLED'}

        # Find and delete the armature object of the imported object
        imported_object = None
        for obj in bpy.context.selected_objects:
            if obj.type == 'ARMATURE':
                imported_object = obj
                break
        
        if imported_object:
            bpy.data.objects.remove(imported_object, do_unlink=True)
        else:
            print("Armature not found in the imported object.")

        # Make the saved active object the active object again
        if active_obj:
            bpy.context.view_layer.objects.active = active_obj

        # Merge the meshes together by distance
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        
        # Check if there are selected mesh objects
        if bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
            bpy.context.selected_objects[0].select_set(True)
            bpy.ops.object.join()
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.remove_doubles(threshold=0.0001)  
            bpy.ops.object.mode_set(mode='OBJECT')
        else:
            print("No mesh objects selected for merging.")

        return {'FINISHED'}