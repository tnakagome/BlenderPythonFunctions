import bpy

def chamferObject(obj1):
    """
    Round sharp edges of the given object with bevel operator.
    Adjust bevel() parameters as well as "sharpness" to get desired result.
    """
    bpy.context.view_layer.objects.active = obj1
    bpy.ops.object.mode_set(mode='EDIT') 
    bpy.ops.mesh.select_mode(type="EDGE")
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.edges_select_sharp(sharpness=1.2)
    bpy.ops.mesh.bevel(offset=1.138, offset_pct=0, segments=20, profile=0.5, release_confirm=True)
    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action='DESELECT')
