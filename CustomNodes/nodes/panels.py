import bpy 

class CUSTOMNODES_PT_CustomPanel(bpy.types.Panel):
  bl_idname = "CUSTOMNODES_PT_CustomPanel"
  bl_label = "Custom Panel"
  bl_space_type = 'PROPERTIES'
  bl_region_type = 'WINDOW'
  bl_context = "render"
  
  @classmethod
  def poll(cls, context):
    return True

  def draw(self, context):
    context.scene.custom_properties.draw(context, self.layout)
