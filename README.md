# Undo Save Marker

**Undo Save Marker** is a simple Blender addon that injects a visual marker into the native Undo History whenever you save your file.

<img width="1494" height="996" alt="image" src="https://github.com/user-attachments/assets/906ee8ce-4c11-4cea-af93-38369dbadb8d" />


## Features

- **Visual Save points**: Adds a `>>> FILE SAVED <<<` entry to your Undo History every time you save.
- **Save Stacking Prevention**: Smartly prevents multiple markers if you spam `Ctrl+S` without making changes.
- **Native Integration**: Uses Blender's native undo system, so it works with the standard Undo History panel.

## Installation

1. Download `undo_save_marker.py` from the [Releases page](../../releases).
2. In Blender, go to **Edit > Preferences > Add-ons**.
3. Click **Install...** and select the file.
4. Enable the checkbox for **System: Undo Save Marker**.

## Usage

1. Work on your project normally.
2. Press `Ctrl+S` to save.
3. Open **Edit > Undo History**.
4. You will see `>>> FILE SAVED <<<` marking exactly where in your history the save occurred.

## Compatibility

- Blender 5.0+
- Blender 4.5+ (should work, untested)

## License

MIT
