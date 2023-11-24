import tkinter as tk
from tkinter import ttk
from frames.MenuPage import MenuPage
import tkinter.messagebox as message


class Route(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        heading = ttk.Frame(self, style="Heading.TFrame")
        ttk.Label(heading, text="Add Bus Route Details", style="Heading.TLabel").pack()
        heading.pack(fill="x")

        self.input = ttk.Frame(self)

        ttk.Label(self.input, text="Route ID").grid(row=1, column=1)
        ttk.Entry(self.input).grid(row=1, column=2, padx=(4, 0))
        ttk.Label(self.input, text="Station ID").grid(row=1, column=3, padx=(10, 0))
        ttk.Entry(self.input).grid(row=1, column=4, padx=(4, 0))
        ttk.Label(self.input, text="Station name").grid(row=1, column=5, padx=(10, 0))
        ttk.Entry(self.input).grid(row=1, column=6, padx=(4, 0))

        self.buttons = ttk.Frame(self.input)
        tk.Button(
            self.buttons, text="Add", background="springgreen", command=self.add
        ).grid(row=1, column=1)
        tk.Button(
            self.buttons, text="Delete", background="springgreen", command=self.edit
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
        message.showinfo(title="Route Entry", message="Route record added.")
        self.details.pack(pady=(15, 0))

    def edit(self):
        message.showinfo(
            title="Route Entry Delete",
            message="Route record deleted sucsessfully.",
        )
