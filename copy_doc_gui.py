import shutil
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class DocumentCopier:
    def __init__(self, root):
        self.root = root
        self.root.title("Copy Word Document to Multiple Folders")
        self.root.geometry("700x550")
        
        # Variables
        self.source_file = None
        self.selected_folders = []
        self.start_directory = None
        self.folder_paths = {}  # Store {display_name: full_path}
        
        # Create GUI
        self.create_widgets()
    
    def create_widgets(self):
        # Source file section
        source_frame = tk.Frame(self.root, pady=10)
        source_frame.pack(fill=tk.X, padx=10)
        
        tk.Label(source_frame, text="Word Document:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        
        self.source_label = tk.Label(source_frame, text="No file selected", fg="gray", anchor="w")
        self.source_label.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        tk.Button(source_frame, text="Browse...", command=self.select_source_file).pack(side=tk.RIGHT)
        
        # Folder selection section
        folder_frame = tk.Frame(self.root, pady=10)
        folder_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        tk.Label(folder_frame, text="Target Folders (Ctrl+Click to select multiple):", font=("Arial", 10, "bold")).pack(anchor="w")
        
        # Listbox with scrollbar
        list_frame = tk.Frame(folder_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.folder_listbox = tk.Listbox(list_frame, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set, width=80, height=15)
        self.folder_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.folder_listbox.yview)
        
        # Button frame for folder operations
        button_frame = tk.Frame(folder_frame)
        button_frame.pack(fill=tk.X, pady=5)
        
        tk.Button(button_frame, text="Add Folders", command=self.add_folders).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Add Subfolders", command=self.add_subfolders).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear All", command=self.clear_folders).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remove Selected", command=self.remove_selected).pack(side=tk.LEFT, padx=5)
        
        # Status and action section
        action_frame = tk.Frame(self.root, pady=10)
        action_frame.pack(fill=tk.X, padx=10)
        
        self.status_label = tk.Label(action_frame, text="Ready", fg="blue", anchor="w")
        self.status_label.pack(fill=tk.X)
        
        tk.Button(action_frame, text="Copy Document to Selected Folders", command=self.copy_document, bg="green", fg="white", font=("Arial", 10, "bold"), height=2).pack(pady=5)
        
        instructions = "Instructions:\n1. Browse for your Word document\n2. Add folders to the list\n3. Select multiple folders with Ctrl+Click\n4. Click 'Copy Document'"
        tk.Label(self.root, text=instructions, justify=tk.LEFT, fg="gray", font=("Arial", 9)).pack(pady=5)
    
    def select_source_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Word Document",
            filetypes=[("Word documents", "*.docx *.doc"), ("All files", "*.*")]
        )
        if file_path:
            self.source_file = file_path
            self.source_label.config(text=os.path.basename(file_path), fg="black")
            self.status_label.config(text="Document selected", fg="green")
    
    def add_folders(self):
        while True:
            if self.start_directory:
                folder = filedialog.askdirectory(
                    title="Select a folder (Cancel to stop)", 
                    initialdir=self.start_directory
                )
            else:
                folder = filedialog.askdirectory(
                    title="Select the first folder"
                )
                if folder:
                    self.start_directory = os.path.dirname(folder)
            
            if not folder:
                break
            
            folder_name = os.path.basename(folder)
            
            if folder_name not in self.folder_paths:
                self.folder_paths[folder_name] = folder
                self.folder_listbox.insert(tk.END, folder_name)
                self.status_label.config(text=f"Added: {folder_name}", fg="blue")
            else:
                messagebox.showinfo("Info", "Folder already in list")
    
    def add_subfolders(self):
        base_folder = filedialog.askdirectory(title="Select parent folder")
        if not base_folder:
            return
        
        subfolders = [f.path for f in os.scandir(base_folder) if f.is_dir()]
        added_count = 0
        
        for subfolder in subfolders:
            folder_name = os.path.basename(subfolder)
            if folder_name not in self.folder_paths:
                self.folder_paths[folder_name] = subfolder
                self.folder_listbox.insert(tk.END, folder_name)
                added_count += 1
        
        self.status_label.config(text=f"Added {added_count} subfolders", fg="blue")
    
    def clear_folders(self):
        self.folder_listbox.delete(0, tk.END)
        self.folder_paths.clear()
        self.status_label.config(text="List cleared", fg="blue")
    
    def remove_selected(self):
        selected_indices = list(self.folder_listbox.curselection())
        selected_indices.reverse()
        
        for index in selected_indices:
            folder_name = self.folder_listbox.get(index)
            self.folder_listbox.delete(index)
            if folder_name in self.folder_paths:
                del self.folder_paths[folder_name]
        
        self.status_label.config(text=f"Removed {len(selected_indices)} folders", fg="blue")
    
    def copy_document(self):
        # Validate
        if not self.source_file:
            messagebox.showerror("Error", "Please select a Word document first!")
            return
        
        if not os.path.exists(self.source_file):
            messagebox.showerror("Error", f"Source file not found:\n{self.source_file}")
            return
        
        # Get selected folders
        selected_indices = self.folder_listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Error", "Please select at least one folder to copy to!")
            return
        
        # Get full paths from dictionary
        selected_folders = []
        for index in selected_indices:
            folder_name = self.folder_listbox.get(index)
            if folder_name in self.folder_paths:
                selected_folders.append(self.folder_paths[folder_name])
        
        # Verify folders exist
        existing_folders = []
        for folder in selected_folders:
            if os.path.exists(folder):
                existing_folders.append(folder)
            else:
                try:
                    os.makedirs(folder, exist_ok=True)
                    existing_folders.append(folder)
                except:
                    messagebox.showerror("Error", f"Cannot create folder:\n{folder}")
                    return
        
        # Copy document to each folder
        success_count = 0
        error_count = 0
        errors = []
        
        for folder in existing_folders:
            try:
                dest_path = os.path.join(folder, os.path.basename(self.source_file))
                shutil.copy2(self.source_file, dest_path)
                success_count += 1
            except Exception as e:
                error_count += 1
                errors.append(f"{folder}: {str(e)}")
        
        # Show results
        result_msg = f"✅ Copied to {success_count} folders"
        if error_count > 0:
            result_msg += f"\n Failed for {error_count} folders"
            for error in errors[:5]:
                result_msg += f"\n   - {error}"
            if len(errors) > 5:
                result_msg += f"\n   ... and {len(errors) - 5} more"
        
        self.status_label.config(text=result_msg, fg="green" if error_count == 0 else "orange")
        messagebox.showinfo("Result", result_msg)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentCopier(root)
    root.mainloop()