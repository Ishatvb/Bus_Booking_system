from tkinter import ttk


class Splash(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text="Name: ISHATV BEOHAR", style="Splash1.TLabel").pack(
            pady=(100, 10)
        )
        ttk.Label(self, text="Er No: 211B147",
                  style="Splash1.TLabel").pack(pady=10)
        ttk.Label(self, text="Mobile: 8878388873", style="Splash1.TLabel").pack(
            pady=(10, 100)
        )
        ttk.Label(
            self,
            text="Submitted to: Dr. Mahesh Kumar",
            style="TitleBar.TLabel",
            font=("Arial", 20, "bold"),
        ).pack()
        ttk.Label(self, text="Project Based Learning", style="Splash2.TLabel").pack(
            pady=5
        )
