import tkinter as tk
from tkinter import messagebox

# Function to handle the submission of data
def submit():
    city = city_entry.get()
    country = country_entry.get()
    angle = angle_entry.get()

    # Basic validation for angle
    try:
        angle = float(angle)
        if not (0 <= angle <= 90):
            raise ValueError("Angle must be between 0 and 90 degrees.")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid angle input: {e}")
        return

    # Display the entered information
    messagebox.showinfo("Submitted Information", f"City: {city}\nCountry: {country}\nAngle: {angle}°")

    # Show a success message
    messagebox.showinfo("Success", "Data Saved!")

    # Close the application
    root.destroy()

# Set up the main application window
root = tk.Tk()
root.title("City and Country Info")

# Create and place the widgets
tk.Label(root, text="City Name:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
city_entry = tk.Entry(root, width=30)
city_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Country Name:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
country_entry = tk.Entry(root, width=30)
country_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Angle (0-90°):").grid(row=2, column=0, padx=10, pady=10, sticky='e')
angle_entry = tk.Entry(root, width=30)
angle_entry.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, columnspan=2, pady=20)

# Run the application
root.mainloop()