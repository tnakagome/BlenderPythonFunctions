import bpy

def subtractObject(obj1, obj2):
    """
    Remove part of obj1 that overlaps with obj2 by "subtract" boolean operation.
    """
    bool1 = obj1.modifiers.new(type="BOOLEAN", name="subtract")
    bool1.object = obj2
    bool1.operation = "DIFFERENCE"
    obj1.select_set(True)
    bpy.context.view_layer.objects.active = obj1
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=bool1.name)
    # Delete obj2 as it is unnecessary.
    bpy.ops.object.select_all(action='DESELECT')
    obj2.select_set(True)
    bpy.ops.object.delete()

# Example with CreatePlate.py
# p1 will become a frame after subtraction.
p1 = createPlate(50, 5)
p2 = createPlate(40, 10)
p2.location[0] += 5
p2.location[1] += 5
p2.location[2] -= 2.5
subtractObject(p1, p2)
