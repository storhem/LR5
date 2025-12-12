import tkinter as tk
import random

root = tk.Tk()
root.title("Цветная панель")

colors = ["red", "green", "blue", "yellow", "purple", "orange"]

panel = tk.Label(root, bg="lightblue", width=40, height=15)
panel.pack(pady=20, padx=20)

tk.Button(root, text="Сменить цвет",
          command=lambda: panel.config(bg=random.choice(colors)),
          width=20).pack(pady=5)

root.mainloop()