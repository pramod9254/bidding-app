"""The following module is created for communication with the user, this is the UI module"""

from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
# from datetime import datetime

import dateutil

from PIL import ImageTk, Image
import tkinter
from abc import ABC

import tkinter as tk
from datetime import datetime, timedelta
import dateutil.parser


class Page(ABC):
    def __init__(self, controller):
        self.root = Tk()

        self.controller = controller

        # Making the frame bigger
        w = 1200
        h = 800
        x = 50
        y = 100
        # use width x height + x_offset + y_offset (no spaces!)
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # Background colour
        self.root['background'] = '#dea5a4'


class Scroll(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, background="#dea5a4")
        self.frame = tk.Frame(self.canvas, background="#dea5a4")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


class ScrollablePage(ABC):
    def __init__(self, controller):
        self.root = Tk()
        self.controller = controller

        # Making the frame bigger
        w = 1200
        h = 800
        x = 50
        y = 100
        # use width x height + x_offset + y_offset (no spaces!)
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # Background colour
        self.root['background'] = '#dea5a4'

        self.scroll = Scroll(self.root)

        self.scroll.pack(side="top", fill="both", expand=True)


class LoginView(Page):
    def __init__(self, controller):
        super().__init__(controller)

        # Making LoginView title
        self.label = Label(self.root, text="Login", fg='#5c3f8f', font=("Arial", 25), justify=CENTER,
                           background="#dea5a4")
        self.label.place(x=360, y=165)

        # Making the username label
        self.username_label = Label(text="Username:", font=("Arial", 14), background="#dea5a4")
        self.username_label.place(x=240, y=250)

        # Making the username textbox
        self.username = Entry(font=("Arial", 14), width=25)
        self.username.place(x=360, y=250)

        # Making the password label
        self.password_label = Label(text="Password:", font=("Arial", 14), background="#dea5a4")
        self.password_label.place(x=240, y=300)

        # Making the password textbox
        self.password = Entry(show="*", font=("Arial", 14), width=25)
        self.password.place(x=360, y=300)

        # Making the button

        self.myButton = Button(text="Log in",
                               command=lambda: self.controller.login_btn2(self.username.get(), self.password.get(),
                                                                         self), bg='#5c3f8f', font=("Arial", 14),
                               fg='black')
        
        self.myButton.place(x=370, y=360)



        self.confirm_password_label = Label(text="Don’t have an account?", font=("Arial", 14), background="#dea5a4")
        self.confirm_password_label.place(x=370, y=450)

        self.myButton = Button(text="Sign up",
                               command=lambda: self.controller.signup_btn(self), bg='#5c3f8f', font=("Arial", 14),
                               fg='black')
        self.myButton.place(x=530, y=446)

        
        self.root.mainloop()

class SignUpView(Page):
    def __init__(self, controller):
        super().__init__(controller)

        x=360
        y=165
        # Making LoginView title
        self.label = Label(self.root, text="Create New User", fg='#5c3f8f', font=("Arial", 25), justify=CENTER,
                           background="#dea5a4")
        self.label.place(x=x, y=y)

        x = 240
        y = 250
        # Making the name label
        self.name_label = Label(text="Name:", font=("Arial", 14), background="#dea5a4")
        self.name_label.place(x=x, y=y)

        x+=130
        # Making the name textbox
        self.name = Entry(font=("Arial", 14))
        self.name.place(x=x, y=y)

        x-=130
        y+=50
        # Making the username label
        self.username_label = Label(text="Username:", font=("Arial", 14), background="#dea5a4")
        self.username_label.place(x=x, y=y)
        

        x+=130
        # Making the username textbox
        self.username = Entry(font=("Arial", 14))
        self.username.place(x=x, y=y)


        x-=130
        y+=50
        # Making the password label
        self.password_label = Label(text="Password:", font=("Arial", 14), background="#dea5a4")
        self.password_label.place(x=x, y=y)

        x+=130
        # Making the password textbox
        self.password = Entry(show="*", font=("Arial", 14))
        self.password.place(x=x, y=y)


        x-=130
        y+=50
        # Making the confirm password label
        self.confirm_password_label = Label(text="Confirm Password:", font=("Arial", 14), background="#dea5a4")
        self.confirm_password_label.place(x=x, y=y)

        x+=130
        # Making the confirm password textbox
        self.confirm_password = Entry(show="*", font=("Arial", 14))
        self.confirm_password.place(x=x, y=y)

        
        x-=130
        y+=50
        # Making the user type label
        self.is_seller_label = Label(text="Is Seller?:", font=("Arial", 14), background="#dea5a4")
        self.is_seller_label.place(x=x, y=y)
    

        self.is_seller = BooleanVar()
        x+=130
        self.is_seller_yes = Radiobutton(self.root, text='Yes', variable=self.is_seller, value=True,)
        self.is_seller_yes.place(x=x, y=y)

        x+=100
        self.is_seller_no = Radiobutton(self.root, text='No', variable=self.is_seller, value=False)
        
        self.is_seller_no.place(x=x, y=y)

        
        # Making the button
        x-=100
        y+=70
        

        self.myButton = Button(text="Create Account",
                               command=lambda: self.controller.signup_btn(self.name.get(), self.username.get(), self.password.get(), self.confirm_password.get(), self.is_seller.get()
                                                                          
                                                                          , self), bg='#5c3f8f', font=("Arial", 14),
                               fg='black')
        self.myButton.place(x=x, y=y)
        
        
        # x-=90
        y+=80
        # Making the confirm password label
        self.confirm_password_label = Label(text="Already have an account?", font=("Arial", 14), background="#dea5a4")
        self.confirm_password_label.place(x=x, y=y)

        x+=175

        self.myButton = Button(text="Log in",
                               command=lambda: self.controller.cancel_signup_btn(self), bg='#5c3f8f', font=("Arial", 14),
                               fg='black')
        self.myButton.place(x=x, y=y-3)

        self.root.mainloop()
class ProfileView1(Page):
    def __init__(self, user, controller, initialisation):
        super().__init__(controller)

        # Create a profile pic image object of the image in the path
        profile_pic = Image.open("images/profile_pic.png")
        profile_pic = profile_pic.resize((130, 130), Image.ANTIALIAS)
        profile_pic = ImageTk.PhotoImage(profile_pic)

        profile_pic_label = tkinter.Label(image=profile_pic, bg='#dea5a4')
        profile_pic_label.image = profile_pic
        # Position image
        profile_pic_label.place(x=350, y=40)

        # Making the username label
        self.username_label = Label(text="Username:", font=("Arial", 14), background="#dea5a4", )
        self.username_label.place(x=330, y=200)

        # Username:
        self.username = user.get_username()

        self.username_place = Label(text= self.username, font=("Arial", 14), fg='blue', background="#dea5a4")
        self.username_place.place(x=450, y=200)


        # Making the Name label
        self.given_name_label = Label(text="Name:", font=("Arial", 14), background="#dea5a4")
        self.given_name_label.place(x=330, y=230)

        self.name_place = Label(text= user.get_name(), font=("Arial", 14), fg='blue', background="#dea5a4")
        self.name_place.place(x=450, y=230)


        y = 270
        # Making the role label
        self.role_label = Label(text="Role:", font=("Arial", 14), background="#dea5a4")
        self.role_label.place(x=330, y=y)

        self.role_label_place = Label(text= user.get_is_seller(), font=("Arial", 14), fg='blue', background="#dea5a4")
        self.role_label_place.place(x=450, y=y)

        
        y += 50
        # Making contract button
        self.contract_button = Button(text="Contracts", bg='#d152ff', font=("Arial", 14), fg='black', width="20",
                                      command=lambda: self.controller.contracts_btn(self))
        self.contract_button.place(x=320, y=y)


        y += 50

        btn_label = 'All Open Bids'
        if user.get_is_seller() == 'Seller':
            btn_label = 'My Open Bids'

        self.student_bids_button = Button(text=btn_label, bg='#7331F7', font=("Arial", 14),
                                            fg='black', width="20",
                                            command=lambda: self.controller.bids_list_btn(self))
        self.student_bids_button.place(x=320, y=y)


        # Make logout button
        y += 50
        self.bid_button = Button(text="Log out", bg='#aec6cf', font=("Arial", 14), fg='black', width="20",
                                 command=lambda: self.controller.log_out_btn(self))
        self.bid_button.place(x=320, y=y)
       
        self.root.mainloop()

def get_date(self):
    # Retrieve selected date from the calendar
    selected_date = Calendar.get_date(self)
    print("Selected Date:", selected_date)
    return selected_date

class CreateBidView2(Page):
    def __init__(self, controller, user, type_bid):
        self.user = user
        super().__init__(controller)
        
        self.label = Label(self.root, text="Create New Bid", fg='#5c3f8f', font=("Arial", 25), justify=CENTER,
                           background="#dea5a4")
        self.label.place(x=250, y=20)

        self.label = Label(self.root, text="Please fill in all the information below", fg='black', font=("Arial", 15),
                           justify=CENTER,
                           background="#dea5a4")
        self.label.place(x=220, y=70)

        x = 70
        y = 135

        # Subject name label
        self.item_name_label = Label(text="Product name: ", font=("Arial", 14), background="#dea5a4")
        self.item_name_label.place(x=x, y=y)

        # Making the subject entry
        x += 130
        self.item_name = Entry(font=("Arial", 12), width=40)
        self.item_name.place(x=x, y=y)

        x -= 130
        y += 40
        # Subject description label
        self.item_description_label = Label(text="Product description: ", font=("Arial", 14), background="#dea5a4")
        self.item_description_label.place(x=x, y=y)

        x += 130
        # Making the subject description entry
        self.item_description = Entry(font=("Arial", 12), width=60)
        self.item_description.place(x=x, y=y)


        x -= 130
        y += 40
        # Subject description label
        self.quantity_label = Label(text="Quantity: ", font=("Arial", 14), background="#dea5a4")
        self.quantity_label.place(x=x, y=y)

        x += 130
        # Making the subject description entry
        self.quantity = Entry(font=("Arial", 12), width=20)
        self.quantity.place(x=x, y=y)

        x -= 130
        y += 40
        # Subject description label
        self.amount_label = Label(text="Amount: ", font=("Arial", 14), background="#dea5a4")
        self.amount_label.place(x=x, y=y)

        x += 130
        # Making the subject description entry
        self.amount = Entry(font=("Arial", 12), width=20)
        self.amount.place(x=x, y=y)
        

        y += 40
        x -= 130
        self.calendar_label = Label(text="Bid Closing Date:", font=("Arial", 14), background="#dea5a4")
        self.calendar_label.place(x=x, y=y)
        
        x += 130
        today = datetime.today()
        self.calendar = Calendar(self.root, selectmode='day', date_pattern='y, mm, dd', year=today.year, month=today.month, day=today.day, selectforeground='red', foreground='red')
        self.calendar.place(x=x, y=y)


        x -= 70
        y += 200
        self.submit_button = Button(text="Submit", bg="#BFA2F7", font=("Arial", 14), fg='black', width="20",
                                    command=lambda: self.controller.submit_form(
                                        self.item_name.get(), 
                                        self.item_description.get(), 
                                        self.quantity.get(), 
                                        self.amount.get(),
                                        self.user.get_id(),
                                        get_date(self.calendar),
                                        self))
        self.submit_button.place(x=x, y=y)

        x += 200
        # Creating close bid button
        self.cancel_bid_button = Button(text="Cancel", bg="#ff6961", font=("Arial", 14), fg='black', width="20",
                                        command=lambda: self.controller.cancel_btn(self))
        self.cancel_bid_button.place(x=x, y=y)
        
        self.root.mainloop()

    def next_click(self):
        # Picking time

        # preferred Day

        self.day = [None] * int(self.ses_per_week.get())
        self.day_label = [None] * int(self.ses_per_week.get())
        self.time_hour = [None] * int(self.ses_per_week.get())
        self.time_min = [None] * int(self.ses_per_week.get())
        self.time_label = [None] * int(self.ses_per_week.get())
        y = 575
        for i in range(int(self.ses_per_week.get())):
            # Day
            self.day_label[i] = Label(text="Preferred day " + str(i + 1) + ": ", font=("Arial", 14),
                                      background="#dea5a4",
                                      justify=LEFT)
            self.day_label[i].place(x=70, y=y)
            self.day[i] = Entry(font=("Arial", 12), width=30)
            self.day[i].place(x=220, y=y + 5)

            # Time
            self.time_label[i] = Label(text="Time: ", font=("Arial", 14),
                                       background="#dea5a4",
                                       justify=LEFT)
            self.time_label[i].place(x=500, y=y)

            self.time_label_extra = Label(text=":", font=("Arial", 14),
                                          background="#dea5a4",
                                          justify=LEFT)
            self.time_label_extra.place(x=595, y=y)
            hour_string = StringVar()
            min_string = StringVar()
            last_value_sec = ""
            last_value = ""

            self.time_min[i] = Spinbox(
                from_=0,
                to=59,
                wrap=True,
                textvariable=min_string,
                font=("Arial", 12),
                width=2,
                justify=CENTER
            )

            self.time_hour[i] = Spinbox(from_=0,
                                        to=23,
                                        wrap=True,
                                        textvariable=hour_string,
                                        width=2,
                                        state="readonly",
                                        font=("Arial", 12),
                                        justify=CENTER
                                        )

            # Time configuration
            if last_value == "59" and min_string.get() == "0":
                hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
                last_value = min_string.get()

            if last_value_sec == "59" and self.time_min[i].get() == "0":
                min_string.set(int(min_string.get()) + 1 if min_string.get() != "59" else 0)
            if last_value == "59":
                hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
            self.time_hour[i].place(x=560, y=y + 5)
            self.time_min[i].place(x=610, y=y + 5)
            y += 35

        # preferred rate
        self.rate_label = Label(text="Preferred rate: ", font=("Arial", 14),
                                background="#dea5a4",
                                justify=LEFT)
        self.rate_label.place(x=70, y=y)
        self.rate = Entry(font=("Arial", 12), width=40)
        self.rate.place(x=200, y=y + 5)

        # Drop down list
        self.rate_per = StringVar(self.root)
        self.rate_per.set("per session")  # default value

        w = OptionMenu(self.root, self.rate_per, "per hour", "per session")
        w.place(x=590, y=y)

        # Contract length
        y += 35
        self.customise_option_label = Label(text="Customise \nContract Length: ", font=("Arial", 14),
                                            background="#dea5a4",
                                            justify=LEFT)

        self.customise_option_label.place(x=70, y=y)

        self.customise_option = BooleanVar()
        self.customise_option_yes = Radiobutton(self.root, text='Yes', variable=self.customise_option, value=True)
        self.customise_option_yes.place(x=240, y=y + 25)
        self.customise_option_no = Radiobutton(self.root, text='No', variable=self.customise_option, value=False)
        self.customise_option_no.place(x=300, y=y + 25)

        self.contract_length_label = Label(text="Contract Length: ", font=("Arial", 14),
                                           background="#dea5a4",
                                           justify=LEFT)
        self.contract_length_label.place(x=360, y=y + 25)
        # Drop down list
        self.contract_length = StringVar(self.root)
        self.contract_length.set(6)  # default value

        contract_list = OptionMenu(self.root, self.contract_length, 3, 6, 12, 24, 36, 48)
        contract_list.place(x=530, y=y + 25)

        self.months_label = Label(text="Months", font=("Arial", 14),
                                  background="#dea5a4",
                                  justify=LEFT)
        self.months_label.place(x=590, y=y + 25)

        y += 60
        # Creating submit button

        bid_info = {
            "subjectName": self.subject_name.get(),
            "subjectDescription": self.subject_description.get(),
            "subjectLevel": self.subject_level.get(),
            "qualificationTitle": self.qualification_title.get()
        }

        lesson_info = {
            "sesPerWeek": self.ses_per_week.get(),
            "hoursPerLes": self.hours_per_lesson.get(),
            "day": self.day,
            "timeHour": self.time_hour,
            "timeMin": self.time_min,
            "rate": self.rate,
            "rateType": self.rate_per,
            "customContract": self.customise_option,
            "contractLen": self.contract_length
        }

        self.submit_button = Button(text="Submit", bg="#BFA2F7", font=("Arial", 14), fg='black', width="20",
                                    command=lambda: self.controller.submit_form(bid_info, lesson_info, self, ))
        self.submit_button.place(x=400, y=y)

        # Creating close bid button
        self.cancel_bid_button = Button(text="Cancel", bg="#ff6961", font=("Arial", 14), fg='black', width="20",
                                        command=lambda: self.controller.cancel_btn(self))
        self.cancel_bid_button.place(x=100, y=y)

class BidsList2View(ScrollablePage):
    def __init__(self, controller, bids, user):
        super().__init__(controller)

        header_frame = Frame(self.scroll.frame, bg='#dea5a4')
        header_frame.grid(row=0, column=0, columnspan=10, padx=(10, 10), pady=(10, 10), sticky="ew")

        # Add Back button in the header frame
        self.back_button = Button(header_frame, text="Back", bg='#aec6cf', font=("Arial", 14), fg='black',
                                width=10,
                                command=lambda: self.controller.back_btn(self))
        self.back_button.grid(row=0, column=0, padx=5, sticky="w")

        # Add Available Bids label in the header frame
        self.label = Label(header_frame, text="Available Bids", fg='#5c3f8f', bg='#f244aa', font=("Arial", 25),
                               justify=CENTER,
                               background="#dea5a4").grid(row=0, column=2, pady=20, padx=53, sticky="W")

        # Add Create New Bid button only if the user is a seller
        if user.get_is_seller() == 'Seller':
            self.bid_button = Button(header_frame, text="Create New Bid", bg='#f244aa', font=("Arial", 14), fg='black',
                                    command=lambda: self.controller.create_bid_btn(self))
            self.bid_button.grid(row=0, column=4, padx=5, sticky="e")

        self.bids = bids

        total_rows = len(self.bids)
        row = 4

        header_frame2 = Frame(self.scroll.frame, bg='red')
        header_frame2.grid(row=row, column=0, columnspan=10, padx=(10, 10),pady=(10, 10), sticky="ew")

        column = 0
        Label(header_frame2, text='Sr no', relief=RIDGE, width=5, background='grey', fg='white', justify=LEFT).grid(row= row, column=column, sticky=NSEW)
        
        column = column + 1
        Label(header_frame2, text='Product', relief=RIDGE, background='grey', fg='white',  width=25, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        
        column = column + 1
        Label(header_frame2, text='Seller', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column = column, sticky=NSEW)
        
        column = column + 1
        Label(header_frame2, text='Quantity', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        
        column = column + 1
        Label(header_frame2, text='Created On', relief=RIDGE, background='grey', fg='white',  width=15, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        
        column = column + 1
        Label(header_frame2, text='Bid Close Date', relief=RIDGE, background='grey', fg='white',  width=15, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        
        column = column + 1
        Label(header_frame2, text='Status', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        
        if user.get_is_seller() == 'Buyer':
            column = column + 1
            Label(header_frame2, text='Accept', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)

        column = column + 1
        Label(header_frame2, text='Description', relief=RIDGE, background='grey', fg='white',  width=30, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        
        
        row = 5
        for i in range(total_rows):
            column = 0
            Label(header_frame2, text=i+1, relief=RIDGE,  width=5, justify=LEFT).grid(row= row+i, column=column, sticky=NSEW)
            
            column = column + 1
            Label(header_frame2, text=bids[i]['item'], relief=RIDGE,  width=25, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            
            column = column + 1
            Label(header_frame2, text=bids[i]['seller'], relief=RIDGE,  width=10, justify=LEFT).grid(row = row+i, column = column, sticky=NSEW)
            
            column = column + 1
            Label(header_frame2, text=bids[i]['quantity'], relief=RIDGE,  width=10, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            
            column = column + 1
            date_created = ''
            if bids[i]['date_created'] is not None:
                date_created = bids[i]['date_created'].strftime("%B %d, %Y")

            Label(header_frame2, text=date_created, relief=RIDGE,  width=15, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            
            column = column + 1
            close_date = ''
            if bids[i]['date_closed'] is not None:
                close_date = bids[i]['date_closed'].strftime("%B %d, %Y")
            Label(header_frame2, text=close_date, relief=RIDGE,  width=15, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            
            column = column + 1
            Label(header_frame2, text=bids[i]['status'], relief=RIDGE,  width=10, justify=LEFT, fg='green').grid(row = row+i, column= column, sticky=NSEW)
            
            if user.get_is_seller() == 'Buyer':
                column = column + 1
                Button(header_frame2, text="Accept", bg='#aec6cf', font=("Arial", 14), fg='green',
                                  command=lambda selected_bid=bids[i]: self.controller.approve_bid_btn(self, selected_bid)).grid(row=row+i, column=column, sticky=NSEW)
       
            column = column + 1
            Label(header_frame2, text=bids[i]['description'], relief=RIDGE,  width=30, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            

        self.root.mainloop()

class ContractsList2View(ScrollablePage):
    def __init__(self, controller, contracts):
        super().__init__(controller)
        self.contracts = contracts
        
        header_frame = Frame(self.scroll.frame, bg='#dea5a4')
        header_frame.grid(row=0, column=0, columnspan=10, padx=(10, 10), pady=(10, 10), sticky="ew")

        # Add Back button in the header frame
        self.back_button = Button(header_frame, text="Back", bg='#aec6cf', font=("Arial", 14), fg='black',
                                width=10,
                                command=lambda: self.controller.back_btn(self))
        self.back_button.grid(row=0, column=0, padx=5, sticky="w")

        # Add Available Bids label in the header frame
        self.label = Label(header_frame, text="Contracts", fg='#5c3f8f', bg='#f244aa', font=("Arial", 25),
                               justify=CENTER,
                               background="#dea5a4").grid(row=0, column=2, pady=20, padx=300, sticky="W")
        
        self.show_contracts(self.contracts)

    def show_contracts(self, contracts):
        self.contracts = contracts
        # printing buttons for each bid on the screen
        row = 2
        total_rows = len(self.contracts)
        row = 3
        column = 2
        Label(self.scroll.frame, text='Sr no', relief=RIDGE, background='grey', fg='white',  width=5, justify=LEFT).grid(row= row, column=column, sticky=NSEW)
        column = column + 1
        Label(self.scroll.frame, text='Seller', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column = column, sticky=NSEW)
        column = column + 1
        Label(self.scroll.frame, text='Buyer', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        column = column + 1
        Label(self.scroll.frame, text='Product', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        column = column + 1
        Label(self.scroll.frame, text='Description', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        column = column + 1
        Label(self.scroll.frame, text='Quantity', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        column = column + 1
        Label(self.scroll.frame, text='Amount', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        column = column + 1
        Label(self.scroll.frame, text='Created On', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        column = column + 1
        Label(self.scroll.frame, text='Signed On', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        column = column + 1
        Label(self.scroll.frame, text='Status', relief=RIDGE, background='grey', fg='white',  width=10, justify=LEFT).grid(row = row, column= column, sticky=NSEW)
        
        row = 4
        for i in range(total_rows):
            column = 2
            Label(self.scroll.frame, text=i+1, relief=RIDGE,  width=5, justify=LEFT).grid(row= row+i, column=column, sticky=NSEW)
            column = column + 1
            Label(self.scroll.frame, text=contracts[i]['seller'], relief=RIDGE,  width=10, justify=LEFT).grid(row = row+i, column = column, sticky=NSEW)
            column = column + 1
            Label(self.scroll.frame, text=contracts[i]['buyer'], relief=RIDGE,  width=10, justify=LEFT).grid(row = row+i, column = column, sticky=NSEW)
            column = column + 1
            Label(self.scroll.frame, text=contracts[i]['item'], relief=RIDGE,  width=10, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            column = column + 1
            Label(self.scroll.frame, text=contracts[i]['description'], relief=RIDGE,  width=10, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            column = column + 1
            Label(self.scroll.frame, text=contracts[i]['quantity'], relief=RIDGE,  width=10, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            column = column + 1
            Label(self.scroll.frame, text=contracts[i]['amount'], relief=RIDGE,  width=10, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            column = column + 1
            Label(self.scroll.frame, text=contracts[i]['bid_date_created'].strftime("%B %d, %Y"), relief=RIDGE,  width=15, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            column = column + 1
            Label(self.scroll.frame, text=contracts[i]['date_signed'].strftime("%B %d, %Y"), relief=RIDGE,  width=15, justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            column = column + 1
            Label(self.scroll.frame, text=contracts[i]['contract_status'], relief=RIDGE,  width=10,  fg='green', justify=LEFT).grid(row = row+i, column= column, sticky=NSEW)
            

        self.root.mainloop()

