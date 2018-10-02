from tkinter import *


main_window = Tk()
main_window.title("First application") # Specify the title of the main window


# my photo section
my_photo = PhotoImage(file="giphy.gif")
# create a label with a photo
Label(main_window, image=my_photo, bg="black") .grid(row=0,column=0, sticky=E)

#
Label(main_window, text="Enter the word you would like a definition for:",bg="black", fg="white", font="none 12 bold") .grid(row=1,column=0,sticky=W)

main_window.mainloop()
