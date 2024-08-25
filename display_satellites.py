import tkinter as tk
from tkinter import messagebox

def on_satellite_click(satname):
    # For now, clicking does nothing, but we can show a message box
    # to demonstrate that the click event works
    messagebox.showinfo("Satellite Clicked", f"You clicked on {satname}")


def create_satellite_gui(satellites):
    # Create the main window
    root = tk.Tk()
    root.title("Satellite List")

    # Create a frame for the list
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    # Add a label
    label = tk.Label(frame, text="Satellite List", font=("Arial", 16))
    label.pack(pady=10)

    # Create a frame to hold the Listbox and Scrollbar
    listbox_frame = tk.Frame(frame)
    listbox_frame.pack()

    # Create a Listbox with a Scrollbar
    listbox = tk.Listbox(listbox_frame, width=50, height=15, font=("Arial", 12))
    scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=listbox.yview)

    # Configure the Listbox to use the scrollbar
    listbox.config(yscrollcommand=scrollbar.set)

    # Pack the Listbox and Scrollbar
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Populate the Listbox with satellite names
    for satellite in satellites:
        listbox.insert(tk.END, satellite['satname'])

    # Bind the Listbox click event
    listbox.bind("<Double-1>", lambda event: on_satellite_click(listbox.get(listbox.curselection())))

    # Start the Tkinter event loop
    root.mainloop()