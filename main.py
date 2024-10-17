import tkinter as tk
from math import pow

def clear():
    display_var.set("")

def append_to_display(value):
    current = display_var.get()
    display_var.set(current + value)

def calculate():
    try:
        expression = display_var.get()
        result = eval(expression)
        display_var.set(str(result))
    except:
        display_var.set("Error")

def future_value():
    try:
        pv = float(entry_pv.get())
        rate = float(entry_rate.get()) / 100
        periods = int(entry_n.get())
        fv = pv * pow(1 + rate, periods)
        display_var.set(f"FV: {fv:.2f}")
    except:
        display_var.set("Error")

def present_value():
    try:
        fv = float(entry_fv.get())
        rate = float(entry_rate.get()) / 100
        periods = int(entry_n.get())
        pv = fv / pow(1 + rate, periods)
        display_var.set(f"PV: {pv:.2f}")
    except:
        display_var.set("Error")
        
def key_event(event):
    key = event.keysym
  
    if key.isdigit() or key in ['plus', 'minus', 'slash', 'asterisk', 'period']:

        append_to_display(event.char)
        return 'break' 
    elif key == 'Return': 
        calculate()
    elif key == 'BackSpace': 
        display_var.set(display_var.get()[:-1])
    elif key == 'Escape': 
        clear()

root = tk.Tk()
root.title("HP 12C - Python")

root.resizable(False, False)

button_color_bg = '#f4d03f' 
button_color_fg = '#4a4a4a'  
button_color_special = '#d4d4d4'  
display_bg = '#1e1e1e'  
display_fg = '#f2f2f2'  

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), bd=10, insertwidth=2, width=20, borderwidth=4, bg=display_bg, fg=display_fg, justify='right')
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def create_button(text, row, col, width=5, height=2, color_bg=button_color_bg, color_fg=button_color_fg, command=None):
    return tk.Button(root, text=text, padx=20, pady=20, width=width, height=height, bg=color_bg, fg=color_fg, font=('Arial', 12), command=command).grid(row=row, column=col, padx=5, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

for (text, row, col) in buttons:
    create_button(text, row, col, command=lambda t=text: append_to_display(t))

create_button('=', 4, 3, command=calculate)
create_button('C', 4, 4, color_bg=button_color_special, command=clear)

tk.Label(root, text="PV:", font=('Arial', 12)).grid(row=5, column=0)
entry_pv = tk.Entry(root, font=('Arial', 12), width=10)
entry_pv.grid(row=5, column=1, columnspan=2)

tk.Label(root, text="Taxa (%):", font=('Arial', 12)).grid(row=6, column=0)
entry_rate = tk.Entry(root, font=('Arial', 12), width=10)
entry_rate.grid(row=6, column=1, columnspan=2)

tk.Label(root, text="Períodos (n):", font=('Arial', 12)).grid(row=7, column=0)
entry_n = tk.Entry(root, font=('Arial', 12), width=10)
entry_n.grid(row=7, column=1, columnspan=2)

tk.Label(root, text="FV:", font=('Arial', 12)).grid(row=8, column=0)
entry_fv = tk.Entry(root, font=('Arial', 12), width=10)
entry_fv.grid(row=8, column=1, columnspan=2)

create_button("FV", 5, 4, color_bg=button_color_special, command=future_value)
create_button("PV", 8, 4, color_bg=button_color_special, command=present_value)

root.bind("<Key>", key_event)

root.mainloop()