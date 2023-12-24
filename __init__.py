bl_info = {
    "name": "Bamboo Tools",
    "blender": (3, 5, 0),
    "category": "Object",
}

if "bpy" in locals():
    import importlib
    importlib.reload(operators)
    importlib.reload(panels)
else:
    from . import operators, panels

def register():
    operators.register()
    panels.register()

def unregister():
    operators.unregister()
    panels.unregister()

if __name__ == "__main__":
    register()
