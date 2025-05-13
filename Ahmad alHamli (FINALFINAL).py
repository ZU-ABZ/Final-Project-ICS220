import tkinter as tk
from tkinter import ttk, messagebox
import os

class Dimensions:
    '''Serves as the parent class of all GUI'''

    def __init__(self, root, title, dimensions):
        self.root = root
        self.root.title(title)
        self.root.geometry(dimensions)

class Login(Dimensions):
    '''The first screen user's are greeted with. Either sends them to the login screen or the registeration screen'''
    def __init__(self, root, admin):
        super().__init__(root, "Login", "400x300")
        self.root = root
        self.admin = admin

        self.login = tk.Button(self.root, text="Login", command=self.go_to_access)
        self.login.pack(pady=10)

        self.register = tk.Button(self.root, text="Register", command=self.go_to_register)
        self.register.pack(pady=10)

    #Switches to the Access GUi
    def go_to_access(self):
        self.root.destroy()
        root = tk.Tk()
        Access(root, self.admin)

    # Switches to the Registration GUi
    def go_to_register(self):
        self.root.destroy()
        root = tk.Tk()
        Register(root, self.admin)


class GUIManagement(Dimensions):
    '''Admin panel that displays the amount of purchases made by any user.'''
    def __init__(self, root, family=0, single=0, weekend=0, season=0, group=0):
        super().__init__(root, "Ticket Sales Management", "500x400")
        self.family = family
        self.single = single
        self.weekend = weekend
        self.season = season
        self.group = group
        totalSold = 0

        tk.Label(self.root, text="Admin Dashboard - Ticket Sales", font=("Helvetica", 16, "bold")).pack(pady=20)
        self.total_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.total_label.pack(pady=10)
        self.total_label_profit = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.total_label_profit.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Ticket Type", font=("Helvetica", 12, "underline"), width=20).grid(row=0, column=0)
        tk.Label(frame, text="Quantity Sold", font=("Helvetica", 12, "underline"), width=20).grid(row=0, column=1)
        tk.Label(frame, text="Profit", font=("Helvetica", 12, "underline"), width=20).grid(row=0, column=2)


        tk.Label(frame, text="Family", font=("Helvetica", 11), width=20).grid(row=1, column=0)
        self.family_label = tk.Label(frame, text=str(self.family), font=("Helvetica", 11), width=20)
        self.family_label.grid(row=1, column=1)
        self.family_label_profit = tk.Label(frame, text=str(self.family), font=("Helvetica", 11), width=20)
        self.family_label_profit.grid(row=1, column=2)

        tk.Label(frame, text="SingleRacePass", font=("Helvetica", 11), width=20).grid(row=2, column=0)
        self.single_label = tk.Label(frame, text=str(self.single), font=("Helvetica", 11), width=20)
        self.single_label.grid(row=2, column=1)
        self.single_label_profit = tk.Label(frame, text=str(self.single), font=("Helvetica", 11), width=20)
        self.single_label_profit.grid(row=2, column=2)

        tk.Label(frame, text="WeekendPackage", font=("Helvetica", 11), width=20).grid(row=3, column=0)
        self.weekend_label = tk.Label(frame, text=str(self.weekend), font=("Helvetica", 11), width=20)
        self.weekend_label.grid(row=3, column=1)
        self.weekend_label_profit = tk.Label(frame, text=str(self.weekend), font=("Helvetica", 11), width=20)
        self.weekend_label_profit.grid(row=3, column=2)

        tk.Label(frame, text="SeasonMembership", font=("Helvetica", 11), width=20).grid(row=4, column=0)
        self.season_label = tk.Label(frame, text=str(self.season), font=("Helvetica", 11), width=20)
        self.season_label.grid(row=4, column=1)
        self.season_label_profit = tk.Label(frame, text=str(self.season), font=("Helvetica", 11), width=20)
        self.season_label_profit.grid(row=4, column=2)

        tk.Label(frame, text="GroupDiscountTicket", font=("Helvetica", 11), width=20).grid(row=5, column=0)
        self.group_label = tk.Label(frame, text=str(self.group), font=("Helvetica", 11), width=20)
        self.group_label.grid(row=5, column=1)
        self.group_label_profit = tk.Label(frame, text=str(self.group), font=("Helvetica", 11), width=20)
        self.group_label_profit.grid(row=5, column=2)

        self.refresh()

    #Refreshes the data from purchases, allowing users to see real time purchases
    def refresh(self):
        self.family_label.config(text=str(self.family))
        self.single_label.config(text=str(self.single))
        self.weekend_label.config(text=str(self.weekend))
        self.season_label.config(text=str(self.season))
        self.group_label.config(text=str(self.group))

        self.family_label_profit.config(text=str(self.family*15))
        self.single_label_profit.config(text=str(self.single*6))
        self.weekend_label_profit.config(text=str(self.weekend*5))
        self.season_label_profit.config(text=str(self.season*12))
        self.group_label_profit.config(text=str(self.group*8))

        total = self.family + self.single + self.weekend + self.season + self.group
        totalSold = self.family*15 + self.single*6 + self.weekend*5 + self.season*12 + self.group*8
        self.total_label.config(text=f"Total Tickets Sold: {total}")
        self.total_label_profit.config(text=f"Total Profits: {totalSold}")

        with open("Admin.txt", "w") as f:
            f.write(f"Family: {self.family}\n")
            f.write(f"SingleRacePass: {self.single}\n")
            f.write(f"WeekendPackage: {self.weekend}\n")
            f.write(f"SeasonMembership: {self.season}\n")
            f.write(f"GroupDiscountTicket: {self.group}\n")

        self.root.after(1000, self.refresh)





class Register(Dimensions):
    '''The registration screen that takes the user's informaion to create their GrandPrix account'''
    def __init__(self, root, admin):
        super().__init__(root, "Register", "400x500")
        self.root = root
        self.admin = admin

        self.name = tk.Entry(self.root)
        self.name.pack(pady=5)
        self.name.insert(0, "Name")

        self.gender = tk.StringVar(value="Male")
        self.genderMale = tk.Radiobutton(self.root, text="Male", variable=self.gender, value="Male")
        self.genderMale.pack()
        self.genderFemale = tk.Radiobutton(self.root, text="Female", variable=self.gender, value="Female")
        self.genderFemale.pack()

        self.age = tk.Entry(self.root)
        self.age.pack(pady=5)
        self.age.insert(0, "Age")

        self.email = tk.Entry(self.root)
        self.email.pack(pady=5)
        self.email.insert(0, "Email")

        self.phone = tk.Entry(self.root)
        self.phone.pack(pady=5)
        self.phone.insert(0, "phone No")

        self.username = tk.Entry(self.root)
        self.username.pack(pady=5)
        self.username.insert(0, "Username")

        self.password = tk.Entry(self.root, show="*")
        self.password.pack(pady=5)
        self.password.insert(0, "Password")

        self.confirm_password = tk.Entry(self.root, show="*")
        self.confirm_password.pack(pady=5)
        self.confirm_password.insert(0, "Password Again")

        self.register = tk.Button(self.root, text="Register", command=self.register_user)
        self.register.pack(pady=10)

        self.back = tk.Button(self.root, text="Back", command=self.returnBack)
        self.back.pack(pady=10)

    # Switches back to the Login GUi
    def returnBack(self):
        self.root.destroy()
        root = tk.Tk()
        Login(root, self.admin)

    # Allows the creation of an account ONLY if the passwords match. Then switches the GUi to the Login screen
    def register_user(self):
        username = self.username.get()
        password = self.password.get()
        confirm_password = self.confirm_password.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        with open("Users.txt", "a") as file:
            file.write(f"{username}:{password}\n")

        messagebox.showinfo("Success", "User Registered Successfully")
        self.root.destroy()
        root = tk.Tk()
        Login(root, self.admin)

class Access(Dimensions):
    '''The real login screen where user's inputs of username and password are verified'''
    def __init__(self, root, admin):
        super().__init__(root, "Access", "400x300")
        self.root = root
        self.admin = admin

        self.username = tk.Entry(self.root)
        self.username.pack(pady=5)
        self.username.insert(0, "Username")

        self.password = tk.Entry(self.root, show="*")
        self.password.pack(pady=5)
        self.password.insert(0, "Password")

        self.login = tk.Button(self.root, text="Login", command=self.verifyUser)
        self.login.pack(pady=10)

        self.back = tk.Button(self.root, text="Back", command=self.returnBack)
        self.back.pack(pady=10)

    # Switches back to the Login GUi
    def returnBack(self):
        self.root.destroy()
        root = tk.Tk()
        Login(root, self.admin)

    # Verifies the user's information, if it is a match sends the user to the Reservation GUi. Otherwise throws an error.
    def verifyUser(self):
        username = self.username.get()
        password = self.password.get()

        with open("Users.txt", "r") as file:
            users = file.readlines()

        for user in users:
            storedU, storedP = user.strip().split(":")
            if username == storedU and password == storedP:
                messagebox.showinfo("Success", "Access Granted")
                self.root.destroy()
                root = tk.Tk()
                Reservation(root, username, self.admin)
                return

        messagebox.showerror("Error", "Invalid Username or Password")



class Reservation(Dimensions):
    '''The screen that allows users to select Ticket Passes : Race dates : Payment type while also updating the Admin GUI with every purchase'''

    def __init__(self, root, username, admin):
        super().__init__(root, "Reservation", "400x400")
        self.root = root
        self.username = username
        self.admin = admin

        self.passes = tk.StringVar(value="Single")
        tk.Label(self.root, text="Pass Type:").pack(pady=5)
        self.pass_type = ttk.Combobox(self.root, values=["Single", "WeekendPackage", "GroupDiscount", "Family", "SeasonMembership"], state="readonly")
        self.pass_type.set("Single")
        self.pass_type.pack(pady=5)

        tk.Label(self.root, text="Race Date:").pack(pady=5)
        self.raceDate = tk.Entry(self.root)
        self.raceDate.insert(0, "dd/mm/yy")
        self.raceDate.pack(pady=5)

        self.payment = tk.StringVar(value="Cash")
        tk.Label(self.root, text="Payment Type:").pack(pady=5)
        self.payment_type = ttk.Combobox(self.root, values=["Cash", "Visa", "Digital Wallet"], state="readonly")
        self.payment_type.set("Cash")
        self.payment_type.pack(pady=5)

        self.purchase = tk.Button(self.root, text="Purchase", command=self.make_purchase)
        self.purchase.pack(pady=5)

        self.modify = tk.Button(self.root, text="Modify", command=self.go_to_modify)
        self.modify.pack(pady=5)

        self.view = tk.Button(self.root, text="View", command=self.go_to_view)
        self.view.pack(pady=5)

    # Takes the values of the boxes and stores them into a file while also updating the ticket purchases and the specific type of it as well.
    def make_purchase(self):
        pass_type = self.pass_type.get()
        raceDate = self.raceDate.get()
        payment_type = self.payment_type.get()
        Userz = f"{self.username}_Reservation.txt"

        ticketID = 1
        if os.path.exists(Userz):
            with open(Userz, "r") as file:
                lines = file.readlines()
                ticketID = len(lines) // 4 + 1

        with open(Userz, "a") as file:
            file.write(f"Pass Type: {pass_type}\n")
            file.write(f"Race Date: {raceDate}\n")
            file.write(f"Payment Type: {payment_type}\n")
            file.write(f"{ticketID}\n")

        if pass_type == "Family":
            self.admin.family += 1
        elif pass_type == "Single":
            self.admin.single += 1
        elif pass_type == "WeekendPackage":
            self.admin.weekend += 1
        elif pass_type == "SeasonMembership":
            self.admin.season += 1
        elif pass_type == "GroupDiscount":
            self.admin.group += 1

        messagebox.showinfo("Success", f"Purchase Recorded (Ticket ID: {ticketID})")

    # Switches to the Modify GUi
    def go_to_modify(self):
        self.root.destroy()
        root = tk.Tk()
        Modify(root, self.username, admin)

    # Switches to the View GUi
    def go_to_view(self):
        self.root.destroy()
        root = tk.Tk()
        View(root, self.username)
        self.root.destroy()
        root = tk.Tk()
        View(root, self.username)
        pass_type = self.pass_type.get()
        raceDate = self.raceDate.get()
        payment_type = self.payment_type.get()

        Userz = f"{self.username}_Reservation.txt"
        with open(Userz, "a") as file:
            file.write(f"Pass Type: {pass_type}\n")
            file.write(f"Race Date: {raceDate}\n")
            file.write(f"Payment Type: {payment_type}\n")
        messagebox.showinfo("Success", "Purchase Recorded")

    # Switches to the Modify GUi
    def go_to_modify(self):
        self.root.destroy()
        root = tk.Tk()
        Modify(root, self.username, admin)

    # Switches to the View GUi
    def go_to_view(self):
        self.root.destroy()
        root = tk.Tk()
        View(root, self.username)


class Modify(Dimensions):
    '''Allows users to modify their reservations by inputting the ticket ID (Found in the View GUI screen) and update any information on it'''

    def __init__(self, root, username, admin):
        super().__init__(root, "Reservation", "400x400")
        self.root = root
        self.username = username
        self.admin = admin

        self.passes = tk.StringVar()
        self.raceDate = tk.StringVar()
        self.payment = tk.StringVar()

        tk.Label(self.root, text="Ticket ID:").pack(pady=5)
        self.ticketID = tk.Entry(self.root)
        self.ticketID.pack(pady=5)

        self.passes = tk.StringVar(value="Single")
        tk.Label(self.root, text="Pass Type:").pack(pady=5)
        self.pass_type = ttk.Combobox(self.root, values=["Single", "WeekendPackage", "GroupDiscount", "Family","SeasonMembership"], state="readonly")
        self.pass_type.set("Single")
        self.pass_type.pack(pady=5)

        tk.Label(self.root, text="Race Date:").pack(pady=5)
        self.raceDate = tk.Entry(self.root)
        self.raceDate.insert(0, "dd/mm/yy")
        self.raceDate.pack(pady=5)

        self.payment = tk.StringVar(value="Cash")
        tk.Label(self.root, text="Payment Type:").pack(pady=5)
        self.payment_type = ttk.Combobox(self.root, values=["Cash", "Visa", "Digital Wallet"], state="readonly")
        self.payment_type.set("Cash")
        self.payment_type.pack(pady=5)


        self.update_btn = tk.Button(self.root, text="Update", command=self.update_reservation)
        self.update_btn.pack(pady=10)

        self.back = tk.Button(self.root, text="Back", command=self.returnBack)
        self.back.pack(pady=10)

    # Switches back to the Reservtaion GUi
    def returnBack(self):
        self.root.destroy()
        root = tk.Tk()
        Reservation(root, self.username, self.admin)

        self.load_data()

    # Loads the user's data from the text file
    def load_data(self):
        Userz = f"{self.username}_Reservation.txt"
        if os.path.exists(Userz):
            with open(Userz, "r") as file:
                lines = file.readlines()
                try:
                    self.passes.set(lines[0].split(": ")[1].strip())
                    self.raceDate.set(lines[1].split(": ")[1].strip())
                    self.payment.set(lines[2].split(": ")[1].strip())
                except IndexError:
                    pass

    # If the ticket ID matches then they are allowed to modify Pass type : Race date : Payment method. Otherwise throws an error based on the issue.
    def update_reservation(self):
        Userz = f"{self.username}_Reservation.txt"
        if not os.path.exists(Userz):
            messagebox.showerror("Error", "Reservation file not found.")
            return

        try:
            ticket_id = int(self.ticketID.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid Ticket ID.")
            return

        with open(Userz, "r") as file:
            lines = file.readlines()

        n = (ticket_id - 1) * 4
        if n + 3 >= len(lines) or lines[n + 3].strip() != str(ticket_id):
            messagebox.showerror("Error", "Ticket ID does not exist.")
            return

        #Update values
        lines[n] = f"Pass Type: {self.pass_type.get()}\n"
        lines[n + 1] = f"Race Date: {self.raceDate.get()}\n"
        lines[n + 2] = f"Payment Type: {self.payment_type.get()}\n"

        with open(Userz, "w") as file:
            file.writelines(lines)

        messagebox.showinfo("Success", f"Ticket {ticket_id} updated.")
        self.root.destroy()
        root = tk.Tk()
        Reservation(root, self.username, self.admin)


class View(Dimensions):
    '''Allows users to view any and all reservations. It's also the main method of finding the TicketID besides memorizing it from the small pop-up screen'''

    def __init__(self, root, username):
        super().__init__(root, "Reservation Information", "400x150")
        self.root = root
        self.username = username
        Userz = f"{self.username}_Reservation.txt"

        tk.Label(self.root, text="Reservation Details", font=("Helvetica", 14, "bold")).pack(pady=10)


        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        titles = ["Pass Type", "Race Date", "Payment Type"]
        for n, text in enumerate(titles):
            tk.Label(frame, text=text, font=("Helvetica", 11, "underline"), width=15).grid(row=0, column=n)

        #Data
        buttons = ["N/A", "N/A", "N/A"]

        if os.path.exists(Userz):
            with open(Userz, "r") as file:
                lines = file.readlines()
            for n in range(0, len(lines), 4):
                try:
                    pass_type = lines[n].split(": ")[1].strip()
                    raceDate = lines[n + 1].split(": ")[1].strip()
                    payment = lines[n + 2].split(": ")[1].strip()
                    ticketID = lines[n + 3].strip()

                    row = (n // 4) + 1

                    tk.Label(frame, text=pass_type, font=("Helvetica", 11), width=15).grid(row=row, column=0)
                    tk.Label(frame, text=raceDate, font=("Helvetica", 11), width=15).grid(row=row, column=1)
                    tk.Label(frame, text=payment, font=("Helvetica", 11), width=15).grid(row=row, column=2)
                    tk.Label(frame, text=ticketID, font=("Helvetica", 11), width=15).grid(row=row, column=3)
                except IndexError:
                    continue



        self.back_btn = tk.Button(self.root, text="Back", command=self.go_back)
        self.back_btn.pack(pady=10)

    # Switches back to the reservation GUi
    def go_back(self):
        self.root.destroy()
        root = tk.Tk()
        Reservation(root, self.username, admin)

#Creates an object and runs the instances to start the GUI screen
if __name__ == "__main__":
    root = tk.Tk()
    root2 = tk.Tk()

    admin = GUIManagement(root2) #Creates instance
    Login(root, admin)  # Opens two seperate GUI windows

    root.mainloop()
