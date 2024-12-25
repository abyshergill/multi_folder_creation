import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os


class FolderCreationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple Folder Creation Solution v 0.0")
        self.root.geometry("442x540")
        self.root.resizable(False, False)
        self.root.config(bg="#1b2631")


        
        self.root.iconbitmap(r"icon\icon.ico")

        # Flag to track whether the text window is open
        #self.is_window_open = False
        #self.multiline_user_text = None  # Initialize as None to track the widget
        #text="Styled Text", font=("Arial", 16, "bold italic")
        # Folder name label and entry
        self.folder_name = tk.Label(self.root,
                                    text="Multi Folder Creation",
                                    font=("Helvetica", 12, "bold italic"),
                                    width=46, 
                                    fg="white",
                                    bg="#1b2631"
                                    )
        self.folder_name.grid(row=0, column=0, 
                            padx=0, pady=10,
                            sticky="w")

        self.folder_name_text = tk.Text(self.root,
                                         font=("Helvetica", 12),
                                         width=46,
                                         height=10, 
                                         relief="solid",
                                         fg="black")
        self.folder_name_text.grid(row=1, column=0,
                                   padx=10, pady=10,
                                   sticky="w")

        # Insert default text into the Text widget
        self.folder_name_text.insert("1.0", "Enter your folder name here")

        # Bind the event to remove default text when user starts typing
        self.folder_name_text.bind("<FocusIn>", self.remove_default_text)
        
        # Browse button to choose output folder
        self.output_browse = tk.Button(self.root,
                                        text="Output Location",
                                        font=("Helvetica", 14, "bold"),
                                        width=34,  
                                        fg="white",
                                        bg="#5dade2",
                                        command=self.choose_folder)
        
        self.output_browse.grid(row=2, column=0,
                                padx=10, pady=10,
                                sticky="w")

        # Entry to display the selected folder path
        self.browse_path = tk.Entry(self.root,
                                    font=("Helvetica", 12),
                                    width=46,
                                    relief="solid", 
                                    fg="black")
        # Insert default text into the Entry widget
        self.browse_path.insert(0, "No output path have selected")

        # Bind the event to remove default text when user starts typing
        self.browse_path.bind("<FocusIn>", self.remove_browse_path)
        
        self.browse_path.grid(row=3, column=0,
                              padx=10, pady=10,
                              sticky="w")
        
        # Submit button
        self.submit_button = tk.Button(self.root,
                                        text="Submit",
                                        font=("Helvetica", 12, "bold"),
                                        width=41,
                                        fg="#f7f9f9",
                                        bg="#5dade2",
                                        command=self.submit)
        self.submit_button.grid(row=4, column=0,
                                padx=10, pady=10,
                                sticky="w")
                       
        # Folder name label and entry
        self.folder_name = tk.Label(self.root,
                                    text="Source Code at github.com/abyshergill",
                                    font=("Helvetica", 12),
                                    width=46, 
                                    fg="white",
                                    bg="#1b2631"
                                    )
        self.folder_name.grid(row=5, column=0, 
                            padx=0, pady=10,
                            sticky="w")
        

    def submit(self):
        self.folder_input = self.folder_name_text.get("1.0", tk.END).strip()
        if self.folder_input:  
            # Call folder_creation with the multiline input and the selected path
            self.folder_creation(self.folder_input, self.browse_path.get())
            self.folder_name_text.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Warning", "No folder name has been provided")


    def folder_creation(self, user_input, file_path):
        # Make sure the file_path is a string, not a widget
        if isinstance(file_path, str):

            # Split user input into lines (folder names)
            lines = user_input.splitlines()

            for line in lines:
                # Use os.path.join to combine the file_path and folder name
                full_path = os.path.join(file_path, line.strip())  # Strip to remove any extra whitespace

                if not os.path.exists(full_path):
                    os.makedirs(full_path)  # Create the directory
                else:
                    messagebox.showwarning("Warning",f"Directory '{line}' already exists at {full_path}")
            self.browse_path.delete(0, tk.END)
            self.browse_path.insert(0, "No output path have selected")
        else:
            messagebox.showwarning("Warning", "Error: file_path is not a valid string!")
        messagebox.showwarning("Information",f"All the folder has been created Successfully")

    def choose_folder(self):
        # Open folder dialog to select path
        folder_selected = filedialog.askdirectory(title="Select Output Folder")
        if folder_selected:
            # Update the browse_path Entry widget with the selected path
            self.browse_path.delete(0, tk.END)
            self.browse_path.insert(0, folder_selected)
        else:
            self.browse_path.delete(0, tk.END)
            self.browse_path.insert(0, "No folder selected")
    
    def remove_default_text(self, event):
        # Check if the text is still the default one
        if self.folder_name_text.get("1.0", "end-1c") == "Enter your folder name here":
            self.folder_name_text.delete("1.0", "end")
    
    def remove_browse_path(self, event):
        # Check if the text is still the default one
        if self.browse_path.get() == "No Output Folder Have been selected":
            self.browse_path.delete("0", "end")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FolderCreationApp(root)
    root.mainloop()
