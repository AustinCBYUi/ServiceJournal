import tkinter as tk
from tkinter import IntVar
import main

root_window = tk.Tk()
root_window.title("Service Journal")
root_window.minsize(width = 600, height = 600)

#Frame
menu_frame = tk.Frame(root_window)
menu_frame.grid(column=0, row=0, columnspan=4, rowspan=2)

#Item Frame used for each window
item_frame = tk.Frame(menu_frame)
item_frame.grid(column=0, row=3, columnspan=5, rowspan=12)

menu = tk.StringVar()
menu.set("Select a Year")

#Functions Below

#Clear function to destroy old stuff
def clear(object):
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()


#Also writes to our main.py


def create_entry_menu():
    clear(item_frame)

    #Encapsulated function to obtain values
    def get_inputs():
        """Obtains all values within window, then send the
        values to the main python file to write the file"""
        finished_write = tk.Label(text="Finished Writing File!")
        finished_write.grid(column=3, row=11)
        fname = first_name.get()
        lname = last_name.get()
        pn = phone_num.get()
        email_add = email.get()
        year_of = year.get()
        make_of = make.get()
        model_of = model.get()
        submodel_of = submodel.get()
        trim_of = trim.get()
        time_service = tos.get()
        labor_time = labor.get()
        hours_labor = hours.get()
        #Gets textbox line 1 to end.
        gen_com = general_comments_text.get("1.0", tk.END)
        get_date = main.datetime.now()
        uid = main.random.randint(100000, 999999)

        main.Jour.write_file(main.Jour, fname, lname, pn, email_add, year_of,
                            make_of, model_of, submodel_of, trim_of, time_service, labor_time,
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


    #Cost of service labor rate
    labor_label = tk.Label(item_frame, text="Labor Rate: ")
    labor_label.grid(column=1, row=9)
    #Scale for COS Labor
    labor = tk.Scale(item_frame, from_=50, to=100) #command=command needs to go in
    labor.grid(column=2, row=9)

    #Labor hours
    hours_label = tk.Label(item_frame, text="Labor Hours: ")
    hours_label.grid(column=3, row=9)
    #Scale scroller for labor hours
    hours = tk.Scale(item_frame, from_=1, to=24) #add in the command
    hours.grid(column=4, row=9)

    #Final general comments text box
    general_comments = tk.Label(item_frame, text="General Comments: ")
    general_comments.grid(column=1, row=10)
    #General comments text box
    general_comments_text = tk.Text(item_frame, height=15, width=50)
    general_comments_text.focus()
    general_comments_text.insert(tk.END, "General Service Comments")
    general_comments_text.grid(column=2, row=10, columnspan=4)

    submit = tk.Button(item_frame, text="Submit", command=get_inputs)
    submit.grid(column=2, row=11)





#Main Selection
service_ticket_writer = tk.Button(menu_frame, text="Create New Entry", command=create_entry_menu, height=1, width=20)
service_ticket_writer.grid(column=0, row=0, sticky="N")
search_entry = tk.Button(menu_frame, text="Search Entries", height=1, width=20)
search_entry.grid(column=1, row=0, sticky="N")

root_window.mainloop()