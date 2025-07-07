import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif op == '%':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 % num2
        else:
            result = "?"

        result_label.config(text=f"Result: {num1} {op} {num2} = {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division or modulo by zero is not allowed.")


window = tk.Tk()
window.title("CodeSoft Calculator")
window.geometry("320x300")
window.resizable(False, False)

# Number inputs
tk.Label(window, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack()


tk.Label(window, text="Select Operation:").pack(pady=10)
operation = tk.StringVar()
operation.set('+')  # Default

op_frame = tk.Frame(window)
op_frame.pack()

for op in ['+', '-', '*', '/', '%']:
    tk.Radiobutton(op_frame, text=op, variable=operation, value=op).pack(side=tk.LEFT, padx=8)


tk.Button(window, text="Calculate", command=calculate, bg="#4CAF50", fg="white", width=20).pack(pady=15)


result_label = tk.Label(window, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)


window.mainloop()
