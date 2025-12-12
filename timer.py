import tkinter as tk

class Timer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Таймер / Секундомер")

        self.time_ms = 0
        self.running = False
        self.mode = "stopwatch"

        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.root, text="00:00.00", font=("Arial", 40))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.insert(0, "60")
        self.entry.pack()

        tk.Button(self.root, text="Старт", command=self.start).pack(fill="x")
        tk.Button(self.root, text="Стоп", command=self.stop).pack(fill="x")
        tk.Button(self.root, text="Сброс", command=self.reset).pack(fill="x")
        tk.Button(self.root, text="Установить таймер (сек)",
                  command=self.set_timer).pack(fill="x")

    def run(self):
        self.root.mainloop()

app = Timer()
app.run()