def cleanupOrphanData():
    # Clear orphan meshes.
    for m in bpy.data.meshes:
        if m.users == 0:
            bpy.data.meshes.remove(m)
    # Clearing an orphan mesh may produce an orphhan material.
    for m in bpy.data.materials:
        if m.users == 0:
            bpy.data.materials.remove(m)
