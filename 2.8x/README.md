# Code snippets for Blender 2.8x

### Create a collection to group objects together
Collection can be useful when deleting a number of objects at once.
```Python
import bpy

myCollection = bpy.data.collections.new("My Collection")
bpy.context.scene.collection.children.link(myCollection)
...
myCollection.objects.link(obj1)
myCollection.objects.link(obj2)
```

### Copy object
Can be made a function.
```Python
obj2 = obj1.copy()
obj2.data = obj1.data.copy()
obj2.name = "New Object"
myCollection.objects.link(obj2)
```

### Move object
```Python
obj.location[0] += 10 # move to the right along X axis
obj.location[1] += 10 # push along Y axis
obj.location[2] += 10 # move up along Z axis
```

### Rotate object
```Python
obj.rotation_euler[0] = math.radians(12) # rotate around X axis
obj.rotation_euler[1] = math.radians(30) # rotate around Y axis
obj.rotation_euler[2] = math.radians(45) # rotate around Z axis
```
