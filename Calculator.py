import tkinter as tk  # Import the Tkinter library

# Create a window
root = tk.Tk()
root.title("Calculator")  # Window title
root.geometry("400x600")  # Window size
root.resizable(False, False)  # Disable resizing


# -- Entry (Calculator Display) --
entry = tk.Entry(
    root,
    width=20,
    font=("Arial", 18),
    bd=5,
    relief="ridge",
    justify="right"  # Text will be right-aligned
)
entry.pack(pady=10)  # Add to the screen with some vertical padding

# -- Button (Calculator Buttons) --
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

for (text, row, col) in buttons:
    btn = tk.Button(
        button_frame, text=text, width=5, height=2, font=("Arial", 14)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

# -- FUNCTIONS --


def button_click(char):
    current = entry.get()  # Get current text from the display
    entry.delete(0, tk.END)  # Clear the display
    entry.insert(0, current + char)  # Add new character to the existing text


def calculate():
    try:
        # Calculate the mathematical expression using eval
        result = eval(entry.get())
        entry.delete(0, tk.END)  # Clear the display
        entry.insert(0, str(result))  # Show the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")  # Show "Error" if calculation fails


for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            button_frame, text=text, width=5, height=2, font=("Arial", 14),
            # "=" button calls calculate function
            command=calculate
        )
    else:  # Other buttons
        btn = tk.Button(
            button_frame, text=text, width=5, height=2, font=("Arial", 14),
            # Calls button_click function when clicked
            command=lambda t=text: button_click(t)
        )
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", width=20, height=2, font=("Arial", 14),
                      # Clears the display when clicked
                      command=lambda: entry.delete(0, tk.END))
clear_btn.pack(pady=10)  # Add to the screen


def key_press(event):
    char = event.keysym  # Get the pressed key

    if char in "0123456789":
        button_click(char)  # Type the number
    elif char in ("plus", "minus", "asterisk", "slash", "period"):
        mapping = {"plus": "+", "minus": "-",
                   "asterisk": "*", "slash": "/", "period": "."}
        button_click(mapping[char])  # Type the operator
    elif char == "Return":
        calculate()  # Press Enter to calculate
    elif char == "BackSpace":  # Delete key
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])  # Remove last character
    elif char == "Escape":  # Clear key
        entry.delete(0, tk.END)  # Clear the display


root.bind("<Key>", key_press)  # Bind keyboard keys


# Keep the application running
root.mainloop()
