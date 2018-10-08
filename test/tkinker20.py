from tkinter import *
from rowTwo import renderRowTwo
def main():
    main_window = Tk()
    main_window.title("First application") # Specify the title of the main window

    main_window.geometry('1000x1000')      # Sets the window size
    # my photo section
    my_photo = PhotoImage(file="giphy.gif")
    # create a label with a photo
    window_pic = Label(main_window, image=my_photo, bg="black")     # binds image to the main window and sets the image using photo image
    window_pic.grid(row=0,column=0, sticky=E)       #this is to make the element show on the page
    #
    text_label = Label(main_window, text="Enter the word you would like a definition for:",bg="black", fg="white", font="none 12 bold")

    text_label.grid(row=1,column=0,sticky=W)        #gives the element a grid area
    main_window.mainloop()
if __name__ == '__main__':
    main()
