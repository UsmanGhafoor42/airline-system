# from business import BusinessLogic
# from models import Flight, Aircraft
# from datetime import datetime

# class CLI:
#     def __init__(self):
#         self.logic = BusinessLogic()
    
#     def display_menu(self):
#         while True:
#             print("\n=== SkyLink Airways ===")
#             print("1. Schedule Flight")
#             print("2. Book Flight")
#             print("3. View Flight Occupancy")
#             print("4. Exit")
            
#             choice = input("Enter choice: ")
            
#             if choice == '1':
#                 self.schedule_flight()
#             elif choice == '2':
#                 self.book_flight()
#             elif choice == '3':
#                 self.view_occupancy()
#             elif choice == '4':
#                 print("Exiting...")
#                 break
#             else:
#                 print("Invalid choice!")

#     def schedule_flight(self):
#         try:
#             aircraft_id = int(input("Enter aircraft ID: "))
#             flight_number = input("Flight number: ")
#             origin = input("Origin: ")
#             destination = input("Destination: ")
#             departure = datetime.strptime(
#                 input("Departure (YYYY-MM-DD HH:MM): "),
#                 "%Y-%m-%d %H:%M"
#             )
#             arrival = datetime.strptime(
#                 input("Arrival (YYYY-MM-DD HH:MM): "),
#                 "%Y-%m-%d %H:%M"
#             )
            
#             flight = Flight(
#                 aircraft_id=aircraft_id,
#                 flight_number=flight_number,
#                 origin=origin,
#                 destination=destination,
#                 departure=departure,
#                 arrival=arrival
#             )
            
#             if self.logic.schedule_flight(flight):
#                 print("Flight scheduled successfully!")
#             else:
#                 print("Failed to schedule flight")
#         except ValueError as e:
#             print(f"Error: {e}")

#     def book_flight(self):
#         try:
#             first_name = input("First name: ")
#             last_name = input("Last name: ")
#             email = input("Email: ")
#             passport = input("Passport: ")
            
#             flight_id = int(input("Flight ID: "))
#             seat_number = input("Seat number: ")
            
#             passenger_data = {
#                 'first_name': first_name,
#                 'last_name': last_name,
#                 'email': email,
#                 'passport': passport
#             }
            
#             if self.logic.book_flight(passenger_data, flight_id, seat_number):
#                 print("Booking successful!")
#             else:
#                 print("Booking failed")
#         except ValueError as e:
#             print(f"Error: {e}")

#     def view_occupancy(self):
#         try:
#             flight_id = int(input("Enter Flight ID: "))
#             occupancy = self.logic.get_flight_occupancy(flight_id)
            
#             if occupancy:
#                 print(f"\nFlight {occupancy.flight_number}")
#                 print(f"Total Seats: {occupancy.capacity}")
#                 print(f"Booked Seats: {occupancy.booked_seats}")
#                 print(f"Available Seats: {occupancy.capacity - occupancy.booked_seats}")
#             else:
#                 print("Flight not found")
#         except ValueError:
#             print("Invalid Flight ID")

# if __name__ == "__main__":
#     cli = CLI()
#     cli.display_menu()

import tkinter as tk
from tkinter import ttk, messagebox
from business import BusinessLogic
from models import Flight
from datetime import datetime

class AirlineGUI:
    def __init__(self, root):
        self.root = root
        self.logic = BusinessLogic()
        self.root.title("SkyLink Airways Management System")
        
        # Configure main window
        self.root.geometry("800x600")
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Cascadia Code', 12), padding=10)
        self.style.configure('TLabel', font=('Cascadia Code', 12))
        
        self.create_main_menu()

    def create_main_menu(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main menu frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, pady=50)
        
        # Menu buttons
        ttk.Button(main_frame, text="1. Schedule Flight", 
                 command=self.show_schedule_flight).pack(pady=10, fill=tk.X)
        ttk.Button(main_frame, text="2. Book Flight", 
                 command=self.show_book_flight).pack(pady=10, fill=tk.X)
        ttk.Button(main_frame, text="3. View Flight Occupancy", 
                 command=self.show_occupancy).pack(pady=10, fill=tk.X)
        ttk.Button(main_frame, text="4. Exit", 
                 command=self.root.destroy).pack(pady=10, fill=tk.X)

    def show_schedule_flight(self):
        window = tk.Toplevel(self.root)
        window.title("Schedule New Flight")
        
        fields = [
            ("Aircraft ID:", "entry_aircraft_id"),
            ("Flight Number:", "entry_flight_number"),
            ("Origin:", "entry_origin"),
            ("Destination:", "entry_destination"),
            ("Departure (YYYY-MM-DD HH:MM):", "entry_departure"),
            ("Arrival (YYYY-MM-DD HH:MM):", "entry_arrival")
        ]
        
        entries = {}
        for idx, (label, name) in enumerate(fields):
            ttk.Label(window, text=label).grid(row=idx, column=0, padx=5, pady=5, sticky=tk.W)
            entry = ttk.Entry(window)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            entries[name] = entry
        
        def submit():
            try:
                flight = Flight(
                    aircraft_id=int(entries['entry_aircraft_id'].get()),
                    flight_number=entries['entry_flight_number'].get(),
                    origin=entries['entry_origin'].get(),
                    destination=entries['entry_destination'].get(),
                    departure=datetime.strptime(entries['entry_departure'].get(), "%Y-%m-%d %H:%M"),
                    arrival=datetime.strptime(entries['entry_arrival'].get(), "%Y-%m-%d %H:%M")
                )
                
                if self.logic.schedule_flight(flight):
                    messagebox.showinfo("Success", "Flight scheduled successfully!")
                    window.destroy()
                else:
                    messagebox.showerror("Error", "Failed to schedule flight")
            except ValueError as e:
                messagebox.showerror("Input Error", str(e))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        ttk.Button(window, text="Submit", command=submit).grid(row=len(fields), columnspan=2, pady=10)

    def show_book_flight(self):
        window = tk.Toplevel(self.root)
        window.title("Book Flight")
        
        # Passenger Details
        ttk.Label(window, text="First Name:").grid(row=0, column=0)
        first_name = ttk.Entry(window)
        first_name.grid(row=0, column=1)
        
        ttk.Label(window, text="Last Name:").grid(row=1, column=0)
        last_name = ttk.Entry(window)
        last_name.grid(row=1, column=1)
        
        ttk.Label(window, text="Email:").grid(row=2, column=0)
        email = ttk.Entry(window)
        email.grid(row=2, column=1)
        
        ttk.Label(window, text="Passport:").grid(row=3, column=0)
        passport = ttk.Entry(window)
        passport.grid(row=3, column=1)
        
        ttk.Label(window, text="Flight ID:").grid(row=4, column=0)
        flight_id = ttk.Entry(window)
        flight_id.grid(row=4, column=1)
        
        ttk.Label(window, text="Seat Number:").grid(row=5, column=0)
        seat_number = ttk.Entry(window)
        seat_number.grid(row=5, column=1)
        
        def submit():
            try:
                passenger_data = {
                    'first_name': first_name.get(),
                    'last_name': last_name.get(),
                    'email': email.get(),
                    'passport': passport.get()
                }
                
                result = self.logic.book_flight(
                    passenger_data,
                    int(flight_id.get()),
                    seat_number.get()
                )
                
                if result:
                    messagebox.showinfo("Success", "Booking successful!")
                    window.destroy()
                else:
                    messagebox.showerror("Error", "Booking failed")
            except ValueError as e:
                messagebox.showerror("Input Error", str(e))
        
        ttk.Button(window, text="Submit Booking", command=submit).grid(row=6, columnspan=2, pady=10)

    def show_occupancy(self):
        window = tk.Toplevel(self.root)
        window.title("Flight Occupancy")
        
        ttk.Label(window, text="Flight ID:").pack(pady=5)
        flight_id = ttk.Entry(window)
        flight_id.pack(pady=5)
        
        def show():
            try:
                occupancy = self.logic.get_flight_occupancy(int(flight_id.get()))
                if occupancy:
                    result = (
                        f"Flight {occupancy.flight_number}\n"
                        f"Total Seats: {occupancy.capacity}\n"
                        f"Booked Seats: {occupancy.booked_seats}\n"
                        f"Available Seats: {occupancy.capacity - occupancy.booked_seats}"
                    )
                    messagebox.showinfo("Occupancy Details", result)
                else:
                    messagebox.showinfo("Not Found", "Flight not found")
            except ValueError:
                messagebox.showerror("Error", "Invalid Flight ID")
        
        ttk.Button(window, text="Show Occupancy", command=show).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AirlineGUI(root)
    root.mainloop()