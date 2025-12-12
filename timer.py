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

    def update_label(self):
        ms = self.time_ms % 1000 // 10
        s = self.time_ms // 1000
        m = s // 60
        s = s % 60
        self.label.config(text=f"{m:02d}:{s:02d}.{ms:02d}")

    def time(self):
        if not self.running:
            return

        if self.mode == "stopwatch":
            self.time_ms += 10
        else:
            if self.time_ms <= 0:
                self.running = False
                self.label.config(text="00:00.00")
                return
            self.time_ms -= 10

        self.update_label()
        self.root.after(10, self.time)

    def start(self):
        if not self.running:
            self.running = True
            self.time()

    def stop(self):
        self.running = False

    def reset(self):
        self.time_ms = 0
        self.update_label()

    def set_timer(self):
        try:
            sec = int(self.entry.get())
            self.time_ms = sec * 1000
            self.mode = "timer"
            self.update_label()
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Введите число!")

    def run(self):
        self.root.mainloop()

app = Timer()
app.run()