import tkinter as tk
from tkinter import messagebox

tasks=[]
def update_task():
    list_box.delete(0,tk.END)

    for task in tasks:
         list_box.insert(tk.END,task)


def add_task():
    task= entry.get()
    if task:
         tasks.append(task)
         update_task()
         entry.delete(0,tk.END)
    else:
        messagebox.showwarning ("warning","Enter task before adding")

def delete_task():
    selected=list_box.curselection()
    if selected:
         task = list_box.get(selected)
         tasks.remove(task)
         update_task()
    else:
        messagebox.showwarning ("warning","Select the deletion task")

root= tk.Tk()
root.title("add title task")
root.geometry("400x400")

entry=tk.Entry(root,width ="20")
entry.pack(pady='10')

add_button= tk.Button(root,text="add task",width="10",command=add_task)
add_button.pack(pady='5')

add_button= tk.Button(root,text="delete task",width="10",command=delete_task)
add_button.pack(pady='5')

list_box=tk.Listbox(root,width='40',height='50')
list_box.pack(pady='10')

print("my to do app is completed")

root.mainloop()