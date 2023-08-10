import tkinter as tk #to make gui

def km_to_miles():
    km = float(entry_km.get())#convert input to float for calculations
    miles = km * 0.621371 #store result of conversion
    label_result.config(text=f"{km} km = {miles:.2f} miles") #show results

def meters_to_feet():
    meters = float(entry_meters.get()) #convert input to float for calculations
    feet = meters * 3.28084 #store result of conversion
    label_result.config(text=f"{meters} meters = {feet:.2f} feet") #show results

def cm_to_inches():
    cm = float(entry_cm.get())#convert input to float for calculations
    inches = cm * 0.393701 #store result of conversion
    label_result.config(text=f"{cm} cm = {inches:.2f} inches") #show results

root = tk.Tk() # Create the main window
root.title("Unit Conversion")

# Kilometers to Miles Conversion
frame_km = tk.Frame(root) #create the frame for this line of the gui
frame_km.pack(padx=20, pady=10)
label_km = tk.Label(frame_km, text="Kilometers:")#create label
label_km.pack(side=tk.LEFT)
entry_km = tk.Entry(frame_km) #input box
entry_km.pack(side=tk.LEFT)
button_km = tk.Button(frame_km, text="Convert", command=km_to_miles)# convert button
button_km.pack(side=tk.LEFT)

# Meters to Feet Conversion
frame_meters = tk.Frame(root) #create frame
frame_meters.pack(padx=20, pady=10)
label_meters = tk.Label(frame_meters, text="Meters:")#label 
label_meters.pack(side=tk.LEFT)
entry_meters = tk.Entry(frame_meters)#input box
entry_meters.pack(side=tk.LEFT)
button_meters = tk.Button(frame_meters, text="Convert", command=meters_to_feet)#convert button
button_meters.pack(side=tk.LEFT)

# Centimeters to Inches Conversion
frame_cm = tk.Frame(root) #frame
frame_cm.pack(padx=20, pady=10)
label_cm = tk.Label(frame_cm, text="Centimeters:")
label_cm.pack(side=tk.LEFT)#label
entry_cm = tk.Entry(frame_cm)
entry_cm.pack(side=tk.LEFT)#input
button_cm = tk.Button(frame_cm, text="Convert", command=cm_to_inches)
button_cm.pack(side=tk.LEFT)#convert button

# Result Label
label_result = tk.Label(root, text="", padx=20, pady=10)
label_result.pack()

# Run the GUI event loop
root.mainloop()
