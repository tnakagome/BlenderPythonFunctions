import bpy
import math

def text3D(string):
    """
    Create a 3D text object with given string.
    """
    font = bpy.data.fonts.load(filepath="/System/Library/AssetsV2/com_apple_MobileAsset_Font6/7912a7db209e28f561e770eb85a0ea9cb39f89ef.asset/AssetData/Hiragino_Sans_CNS.ttc")
    textCurve = bpy.data.curves.new(type="FONT",name="textCurve")
    text = bpy.data.objects.new("text1",textCurve)
    text.data.body = string
    text.data.font = font
    text.data.size = 1.6
    bpy.context.scene.collection.objects.link(text)
    text.data.extrude = 0.1 # thickness
    # rotation and position
    text.rotation_euler[0] = math.radians(90)
    text.location = (0.4, -0.1, 0.5)
    return text

text = text3D('あいうえお')

# convert to mesh for editing
text.select_set(True)
bpy.context.view_layer.objects.active = text
bpy.ops.object.convert(target='MESH')
