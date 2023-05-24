import bpy
from nodeitems_utils import NodeItem, NodeCategory

class CustomNodeCategory(NodeCategory):
  @classmethod
  def poll(cls, context):
    return context.space_data.tree_type == "CustomNodeTree"

categories = [
  CustomNodeCategory("CUSTOM_CATEGORY", "Category", items = [
    NodeItem("CustomNode"),
    NodeItem("CustomNodeTwo"),
  ]),
]
