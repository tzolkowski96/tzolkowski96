"""
Automatic File Sorter with GUI

This program automatically sorts files in a specified folder by file type. It uses the os library to access files and folders and the shutil library to move files.

Usage:
1. Run the script.
2. A GUI window will appear.
3. Click the "Load Files" button to open a directory selection dialog.
4. Select the folder you want to sort.
5. Choose whether to create new folders for each file type or relocate files to an existing folder.
6. Select files to move using checkboxes.
7. Choose how to handle duplicate files.
8. The script will sort the files and display a success message.
9. The log display will show the operations performed by the script.

Dependencies:
- tkinter: Standard GUI toolkit in Python.
- pathlib: Provides an object-oriented interface to the filesystem paths.
- shutil: High-level file operations.
- logging: Provides a flexible framework for emitting log messages from Python programs.

Ensure you have the necessary permissions to create folders and move files in the selected directory.
"""

import os
import shutil
import logging
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_folders(base_path, folder_names):
    """Create folders if they do not exist."""
    for folder_name in folder_names:
        folder_path = base_path / folder_name
        if not folder_path.exists():
            try:
                folder_path.mkdir(parents=True)
                logging.info(f"Created folder: {folder_path}")
            except Exception as e:
                logging.error(f"Failed to create folder {folder_path}: {e}")

def move_files(base_path, file_type_map, selected_files, relocate=False, relocate_path=None, duplicate_handling="skip"):
    """Move files to their respective folders."""
    for file in base_path.iterdir():
        if file.is_file() and file.name in selected_files:
            moved = False
            for folder_name, extensions in file_type_map.items():
                if file.suffix in extensions:
                    destination = relocate_path / folder_name / file.name if relocate else base_path / folder_name / file.name
                    try:
                        if destination.exists():
                            if duplicate_handling == "skip":
                                logging.info(f"Skipped duplicate file: {file.name}")
                                moved = True
                                break
                            elif duplicate_handling == "overwrite":
                                shutil.move(str(file), str(destination))
                                logging.info(f"Overwritten duplicate file: {file.name}")
                                moved = True
                                break
                            elif duplicate_handling == "rename":
                                new_destination = get_new_filename(destination)
                                shutil.move(str(file), str(new_destination))
                                logging.info(f"Renamed and moved duplicate file: {file.name} to {new_destination.name}")
                                moved = True
                                break
                        else:
                            shutil.move(str(file), str(destination))
                            logging.info(f"Moved file {file.name} to {folder_name}")
                            moved = True
                            break
                    except Exception as e:
                        logging.error(f"Failed to move file {file.name} to {destination}: {e}")
            if not moved:
                logging.warning(f"No matching folder for file: {file.name}")

def get_new_filename(destination):
    """Generate a new filename if a file already exists."""
    counter = 1
    new_destination = destination
    while new_destination.exists():
        new_destination = destination.with_name(f"{destination.stem}_{counter}{destination.suffix}")
        counter += 1
    return new_destination

def start_sorting():
    """Start the sorting process by moving files."""
    global base_path, relocate_path

    if not base_path:
        messagebox.showerror("Error", "No directory loaded. Please load a directory first.")
        return

    if not base_path.exists() or not base_path.is_dir():
        messagebox.showerror("Error", f"Invalid directory path: {base_path}")
        return

    if relocate_var.get() and (not relocate_path or not relocate_path.exists() or not relocate_path.is_dir()):
        messagebox.showerror("Error", f"Invalid relocation directory path: {relocate_path}")
        return

    # Create folders
    file_type_map = {}
    for file in base_path.iterdir():
        if file.is_file() and not file.name.startswith('.'):
            ext = file.suffix.lower()
            if ext not in file_type_map:
                folder_name = ext[1:].upper() + "_Files"
                file_type_map[folder_name] = [ext]

    create_folders(relocate_path if relocate_var.get() else base_path, file_type_map.keys())

    # Get selected files
    selected_files = [file for file, var in file_vars.items() if var.get()]

    # Get duplicate handling option
    duplicate_handling = duplicate_handling_var.get()

    # Move files
    move_files(base_path, file_type_map, selected_files, relocate_var.get(), relocate_path, duplicate_handling)

    messagebox.showinfo("Success", "Files have been sorted successfully!")
    update_log_display()

def update_log_display():
    """Update the log display with the latest log entries."""
    try:
        with open('log.txt', 'r') as log_file:
            log_display.delete(1.0, tk.END)
            log_display.insert(tk.END, log_file.read())
    except Exception as e:
        logging.error(f"Failed to update log display: {e}")

def setup_logging_to_file():
    """Set up logging to write to a file."""
    handler = logging.FileHandler('log.txt', 'w', 'utf-8')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(handler)

def load_files():
    """Load files from the selected directory and display checkboxes."""
    global base_path, relocate_path

    path = filedialog.askdirectory()
    if not path:
        return

    base_path = Path(path)

    if not base_path.exists() or not base_path.is_dir():
        messagebox.showerror("Error", f"Invalid directory path: {base_path}")
        return

    for widget in files_frame.winfo_children():
        widget.destroy()

    global file_vars
    file_vars = {}
    for file in base_path.iterdir():
        if file.is_file() and not file.name.startswith('.'):
            var = tk.BooleanVar(value=True)
            chk = ttk.Checkbutton(files_frame, text=file.name, variable=var)
            chk.pack(anchor='w')
            file_vars[file.name] = var

def select_relocation_folder():
    """Select a folder to relocate files."""
    global relocate_path

    relocate_path = filedialog.askdirectory(title="Select Folder to Relocate Files")
    if not relocate_path:
        relocate_var.set(False)
        relocation_status_label.config(text="Relocation: Disabled")
        return
    relocate_path = Path(relocate_path)
    if not relocate_path.exists() or not relocate_path.is_dir():
        messagebox.showerror("Error", f"Invalid directory path: {relocate_path}")
        relocate_var.set(False)
        relocation_status_label.config(text="Relocation: Disabled")
        return
    relocate_var.set(True)
    relocation_status_label.config(text=f"Relocation: Enabled ({relocate_path})")

def cancel_relocation():
    """Cancel the relocation process and reset relocation settings."""
    global relocate_path
    relocate_path = None
    relocate_var.set(False)
    relocation_status_label.config(text="Relocation: Disabled")

# GUI Setup
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Automatic File Sorter")
        self.geometry("700x600")
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface."""
        frame = tk.Frame(self, padx=10, pady=10)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        load_button = ttk.Button(frame, text="Load Files", command=load_files)
        load_button.pack(pady=10)

        global files_frame
        files_frame = tk.Frame(frame)
        files_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        global relocate_var, duplicate_handling_var, relocation_status_label

        relocate_var = tk.BooleanVar()
        relocate_button = ttk.Button(frame, text="Relocate Files to Another Folder", command=select_relocation_folder)
        relocate_button.pack(pady=5)

        cancel_relocation_button = ttk.Button(frame, text="Cancel Relocation", command=cancel_relocation)
        cancel_relocation_button.pack(pady=5)

        relocation_status_label = ttk.Label(frame, text="Relocation: Disabled")
        relocation_status_label.pack(pady=5)

        duplicate_handling_label = ttk.Label(frame, text="How to Handle Duplicate Files:")
        duplicate_handling_label.pack(pady=5)
        duplicate_handling_var = tk.StringVar(value="skip")
        duplicate_handling_options = ["skip", "overwrite", "rename"]
        duplicate_handling_menu = ttk.OptionMenu(frame, duplicate_handling_var, "skip", *duplicate_handling_options)
        duplicate_handling_menu.pack(pady=5)

        select_button = ttk.Button(frame, text="Sort Files", command=start_sorting)
        select_button.pack(pady=10)

        global log_display
        log_display = scrolledtext.ScrolledText(frame, width=80, height=20, state='normal')
        log_display.pack(pady=10, fill=tk.BOTH, expand=True)

        setup_logging_to_file()
        update_log_display()

    def applicationSupportsSecureRestorableState_(self):
        """Enable secure coding for restorable state on macOS."""
        return True

if __name__ == "__main__":
    base_path = None
    relocate_path = None
    app = App()
    app.mainloop()
