import tkinter as tk
class Root(tk.Tk):
    '''This class males a label and will also render the rest of the widgets'''
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text="Hello World", padx=5, pady=5)
        self.label.pack()
        print('this works')
if __name__ == "__main__":
    root = Root()
    root.mainloop()
