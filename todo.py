import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, "⬛ " + task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

def mark_done():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        if task.startswith("⬛"):
            task = task.replace("⬛", "✅", 1)
            listbox.delete(index)
            listbox.insert(index, task)
    except:
        messagebox.showwarning("Warning", "Please select a task.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task.")

root = tk.Tk()
root.title("To-Do List")
root.geometry("350x400")
root.resizable(False, False)
root.config(bg="#f0f8ff")
# Entry field
entry = tk.Entry(root, width=25, font=("Arial", 12))
entry.pack(pady=10)

# Frame for buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=5)

add_btn = tk.Button(button_frame, text="Add Task", width=15, command=add_task)
add_btn.grid(row=0, column=0, padx=5, pady=2)

done_btn = tk.Button(button_frame, text="Mark as Done", width=15, command=mark_done)
done_btn.grid(row=0, column=1, padx=5, pady=2)

delete_btn = tk.Button(button_frame, text="Delete Task", width=15, command=delete_task)
delete_btn.grid(row=1, column=0, padx=5, pady=2)

exit_btn = tk.Button(button_frame, text="Exit", width=15, command=root.quit)
exit_btn.grid(row=1, column=1, padx=5, pady=2)


listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=20)

root.mainloop()
