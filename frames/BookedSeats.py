import tkinter as tk
from tkinter import ttk
from frames.MenuPage import MenuPage


class BookedSeats(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        heading = ttk.Frame(self, style="Heading.TFrame")
        ttk.Label(heading, text="Check Your Booking",
                  style="Heading.TLabel").pack()
        heading.pack(fill="x")
        self.input = ttk.Frame(self)
        ttk.Label(self.input, text="Enter Your Mobile No: ").grid(
            row=1, column=0)
        ttk.Entry(self.input).grid(row=1, column=1)
        tk.Button(self.input, text="Show Bus", background="springgreen", command=self.tickets).grid(
            row=1, column=2, padx=10
        )
        self.input.pack(pady=(25, 15))

        ttk.Button(
            self,
            image=controller.home,
            command=lambda: controller.show_frame(MenuPage),
        ).pack(side="bottom", anchor="e")

    def tickets(self):
        self.data = dict()
        from main import ticket
        self.ticket = ticket(self)
        self.ticket.pack()
