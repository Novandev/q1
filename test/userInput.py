from tkinter import *
from rowTwo import renderRowTwo



main_window = Tk()
main_window.title("First application") # Specify the title of the main window

main_window.geometry('1000x1000')      # Sets the window size



'''ROW ONE'''
def turnToInt():
    try:
        res =  int(txt.get())
        return_field.configure(text= res)
    except ValueError:
        print('Wrong type of input for this feild, Please enter a number')


# Button to Click
btn = Button(main_window, text="Click Me", command=turnToInt)
btn.grid(column=2, row=0)
#
txt = Entry(main_window,width=10)
txt.grid(column=0, row=0)

return_field = Label(main_window, text="0")
return_field.grid(column=3, row=0)
''' END ROW ONE'''

'''ROW TWO'''
renderRowTwo(main_window)
'''END ROW TWO'''
'''RENDER MAIN LOOP PROGRAM'''
main_window.mainloop()
