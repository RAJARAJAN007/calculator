import tkinter as tk
from tkinter import messagebox

# Step 1: Choose operation
def choose_operation():
    global operation
    operation = operation_var.get()

    if operation == "":
        messagebox.showwarning("Warning", "Please select an operation!")
        return

    # Close first window and open second
    op_window.destroy()
    enter_numbers_window()


def enter_numbers_window():
    global num_window, entry1, entry2, result_label

    num_window = tk.Tk()
    num_window.title("Enter Numbers")
    num_window.geometry("350x250")

    tk.Label(num_window, text=f"Operation: {operation}", font=("Arial", 12)).pack(pady=5)

    tk.Label(num_window, text="Enter first number:").pack(pady=5)
    entry1 = tk.Entry(num_window, font=("Arial", 12))
    entry1.pack()

    tk.Label(num_window, text="Enter second number:").pack(pady=5)
    entry2 = tk.Entry(num_window, font=("Arial", 12))
    entry2.pack()

    tk.Button(num_window, text="Submit", font=("Arial", 12), command=calculate).pack(pady=10)

    result_label = tk.Label(num_window, text="Result: ", font=("Arial", 13))
    result_label.pack(pady=20)

    num_window.mainloop()


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers only!")


# Step 1 window
op_window = tk.Tk()
op_window.title("Choose Operation")
op_window.geometry("300x250")

tk.Label(op_window, text="Select an operation:", font=("Arial", 12)).pack(pady=10)

operation_var = tk.StringVar()
operations = ["Add", "Subtract", "Multiply", "Divide"]

for op in operations:
    tk.Radiobutton(
        op_window,
        text=op,
        variable=operation_var,
        value=op,
        font=("Arial", 12)
    ).pack(anchor="w")

tk.Button(op_window, text="Next", font=("Arial", 12), command=choose_operation).pack(pady=20)

op_window.mainloop()
