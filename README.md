# CopyWordToFolders
A Python GUI application that allows you to copy a Word document to multiple folders simultaneously.
# 📄 Copy Word Document to Multiple Folders

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

A **Python GUI application** that allows you to copy a Word document to multiple folders simultaneously with just a few clicks. Perfect for educators, administrators, or anyone who needs to distribute the same document to multiple directories.

---

## **Purpose**

Have you ever needed to copy the same Word document into dozens of folders? Doing it manually is time-consuming and error-prone. This tool automates the process, saving you hours of repetitive work.

---

## **Key Features**

| Feature | Description |
|---------|-------------|
| **User-Friendly GUI** | Clean, intuitive interface built with tkinter |
| **Multiple Folder Selection** | Select multiple folders at once with Ctrl+Click |
| **Word Document Support** | Works with both `.docx` and `.doc` files |
| **Batch Add Folders** | Add all subfolders from a parent directory in one click |
| **Smart Navigation** | Remembers the parent folder so you don't have to re-navigate |
| **Clean Display** | Shows only folder names, not full paths, for better readability |
| **Error Handling** | Detailed status messages and error reporting |
| **No External Dependencies** | Uses only Python's built-in modules |

---

## **Requirements**

- **Python** 3.6 or higher
- **No external packages** (uses only built-in modules)

| Module | Purpose |
|--------|---------|
| `tkinter` | GUI interface |
| `shutil` | File copying operations |
| `os` | File and directory operations |
| `filedialog` | Folder selection dialogs |

---

##  **Installation**

### **Option 1: Clone from GitHub**

```bash
  # Clone the repository
  git clone https://github.com/yourusername/CopyWordToFolders.git
  
  # Navigate to the folder
  cd CopyWordToFolders
  
  # Run the application
  python copy_doc.py
```


### **Option 2: Download ZIP**
```bash
  Go to the repository on GitHub
  
  Click "Code" → "Download ZIP"
  
  Extract the ZIP file
  
  Run python copy_doc.py
```

Option 3: Copy the script directly
```bash
  If you just want the script without the repository:
  
  Copy the copy_doc.py file
  
  Save it anywhere on your computer
  
  Run python copy_doc.py in your terminal
```
