import bpy

class CustomNodeSocket(bpy.types.NodeSocket):
  bl_idname = "CustomNodeSocket"
  bl_label = "Custom Node Socket"

  def draw(self, context, layout, node, x):
    layout.label(text=self.name)

  def draw_color(self, context, node):
    return (1,1,1,1)