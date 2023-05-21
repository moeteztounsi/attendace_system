import tkinter as tk
import tkinter.ttk as ttk
import csv

class CSVApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Attendance List")

        self.tree = ttk.Treeview(self, columns=("column1", "column2"))
        self.tree.pack(fill='both', expand=True)

        self.tree.heading("#0", text="Index")
        self.tree.heading("column1", text="Name")
        self.tree.heading("column2", text="Time")
      
        ttk.Style().configure("Treeview", font= ("century gothic", 10), rowheight=15, columnwidth = 5)

        self.load_csv("attendance.csv")

    def load_csv(self, filename):
        with open(filename) as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                self.tree.insert("", i, text=str(i+1), values=row)


def run():
    app = CSVApp()
    app.mainloop()