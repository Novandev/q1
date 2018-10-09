from tkinter import *
from rowTwo import renderRowTwo
from rowOne import renderRowOne


'''Main Window'''
main_window = Tk()
main_window.title("First application") # Specify the title of the main window

main_window.geometry('1000x1000')      # Sets the window size



'''ROW ONE'''
renderRowOne(main_window)
''' END ROW ONE'''

'''ROW TWO'''
renderRowTwo(main_window)
'''END ROW TWO'''


'''RENDER MAIN LOOP PROGRAM'''
main_window.mainloop()
