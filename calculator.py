import tkinter as tk
#-----------by Ahmed ------------------------
# ---------------- Functions ----------------
def press(key):
    display.insert(tk.END, key)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        clear()
        display.insert(0, result)
    except:
        clear()
        display.insert(0, "Error")

# ---------------- Window ----------------
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# ---------------- Display ----------------
display = tk.Entry(
    root,
    font=("Segoe UI", 24),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)
display.pack(fill="x", padx=15, pady=20, ipady=10)

# ---------------- Buttons ----------------
buttons = [
    ("7", "#3a3a3a"), ("8", "#3a3a3a"), ("9", "#3a3a3a"), ("/", "#ff9500"),
    ("4", "#3a3a3a"), ("5", "#3a3a3a"), ("6", "#3a3a3a"), ("*", "#ff9500"),
    ("1", "#3a3a3a"), ("2", "#3a3a3a"), ("3", "#3a3a3a"), ("-", "#ff9500"),
    ("0", "#3a3a3a"), (".", "#3a3a3a"), ("=", "#00c853"), ("+", "#ff9500"),
]

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(padx=10, pady=10)

row = col = 0
for text, color in buttons:
    if text == "=":
        btn = tk.Button(
            frame, text=text, bg=color, fg="white",
            font=("Segoe UI", 18), bd=0,
            command=calculate
        )
    else:
        btn = tk.Button(
            frame, text=text, bg=color, fg="white",
            font=("Segoe UI", 18), bd=0,
            command=lambda t=text: press(t)
        )

    btn.grid(row=row, column=col, padx=6, pady=6, ipadx=15, ipady=15)

    col += 1
    if col == 4:
        col = 0
        row += 1

# ---------------- Clear Button ----------------
clear_btn = tk.Button(
    root, text="CLEAR", bg="#d32f2f", fg="white",
    font=("Segoe UI", 16), bd=0,
    command=clear
)
clear_btn.pack(fill="x", padx=15, pady=15, ipady=8)

root.mainloop()
