import tkinter as tk
import random
import string
from tkinter import messagebox


def generate_hex_color():
    return f"#{''.join(random.choices('0123456789ABCDEF', k=6))}"


def create_color_palette(root, grid_frame):
    
    for widget in grid_frame.winfo_children():
        widget.destroy()

    
    rows, cols = 6, 6

    
    for row in range(rows):
        for col in range(cols):
            color_hex = generate_hex_color()

            
            color_frame = tk.Frame(grid_frame, bd=2, relief=tk.SOLID)
            color_frame.grid(row=row, column=col, padx=5, pady=5)

            
            color_box = tk.Label(color_frame, bg=color_hex, width=10, height=3)
            color_box.pack()

            
            hex_label = tk.Label(color_frame, text=color_hex, font=("Arial", 10), fg='black')
            hex_label.pack()

            def copy_to_clipboard(event, color_hex=color_hex):
                root.clipboard_clear()
                root.clipboard_append(color_hex)
                messagebox.showinfo("Copied", f"Color {color_hex} copied to clipboard.")

            
            hex_label.bind("<Button-1>", copy_to_clipboard)


def refresh_color_palette():
    create_color_palette(root, grid_frame)


root = tk.Tk()
root.title("Color Palette Generator")


grid_frame = tk.Frame(root)
grid_frame.pack(padx=10, pady=10)


refresh_button = tk.Button(root, text="Refresh Palette", command=refresh_color_palette, bg="#f0f0f0")
refresh_button.pack(pady=10)


def on_hover(event):
    refresh_button.config(bg="#d0d0d0")

def off_hover(event):
    refresh_button.config(bg="#f0f0f0")

refresh_button.bind("<Enter>", on_hover)
refresh_button.bind("<Leave>", off_hover)


create_color_palette(root, grid_frame)


root.mainloop()