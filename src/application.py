import tkinter as tk
from tkinter import IntVar
from functools import partial
import main
import glob

root_window = tk.Tk()
root_window.title("Service Journal")
root_window.minsize(width = 600, height = 600)

#Frame
menu_frame = tk.Frame(root_window)
menu_frame.grid(column=0, row=0, columnspan=4, rowspan=2)

#Item Frame used for each window
item_frame = tk.Frame(menu_frame)
item_frame.grid(column=0, row=3, columnspan=5, rowspan=12)



#Functions Below

#Clear function to destroy old stuff
def clear(object):
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()



#Creates the entire Create a New Entry menu.
def create_entry_menu():
    #Clears the item frame.
    clear(item_frame)

    def clear_boxes():
        """Deletes all content in entry boxes."""
        first_name.delete(0, tk.END)
        last_name.delete(0, tk.END)
        phone_num.delete(0, tk.END)
        email.delete(0, tk.END)
        year.delete(0, tk.END)
        make.delete(0, tk.END)
        model.delete(0, tk.END)
        submodel.delete(0, tk.END)
        trim.delete(0, tk.END)
        tos.delete(0, tk.END)
        miles.delete(0, tk.END) #Will add this
        general_comments_text.delete("1.0", "end")


    #Encapsulated function to obtain values
    def get_inputs():
        """Obtains all values within window, then send the
        values to the main python file to write the file"""
        finished_write = tk.Label(item_frame, text="Finished Writing File!")
        finished_write.grid(column=3, row=11)
        fname = first_name.get().capitalize()
        lname = last_name.get().capitalize()
        pn = phone_num.get()
        email_add = email.get()
        year_of = year.get()
        make_of = make.get().capitalize()
        model_of = model.get().capitalize()
        submodel_of = submodel.get().capitalize()
        trim_of = trim.get().capitalize()
        time_service = tos.get()
        miles_of = miles.get() #TODO
        labor_time = labor.get()
        hours_labor = hours.get()
        #Gets textbox line 1 to end.
        gen_com = general_comments_text.get("1.0", tk.END)
        get_date = main.datetime.now()
        uid = main.random.randint(100000, 999999)

        main.Jour.write_file(main.Jour, fname, lname, pn, email_add, year_of,
                            make_of, model_of, submodel_of, trim_of, time_service, miles_of, labor_time,
                            hours_labor, gen_com, get_date, uid)


    #Title
    title_label = tk.Label(item_frame, text="Service Journal")
    title_label.grid(row = 1, column = 3)

    #First name, Last name, Phone number, email, year, make model
    #submodel, trim, time of service, cost of service in labor,
    #service general comments, date of service.

    #First name label
    first_name_label = tk.Label(item_frame, text="First Name: ")
    first_name_label.grid(column=1, row=2)
    #First name entry
    first_name = tk.Entry(item_frame, width=15) #Entry width
    first_name.insert(tk.END, string="(First Name)")
    first_name.grid(column=2, row=2)

    #Last name label
    last_name_label = tk.Label(item_frame, text="Last Name: ")
    last_name_label.grid(column=1, row=3)
    #Last name entry
    last_name = tk.Entry(item_frame, width=15)
    last_name.insert(tk.END, string="(Last Name)")
    last_name.grid(column=2, row=3)

    #Phone number label
    phone_label = tk.Label(item_frame, text="Phone Number: ")
    phone_label.grid(column=1, row=4)
    #Phone number entry
    phone_num = tk.Entry(item_frame, width=15)
    phone_num.insert(tk.END, string="(123)456-7890")
    phone_num.grid(column=2, row=4)


    #email label
    email_label = tk.Label(item_frame, text="Email Address: ")
    email_label.grid(column=1, row=5)
    #email entry
    email = tk.Entry(item_frame, width=30)
    email.insert(tk.END, string="email.address@gmail.com")
    email.grid(column=2, row=5, pady=5)


    #Year, make and model
    year_label = tk.Label(item_frame, text="Year: ")
    year_label.grid(column=1, row=6)
    #Year text
    year = tk.Entry(item_frame, width=10)
    year.insert(tk.END, string="Year")
    year.grid(column=2, row=6)

    #Make of car label
    make_label = tk.Label(item_frame, text="Make: ")
    make_label.grid(column=3, row=6)
    #Make entry
    make = tk.Entry(item_frame, width=25)
    make.insert(tk.END, string="Make")
    make.grid(column=4, row=6)

    #Model of car
    model_label = tk.Label(item_frame, text="Model: ")
    model_label.grid(column=1, row=7)
    #entry box for model
    model = tk.Entry(item_frame, width=20)
    model.insert(tk.END, string="Model")
    model.grid(column=2, row=7)

    #Submodel
    submodel_label = tk.Label(item_frame, text="Submodel: ")
    submodel_label.grid(column=3, row=7)
    #Entrybox for submodel
    submodel = tk.Entry(item_frame, width=20)
    submodel.insert(tk.END, string="Optional Submodel")
    submodel.grid(column=4, row=7)

    #Trim and Time of Service
    trim_label = tk.Label(item_frame, text="Trim: ")
    trim_label.grid(column=1, row=8)
    #Trim entrybox
    trim = tk.Entry(item_frame, width=20)
    trim.insert(tk.END, string="Optional Trim")
    trim.grid(column=2, row=8)

    #Time of service label
    tos_label = tk.Label(item_frame, text="Time of Service: ")
    tos_label.grid(column=3, row=8)
    #TOS entry
    tos = tk.Entry(item_frame, width=10)
    tos.insert(tk.END, string="2400")
    tos.grid(column=4, row=8)

    #Mileage
    miles_label = tk.Label(item_frame, text="Mileage: ")
    miles_label.grid(column=1, row=9)
    #Entry
    miles = tk.Entry(item_frame, width=15)
    miles.insert(tk.END, string="12345")
    miles.grid(column=2, row=9)

    #Cost of service labor rate
    labor_label = tk.Label(item_frame, text="Labor Rate (per/hr): ")
    labor_label.grid(column=1, row=10)
    #Scale for COS Labor
    labor = tk.Scale(item_frame, from_=50, to=120) #command=command needs to go in
    labor.grid(column=2, row=10)

    #Labor hours
    hours_label = tk.Label(item_frame, text="Billable Hours: ")
    hours_label.grid(column=3, row=10)
    #Scale scroller for labor hours
    hours = tk.Scale(item_frame, from_=1, to=24) #add in the command
    hours.grid(column=4, row=10)

    #Final general comments text box
    general_comments = tk.Label(item_frame, text="General Comments: ")
    general_comments.grid(column=1, row=11)
    #General comments text box
    general_comments_text = tk.Text(item_frame, height=15, width=50)
    general_comments_text.focus()
    general_comments_text.insert(tk.END, "General Service Comments")
    general_comments_text.grid(column=2, row=10, columnspan=4)

    submit = tk.Button(item_frame, text="Submit", command=get_inputs)
    clear_entry_stuff = tk.Button(item_frame, text="Clear", command=clear_boxes)
    submit.grid(column=2, row=12)
    clear_entry_stuff.grid(column=3, row=12)



#Also writes to our main.py
def search_entries():
    clear(item_frame)

    def search_file():
        """Parses all files in the \data folder according to search parameters and will display
        a list of all results."""

        #This will retrieve the specific tickets generated by the search_file function.
        def retrieve_ticket(num):
            """Retrieves specific tickets that are generated by the parent function named search_file"""
            clear(item_frame)
            #Thankfully stackoverflow helped with this a lot
            #num parameter is counted off the lambda.
            with open(num, "r") as file:
                #It will open whatever file you chose and display the data in the form of Tkinter Labels.
                for line in file:
                    #for loop to display all labels
                    label = tk.Label(item_frame, text=line)
                    #Non-specific grid will automatically place in accordance to where everything needs to go
                    label.grid()

        #currently only last name will be the option to search. However I do plan to add the phone-number search as
        #mentioned.
        last_name = s_lname_entry.get().capitalize() #Make sure it still searches.
        #using glob library to parse all files in the \data\ section with .txt extensions
        files = glob.glob(r"Projects\ServiceJournal\data\*.txt") #Projects\ServiceJournal\data
        #Loop to loop through all files from above
        for f in files:
            #open each file and name as in_file.
            with open(f, "r") as in_file:
                #Loop again through each line within that specific file.
                for line in in_file:
                    #We are looking for a line named Date
                    date = "Date"
                    #If that string is in the line,
                    if date in line:
                        #We will strip it. This will be used for accurate searches
                        strip_date = line.strip()
                    #Same thing as above, used first name to help myself out because I work on my wife's car.
                    get_first = "First"
                    #If the "First" string is in the line..
                    if get_first in line:
                        #Strip it. It will be used to identify each ticket
                        strip_first = line.strip()
                    #Lastly the most important part, whatever the last name you searched, it will be listed
                    if last_name in line:
                        #Same principle, it will also get stripped.
                        stripline = line.strip()
                        #And in the process we will create a button for each service found.
                        #The lambda function being used to take a snap shot of each "f" through the loops.
                        #it will match f to f in which case it will call the retrieve_ticket function with
                        #the parameter of the specific f file.
                        found_service = tk.Button(item_frame, text=f"{strip_date} | {stripline} | {strip_first}",
                                                    width=60, command=lambda f=f: retrieve_ticket(f))
                        #Same thing as above, non-specific grid placement will automatically place everything.
                        found_service.grid()

       
    #Label / title for the search entries
    title_label = tk.Label(item_frame, text="Search Entries")
    title_label.grid(row=1, column=3)

    #Search by Last Name
    s_last_name_label = tk.Label(item_frame, text="Last Name: ")
    s_last_name_label.grid(row=2, column=1)
    s_lname_entry = tk.Entry(item_frame, width=15)
    s_lname_entry.grid(row=2, column=2)
    #Command will call search_file which does all the hard work.
    s_lname_button = tk.Button(item_frame, text="Search", command=search_file)
    #Sticky actually didn't work for what I needed it to do. Can't figure out how to keep the window from
    #expanding when results are found.
    s_lname_button.grid(row=2, column=3, sticky="N")

    #TODO Add the functionality for this at a later time.
    #Search by Phone Number
    # s_phone_label = tk.Label(item_frame, text="Phone Number: ")
    # s_phone_label.grid(row=3, column=1)
    # s_phone_entry = tk.Entry(item_frame, width=15)
    # s_phone_entry.grid(row=3, column=2)
    # s_phone_button = tk.Button(item_frame, text="Search", command=search_file)
    # s_phone_button.grid(row=3, column=3)


def labor_menu():
    """Labor recommendation Menu, will eventually be sent to the ticket writer."""
    #Encapsulated to calculate the value.
    def get_values_from_labor():
        """Simply takes the input from the entries and converts them to floats to send to the main file which
        just returns the answer."""
        job_hours = float(recommend_hours_entry.get())
        rate = float(hourly_rate_entry.get())
        #Answer is stored from the function call.
        answer = main.Jour.labor_recommend(main.Jour, job_hours, rate)
        #Put the answer in a label next to the submit button.
        answer_title = tk.Label(item_frame, text=f"${answer} in Labor")
        answer_title.grid(column=3, row=4)

    #Clear the item frame.
    clear(item_frame)
    #title
    labor_title = tk.Label(item_frame, text="Labor Recommendation")
    labor_title.grid(column=1, row=1)

    #Label
    recommended_hours = tk.Label(item_frame, text="Recommended Hours: ")
    recommended_hours.grid(column=1, row=2)
    #Entry
    recommend_hours_entry = tk.Entry(item_frame, width=15)
    recommend_hours_entry.insert(tk.END, "0.5")
    recommend_hours_entry.grid(column=2, row=2)
    #Label for hourly rate.
    hourly_rate = tk.Label(item_frame, text="Shop's Hourly Rate in $")
    hourly_rate.grid(column=1, row=3)
    #Entry for hourly rate
    hourly_rate_entry = tk.Entry(item_frame, width=15)
    hourly_rate_entry.insert(tk.END, "60")
    hourly_rate_entry.grid(column=2, row=3)
    #Button
    submit_button = tk.Button(item_frame, text="Calculate", command=get_values_from_labor)
    submit_button.grid(column=2, row=4)



#Main Selection
service_ticket_writer = tk.Button(menu_frame, text="Create New Entry", command=create_entry_menu, height=1, width=20)
service_ticket_writer.grid(column=0, row=0, sticky="N")
search_entry = tk.Button(menu_frame, text="Search Entries", command=search_entries, height=1, width=20)
search_entry.grid(column=1, row=0, sticky="N")
labor_calculator = tk.Button(menu_frame, text="Labor Recommend", command=labor_menu, height=1, width=20)
labor_calculator.grid(column=2, row=0, sticky="N")

root_window.mainloop()