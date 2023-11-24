import tkinter as tk
from tkinter import ttk
import sqlite3 as sql

from frames.Splash import Splash
from frames.MenuPage import MenuPage
from frames.SeatBooking import SeatBooking
from frames.BookedSeats import BookedSeats
from frames.admin.BusDetails import BusDetails
from frames.admin.Operator import Operator
from frames.admin.Bus import Bus
from frames.admin.Route import Route
from frames.admin.Run import Run
from frames.Ticket import Ticket


dbConnect = sql.Connection('db.sqlite3')
db = dbConnect.cursor()
db.execute('SELECT * FROM sqlite_master WHERE type="table"')
print(db.fetchall())

def ticket(parent):
    data = parent.data
    frame = ttk.Frame(parent, borderwidth=3, relief="groove")
    ttk.Label(frame, text="Passengers:").grid(row=1, column=1)
    ttk.Label(frame, text="Gender:").grid(row=1, column=2)
    ttk.Label(frame, text="Age:").grid(row=2, column=1)
    ttk.Label(frame, text="No. of Seats:").grid(row=2, column=2)
    ttk.Label(frame, text="Phone:").grid(row=3, column=1)
    ttk.Label(frame, text="Fare:").grid(row=3, column=2)
    ttk.Label(frame, text="Booking Ref.:").grid(row=4, column=1)
    ttk.Label(frame, text="Bus Detail:").grid(row=4, column=2)
    ttk.Label(frame, text="Travel On:").grid(row=5, column=1)
    ttk.Label(frame, text="Booked On:").grid(row=5, column=2)
    ttk.Label(frame, text="Boarding Point:").grid(row=6, column=1)
    ttk.Label(
        frame,
        text="*Total amount to be paid at the time of boarding:",
        style="Italic.TLabel",
    ).grid(row=7, column=1, columnspan=2, pady=(5, 0))

    return frame


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a meta information to the window
        self.wm_title("Booking System")
        self.geometry("1200x640")
        self.style = ttk.Style()
        self.logo = tk.PhotoImage(file="logo.png")
        self.home = tk.PhotoImage(file="home.png")

        # Theming the UI
        self.style.configure("TFrame", background="white")
        self.style.configure("TMenubutton", background="white")
        self.style.configure("TLabel", background="white", font=("Arial", 14))
        self.style.configure("TButton", font=("Arial", 12))
        self.style.configure("TitleBar.TFrame", background="skyblue")
        self.style.configure("Status.TFrame", background="lightgrey")
        self.style.configure("Heading.TFrame", background="lightgreen")
        self.style.configure("Logo.TLabel", background="skyblue")
        self.style.configure("Error.TLabel", foreground="red")
        self.style.configure(
            "Italic.TLabel", foreground="grey", font=("Arial", 14, "italic")
        )
        self.style.configure("Status.TLabel", background="lightgrey")
        self.style.configure(
            "Heading.TLabel", background="lightgreen", foreground="darkgreen"
        )
        self.style.configure("TitleBar.TLabel", background="skyblue", foreground="red")
        self.style.configure(
            "Splash1.TLabel", background="white", foreground="blue", font=("Arial", 14)
        )
        self.style.configure(
            "Splash2.TLabel", background="white", foreground="red", font=("Arial", 14)
        )
        self.style.configure("Menu.TButton", background="white", foreground="green")

        # Title Bar
        self.titlebar = ttk.Frame(self, style="TitleBar.TFrame")
        ttk.Label(
            self.titlebar, image=self.logo, borderwidth=0, style="Logo.TLabel"
        ).grid(row=0, column=0)
        ttk.Label(
            self.titlebar,
            text="Online Bus Booking System",
            style="TitleBar.TLabel",
            font=("Arial", 36, "bold"),
        ).grid(row=0, column=1)
        self.titlebar.grid_rowconfigure(0, weight=1)
        self.titlebar.grid_columnconfigure(1, weight=1)
        self.titlebar.pack(side="top", fill="x")

        # creating a frame to hold all the others
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Status Bar
        self.statusbar = ttk.Frame(self, style="Status.TFrame")
        ttk.Label(
            self.statusbar, text="Ishatv Beohar (211B147)", style="Status.TLabel"
        ).pack(side="left", fill="x")

        # Configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Load all the Frames in a dictionary
        self.frames = {}
        for F in (
            Splash,
            MenuPage,
            SeatBooking,
            BookedSeats,
            BusDetails,
            Ticket,
            Operator,
            Bus,
            Route,
            Run,
        ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Initialize the first frame
        self.show_frame(Splash)

    # Raises a frame to the top
    def show_frame(self, frame):
        if frame == Splash:
            self.statusbar.pack_forget()
            # Remove Splash screen at interaction
            self.bind("<Key>", lambda event: self.show_frame(MenuPage))
            self.bind("<Button-1>", lambda event: self.show_frame(MenuPage))
        else:
            self.statusbar.pack(side="bottom", fill="x")
            # Remove splash binds
            self.unbind("<Key>")
            self.unbind("<Button-1>")

        cont = self.frames[frame]
        # raises the current frame to the top
        cont.tkraise()


if __name__ == "__main__":
    oBBS = windows()
    # oBBS.state("zoomed")
    oBBS.mainloop()
