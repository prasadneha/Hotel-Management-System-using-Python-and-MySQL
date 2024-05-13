from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_Win
from room import RoomBooking
from details import DetailsRoom
class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

#First Image
        img1=Image.open("hotel1.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=1550,height=140)

#Logo
        img2=Image.open(r"LOGO2.png")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

#Title
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman", 40," bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

    #Main frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

    #menuu
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

    #btn frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22)
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame,command=self.room_booking, text="ROOM", font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0,width=22,cursor="hand1")
        room_btn.grid(row=1, column=0,pady=1)

        details_btn = Button(btn_frame,command=self.details_room, text="DETAILS", font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0,width=22)
        details_btn.grid(row=2, column=0,pady=1)

        report_btn = Button(btn_frame, text="REPORT", font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0,width=22)
        report_btn.grid(row=3, column=0,pady=1)

        logout_btn = Button(btn_frame,command=self.logout, text="LOG OUT", font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0,width=22)
        logout_btn.grid(row=4, column=0,pady=1)

        #right side image
        img3 = Image.open(r"hotel3.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1310, height=590)

        #down images
        img4 = Image.open(r"hotel5.jpeg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"hotel4.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=420, width=230, height=190)
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def room_booking(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)
    def logout(self):
        self.root.destroy()

if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
