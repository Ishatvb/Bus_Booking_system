import tkinter as tk
from tkinter import ttk
from frames.MenuPage import MenuPage


class Ticket(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        from main import ticket
        self.data = dict()
        self.ticket = ticket(self)

        heading = ttk.Frame(self, style="Heading.TFrame")
        ttk.Label(heading, text="Bus Ticket",
                  style="Heading.TLabel").pack()
        heading.pack(fill="x")

        self.ticket.pack(pady=(20, 0))
