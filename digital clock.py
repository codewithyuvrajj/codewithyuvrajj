import tkinter as tk
import time

def update_time():
    """Update the time display on the label."""
    current_time = time.strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
    clock_label.config(text=current_time)     # Update the label with the current time
    root.after(1000, update_time)             # Schedule the update_time function to be called every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set the dimensions of the window
root.geometry("300x100")
root.configure(bg="blue")

# Create a label widget to display the time
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
clock_label.pack(anchor='center')

# Initialize the time display
update_time()

# Start the GUI event loop
root.mainloop()
