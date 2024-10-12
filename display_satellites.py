import tkinter as tk
from tkinter import messagebox

from Satellite_API_Call import get_satellites_info
from velocity_calculator import velocity


def on_satellite_click(satellite,observer_lat,observer_lng,observer_alt):
    # Extract satname and satid
    satname = satellite['satname']
    satid = satellite['satid']
    #Positions of satellite:
    positions = get_satellites_info(satid, observer_lat, observer_lng, observer_alt, 2, 'WAZM2J-MJM3EL-MDVLM4-5BQS')
    # Show a message box with the satellite name and id
    # Extracting and storing values into variables
    lat1 = positions[0]['satlatitude']
    lon1 = positions[0]['satlongitude']
    alt1 = positions[0]['sataltitude']

    lat2 = positions[1]['satlatitude']
    lon2 = positions[1]['satlongitude']
    alt2 = positions[1]['sataltitude']

    #Velocity:

    Velocity = velocity(lat1,lon1,alt1,lat2,lon2,alt2) * 3.6

    Velocity = Velocity.real

    # Format the velocity to three decimal places
    formatted_velocity = f"{Velocity:.3f}"

    # Show the message box
    messagebox.showinfo("Satellite Clicked", f"You clicked on {satname}, Velocity: {formatted_velocity} km/h, Latitude: {lat2} °, "
                                             f"Longitude: {lon2} °, Altitude: {alt2} km")


def create_satellite_gui(satellites,lat,lng,alt):
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

    # Store the satellites in a list (for later retrieval)
    satellite_data = []

    # Populate the Listbox with satellite names and store the satellite dictionaries
    for satellite in satellites:
        listbox.insert(tk.END, satellite['satname'])
        satellite_data.append(satellite)

    # Define the click event handler
    def on_listbox_click(event):
        # Get the selected index from the Listbox
        selected_index = listbox.curselection()[0]

        # Retrieve the satellite data from the corresponding index
        selected_satellite = satellite_data[selected_index]

        # Call the click handler with the satellite data
        on_satellite_click(selected_satellite,lat,lng,alt)

    # Bind the Listbox click event
    listbox.bind("<Double-1>", on_listbox_click)

    # Start the Tkinter event loop
    root.mainloop()