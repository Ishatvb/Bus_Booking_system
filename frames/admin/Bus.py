import tkinter as tk
from tkinter import ttk
from frames.MenuPage import MenuPage
import tkinter.messagebox as message


class Bus(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        heading = ttk.Frame(self, style="Heading.TFrame")
        ttk.Label(heading, text="Add Bus Details", style="Heading.TLabel").pack()
        heading.pack(fill="x")

        self.input = ttk.Frame(self)

        ttk.Label(self.input, text="Bus ID").grid(row=1, column=1)
        ttk.Entry(self.input).grid(row=1, column=2, padx=(4, 0))
        ttk.Label(self.input, text="Bus Type").grid(row=1, column=3, padx=(10, 0))
        BusType = tk.StringVar()
        option = ["AC 2X2", "Non AC 2X2", "AC 3X2", "Non AC 3X2"]
        l = ttk.OptionMenu(self.input, BusType, *option)
        l.grid(row=1, column=4, padx=(4, 0))
        l["menu"].config(bg="white")
        ttk.Label(self.input, text="Capacity").grid(row=1, column=5, padx=(10, 0))
        ttk.Entry(self.input).grid(row=1, column=6, padx=(4, 0))
        ttk.Label(self.input, text="Fare").grid(row=1, column=7, padx=(10, 0))
        ttk.Entry(self.input).grid(row=1, column=8, padx=(4, 0))
        ttk.Label(self.input, text="Op ID").grid(row=1, column=9, padx=(10, 0))
        ttk.Entry(self.input).grid(row=1, column=10, padx=(4, 0))
        ttk.Label(self.input, text="Route ID").grid(row=1, column=11, padx=(10, 0))
        ttk.Entry(self.input).grid(row=1, column=12, padx=(4, 0))

        self.buttons = ttk.Frame(self.input)
        tk.Button(
            self.buttons, text="Add", background="springgreen", command=self.add
        ).grid(row=1, column=1)
        tk.Button(
            self.buttons, text="Edit", background="springgreen", command=self.edit
        ).grid(row=1, column=2, padx=(10, 0))
        self.buttons.grid(row=2, column=1, columnspan=14, pady=(10, 0))

        self.input.pack(pady=(25, 0))

        self.details = ttk.Frame(self)

        ttk.Label(self.details, text="8").grid(row=1, column=1)
        ttk.Label(self.details, text="AC 2x2").grid(row=1, column=2, padx=(10, 0))
        ttk.Label(self.details, text="30").grid(row=1, column=3, padx=(10, 0))
        ttk.Label(self.details, text="1200").grid(row=1, column=4, padx=(10, 0))
        ttk.Label(self.details, text="8").grid(row=1, column=5, padx=(10, 0))
        ttk.Label(self.details, text="14").grid(row=1, column=6, padx=(10, 0))

        ttk.Button(
            self,
            image=controller.home,
            command=lambda: controller.show_frame(MenuPage),
        ).pack(side="bottom", anchor="e")

    def add(self):
        message.showinfo(title="Bus Entry", message="Bus record added.")
        self.details.pack(pady=(15, 0))

    def edit(self):
        message.showinfo(
            title="Bus Entry Update",
            message="Bus record updated sucsessfully.",
        )
        self.details.pack(pady=(15, 0))
