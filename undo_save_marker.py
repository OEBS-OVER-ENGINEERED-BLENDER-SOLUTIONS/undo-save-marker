# undo_save_marker.py
bl_info = {
    "name": "Undo Save Marker",
    "author": "Eric Mwangi",
    "version": (1, 0, 0),
    "blender": (5, 0, 0),
    "location": "Automatic - marks saves in Edit > Undo History",
    "description": "Injects save markers into the native undo history",
    "category": "System",
}

import bpy
from bpy.app.handlers import persistent

# Track last 3 save step names
save_markers = []


@persistent
def save_pre_handler(dummy):
    """Push a marker into undo history right before saving."""
    global save_markers
    
    # NEW: Prevent stacking markers if saved multiple times in a row
    # If the file hasn't changed since the last save (is_dirty is False), 
    # we don't need another marker.
    if not bpy.data.is_dirty:
        return
    
    # Create marker name
    marker_name = ">>> FILE SAVED <<<"
    
    # Push custom undo step - this appears in native undo history!
    # We wrap in try/except because undo_push might fail in some contexts (like rendering or background mode)
    try:
        bpy.ops.ed.undo_push(message=marker_name)
        print(f"Save marker added to undo history")
    except Exception as e:
        print(f"Could not push undo marker: {e}")
    
    # Track it
    save_markers.append(marker_name)
    
    # Keep only last 3
    if len(save_markers) > 3:
        save_markers.pop(0)


def register():
    if save_pre_handler not in bpy.app.handlers.save_pre:
        bpy.app.handlers.save_pre.append(save_pre_handler)


def unregister():
    if save_pre_handler in bpy.app.handlers.save_pre:
        bpy.app.handlers.save_pre.remove(save_pre_handler)


if __name__ == "__main__":
    register()
