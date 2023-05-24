import bpy 

class CustomNodeTree(bpy.types.NodeTree):
  bl_idname = "CustomNodeTree"
  bl_label = "Custom Node Tree"
  bl_description = "A Custom Node Tree"
  bl_icon = "NODETREE"