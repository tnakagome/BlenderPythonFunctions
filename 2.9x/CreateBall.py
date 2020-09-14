import bpy, bmesh

def createBall():
    """
    Create a ball. Taken from:
    https://blender.stackexchange.com/questions/93298/create-a-uv-sphere-object-in-blender-from-python
    The parameter "diameter" for create_uvsphere() is radius actually. See:
    https://developer.blender.org/T52923
    Therefore, the "ballSize" of 50 will create a ball whose diameter is 100mm.
    u_segments and v_segments should be adjusted based on ballSize if you want a smooth ball.
    """
    ballSize = 50
    mesh = bpy.data.meshes.new('Ball')
    ball = bpy.data.objects.new("Ball", mesh)
    bpy.context.collection.objects.link(ball)
    bpy.context.view_layer.objects.active = ball
    ball.select_set(True)
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=30, v_segments=30, diameter=ballSize)
    bm.to_mesh(mesh)
    bm.free()
    ball.location[2] = ballSize
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.ops.object.shade_smooth()
    return ball
    