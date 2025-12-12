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