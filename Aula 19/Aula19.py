import tkinter as tk
from tkinter import PhotoImage


# Create the main window
parent = tk.Tk()



f  = tk.Frame(parent, bg='yellow')
f.pack()


# Load the image 
image = PhotoImage(file="img.png")


# Create a label to display the image
image_label = tk.Label(f, image=image, width=250)
image_label.pack()
# img = image_label.size((150,150));
# Start the Tkinter event loop
parent.mainloop()