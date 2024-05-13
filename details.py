from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from time import strftime
from datetime import datetime
import random
import mysql.connector
from tkinter import messagebox
class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")
    #Title
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, " bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open(r"LOGO2.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=3, width=100, height=40)

         #Labelframe
        lbl_frame_left = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", padx=2,
                                    font=("times new roman", 12, " bold"))
        lbl_frame_left.place(x=5, y=50, width=540, height=350)

        #
        # Floor
        lbl_floor = Label(lbl_frame_left, text="Floor :", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky="w")

        self.var_floor=StringVar()

        entry_floor = ttk.Entry(lbl_frame_left,textvariable=self.var_floor, width=29, font=("arial", 13, " bold"))
        entry_floor.grid(row=0, column=1)

        #Room No
        lbl_RoomNo = Label(lbl_frame_left, text="Room No. :", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky="w")

        self.var_roomNo = StringVar()
        entry_RoomNo = ttk.Entry(lbl_frame_left,textvariable=self.var_roomNo, width=29, font=("arial", 13, " bold"))
        entry_RoomNo.grid(row=1, column=1)

        #Room Type
        lbl_RoomType = Label(lbl_frame_left, text="Room Type :", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky="w")

        self.var_roomType = StringVar()
        entry_RoomType = ttk.Entry(lbl_frame_left,textvariable=self.var_roomType, width=29, font=("arial", 13, " bold"))
        entry_RoomType.grid(row=2, column=1)

        # Button
        btn_frame = Frame(lbl_frame_left, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btn_add = Button(btn_frame,command=self.addData, text="Add", font=("arial", 12, " bold"), bg="black",
                         fg="gold", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame,command=self.update, text="Update", font=("arial", 12, " bold"), bg="black",
                            fg="gold", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        btn_reset = Button(btn_frame,command=self.reset, text="Reset", font=("arial", 12, " bold"), bg="black",
                           fg="gold", width=9)
        btn_reset.grid(row=0, column=2, padx=1)

        btn_del = Button(btn_frame,command=self.delete, text="Delete", font=("arial", 12, " bold"), bg="black",
                         fg="gold", width=9)
        btn_del.grid(row=0, column=3, padx=1)

        #Label Frame

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", padx=2,
                                    font=("times new roman", 12, " bold"))
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        #Table
        self.room_table = ttk.Treeview(Table_Frame, column=(
            "Floor", "Room_No", "Room_Type", "roomType"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor", text="Floor")
        self.room_table.heading("Room_No", text="Room No")
        self.room_table.heading("Room_Type", text="Room Type")


        self.room_table["show"] = "headings"

        self.room_table.column("Floor", width=200)
        self.room_table.column("Room_No", width=200)
        self.room_table.column("Room_Type", width=200)


        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # add Data
    def addData(self):
        if self.var_floor.get() == "" or self.var_roomType.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39",
                                                   database="Management")
                my_curser = conn.cursor()
                my_curser.execute("insert into details values(%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_roomNo.get(),
                    self.var_roomType.get(),


                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New Room Added Successfully", parent=self.root)
            except Exception as e:
                messagebox.showwarning("warning", f"Something went wrong:{str(e)}", parent=self.root)
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
        my_curser = conn.cursor()
        my_curser.execute("select * from details")
        rows = my_curser.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
            conn.close()
        # get cursor #to automatically fill the data by clicking on the row in table

    def get_cursor(self, event):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_roomType.set(row[2])

    #Update
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter floor number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
            my_curser = conn.cursor()
            my_curser.execute(
                "update details set Floor=%s,Room_Type=% where Room_No=%s",
                (
                    self.var_floor.get(), self.var_roomType.get(),
                    self.var_roomNo.get()
                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "New room details has been updated successfully.", parent=self.root)

        # Delete
    def delete(self):
        delete = messagebox.askquestion("Hotel Management System", "Do you want to this room details",
                                            parent=self.root)
        if delete:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39",
                                               database="Management")
            my_curser = conn.cursor()
            # another methhod to run query
            query = "delete from details where Room_No=%s"
            value = (self.var_roomNo.get(),)
            my_curser.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset
    def reset(self):
        self.var_floor.set("")
        self.var_roomNo.set("")
        self.var_roomType.set("")



if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
