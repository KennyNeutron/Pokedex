import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
ihap = tk.IntVar()

# Create a label to display the image
label = tk.Label(root)
label.pack()

# Function to change the image when the button is pressed
def change_image():
    ihap.set(ihap.get() + 1)
    formatted_count = "{:03d}".format(ihap.get())
    print(f'count: {formatted_count}')
    img_path = f'thumbnails/{formatted_count}.png'
    print(f'image name: {img_path}')
    image = Image.open(img_path)
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # Keep a reference to the image

# Create a button to trigger the image change
button = tk.Button(root, text="Change Image", command=change_image)
button.pack()

# Start the main loop
root.mainloop()