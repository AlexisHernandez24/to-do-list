from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# ---- Creating the Main Window with ttkbootstrap ---
window = ttk.Window(themename="minty")
window.title("Todo List App")
window.geometry("400x450")
# -------

# List to keep track of completed (green) tasks
completedTasks = []

def addTasks():
    taskInput = entryBox.get().strip()

    if taskInput:
        tasks = taskListBox.get(0, END)
        if taskInput in tasks:
            messagebox.showerror("Error", f"Error: {taskInput} already exists!")
        else:
            taskListBox.insert(END, taskInput)
            messagebox.showinfo("Info", f"Added Task: '{taskInput}'!")

def completedTask():
    selectedTask = taskListBox.curselection()
    if selectedTask:
        index = selectedTask[0]
        taskText = taskListBox.get(index)

        # Check if the task is already marked as completed
        if index not in completedTasks:
            # Mark task as complete by changing color to green
            taskListBox.delete(index)
            taskListBox.insert(index, taskText)
            taskListBox.itemconfig(index, {'fg': 'green'})
            # Add to completed tasks list
            completedTasks.append(index)

def deleteTask():
    selectedTask = taskListBox.curselection()
    if selectedTask:
        index = selectedTask[0]
        taskListBox.delete(index)
        # Remove from completed tasks list if it was completed
        if index in completedTasks:
            completedTasks.remove(index)

def viewStats():
    # Calculate total tasks and completed tasks
    totalTasks = taskListBox.size()  # Get the total number of tasks in the Listbox
    completedTaskCount = len(completedTasks)  # Count of completed (green) tasks

    # Display both counts in a messagebox
    messagebox.showinfo("Task Stats", f"Total tasks: {totalTasks}\nCompleted tasks: {completedTaskCount}")

# ---- Creating Frames for Layout ---
topFrame = ttk.Frame(window, padding=10)
topFrame.pack(fill=BOTH)

middleFrame = ttk.Frame(window, padding=10)
middleFrame.pack(fill=BOTH, expand=True)

bottomFrame = ttk.Frame(window, padding=10)
bottomFrame.pack(fill=BOTH)

# ---- Creating Widgets with ttkbootstrap ---
entryBox = ttk.Entry(topFrame, bootstyle="info", width=40)
entryBox.pack(pady=5)

add_button = ttk.Button(topFrame, text="Add Task", command=addTasks, bootstyle="primary")
add_button.pack(pady=5)

taskListBox = Listbox(middleFrame, height=10, font=('Helvetica', 12), selectbackground="#D3E4CD")
taskListBox.pack(fill=BOTH, expand=True)

done_button = ttk.Button(bottomFrame, text="Mark as Done", command=completedTask, bootstyle="success")
done_button.pack(side=LEFT, padx=5, pady=10)

delete_button = ttk.Button(bottomFrame, text="Delete Task", command=deleteTask, bootstyle="danger")
delete_button.pack(side=RIGHT, padx=5, pady=10)

stats_button = ttk.Button(bottomFrame, text="View Stats", command=viewStats, bootstyle="info")
stats_button.pack(side=BOTTOM, pady=10)

# ------- Run the Application ----
window.mainloop()