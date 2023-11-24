import tkinter as tk
from tkinter import ttk


class MenuPage(ttk.Frame):
    def __init__(self, parent, controller):

        from frames.SeatBooking import SeatBooking
        from frames.BookedSeats import BookedSeats
        from frames.admin.BusDetails import BusDetails

        ttk.Frame.__init__(self, parent)
        self.menu = ttk.Frame(self)
        tk.Button(
            self.menu,
            command=lambda: controller.show_frame(SeatBooking),
            text="Seat Booking",
            background="green2",
            font=("Arial", 14, "bold"),
        ).grid(row=0, column=0)
        tk.Button(
            self.menu,
            command=lambda: controller.show_frame(BookedSeats),
            text="Check Booked Seat",
            background="green3",
            font=("Arial", 14, "bold"),
        ).grid(row=0, column=1, padx=75)
        tk.Button(
            self.menu,
            command=lambda: controller.show_frame(BusDetails),
            text="Add Bus Details",
            background="green4",
            font=("Arial", 14, "bold"),
        ).grid(row=0, column=2)
        ttk.Label(self.menu, text="For Admin Only", style="Splash2.TLabel").grid(
            row=1, column=2, pady=25
        )
        self.menu.pack(pady=50)
