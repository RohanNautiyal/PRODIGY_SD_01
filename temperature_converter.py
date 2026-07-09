import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("500x450")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="🌡 Temperature Converter",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# Temperature input
tk.Label(root, text="Enter Temperature:", font=("Arial", 12)).pack()

temp_entry = tk.Entry(root, font=("Arial", 14), width=20)
temp_entry.pack(pady=10)

# Unit selection
tk.Label(root, text="Select Unit:", font=("Arial", 12)).pack()

unit_var = tk.StringVar()

unit_dropdown = ttk.Combobox(
    root,
    textvariable=unit_var,
    values=["Celsius", "Fahrenheit", "Kelvin"],
    state="readonly",
    width=18,
    font=("Arial", 12)
)

unit_dropdown.current(0)
unit_dropdown.pack(pady=10)

# Convert button
convert_btn = tk.Button(
    root,
    text="Convert",
    font=("Arial", 12, "bold"),
    width=15
)
convert_btn.pack(pady=20)

# Result Label
result_label = tk.Label(
    root,
    text="Converted values will appear here.",
    font=("Arial", 12),
    justify="left"
)
result_label.pack(pady=20)

root.mainloop()