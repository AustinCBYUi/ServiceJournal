from datetime import datetime
import random
import glob
#Author Austin Campbell
#The application.py program must be ran, not the main.py.
#
#
#Primary logic behind program.
#Journal
class Jour:
    
    #Only reason this is still here is because I don't want to change the self out of all the functions.
    def __init__(self, name, pn, email):
        self.fname = name
        self.lname = name
        self.phone = pn #Phone number
        self.email = email


    #Writes the file created from application.py
    def write_file(self, fname, lname, pn, email, year,
                    make, model, submodel, trim, tos, miles, labor_rate,
                    labor_hours, service, today, uid):
        """Try writing a file with a unique identification number ranging
        from 100,000 to 999,999. If successful it will include the date of
        writing ticket, and all information included."""
        #Will use first name for now instead of UID
        try:
            #Write to this file with the randomly generated UID
            root = f"Projects\ServiceJournal\data\{uid}.txt"
            #root file is then opened.
            file = open(root, "w")

            #Now it will write all these things to 
            file.write(f"Date: {today:%m %d %Y}\n\n")
            file.write(f"First: {fname}\n")
            file.write(f"Last: {lname}\n")
            file.write(f"Phone: {pn},  Email: {email}\n")
            file.write(f"Year: {year} |  Make: {make} |  Model: {model}\n")
            file.write(f"Submodel: {submodel} | Trim Package: {trim}\n")
            file.write(f"Time of Service: {tos}\n")
            file.write(f"Mileage: {miles}\n\n")
            file.write(f"Labor Rate: {labor_rate}\n")
            file.write(f"Labor Hours: {labor_hours}\n")
            file.write(f"Service General Comments: {service}\n")
            file.write(f"Unique Identification: {uid}\n")

        #If the file you're creating doesn't exist.
        except FileNotFoundError as file_not_found:
            print(type(file_not_found).__name__, file_not_found, sep=":")
            print("Major error discovered, please re-try.")
        #If the file you're writing to already exists, don't overwrite it.
        except FileExistsError as file_overwrite:
            print(type(file_overwrite).__name__, file_overwrite, sep=":")
            print("This UID is already used. Please re-try inputting your information.")

        
    #This will actually probably be radio buttons for the last option on the menu which
    #will also create a separate receipt.
    def detailing_calculator(self, car_size, package_type):
        #2 door / 4 door CARS.
        #Material Charge
        mat_charge = 5
        #Not yet fully implemented
        SMALL_CAR = 50
        #SUVs with 4 doors
        MEDIUM_CAR = 70
        #Trucks / Luxury Car Quote
        LARGE_CAR = 90
        #Simple interior wipe down, and vacuum, inside windows cleaned too.
        BASIC_PACK = 10
        #Shined interior with wipe down, and vacuum.
        INTERMEDIETE = 20
        #Shined interior, seats removed possibly, carpet and seat cleaning, vacuum. The entire works
        ADVANCED = 30

        return car_size + package_type + mat_charge
    

    def labor_recommend(self, hourly_rate, hours):
        """Simple function to get rate. Will eventually 
        include a dictionary with all hours to reference.
        Multiplies labor rate by hours billable. 
        Example: Oil Change Hours by state is .5.
                Shop charges $80/hr. .5 * 80 = 40.
                Labor cost should be $40.
        Returns: Total labor cost."""
        return hourly_rate * hours


# testMe = Jour.main(Jour)
# testMe