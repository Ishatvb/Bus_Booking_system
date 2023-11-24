import tkinter as tk
from tkinter import ttk
from frames.MenuPage import MenuPage
from frames.admin.Operator import Operator
from frames.admin.Bus import Bus
from frames.admin.Route import Route
from frames.admin.Run import Run


class BusDetails(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        heading = ttk.Frame(self, style="Heading.TFrame")
        ttk.Label(
            heading, text="Add new details to database", style="Heading.TLabel"
        ).pack()
        heading.pack(fill="x")

        self.input = ttk.Frame(self)

        tk.Button(self.input, text="New Operator", background="springgreen", command=lambda: controller.show_frame(Operator)).grid(
            row=1, column=0, padx=10
        )
        tk.Button(self.input, text="New Bus", background="tomato", command=lambda: controller.show_frame(Bus)).grid(
            row=1, column=1, padx=10
        )
        tk.Button(self.input, text="New Route", background="steelblue", command=lambda: controller.show_frame(Route)).grid(
            row=1, column=2, padx=10
        )
        tk.Button(self.input, text="New Run", background="rosybrown", command=lambda: controller.show_frame(Run)).grid(
            row=1, column=3, padx=10
        )

        self.input.pack(pady=(25, 0))

        ttk.Button(
            self,
            image=controller.home,
            command=lambda: controller.show_frame(MenuPage),
        ).pack(side="bottom", anchor="e")
