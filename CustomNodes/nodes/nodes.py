import bpy
from bpy.props import IntProperty, FloatProperty, PointerProperty
from . properties import CustomPropertyGroup

class CUSTOMNODES_NT_ExampleNode(bpy.types.Node):
  bl_idname = "CustomNode"
  bl_label = "Example Node"

  custom_properties = PointerProperty(type=CustomPropertyGroup)

  def init(self, context):
    self.inputs.new("CustomNodeSocket", "in")
    self.outputs.new("CustomNodeSocket", "out")


class CUSTOMNODES_NT_AllSockets(bpy.types.Node):
  bl_idname = "CustomNodeTwo"
  bl_label = "All Sockets"

  custom_properties = PointerProperty(type=CustomPropertyGroup)

  def init(self, context):
    # all of the default socket types, as noted here in the "subclasses" section
    # https://docs.blender.org/api/current/bpy.types.NodeSocketStandard.html#bpy.types.NodeSocketStandard

    self.inputs.new(type="NodeSocketBool", name="NodeSocketBool")
    self.inputs.new(type="NodeSocketCollection", name="NodeSocketCollection")
    self.inputs.new(type="NodeSocketColor", name="NodeSocketColor")
    self.inputs.new(type="NodeSocketFloat", name="NodeSocketFloat")
    self.inputs.new(type="NodeSocketFloatAngle", name="NodeSocketFloatAngle")
    self.inputs.new(type="NodeSocketFloatDistance", name="NodeSocketFloatDistance")
    self.inputs.new(type="NodeSocketFloatFactor", name="NodeSocketFloatFactor")
    self.inputs.new(type="NodeSocketFloatPercentage", name="NodeSocketFloatPercentage")
    self.inputs.new(type="NodeSocketFloatTime", name="NodeSocketFloatTime")
    self.inputs.new(type="NodeSocketFloatTimeAbsolute", name="NodeSocketFloatTimeAbsolute")
    self.inputs.new(type="NodeSocketFloatUnsigned", name="NodeSocketFloatUnsigned")
    self.inputs.new(type="NodeSocketFloatGeometry", name="NodeSocketFloatGeometry")
    self.inputs.new(type="NodeSocketImage", name="NodeSocketImage")
    self.inputs.new(type="NodeSocketInt", name="NodeSocketInt")
    self.inputs.new(type="NodeSocketIntFactor", name="NodeSocketIntFactor")
    self.inputs.new(type="NodeSocketIntPercentage", name="NodeSocketIntPercentage")
    self.inputs.new(type="NodeSocketIntUnsigned", name="NodeSocketIntUnsigned")
    self.inputs.new(type="NodeSocketMaterial", name="NodeSocketMaterial")
    self.inputs.new(type="NodeSocketObject", name="NodeSocketObject")
    self.inputs.new(type="NodeSocketShader", name="NodeSocketShader")
    self.inputs.new(type="NodeSocketString", name="NodeSocketString")
    self.inputs.new(type="NodeSocketTexture", name="NodeSocketTexture")
    self.inputs.new(type="NodeSocketVector", name="NodeSocketVector")
    self.inputs.new(type="NodeSocketVectorAcceleration", name="NodeSocketVectorAcceleration")
    self.inputs.new(type="NodeSocketVectorDirection", name="NodeSocketVectorDirection")
    self.inputs.new(type="NodeSocketVectorEuler", name="NodeSocketVectorEuler")
    self.inputs.new(type="NodeSocketVectorTranslation", name="NodeSocketVectorTranslation")
    self.inputs.new(type="NodeSocketVectorVelocity", name="NodeSocketVectorVelocity")
    self.inputs.new(type="NodeSocketVectorXYZ", name="NodeSocketVectorXYZ")
    self.inputs.new(type="NodeSocketVirtual", name="NodeSocketVirtual")


nodes = [CUSTOMNODES_NT_ExampleNode, CUSTOMNODES_NT_AllSockets]
