import tkinter as tk
from player.ui import MusicPlayerUI

def main():
    # Create the main window
    root = tk.Tk()

    # Initialize the MusicPlayerUI
    app = MusicPlayerUI(root)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()