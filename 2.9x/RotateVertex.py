import math

def rotateVertex(x, y, degrees):
    """
    Rotate a vertex on X-Y plane.
    This is not Blender specific.
    """
    if (degrees == 0):
        return (x, y)
    rad = math.radians(degrees)
    newX = x * math.cos(rad) - y * math.sin(rad)
    newY = x * math.sin(rad) + y * math.cos(rad)
    return (newX, newY)
