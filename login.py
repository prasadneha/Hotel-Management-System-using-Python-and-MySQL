from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import  datetime
import  mysql.connector
from hotel import HotelManagementSystem

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.new_window=None

        self.bg=ImageTk.PhotoImage(file=r"reg1.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"loginnnnn.jpg")
        img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbl_img1.place(x=730,y=175,width=90,height=90)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #Label
        #username
        username=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=185,width=270)

        #password
        password = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        password.place(x=70, y=230)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 20, "bold"))
        self.txtpass.place(x=40, y=260, width=270)

        #Icon imagess
        img2 = Image.open(r"icon1.jpg")
        img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lbl_img2.place(x=650, y=324, width=25, height=25)

        #password icon
        img3 = Image.open(r"icon2.jpg")
        img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lbl_img3.place(x=650, y=399, width=25, height=25)

        #login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman", 20, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button
        registerbtn = Button(frame,command=self.register_window, text="Create New Account", font=("times new roman", 10, "bold"),borderwidth=0, fg="white",
                          bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=20, y=350, width=160)

        #forget password button
        forgetpassbtn = Button(frame,command=self.forget_password, text="Forget Password", font=("times new roman", 10, "bold"),borderwidth=0,fg="white",
                          bg="black", activeforeground="white", activebackground="black")
        forgetpassbtn.place(x=10, y=370, width=160)

#Loginnn
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="neha" and self.txtpass.get()=="prasad":
            messagebox.showinfo("success","Welcome to Neha ki Duniya")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="@Neha39", database="Management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",
                              (
                                  self.txtuser.get(),
                                  self.txtpass.get()
                              ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password ")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #Reset Password*****************
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select Option":
            messagebox.showerror("Error","Select Security Question ",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="@Neha39", database="Management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
               query=("update register set password=%s where email=%s")
               value=(self.txt_newpassword.get(),self.txtuser.get())
               my_cursor.execute(query,value)
               conn.commit()
               conn.close()
               messagebox.showinfo("Info","Your password has been reset ,please login with new password",parent=self.root2)
               self.root2.destroy()


    #Forget Password
    def forget_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="@Neha39", database="Management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman", 20, "bold"),fg="red",bg="white")
                l.place(x=0,y=0,relwidth=1)

                security_q = Label(self.root2, text="Select Security Questions", font=("times new roman", 15, "bold"),
                                   bg="white")
                security_q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,
                                                     font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = (
                "Select Option", "Your Birth Place", "Your Nick Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)
                self.txt_security = ttk.Entry(self.root2,
                                              font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)
                self.txt_newpassword = ttk.Entry(self.root2,font=("times new roman", 15, "bold"))
                self.txt_newpassword.place(x=50, y=250, width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman", 15, "bold"),fg="white",bg="green")
                btn.place(x=100,y=290)




    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #text variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

         #background image
        self.bg=ImageTk.PhotoImage(file=r"reg1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

    #left image
        self.bg1 = ImageTk.PhotoImage(file=r"left.png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

    #Frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE!",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)

        #labels and entrys
        #Row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname.place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        #row 2
        contact = Label(frame, text="Contact No.", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="E-Mail", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        #row 3
        security_q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white")
        security_q.place(x=50, y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select Option","Your Birth Place","Your Nick Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        #row 4
        pswd = Label(frame, text="New Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)
        self.txt_confirm = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_confirm.place(x=370, y=340, width=250)

        #CheckButton
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms & conditions",font=("times new roman", 12, "bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=370)

        #Button
        img=Image.open(r"register1.jpg")
        img=img.resize((200,70),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=40,y=420,width=200)

        img1 = Image.open(r"loginbutton.jpg")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2")
        b2.place(x=330, y=430, width=200)

        #Function Declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select Option":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@Neha39",database="Management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row !=None:
                messagebox.showerror("Error","User already exist.Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                      self.var_fname.get(),
                                      self.var_lname.get(),
                                      self.var_contact.get(),
                                      self.var_email.get(),
                                      self.var_securityQ.get(),
                                      self.var_securityA.get(),
                                      self.var_pass.get()
                                  ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registeration Successful")

    def return_login(self):
        self.root.destroy()
if __name__ == "__main__":
    main()




