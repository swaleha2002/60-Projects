# Develop a simple command-line or GUI-based to-do list application where users can add, remove, and view tasks.
# Include features like task categorization and due dates.


import tkinter as tk
from tkinter import simpledialog, messagebox

def task_manager():
    tasks = []  # Empty list for tasks

    def add_task():
        task_name = simpledialog.askstring("Input", "Enter task:")
        if task_name:
            tasks.append(task_name)
            update_task_list()

    def update_task():
        selected_task = listbox.get(tk.ACTIVE)
        if selected_task:
            new_task = simpledialog.askstring("Input", f"Update task '{selected_task}' to:")
            if new_task:
                index = tasks.index(selected_task)
                tasks[index] = new_task
                update_task_list()

    def delete_task():
        selected_task = listbox.get(tk.ACTIVE)
        if selected_task:
            tasks.remove(selected_task)
            update_task_list()

    def update_task_list():
        listbox.delete(0,tk.END)
        for task in tasks:
            listbox.insert(tk.END, task)

    def exit_app():
        root.destroy()

    # Create the main window for adding tasks
    root = tk.Tk()
    root.title("Task Management App")

    # Listbox to display tasks
    listbox = tk.Listbox(root, width=50, height=15)
    listbox.pack(pady=20)

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Buttons for operations
    add_button = tk.Button(button_frame, text="Add Task", command=add_task)
    add_button.grid(row=0, column=0, padx=10)

    update_button = tk.Button(button_frame, text="Update Task", command=update_task)
    update_button.grid(row=0, column=1, padx=10)

    delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
    delete_button.grid(row=0, column=2, padx=10)

    exit_button = tk.Button(button_frame, text="Exit", command=exit_app)
    exit_button.grid(row=0, column=3, padx=10)

    # ToRun the main loop
    root.mainloop()

task_manager()
