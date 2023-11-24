import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as message
from frames.MenuPage import MenuPage
from frames.Ticket import Ticket


class SeatBooking(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.passenger = dict()
        self.move = controller.show_frame

        self.heading = ttk.Frame(self, style="Heading.TFrame")
        ttk.Label(self.heading, text="Enter Journey Details",
                  style="Heading.TLabel").pack()
        self.heading.pack(fill="x")

        self.input = ttk.Frame(self)

        ttk.Label(self.input, text="To: ").grid(row=1, column=0)
        self.passenger['fromCity'] = ttk.Entry(self.input)
        self.passenger['fromCity'].grid(row=1, column=1)
        ttk.Label(self.input, text="From: ").grid(
            row=1, column=2, padx=(50, 0))
        self.passenger['toCity'] = ttk.Entry(self.input)
        self.passenger['toCity'].grid(row=1, column=3, padx=(0, 50))
        ttk.Label(self.input, text="Journey Date: ").grid(row=1, column=4)
        self.passenger['onDate'] = ttk.Entry(self.input)
        self.passenger['onDate'].grid(row=1, column=5)
        tk.Button(
            self.input,
            text="Show Bus",
            background="springgreen",
            command=self.valSearch,
        ).grid(row=2, column=0, columnspan=10, pady=(25, 0))
        self.input.pack(pady=(20, 0))

        self.passenger['bus'] = tk.IntVar()
        self.details = ttk.Frame(self)

        self.passHead = ttk.Frame(self, style="Heading.TFrame")
        ttk.Label(
            self.passHead,
            text="Fill Passenger Details to book the bus tickets",
            style="Heading.TLabel",
        ).pack()

        self.passengers = ttk.Frame(self)

        ttk.Label(self.passengers, text="Name: ").grid(row=1, column=0)
        self.passenger['name'] = ttk.Entry(self.passengers)
        self.passenger['name'].grid(row=1, column=1)
        ttk.Label(self.passengers, text="Gender: ").grid(
            row=1, column=2, padx=(50, 0))
        self.passenger['gender'] = ttk.Entry(self.passengers)
        self.passenger['gender'].grid(row=1, column=3, padx=(0, 50))
        ttk.Label(self.passengers, text="No. of Seats: ").grid(row=1, column=4)
        self.passenger['seats'] = ttk.Entry(self.passengers)
        self.passenger['seats'].grid(row=1, column=5)
        ttk.Label(self.passengers, text="Mobile No: ").grid(row=1, column=6)
        self.passenger['mobile'] = ttk.Entry(self.passengers)
        self.passenger['mobile'].grid(row=1, column=7)
        ttk.Label(self.passengers, text="Age: ").grid(row=1, column=8)
        self.passenger['age'] = ttk.Entry(self.passengers)
        self.passenger['age'].grid(row=1, column=9)
        tk.Button(self.passengers, text="Book Seat", background="springgreen",
                  command=self.book).grid(row=2, column=0, columnspan=10, pady=25)

        self.error1 = ttk.Label(
            self, text="Fill all the values!", style="Error.TLabel"
        )

        self.error2 = ttk.Label(
            self, text="Select a bus!", style="Error.TLabel"
        )

        ttk.Button(
            self,
            image=controller.home,
            command=lambda: controller.show_frame(MenuPage),
        ).pack(side="bottom", anchor="e")

    def valSearch(self):
        self.error1.pack_forget()
        self.details.pack_forget()
        self.error2.pack_forget()
        self.passHead.pack_forget()
        self.passengers.pack_forget()
        if (self.passenger['toCity'].get()) and (self.passenger['fromCity'].get()) and (self.passenger['onDate'].get()):
            self.search()
        else:
            self.error1.pack(pady=(5, 0))

    def valBook(self):
        self.error2.pack_forget()
        self.passHead.pack_forget()
        self.passengers.pack_forget()
        if self.passenger['bus'].get() != 0:
            self.passHead.pack(fill='x', pady=(25, 0))
            self.passengers.pack(pady=(20, 0))
        else:
            self.error2.pack(pady=(5, 0))

    def search(self):
        self.passenger['bus'].set(0)
        self.details.destroy()
        self.details = ttk.Frame(self)

        ttk.Label(self.details, text="Select Bus").grid(
            row=1, column=0, padx=15)
        ttk.Label(self.details, text="Operator").grid(row=1, column=1, padx=15)
        ttk.Label(self.details, text="Bus Type").grid(row=1, column=2, padx=15)
        ttk.Label(self.details, text="Available/Capacity").grid(row=1,
                                                                column=3, padx=15)
        ttk.Label(self.details, text="Fare").grid(row=1, column=4, padx=15)

        tk.Radiobutton(self.details, text="Bus 1", indicator=0, selectcolor='lightgreen',
                       background="light blue", variable=self.passenger['bus'], value=1).grid(
            row=2, column=0, padx=15
        )
        ttk.Label(self.details, text="Kamla").grid(row=2, column=1, padx=15)
        ttk.Label(self.details, text="AC 2x2").grid(row=2, column=2, padx=15)
        ttk.Label(self.details, text="25/30").grid(row=2, column=3, padx=15)
        ttk.Label(self.details, text="1000").grid(row=2, column=4, padx=15)

        tk.Button(self.details, text="Proceed to book", background="springgreen", command=self.valBook).grid(
            row=3, column=0, columnspan=10, padx=15, pady=(10, 0)
        )
        self.details.pack(pady=(20, 0))

    def book(self):
        confirmation = message.askyesno(title='Fare Confirm', message='Total amount to be paid is Rs. ' +
                                        str(1000 * int(self.passenger['seats'].get())))
        if confirmation:
            self.move(Ticket)
