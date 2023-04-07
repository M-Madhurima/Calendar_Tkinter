# import all methods and classes from the tkinter  
from tkinter import *
 
# import calendar module
import calendar

# Function for showing the calendar of the given year
def showCal() :
 
    # Create a GUI window
    new_gui = Tk()
     
    # Set the background colour of GUI window
    new_gui.config(background = "white")
 
    # set the name of tkinter GUI window
    new_gui.title("CALENDAR")
 
    # Set the configuration of GUI window
    new_gui.geometry("550x600")
 
    # get method returns current text as string
    fetch_year = int(year_field.get())
 
    # calendar method of calendar module return
    # the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)
 
    # Create a label for showing the content of the calendar
    cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal_year.grid(row = 5, column = 1, padx = 20)
     
    # start the GUI
    new_gui.mainloop()
 
     
