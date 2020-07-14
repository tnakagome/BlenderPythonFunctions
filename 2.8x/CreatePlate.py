import bpy, bmesh
import mathutils

def createPlate(width, thickness):
    """
    Create a plate. For normals (surfaces) to be directed outward,
    the vertices must be ordered counter-clockwise in the vector,
    and the surface must be pulled up as in this code.
    If you want to pull down the surface, the vertices must be ordered clockwise.
    Normal direction is significant when you export the data as STL.
    If surfaces are flipped, they may appear translucent from outside.
    Such a model cannot be output by 3D printers.
    In case you need to fix flipped faces/normals, call:
        bm.normal_update()
    """
    points = []
    points.append([0,     0,      0])
    points.append([width, 0,      0])
    points.append([width, width,  0])
    points.append([0,     width,  0])
    bm = bmesh.new()
    for v in points:
        bm.verts.new(v)
    bottom = bm.faces.new(bm.verts)        
    top = bmesh.ops.extrude_face_region(bm, geom=[bottom])
    bmesh.ops.translate(bm, vec=mathutils.Vector((0, 0, thickness)),
                        verts=[v for v in top["geom"] if isinstance(v, bmesh.types.BMVert)])
    # In case you need to fix flipped faces/normals, call:
    # bm.normal_update()
    frameMesh = bpy.data.meshes.new("PlateMesh")
    bm.to_mesh(frameMesh)
    bm.free()
    plate = bpy.data.objects.new("Plate", frameMesh)
    bpy.context.collection.objects.link(plate)
    return plate
