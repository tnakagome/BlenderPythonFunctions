import bpy

def cleanupOrphanData():
    # Clearing unused objects
    for o in bpy.data.objects:
        if o.users == 0:
            bpy.data.objects.remove(o)
    # Clear orphan meshes.
    for m in bpy.data.meshes:
        if m.users == 0:
            bpy.data.meshes.remove(m)
    # Clearing an orphan mesh may produce an orphhan material.
    for m in bpy.data.materials:
        if m.users == 0:
            bpy.data.materials.remove(m)
    # Clearing unused fonts
    for f in bpy.data.fonts:
        if f.users == 0:
            bpy.data.fonts.remove(f)
    # Clearing unused curves
    for c in bpy.data.curves:
        if c.users == 0:
            bpy.data.curves.remove(c)
