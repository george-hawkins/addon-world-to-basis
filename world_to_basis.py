bl_info = {
    "name": "World to basis",
    "author": "George Hawkins",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > Item",
    "description": "Calculate delta between the active and selected objects and apply it to the basis transform.",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy


class WorldToBasisPanel(bpy.types.Panel):
    # Create a panel in the Item tab of the 3D Viewport.
    bl_label = "World to Basis"
    bl_idname = "ITEM_PT_world_to_basis"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("button.copy_world_to_basis")
        
class ButtonCopyWorldToBasis(bpy.types.Operator):
    # This docstring (with a period appeneded) becomes the tooltip for the operator.
    """Calculate the delta between the active and selected objects and apply it to the basis transform"""
    bl_idname = "button.copy_world_to_basis"
    bl_label = "Copy All to Selected"

    def execute(self, context):
        a = context.active_object
        for o in context.selected_objects:
            if o != a:
                # Don't rearrange the terms here unless you know your matrix maths.
                factor = a.matrix_world @ o.matrix_world.inverted_safe()
                o.matrix_basis = factor @ o.matrix_basis
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ButtonCopyWorldToBasis)
    bpy.utils.register_class(WorldToBasisPanel)


def unregister():
    bpy.utils.unregister_class(WorldToBasisPanel)
    bpy.utils.unregister_class(ButtonCopyWorldToBasis)


if __name__ == "__main__":
    register()
