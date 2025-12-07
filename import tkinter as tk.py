import tkinter as tk
import winsound  # لإضافة الصوت

special_tasks = []

# --- الأصوات ---
def sound_add():
    winsound.MessageBeep(winsound.MB_ICONASTERISK)

def sound_delete():
    winsound.MessageBeep(winsound.MB_ICONHAND)

# --- الدوال ---
def add_task():
    task = entry.get().strip()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
        sound_add()

def delete_task():
    try:
        selected = task_list.curselection()[0]
        task_list.delete(selected)
        sound_delete()
    except:
        pass

def clear_all():
    task_list.delete(0, tk.END)
    special_tasks.clear()
    sound_delete()

def add_special(task):
    task_list.insert(tk.END, task)
    special_tasks.append(task)
    sound_add()

def delete_special():
    global special_tasks
    remaining = []

    # نمسح المهام الخاصة فقط
    for i in range(task_list.size()):
        if task_list.get(i) not in special_tasks:
            remaining.append(task_list.get(i))

    task_list.delete(0, tk.END)

    # نرجع المهام العادية فقط
    for task in remaining:
        task_list.insert(tk.END, task)

    special_tasks.clear()
    sound_delete()

# --- واجهة البرنامج ---
root = tk.Tk()
root.title("To-Do List with Special Tasks & Sound")

entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# أزرار التحكم
tk.Button(root, text="Add", width=10, command=add_task).grid(row=1, column=0)
tk.Button(root, text="Delete", width=10, command=delete_task).grid(row=1, column=1)
tk.Button(root, text="Clear All", width=10, command=clear_all).grid(row=1, column=2)
tk.Button(root, text="Delete Special", width=12, command=delete_special).grid(row=1, column=3)

# أزرار المهام الجاهزة
tk.Button(root, text="Add Homework", width=12, command=lambda: add_special("Do Homework")).grid(row=2, column=0)
tk.Button(root, text="Add Shopping", width=12, command=lambda: add_special("Go Shopping")).grid(row=2, column=1)
tk.Button(root, text="Add Study", width=12, command=lambda: add_special("Study Python")).grid(row=2, column=2)

# قائمة عرض المهام
task_list = tk.Listbox(root, width=45, height=10, font=("Arial", 12))
task_list.grid(row=3, column=0, columnspan=4, pady=10)

root.mainloop()