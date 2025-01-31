# import createDB
import os
import sqlite3 as sql
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser as web
from tkinter.filedialog import askopenfilename as afn


def test(win: tk.Tk | tk.Toplevel):
    def main():
        def addToDB():
            top.destroy()
            btns(name.get(), path.get())
            con = sql.connect("test.db")
            cur = con.cursor()
            cur.execute(
                "INSERT INTO data (name, path) VALUES(?, ?)", (name.get(), path.get()))
            con.commit()

        def browse():
            program = afn(title="program",
                          filetypes=(("exe files", "*.exe"), ("url files", "*.url"), ("all files", "*.*")))
            path.set(path.get() +" ; "+ program if path.get() else program)

        top = tk.Toplevel()
        top.geometry("400x200")
        entryframe = tk.Frame(top)
        btnsframe = tk.Frame(top)
        infoframe = tk.Frame(top)
        entry = ttk.Entry(entryframe, font=(
            "comic sans", 14), textvariable=name)
        entry2 = ttk.Entry(entryframe, font=(
            "comic sans", 14), textvariable=path)
        namelbl = ttk.Label(entryframe, text="name:", font=("comic sans", 14))
        pathlbl = ttk.Label(entryframe, text="path:", font=("comic sans", 14))
        infolbl = ttk.Label(infoframe, text="use ' ; ' to separate between programes", font=("comic sans", 12))
        doneBtn = ttk.Button(btnsframe, text="done", command=addToDB)
        fileBtn = ttk.Button(btnsframe, text="file", command=browse)

        top.rowconfigure((0, 1, 2), weight=1)
        top.columnconfigure(0, weight=1)
        entryframe.rowconfigure((0, 1), weight=1)
        entryframe.columnconfigure((0, 1), weight=1)
        btnsframe.rowconfigure((0, 1), weight=1)
        btnsframe.columnconfigure(0, weight=1)
        infoframe.rowconfigure(0, weight=1)
        infoframe.columnconfigure(0, weight=1)

        entryframe.grid(row=0, column=0, sticky="nswe")
        entry.grid(row=0, column=1, sticky="w")
        entry2.grid(row=1, column=1, sticky="w")
        namelbl.grid(row=0, column=0, sticky="e")
        pathlbl.grid(row=1, column=0, sticky="e")

        btnsframe.grid(row=2, column=0, sticky="nswe")
        doneBtn.grid(row=0)
        fileBtn.grid(row=1)
        
        infoframe.grid(row=1, column=0, sticky="nswe")
        infolbl.grid(row=0, column=0, sticky="w")

    def btns(name, path):
        def des(event=None):
            actionBtns.grid_forget()
            # print(actionBtns["text"])
            con = sql.connect("test.db")
            cur = con.cursor()
            cur.execute("DELETE FROM data WHERE name = ?",
                        (actionBtns["text"],))
            con.commit()
            addBtns.grid(row=0, column=0)
            fetch_data()
        
        # if "exe" in path or "url" in path:
        #     def command(g=path): return os.startfile(f"{g}")
        # elif "www" in path or ".com" in path or "http" in path:
        #     def command(g=path): return web.open(f"{g}")
        # else:
        #     command = ""
        if path and " ; " not in path:
            def command(g=path): os.startfile(f"{g}")
        elif " ; " in path:
            paths = path.split(" ; ")
            def command(g=paths): [os.startfile(f"{i}") for i in g]
        else:
            command = ""

        actionBtns = ttk.Button(win,
                                text=name,
                                command=command)
        actionBtns.config(width=len(name))

        row_info, column_info = addBtns.grid_info()['row'], addBtns.grid_info()[
            "column"]

        actionBtns.bind("<Button-3>", des)

        addBtns.grid_forget()
        actionBtns.grid(row=row_info, column=column_info)

        if (column_info + 1) % 5 == 0:
            addBtns.grid(row=row_info+1, column=0)
        else:
            addBtns.grid(row=row_info, column=column_info+1)

    def fetch_data():
        con = sql.connect("test.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM DATA")
        row = cur.fetchall()

        if len(row) != 0:
            for i in win.winfo_children()[1:]:
                i.grid_forget()

        for i in row:
            btns(i[0], i[1])

    # def loc(event):
    #     name, path = event.x_root-win.winfo_rootx(), event.y_root-win.winfo_rooty()
    #     print(win.grid_location(name, path))

    # win = tk.Tk()
    win.geometry("600x480+540+230")
    style = ttk.Style()
    style.configure("TButton",
                    font=("comic sans", 14),
                    width=4)

    name = tk.StringVar()
    path = tk.StringVar()

    addBtns = ttk.Button(win, text="+", command=main)
    addBtns.grid(row=0, column=0)

    win.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    win.columnconfigure((0, 1, 2, 3, 4), weight=1)
    # print(addBtns.grid_info())
    # win.bind("<Button-1>", loc)
    # print(win.grid_size())
    fetch_data()
    # print(win.winfo_children())
    win.mainloop()


if __name__ == '__main__':
    test(tk.Tk())
else:
    def test2():
        test(tk.Toplevel())
