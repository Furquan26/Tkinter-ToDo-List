import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x450")
        
        # Task counter
        self.task_count = 0
        self.task_counter = tk.Label(root, text="Tasks: 0", fg="gray")
        self.task_counter.pack(anchor="ne", padx=10)
        
        # Task entry frame
        frame_input = tk.Frame(root)
        frame_input.pack(pady=10)
        
        self.entry_task = tk.Entry(frame_input, width=30, font=('Arial', 12))
        self.entry_task.pack(side=tk.LEFT, padx=5)
        self.entry_task.bind("<Return>", lambda event: self.add_task())  # Enter key binding
        
        button_add = tk.Button(frame_input, text="Add", command=self.add_task, bg="#4CAF50", fg="white")
        button_add.pack(side=tk.LEFT)
        
        # Task list frame
        frame_tasks = tk.Frame(root)
        frame_tasks.pack(pady=5)
        
        self.listbox_tasks = tk.Listbox(
            frame_tasks, 
            width=40, 
            height=12, 
            font=('Arial', 11), 
            selectbackground="#a6a6a6"
        )
        self.listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)
        
        scrollbar = tk.Scrollbar(frame_tasks)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox_tasks.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox_tasks.yview)
        
        # Button frame
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)
        
        button_delete = tk.Button(
            frame_buttons, 
            text="Delete Selected", 
            command=self.delete_task,
            bg="#f44336",
            fg="white"
        )
        button_delete.pack(side=tk.LEFT, padx=5)
        
        button_clear = tk.Button(
            frame_buttons,
            text="Clear All",
            command=self.clear_all,
            bg="#FF9800",
            fg="white"
        )
        button_clear.pack(side=tk.LEFT)
    
    def add_task(self):
        task = self.entry_task.get().strip()
        
        if task:
            # Check for duplicates
            if task.lower() in [self.listbox_tasks.get(i).lower() for i in range(self.listbox_tasks.size())]:
                messagebox.showwarning("Warning", "This task already exists!")
            else:
                self.listbox_tasks.insert(tk.END, task)
                self.task_count += 1
                self.task_counter.config(text=f"Tasks: {self.task_count}")
                self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def delete_task(self):
        try:
            selected_index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.delete(selected_index)
            self.task_count -= 1
            self.task_counter.config(text=f"Tasks: {self.task_count}")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")
    
    def clear_all(self):
        if self.listbox_tasks.size() > 0:
            if messagebox.askyesno("Confirm", "Clear all tasks?"):
                self.listbox_tasks.delete(0, tk.END)
                self.task_count = 0
                self.task_counter.config(text=f"Tasks: {self.task_count}")
        else:
            messagebox.showinfo("Info", "No tasks to clear!")

# Create and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
    