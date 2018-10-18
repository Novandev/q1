import tkinter as tk
import tkinter.messagebox as msg
from tkinter import filedialog

class Todo(tk.Tk):
    def __init__(self, tasks=None):     # Tasks must be set to none to avoid eror issues
        super().__init__()

        if not tasks:       # If there are no tasks, delcare an empty list to hold the tasks
            self.tasks = []
        else:
            self.tasks = tasks      # Set self.tasks to be tasks

        self.tasks_canvas = tk.Canvas(self)     # Using frame to wold the widget for it's ability to scroll and to hold other widgets


        '''DO NOT PACK THE TASK FRAME YET WILL BE PACKED LATER'''
        self.tasks_frame = tk.Frame(self.tasks_canvas)      # Put the task frame into the
        self.text_frame = tk.Frame(self)            # Appended to the main window so it will be outsid eof the scroll bar

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)            #   This is telling tk that we want a vertical side scroller for just the task canvas

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("Row to Json")     # Sets the title

        self.geometry("500x750")        # Sets initial dimensions upons opening


        # Define task_create as a Text object/widget and pind it to text_frame giving it a height of 3 with a backgorund of white and a text color of white
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        # Packs the task_canvas to the op and tells it to fill the entire screen untill it finds another widget
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Packs the scroll bar into the right side of the screen
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)


        #  We use the canvas to create a new window with task fram that we created it. It ill be packed starting from 0,0 and anchored it to the north to cover the entire screen

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        # Packs the task create to the bottom and has it fill the whole x of the screen for text input
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)

        # Packs the text frrame to the bottom.
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()        # Focus set puts the curser in the input

        # Packs the Top level element into the top
        todo1 = tk.Label(self.tasks_frame, text="--- Get your data below ---", bg="lightgrey", fg="black", pady=10)

        # Button one is the normal click button in most systems think mouseclicks in js
        # This binds the cllick to delete the information
        todo1.bind("<Button-1>", self.remove_task)

        self.tasks.append(todo1)        # Appends the task number one to the list to be rendered

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)        # by presseing the  return button the task is added to the list
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()    # Gets the text from the task and

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task)

            new_task.bind("<Button-1>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
    todo = Todo()
    # This next section is to fix the scrolling errors that seem to appear even though nothing seems to be wrong with the code itself. Seems to be a recurring issue
    while True:
        try:
            todo.mainloop()
            break
        except UnicodeDecodeError:
            pass
