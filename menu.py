import tkinter as tk

root = tk.Tk()
root.title("Окно с меню")

menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
root.config(menu=menu)

root.mainloop()