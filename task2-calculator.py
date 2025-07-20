import tkinter as tk

def click(event):
    current = entry.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    
    elif text == "C":
        entry.delete(0, tk.END)

    elif text == "DEL":
        entry.delete(len(current)-1, tk.END)

    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Simple Basic Calculator")
root.geometry("320x450")
root.config(bg="#f0f0f0")
root.resizable(0, 0)


entry = tk.Entry(root, font="Arial 24", bd=8, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "DEL", "=", "+"],
    ["C"]
]


btn_colors = {
    "C": "#ff4d4d",
    "DEL": "#ff944d",
    "=": "#4dff4d",
    "+": "#80bfff",
    "-": "#80bfff",
    "*": "#80bfff",
    "/": "#80bfff"
}

for row in buttons:
    frame = tk.Frame(button_frame, bg="#f0f0f0")
    frame.pack()
    for btn_text in row:
        color = btn_colors.get(btn_text, "#e6e6e6")
        button = tk.Button(
            frame,
            text=btn_text,
            font="Arial 18",
            width=5,
            height=2,
            bg=color,
            activebackground="#d9d9d9",
            relief=tk.RAISED,
            bd=3
        )
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()
