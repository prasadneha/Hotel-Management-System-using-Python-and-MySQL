from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from time import strftime
from datetime import datetime
import random
import mysql.connector
from tkinter import messagebox
class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")

        #Vasriablessss
        self.var_contact=StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        lbl_title = Label(self.root, text="ROOM BOOKING", font=("times new roman", 18, " bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open(r"LOGO2.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=3, width=100, height=40)

        lbl_frame_left = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking", padx=2,
                                    font=("times new roman", 12, " bold"))
        lbl_frame_left.place(x=5, y=50, width=425, height=490)

        #Label and Entrys
#customer contact

        lbl_cust_contact = Label(lbl_frame_left, text="Contact No.:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky="w")

        entry_contact = ttk.Entry(lbl_frame_left,textvariable=self.var_contact, width=20, font=("arial", 13, " bold"))
        entry_contact.grid(row=0, column=1,sticky="w")

        #fetch data button
        btn_fetchData = Button(lbl_frame_left,command=self.fetchContactData, text="Fetch Data", font=("arial", 8, " bold"), bg="black",
                            fg="gold", width=8)
        btn_fetchData.place(x=335,y=4)

        #bill button
        btn_bill = Button(lbl_frame_left,command=self.total, text="Bill", font=("arial", 12, " bold"), bg="black",
                         fg="gold", width=9)
        btn_bill.grid(row=10, column=0, padx=1,sticky="w")

        # Button
        btn_frame = Frame(lbl_frame_left, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btn_add = Button(btn_frame,command=self.addData, text="Add", font=("arial", 12, " bold"), bg="black",
                         fg="gold", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame,command=self.update, text="Update", font=("arial", 12, " bold"), bg="black",
                            fg="gold", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        btn_reset = Button(btn_frame,command=self.reset, text="Reset", font=("arial", 12, " bold"), bg="black",
                           fg="gold", width=9)
        btn_reset.grid(row=0, column=2, padx=1)

        btn_del = Button(btn_frame,command=self.delete,text="Delete", font=("arial", 12, " bold"), bg="black",
                         fg="gold", width=9)
        btn_del.grid(row=0, column=3, padx=1)


#Check in data
        check_in_date = Label(lbl_frame_left, text="Check_in Date:", font=("arial", 12, " bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky="w")

        txt_check_in_Date = ttk.Entry(lbl_frame_left,textvariable=self.var_checkin, width=29, font=("arial", 13, " bold"))
        txt_check_in_Date.grid(row=1, column=1)

    #check ou data
        lbl_check_out_date = Label(lbl_frame_left, text="Check_out Date:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_check_out_date.grid(row=2, column=0, sticky="w")

        txt_check_out_date = ttk.Entry(lbl_frame_left,textvariable=self.var_checkout, width=29, font=("arial", 13, " bold"))
        txt_check_out_date.grid(row=2, column=1)

    #Room type
        lbl_room_type = Label(lbl_frame_left, text="Room Type:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_room_type.grid(row=3, column=0, sticky="w")

        conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
        my_curser = conn.cursor()
        my_curser.execute("select Room_Type from details")
        ide = my_curser.fetchall()


        combo_roomType = ttk.Combobox(lbl_frame_left,textvariable=self.var_roomtype, font=("arial", 12, " bold"), width=27,
                                    state="readonly")
        # combo_roomType["value"] =ide
        # combo_roomType.current(0)
        if ide:
            combo_roomType["value"] = ide
            combo_roomType.current(0)
        else:
            combo_roomType["value"] = ["No Room Types Available"]  # Set a default message if no values are found


        combo_roomType.grid(row=3, column=1)

    #Available room
        lbl_availableRoom = Label(lbl_frame_left, text="Available room:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_availableRoom.grid(row=4, column=0, sticky="w")

        # entry_avail_room = ttk.Entry(lbl_frame_left,textvariable=self.var_roomavailable, width=29, font=("arial", 13, " bold"))
        # entry_avail_room.grid(row=4, column=1)
        conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
        my_curser = conn.cursor()
        my_curser.execute("select Room_No from details")
        rows=my_curser.fetchall()

        combo_roomNo = ttk.Combobox(lbl_frame_left, textvariable=self.var_roomavailable, font=("arial", 12, " bold"),
                                      width=27,
                                      state="readonly")
        combo_roomNo["value"] = rows
        combo_roomNo.grid(row=4, column=1)

    #Meal
        lbl_meal = Label(lbl_frame_left, text="Meal:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky="w")

        entry_meal = ttk.Entry(lbl_frame_left,textvariable=self.var_meal, width=29, font=("arial", 13, " bold"))
        entry_meal.grid(row=5, column=1)

    #no of days
        lbl_no_of_days = Label(lbl_frame_left, text="No of Days:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_no_of_days.grid(row=6, column=0, sticky="w")

        entry_no_of_days = ttk.Entry(lbl_frame_left,textvariable=self.var_noofdays, width=29, font=("arial", 13, " bold"))
        entry_no_of_days.grid(row=6, column=1)

    #Paid tax
        lbl_paidtax = Label(lbl_frame_left, text="Paid Tax:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_paidtax.grid(row=7, column=0, sticky="w")

        entry_paidTax = ttk.Entry(lbl_frame_left,textvariable=self.var_paidtax, width=29, font=("arial", 13, " bold"))
        entry_paidTax.grid(row=7, column=1)

    #sub total
        lbl_subTotal = Label(lbl_frame_left, text="Sub Total:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_subTotal.grid(row=8, column=0, sticky="w")

        entry_subTotal = ttk.Entry(lbl_frame_left,textvariable=self.var_actualtotal, width=29, font=("arial", 13, " bold"))
        entry_subTotal.grid(row=8, column=1)

    #total cost
        lbl_totalCost = Label(lbl_frame_left, text="Total cost:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_totalCost.grid(row=9, column=0, sticky="w")

        entry_totalCost = ttk.Entry(lbl_frame_left,textvariable=self.var_total, width=29, font=("arial", 13, " bold"))
        entry_totalCost.grid(row=9, column=1)

        #right side image
        img3 = Image.open(r"hotelin.jpg")
        img3 = img3.resize((550, 250), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=550, height=250)

        #table frame
        table_frame = LabelFrame(self.root, text="View Details and Search System", font=("times new roman", 12, " bold"),
                                 fg="black", bd=4, relief=RIDGE)
        table_frame.place(x=435, y=280, width=860, height=260)

        lbl_search_by = Label(table_frame, text="Search By", font=("arial", 12, " bold"), bg="red", fg="white")
        lbl_search_by.grid(row=0, column=0, sticky="w", padx=2)

        self.search_var = StringVar()

        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, " bold"), width=24,
                                    state="readonly")
        combo_search["value"] = ("contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()

        sreachtxt = ttk.Entry(table_frame, textvariable=self.txt_search, width=24, font=("arial", 13, " bold"))
        sreachtxt.grid(row=0, column=2, padx=2)

        btn_search = Button(table_frame,command=self.search, text="Search", font=("arial", 12, " bold"), bg="black",
                            fg="gold", width=9)
        btn_search.grid(row=0, column=3, padx=1)

        btn_show_all = Button(table_frame,command=self.fetch_data, text="Show All", font=("arial", 12, " bold"),
                              bg="black", fg="gold", width=9)
        btn_show_all.grid(row=0, column=4, padx=1)

        # Show Data Table
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=(
        "contact", "check_in_date", "check_out_date", "roomType", "Room", "meal", "noOfDays", "paidTax", "subTotal", "totalCost",
        "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("check_in_date", text="Check-in")
        self.room_table.heading("check_out_date", text="Check-out")
        self.room_table.heading("roomType", text="Room Type")
        self.room_table.heading("Room", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfDays", text="NoOfDays")


        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("check_in_date", width=100)
        self.room_table.column("check_out_date", width=100)
        self.room_table.column("roomType", width=100)
        self.room_table.column("Room", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfDays", width=100)


        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

#add Data
    def addData(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Neha39",database="Management")
                my_curser=conn.cursor()
                my_curser.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                    self.var_contact.get(),
                                    self.var_checkin.get(),
                                    self.var_checkout.get(),
                                    self.var_roomtype.get(),
                                    self.var_roomavailable.get(),
                                    self.var_meal.get(),
                                    self.var_noofdays.get(),

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as e:
                messagebox.showwarning("warning",f"Something went wrong:{str(e)}",parent=self.root)

   #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
        my_curser = conn.cursor()
        my_curser.execute("select * from room")
        rows = my_curser.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
            conn.close()
    #get cursor #to automatically fill the data by clicking on the row in table
    def get_cursor(self,event):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

        #update function

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
            my_curser = conn.cursor()
            my_curser.execute(
                "update room set check_in_date=%s,check_out_date=%s,roomType=%s,Room=%s,meal=%s,noOfDays=%s where contact=%s",
                (
                    self.var_checkin.get(), self.var_checkout.get(),
                    self.var_roomtype.get(), self.var_roomavailable.get(), self.var_meal.get(),
                    self.var_noofdays.get(), self.var_contact.get()
                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details has been updated successfully.", parent=self.root)

    #Delete
    def delete(self):
        delete = messagebox.askquestion("Hotel Management System", "Do you want to this room details",
                                        parent=self.root)
        if delete:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
            my_curser = conn.cursor()
            # another methhod to run query
            query = "delete from room where contact=%s"
            value = (self.var_contact.get(),)
            my_curser.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    #all data fetch
    def fetchContactData(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number.",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
            my_curser = conn.cursor()
            query="select name from customer where mobile=%s"
            value=(self.var_contact.get(),)
            my_curser.execute(query,value)
            row=my_curser.fetchone()
            if row == None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)


                lblname=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                lblname.place(x=0,y=0)


                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                my_curser.close()
               #Gender
                conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39",
                                               database="Management")
                my_curser = conn.cursor()
                query = "select gender from customer where mobile=%s"
                value = (self.var_contact.get(),)
                my_curser.execute(query, value)
                row = my_curser.fetchone()


                lblgender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                lblgender.place(x=0,y=30)


                lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)
                my_curser.close()
                #Email
                conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39",
                                               database="Management")
                my_curser = conn.cursor()
                query = "select email from customer where mobile=%s"
                value = (self.var_contact.get(),)
                my_curser.execute(query, value)
                row = my_curser.fetchone()

                lblemail = Label(showDataFrame, text="E-mail:", font=("arial", 12, "bold"))
                lblemail.place(x=0, y=60)

                lbl3 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=60)
                my_curser.close()

                #nationality

                conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39",
                                               database="Management")
                my_curser = conn.cursor()
                query = "select nationality from customer where mobile = %s "
                value = (self.var_contact.get(),)
                my_curser.execute(query, value)
                row = my_curser.fetchone()

                lblnation = Label(showDataFrame, text="Nationality:", font=("arial", 12, "bold"))
                lblnation.place(x=0, y=90)

                lbl4 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=90)
                my_curser.close()

              #address
                conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39",
                                               database="Management")
                my_curser = conn.cursor()
                query = "select address from customer where mobile=%s"
                value = (self.var_contact.get(),)
                my_curser.execute(query, value)
                row = my_curser.fetchone()

                lbladdress = Label(showDataFrame, text="Address:", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=120)

                lbl5 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)

    #Sreach systemm
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
        my_curser = conn.cursor()
        my_curser.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_curser.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def total(self):
        inDate=self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
              q1=float(300)
              q2=float(700)
              q3=float(self.var_noofdays.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              Tax="Rs."+str("%.2f"%((q5)*0.09))
              ST="Rs."+str("%.2f"%((q5)))
              TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))

              self.var_paidtax.set(Tax)
              self.var_actualtotal.set(ST)
              self.var_total.set(TT)
        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
              q1=float(300)
              q2=float(700)
              q3=float(self.var_noofdays.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              Tax="Rs."+str("%.2f"%((q5*0.09)))
              ST="Rs."+str("%.2f"%(q5))
              TT="Rs."+str("%.2f"%(q5+(q5*0.09)))

              self.var_paidtax.set(Tax)
              self.var_actualtotal.set(ST)
              self.var_total.set(TT)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "luxury"):
            q1 = float(500)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5 * 0.09)))
            ST = "Rs." + str("%.2f" % (q5))
            TT = "Rs." + str("%.2f" % (q5 + (q5 * 0.09)))

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)






if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()