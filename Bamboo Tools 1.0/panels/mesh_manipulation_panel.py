import bpy
from ..operators.nsfw_mesh_high_attach_operator import OBJECT_OT_NsfwMeshHighAttach
from ..operators.nsfw_mesh_low_attach_operator import OBJECT_OT_NsfwMeshLowAttach
from ..operators.sfw_mesh_high_attach_operator import OBJECT_OT_SfwMeshHighAttach
from ..operators.sfw_mesh_low_attach_operator import OBJECT_OT_SfwMeshLowAttach

class OBJECT_PT_MeshManipulation(bpy.types.Panel):
    """Creates a Panel to incorporate SFW and NSFW mesh"""
    bl_label = "SFW and NSFW Mesh manipulation"
    bl_idname = "OBJECT_PT_mesh_manipulation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Bamboo Tools'
    
    def draw(self, context):
        layout = self.layout
        
        # NSFW mesh attach
        layout.operator(OBJECT_OT_NsfwMeshHighAttach.bl_idname, text="Attach High Poly NSFW mesh to base")
        layout.operator(OBJECT_OT_NsfwMeshLowAttach.bl_idname, text="Attach Low Poly NSFW mesh to base")

        # SFW mesh attach
        layout.separator()
        layout.operator(OBJECT_OT_SfwMeshHighAttach.bl_idname, text="Attach High Poly SFW mesh to base")
        layout.operator(OBJECT_OT_SfwMeshLowAttach.bl_idname, text="Attach Low Poly SFW mesh to base")