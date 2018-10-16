# and .x for .X usually singnifies the x axis aka width
import tkinter as tk

# import pandas as pd
# comments = pd.read_csv('user_comments.csv')
class Todo(tk.Tk):
    def __init__(self, tasks=None):     # for the init, must be set to non to avoid issues
        super().__init__()

        if not tasks:           # If there are no tasks
            self.tasks = []     # set it to an empty array ready to fll
        else:
            self.tasks = tasks

        self.title("To-Do App v1")  # Gives the title to the window app

        self.geometry("300x400")    # Sets the window height and width

        '''Default task if there are none, just to make sure'''
        # Makes a label with the text that adds items
        todo1 = tk.Label(self, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)

        self.tasks.append(todo1)  # append this task o the tasks list

        '''Loading tasks into the task lost'''
        for task in self.tasks:  # With all of the tasks contained in self.tasks
            task.pack(side=tk.TOP, fill=tk.X)   # renders the element and packs it to the TOP
                                                # the fill functiontells it how much space to fill horizonatally

        '''Text input section'''
        self.task_create = tk.Text(self, height=2, bg="white", fg="black")    # creates a text imut box
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)        # Packs the input box on the bottom
        self.task_create.focus_set()                    # Places the cursor in the this box as the applictions default position
        self.bind("<Return>", self.add_task)    # Binds hitting the return button to execute the add_task class method
        '''END Text input section'''

        '''Color scheme section'''
        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": " white"}]
        # Defines color schemes for this application

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip() # This gets the input text from the text box we created as task_create the 1.0 starts at the beginning
        if len(task_text) > 0:      # If there is text in the task_text field prevents just spaces or returns as input

            new_task = tk.Label(self, text=task_text, pady=10)      # Create a new label with the text from the input box
            _, task_style_choice = divmod(len(self.tasks), 2)   # Odd and even numbers will have diffrent color schemes
            my_scheme_choice = self.colour_schemes[task_style_choice]   # Sets the dictionary to one of the color schemese
            new_task.configure(bg=my_scheme_choice["bg"])       # Configures the bg from the chosen dictionary
            new_task.configure(fg=my_scheme_choice["fg"])       # Configures text clor from the chosen dictionary
            new_task.pack(side=tk.TOP, fill=tk.X)           # Packs the task to the top and makes it fillthe entire width
            self.tasks.append(new_task)             # Appends the task to the task list
        self.task_create.delete(1.0, tk.END)        # Deletes the text in the box
if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
