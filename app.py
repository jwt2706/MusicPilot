import tkinter as tk

def say_hello():
    print("Hello, World!")

# Create the main window
root = tk.Tk()
root.title("Hello Tkinter")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack(pady=10)

# Run the application
root.mainloop()