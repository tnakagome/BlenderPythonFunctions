import bpy

def mergeObjects(obj1, obj2):
    """
    Merge the two objects together by "union" boolean operation.
    The second object is deleted after merge as it will be unnecessary.
    If the resulting object is not what you have expected,
    experiment with double_threshold for a different value or comment out the line.
    """
    bool1 = obj1.modifiers.new(type="BOOLEAN", name="merge")
    bool1.object = obj2
    bool1.operation = "UNION"
    bool1.double_threshold = 0.001
    obj1.select_set(True)
    bpy.context.view_layer.objects.active = obj1
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=bool1.name)
    # Delete obj2 as it is unnecessary.
    bpy.ops.object.select_all(action='DESELECT')
    obj2.select_set(True)
    bpy.ops.object.delete()

# Example with CreatePlate.py
p1 = createPlate(50, 5)
p2 = createPlate(40, 30)
p2.location[0] += 5
p2.location[1] += 5
p2.location[2] -= 10
mergeObjects(p1, p2)
