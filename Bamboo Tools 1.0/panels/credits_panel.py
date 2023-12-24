import bpy
from ..operators.discord_operator import OpenURL

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
        
        row = text_box.row()
        row.operator(OpenURL.bl_idname, text="Pandaabear's Discord").url = "https://discord.gg/Xt6mgjK"
        
        row = text_box.row()
        row.operator(OpenURL.bl_idname, text="MapleYuudachi's Discord").url = "https://discord.gg/kGmNWCtW9D"

