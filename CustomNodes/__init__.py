import bpy
from bpy.props import IntProperty, FloatProperty, PointerProperty
import nodeitems_utils
from . nodes import *

bl_info = {
    "name" : "Custom Nodes",
    "author" : "James Alt",
    "description" : "An example of custom nodes in Blender",
    "blender" : (3, 0, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Node"
}

classes = [CustomNodeTree, CustomNodeSocket, CustomPropertyGroup, CUSTOMNODES_PT_CustomPanel]
classes += nodes

def register():
  for cls in classes:
    bpy.utils.register_class(cls)
  bpy.types.Scene.custom_properties = PointerProperty(type=CustomPropertyGroup)
  nodeitems_utils.register_node_categories("CUSTOM_CATEGORIES", categories)

def unregister():
  for cls in classes:
      bpy.utils.unregister_class(cls)
  del bpy.types.Scene.custom_properties
  nodeitems_utils.unregister_node_categories("CUSTOM_CATEGORIES")