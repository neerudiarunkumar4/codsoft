import tkinter as tk
from tkinter import messagebox
import os

TODO_FILE = "todo_list.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def refresh_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(f"[ ] {task}")
        entry.delete(0, tk.END)
        refresh_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def complete_task():
    try:
        index = task_listbox.curselection()[0]
        if tasks[index].startswith("[✓]"):
            messagebox.showinfo("Info", "Task already completed.")
        else:
            tasks[index] = tasks[index].replace("[ ]", "[✓]", 1)
            refresh_listbox()
            save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task.")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        tasks.pop(index)
        refresh_listbox()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# GUI setup
root = tk.Tk()
root.title("📝 To-Do List")

tasks = load_tasks()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=0, padx=5, pady=5)

add_btn = tk.Button(frame, text="Add Task", width=12, command=add_task, bg="green", fg="white")
add_btn.grid(row=0, column=1, padx=5)

task_listbox = tk.Listbox(frame, width=50, height=10)
task_listbox.grid(row=1, column=0, columnspan=2, pady=10)

complete_btn = tk.Button(frame, text="Mark as Done", width=12, command=complete_task, bg="blue", fg="white")
complete_btn.grid(row=2, column=0, pady=5, sticky="w")

delete_btn = tk.Button(frame, text="Delete Task", width=12, command=delete_task, bg="red", fg="white")
delete_btn.grid(row=2, column=1, pady=5, sticky="e")

refresh_listbox()
root.mainloop()
