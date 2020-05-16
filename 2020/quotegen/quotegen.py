from functions import *
from tkinter import *
from tkinter import ttk

window = Tk()

# creating a label
label_area = Label(window, text="Game of Thrones Quotes Generator")
# printing said label into newly created window
label_area.pack()

options = Listbox(window)
options.pack()
options.insert(END, "One Random Quote")
options.insert(END, "All quotes")


text_area = StringVar()
textline = Entry(window, textvariable=text_area, width=50)
textline.pack()

exit_button = Button(window, text="Exit", command=window.quit)
exit_button.pack()

#starting window loop which end when the window gets closed
window.mainloop()

# options = [
#     {1: "random quotes"},
#     {2: "all quotes"}
# ]

# print(options)
# user_choice = input("Hello user ! Pick an option please: ")

try :
    val = int(user_choice)
    if val == 1:
        print("random quote")
        rand_quote()
    elif val == 2:
        print("all quotes")
        all_quotes()
except ValueError:
    print("Please enter a number, not a string")
    user_choice = input("Hello user ! Pick an option please: ")

# ideas :
    # create a game : - you have to game who says which quote (lvl 1)
    #                 - you have to guess which season of game of thrones (lvl 2)
    # show one random quote whenever terminal boots
    # create a file to store scores
    # add background img to the window object
