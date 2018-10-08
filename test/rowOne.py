from tkinter import *


'''ROW ONE CODE '''

def renderRowOne(window):
    def turnToInt():
        try:
            response =  int(txt_field.get())
            answer_field.configure(text= response)
        except ValueError:
            print('Wrong type of input for this feild, Please enter a number')

    # The button what when clicked
    button = Button(window, text="Click Me", command=turnToInt)
    button.grid(column=1, row=0)

    # Text field that render beore the text that will change
    txt_field = Entry(window,width=10)
    txt_field.grid(column=2, row=0)

    # This is where the computated answer will go
    answer_field = Label(window, text="0")
    answer_field.grid(column=3, row=0)

''' END ROW ONE'''
if __name__ == '__main__':
    main()
