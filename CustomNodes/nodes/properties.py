import bpy
from bpy.props import IntProperty, FloatProperty

class CustomPropertyGroup(bpy.types.PropertyGroup):
  int_value = IntProperty()
  float_value = FloatProperty()
  
  def draw(self, context, layout):
    row = layout.row()
    row.prop(self, "int_value")
    row = layout.row()
    row.prop(self, "float_value")