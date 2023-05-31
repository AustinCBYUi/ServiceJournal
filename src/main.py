from datetime import datetime
import random

#Bonjour or Journal?
class Jour:
    
    def __init__(self, name, pn, email):
        self.fname = name
        self.lname = name
        self.phone = pn #Phone number
        self.email = email


    def main(self):
        print("Search or create an entry: ")
        find = input("")
        if find == "search":
            find_name = input("Enter a name to search:\n")
            Jour.get_data(self, find_name)
        elif find == "create":
            Jour.create_entry(self)


    def get_data(self, name):
        pass


    def create_entry(self):
        fname = input("First name: ")
        lname = input("Last name: ")
        pn = int(input("Phone Number: "))
        email = input("Email: ")
        year = int(input("Year of vehicle: "))
        make = input("Make: ")
        model = input("Model: ")
        trim = input("Trim Package(If any): ")
        tos = input("Type of Service: ")
        cos = float(input("Cost of Service(Labor): $"))
        service = input("General Comments: ")
        today = datetime.now()
        uid = random.randint(100000, 999999) #Pick a number from 100,000 - 999,999
        Jour.write_file(self, fname, lname, pn, email, year, make,
                        model, trim, tos, cos, service, today, uid)
        #TODO Add Submodel, don't know how I missed submodel.
        #TODO Add in mileage.
        #TODO Search function should search by keywords as phone number, first or last name and display all results.

    def write_file(self, fname, lname, pn, email, year,
                    make, model, submodel, trim, tos, labor_rate,
                    labor_hours, service, today, uid):
        #Will use first name for now instead of UID
        root = f"Projects\ServiceJournal\data\{uid}.txt"
        file = open(root, "w")

        file.write(f"Date: {today}\n\n")
        file.write(f"First: {fname}\n")
        file.write(f"Last: {lname}\n")
        file.write(f"Phone: {pn},  Email: {email}\n")
        file.write(f"Year: {year} |  Make: {make} |  Model: {model}\n")
        file.write(f"Submodel: {submodel} | Trim Package: {trim}\n")
        file.write(f"Time of Service: {tos}\n\n")
        file.write(f"Labor Rate: {labor_rate}\n")
        file.write(f"Labor Hours: {labor_hours}\n")
        file.write(f"Service General Comments: {service}\n")
        file.write(f"Unique Identification: {uid}\n")

# testMe = Jour.main(Jour)
# testMe