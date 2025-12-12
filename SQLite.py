import tkinter as tk
import sqlite3

DB = "simple.db"

conn = sqlite3.connect(DB)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, text TEXT)")
conn.commit()

root = tk.Tk()
root.title("SQLite GUI")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=5)

def refresh_list():
    listbox.delete(0, tk.END)
    rows = c.execute("SELECT id, text FROM items").fetchall()
    for r in rows:
        listbox.insert(tk.END, f"{r[0]}: {r[1]}")

def add_item():
    txt = entry.get().strip()
    if txt:
        c.execute("INSERT INTO items (text) VALUES (?)", (txt,))
        conn.commit()
        entry.delete(0, tk.END)
        refresh_list()

def delete_selected():
    sel = listbox.curselection()
    if not sel:
        return
    item = listbox.get(sel[0])
    item_id = item.split(":")[0]
    c.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()
    refresh_list()

refresh_list()
root.mainloop()