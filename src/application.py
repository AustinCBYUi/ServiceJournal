import tkinter
from tkinter import *
import main

window = Tk()
window.title("Service Journal")
window.minsize(width = 600, height = 600)

menu = StringVar()
menu.set("Select a Year")

#Also writes to our main.py
def get_inputs():
    finished_write = Label(text="Finished Writing File!")
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
    gen_com = general_comments_text.get("1.0", END)
    get_date = main.datetime.now()
    uid = main.random.randint(100000, 999999)

    main.Jour.write_file(main.Jour, fname, lname, pn, email_add, year_of,
                         make_of, model_of, submodel_of, trim_of, time_service, labor_time,
                         hours_labor, gen_com, get_date, uid)


#Title
title_label = Label(text="Service Journal")
title_label.grid(row = 1, column = 3)

#First name, Last name, Phone number, email, year, make model
#submodel, trim, time of service, cost of service in labor,
#service general comments, date of service.

#First name label
first_name_label = Label(text="First Name: ")
first_name_label.grid(column=1, row=2)
#First name entry
first_name = Entry(width=15) #Entry width
first_name.insert(END, string="(First Name)")
first_name.grid(column=2, row=2)

#Last name label
last_name_label = Label(text="Last Name: ")
last_name_label.grid(column=1, row=3)
#Last name entry
last_name = Entry(width=15)
last_name.insert(END, string="(Last Name)")
last_name.grid(column=2, row=3)

#Phone number label
phone_label = Label(text="Phone Number: ")
phone_label.grid(column=1, row=4)
#Phone number entry
phone_num = Entry(width=15)
phone_num.insert(END, string="(123)456-7890")
phone_num.grid(column=2, row=4)


#email label
email_label = Label(text="Email Address: ")
email_label.grid(column=1, row=5)
#email entry
email = Entry(width=30)
email.insert(END, string="email.address@gmail.com")
email.grid(column=2, row=5, pady=5)


#Year, make and model
year_label = Label(text="Year: ")
year_label.grid(column=1, row=6)
#Year text
year = Entry(width=10)
year.insert(END, string="Year")
year.grid(column=2, row=6)

#Make of car label
make_label = Label(text="Make: ")
make_label.grid(column=3, row=6)
#Make entry
make = Entry(width=25)
make.insert(END, string="Make")
make.grid(column=4, row=6)

#Model of car
model_label = Label(text="Model: ")
model_label.grid(column=1, row=7)
#entry box for model
model = Entry(width=20)
model.insert(END, string="Model")
model.grid(column=2, row=7)

#Submodel
submodel_label = Label(text="Submodel: ")
submodel_label.grid(column=3, row=7)
#Entrybox for submodel
submodel = Entry(width=20)
submodel.insert(END, string="Optional Submodel")
submodel.grid(column=4, row=7)

#Trim and Time of Service
trim_label = Label(text="Trim: ")
trim_label.grid(column=1, row=8)
#Trim entrybox
trim = Entry(width=20)
trim.insert(END, string="Optional Trim")
trim.grid(column=2, row=8)

#Time of service label
tos_label = Label(text="Time of Service: ")
tos_label.grid(column=3, row=8)
#TOS entry
tos = Entry(width=10)
tos.insert(END, string="2400")
tos.grid(column=4, row=8)


#Cost of service labor rate
labor_label = Label(text="Labor Rate: ")
labor_label.grid(column=1, row=9)
#Scale for COS Labor
labor = Scale(from_=50, to=100) #command=command needs to go in
labor.grid(column=2, row=9)

#Labor hours
hours_label = Label(text="Labor Hours: ")
hours_label.grid(column=3, row=9)
#Scale scroller for labor hours
hours = Scale(from_=1, to=24) #add in the command
hours.grid(column=4, row=9)

#Final general comments text box
general_comments = Label(text="General Comments: ")
general_comments.grid(column=1, row=10)
#General comments text box
general_comments_text = Text(height=15, width=50)
general_comments_text.focus()
general_comments_text.insert(END, "General Service Comments")
general_comments_text.grid(column=2, row=10, columnspan=4)

submit = Button(text="Submit", command=get_inputs)
submit.grid(column=2, row=11)

window.mainloop()