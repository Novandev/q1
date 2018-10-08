import os
from tkinter import filedialog
from tkinter import *
import pandas as pd
'''Options for the csv files'''
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)
'''END Options for the csv files'''


'''ROW TWO CODE'''

def renderRowTwo(window):
    '''This will be used to read in CSV files'''
    csv_file=  filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select CSV file",filetypes = (("csv files","*.csv"),("all files","*.*")))

    # Using pandas to display a datafram
    dataframe = pd.read_csv(csv_file)
    Label(window, text='Python')
    print(dataframe)



if __name__ == '__main__':
    renderRowTwo()
