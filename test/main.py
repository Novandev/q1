"""
Test  application to learn tkinter from youtube video
https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
"""

from tkinter import *



def main():

    root_window = Tk()      # Basic  window that has close buttons

    the_label = Label(root_window,text="Hello world!")     # this creates a text label , needs a window to output as the first parameter

    the_label.pack()        # fits the window in wherever it can on the screen...lazy waht of doing it

    root_window.mainloop()      #keeps the window open continuously on the screen


if __name__ == '__main__':
    main()
