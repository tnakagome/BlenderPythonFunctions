import bpy

def deleteObject(obj1):
    """
    Delete one object.
    """
    bpy.ops.object.select_all(action='DESELECT')
    obj1.select_set(True)
    bpy.ops.object.delete()
