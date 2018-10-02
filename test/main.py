"""
Test  application to learn tkinter from youtube video
https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
"""

from tkinter import *



def main():

    root_window = Tk()      # Main window for the application



    top_frame = Frame(root_window).pack(side=TOP)        # declaring the top button as a frame object and binding it to the root window and pacs it on the top
    bottom_frame = Frame(root_window).pack(side=BOTTOM)      # declarng the bottom froam as a frame obect to bind it the root window. and packs it on the bottom

    #BUTTON SECTION
    top_frame_button = Button(top_frame,text="Hi im a top fram button",fg="red").pack()     # T

    bottom_frame_button = Button(bottom_frame,text="Hi im a top fram button",fg="red").pack()


    root_window.mainloop()      #keeps the window open continuously on the screen the most important since it is the main loop

if __name__ == '__main__':
    main()
