import bpy

def createPole(_x, _y, _z, _radius, _height, _segments, round=False):
    '''
    Create a pole with given parameters.
    The top of the pole can be rounded if the last parameter is True.
    '''
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.mesh.primitive_cylinder_add(vertices=_segments, radius=_radius,
                    depth=_height, enter_editmode=False,
                    align='WORLD', location=(_x, _y, _z), scale=(1, 1, 1))
    pole = bpy.context.object
    pole.name = 'Pole'
    if round:
        # Round the top
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
        pole.data.polygons[_segments-2].select=True
        bpy.ops.object.mode_set(mode='EDIT')
        # adjust the parameters if necessary
        bpy.ops.mesh.bevel(offset=15, offset_pct=0, segments=16, profile=0.5, release_confirm=True)
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
    return pole
