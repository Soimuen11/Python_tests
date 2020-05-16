from tkinter import *

# creating a window
window = Tk()

# creating a label
label_area = Label(window, text="Python Login Manager")

# printing said label into newly created window
label_area.pack()

login_area = StringVar()
textline = Entry(window, textvariable=login_area, width=50)
textline.pack()

password_area = StringVar()
textline = Entry(window, textvariable=password_area, width=50)
textline.pack()

exit_button = Button(window, text="Exit", command=window.quit)
exit_button.pack()

#starting window loop which end when the window gets closed
window.mainloop()
