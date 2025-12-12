import tkinter as tk

def calculator(operation):
    try:
        number1 = float(entry1.get())
        number2 = float(entry2.get())
        if operation == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "*":
            result = number1 * number2
        elif operation == "/":
            if number2 == 0:
                result_label.config(text="Ошибка: деление на 0 невозможно!")
                return
            result = number1 / number2
        else:
            result = 0
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Пожалуйста, введите число")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x500")

input_frame = tk.Frame(root)
input_frame.pack(pady=100)

tk.Label(input_frame, text="Введите первое число: ").grid(row=0, column=0)
entry1 = tk.Entry(input_frame)
entry1.grid(row=0, column=1)

tk.Label(input_frame, text="Введите второе число: ").grid(row=1, column=0)
entry2 = tk.Entry(input_frame)
entry2.grid(row=1, column=1)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=5)

btn_plus = tk.Button(buttons_frame, text="+", width=10, height=4,
                     command=lambda: calculator("+"))
btn_plus.grid(row=0, column=0, padx=2)

btn_minus = tk.Button(buttons_frame, text="-", width=10, height=4,
                      command=lambda: calculator("-"))
btn_minus.grid(row=0, column=1, padx=2)

btn_multiply = tk.Button(buttons_frame, text="*", width=10, height=4,
                         command=lambda: calculator("*"))
btn_multiply.grid(row=0, column=2, padx=2)

btn_divide = tk.Button(buttons_frame, text="/", width=10, height=4,
                       command=lambda: calculator("/"))
btn_divide.grid(row=0, column=3, padx=2)

result_label = tk.Label(root, text="Результат: ")
result_label.pack()
root.mainloop()