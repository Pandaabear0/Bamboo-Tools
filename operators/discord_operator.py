import bpy
import webbrowser

class OpenURL(bpy.types.Operator):
    bl_idname = "wm.url_open"
    bl_label = "Open URL"

    url: bpy.props.StringProperty()

    def execute(self, context):
        webbrowser.open(self.url)
        return {'FINISHED'}