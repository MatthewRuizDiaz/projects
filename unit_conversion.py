import tkinter as tk

def km_to_miles():
    km = float(entry_km.get())
    miles = km * 0.621371
    label_result.config(text=f"{km} km = {miles:.2f} miles")

def meters_to_feet():
    meters = float(entry_meters.get())
    feet = meters * 3.28084
    label_result.config(text=f"{meters} meters = {feet:.2f} feet")

# Create the main window
root = tk.Tk()
root.title("Unit Conversion")

# Kilometers to Miles Conversion
frame_km = tk.Frame(root)
frame_km.pack(padx=20, pady=10)
label_km = tk.Label(frame_km, text="Kilometers:")
label_km.pack(side=tk.LEFT)
entry_km = tk.Entry(frame_km)
entry_km.pack(side=tk.LEFT)
button_km = tk.Button(frame_km, text="Convert", command=km_to_miles)
button_km.pack(side=tk.LEFT)

# Meters to Feet Conversion
frame_meters = tk.Frame(root)
frame_meters.pack(padx=20, pady=10)
label_meters = tk.Label(frame_meters, text="Meters:")
label_meters.pack(side=tk.LEFT)
entry_meters = tk.Entry(frame_meters)
entry_meters.pack(side=tk.LEFT)
button_meters = tk.Button(frame_meters, text="Convert", command=meters_to_feet)
button_meters.pack(side=tk.LEFT)

# Result Label
label_result = tk.Label(root, text="", padx=20, pady=10)
label_result.pack()

# Run the GUI event loop
root.mainloop()
