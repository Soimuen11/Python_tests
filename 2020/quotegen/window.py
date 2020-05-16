from tkinter import *

# creating a window
window = Tk()
# title = Labelframe(window, text="Game of Thrones Quotes Generator")
# title.pack(fill="both", expand="yes")

options = Listbox(window)
options.pack()
options.insert(END, "One Random Quote")
options.insert(END, "All quotes")

# creating a label
label_area = Label(window, text="Hello world!")

# printing said label into newly created window
label_area.pack()

text_area = StringVar()
textline = Entry(window, textvariable=text_area, width=50)
textline.pack()

exit_button = Button(window, text="Exit", command=window.quit)
exit_button.pack()

#starting window loop which end when the window gets closed
window.mainloop()
