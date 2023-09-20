
import tkinter as tk

def convert_to_fahrenheit():
    try:
        # Try to get number from the entry box
        celsius = float(entry_box.get())
        # Calculate the fahrenheit number
        fahrenheit = (9 / 5) * celsius + 32
        # Changing text of label to display the result
        label_result.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        # If there's any problem with value to throw exception that something is wrong
        label_result.config(text="Invalid input")

# Creating a window for the program
window = tk.Tk()
# Adding title for left corner
window.title("Celsius to Fahrenheit Converter")
# Resolution of this window 300x150
window.geometry("300x150")

# Creating a label for this window to explain what to do
label_celsius = tk.Label(window, text="Enter Celsius temperature:")

# Pack is used like <div> in HTML to organize and display widgets in a container
# Pady=5 (padding Y) specifies the amount of vertical padding (empty space) to be added around the widget.
label_celsius.pack(pady=5)

# Creating a entrybox to enter the valie
entry_box = tk.Entry(window)
# Adding some space between them
entry_box.pack(pady=5)

# Convert button
button = tk.Button(window, text="Convert", command=convert_to_fahrenheit)
button.pack(pady=10)

# Label to display a result of this the function convert_to_fahrenheit()
label_result = tk.Label(window, text="", font=("Helvetica", 18))
label_result.pack(pady=10)

# Start the main event loop
window.mainloop()
