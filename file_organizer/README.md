# File Organizer

This script automatically sorts files in a specified folder by file type using a graphical user interface (GUI).

## Features

- **Dynamic File Handling**: Automatically detects and handles various file types by creating folders based on file extensions.
- **Folder Creation or Relocation**: Prompts the user to either create new folders for each file type or relocate files to an existing folder using a button.
- **Visual File Selection**: Displays a list of files with checkboxes, allowing users to select which files to move.
- **Handle Duplicate Files**: Allows users to choose how to handle duplicate files (skip, overwrite, or rename) using a dropdown menu.
- **User-Friendly Interface**: Provides a GUI for easy interaction and file sorting.
- **Logging**: Logs all operations performed by the script for easy tracking and debugging.
- **Secure Coding**: Enables secure coding for restorable state on macOS.
- **Conditional Popup**: The popup for selecting a relocation folder only appears when the user explicitly requests file relocation.
- **Cancel Relocation Button**: Allows users to cancel the relocation process if they change their mind.
- **Relocation Status Label**: Indicates whether the relocation option is currently enabled or disabled, and shows the selected relocation path if enabled.

## Usage

1. **Run the script**:
    ```bash
    python file_organizer_gui.py
    ```

2. **Open the GUI**:
    - Click the "Load Files" button to open a directory selection dialog and load files.
    - Select the files you want to move using the checkboxes.
    - Click the "Relocate Files to Another Folder" button to select a folder for relocation.
    - Click the "Cancel Relocation" button if you change your mind about relocating files.
    - Choose how to handle duplicate files (skip, overwrite, or rename) using a dropdown menu.
    - Click the "Sort Files" button to sort the files.
    - The script will sort the files and display a success message.
    - The log display will show the operations performed by the script.

## Dependencies

- `tkinter`: Standard GUI toolkit in Python.
- `pathlib`: Provides an object-oriented interface to the filesystem paths.
- `shutil`: High-level file operations.
- `logging`: Provides a flexible framework for emitting log messages from Python programs.

Ensure you have the necessary permissions to create folders and move files in the selected directory.
