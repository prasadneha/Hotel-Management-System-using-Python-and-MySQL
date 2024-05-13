from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")
    #####Variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()

        #customer details
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, " bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open(r"LOGO2.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=3, width=100, height=40)

        #lABEL FRAME
        lbl_frame_left=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman", 12, " bold"))
        lbl_frame_left.place(x=5,y=50,width=425,height=490)

        #lbels and entrys
        #customerref
        lbl_cust_ref=Label(lbl_frame_left,text="Customer Ref",font=("arial", 12, " bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky="w")

        entry_ref=ttk.Entry(lbl_frame_left,textvariable=self.var_ref,width=29,font=("arial", 13, " bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #cust_name
        lbl_cust_ref = Label(lbl_frame_left, text="Customer Name", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=1, column=0, sticky="w")

        entry_ref = ttk.Entry(lbl_frame_left,textvariable=self.var_cust_name, width=29, font=("arial", 13, " bold"))
        entry_ref.grid(row=1, column=1)

        #Mother's name
        lbl_cust_ref = Label(lbl_frame_left, text="Mother's Name", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=2, column=0, sticky="w")

        entry_ref = ttk.Entry(lbl_frame_left,textvariable=self.var_mother, width=29, font=("arial", 13, " bold"))
        entry_ref.grid(row=2, column=1)

        #gender combobox
        lbl_cust_ref = Label(lbl_frame_left, text="Gender", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=3, column=0, sticky="w")
        combo_gender=ttk.Combobox(lbl_frame_left,textvariable=self.var_gender,font=("arial", 12, " bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)



        #postcode

        lbl_cust_ref = Label(lbl_frame_left, text="Postcode:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=4, column=0, sticky="w")

        entry_ref = ttk.Entry(lbl_frame_left,textvariable=self.var_post, width=29, font=("arial", 13, " bold"))
        entry_ref.grid(row=4, column=1)

        #mobile Number

        lbl_cust_ref = Label(lbl_frame_left, text="Mobile Num:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=5, column=0, sticky="w")

        entry_ref = ttk.Entry(lbl_frame_left,textvariable=self.var_mobile, width=29, font=("arial", 13, " bold"))
        entry_ref.grid(row=5, column=1)

        #email

        lbl_cust_ref = Label(lbl_frame_left, text="E-mail:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=6, column=0, sticky="w")

        entry_ref = ttk.Entry(lbl_frame_left,textvariable=self.var_email, width=29, font=("arial", 13, " bold"))
        entry_ref.grid(row=6, column=1)

        #nationality

        lbl_cust_ref = Label(lbl_frame_left, text="Nationality:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=7, column=0, sticky="w")

        combo_natio = ttk.Combobox(lbl_frame_left,textvariable=self.var_nationality, font=("arial", 12, " bold"), width=27, state="readonly")
        combo_natio["value"] = ("Indian", "American", "Britist")
        combo_natio.current(0)
        combo_natio.grid(row=7, column=1)

        #idproof type combobox

        lbl_cust_ref = Label(lbl_frame_left, text="Id Proof Type:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=8, column=0, sticky="w")

        combo_idproof = ttk.Combobox(lbl_frame_left,textvariable=self.var_id_proof, font=("arial", 12, " bold"), width=27, state="readonly")
        combo_idproof["value"] = ("Adhar Card", "Driving Licence", "Passport","Ration Card")
        combo_idproof.current(0)
        combo_idproof.grid(row=8, column=1)

        #id number

        lbl_cust_ref = Label(lbl_frame_left, text="Id Number:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=9, column=0, sticky="w")

        entry_ref = ttk.Entry(lbl_frame_left,textvariable=self.var_id_number, width=29, font=("arial", 13, " bold"))
        entry_ref.grid(row=9, column=1)

        #address

        lbl_cust_ref = Label(lbl_frame_left, text="Address:", font=("arial", 12, " bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=10, column=0, sticky="w")

        entry_ref = ttk.Entry(lbl_frame_left,textvariable=self.var_address, width=29, font=("arial", 13, " bold"))
        entry_ref.grid(row=10, column=1)

        #Button
        btn_frame=Frame(lbl_frame_left,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.addData,font=("arial", 12, " bold"),bg="black",fg="gold",width=9)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update = Button(btn_frame,command=self.update ,text="Update", font=("arial", 12, " bold"), bg="black", fg="gold", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        btn_reset = Button(btn_frame,command=self.reset, text="Reset", font=("arial", 12, " bold"), bg="black", fg="gold", width=9)
        btn_reset.grid(row=0, column=2, padx=1)

        btn_del = Button(btn_frame,command=self.delete, text="Delete", font=("arial", 12, " bold"), bg="black", fg="gold", width=9)
        btn_del.grid(row=0, column=3, padx=1)

      #table frame
        table_frame = LabelFrame(self.root, text="View Details and Search System", font=("times new roman", 12, " bold"),fg="black", bd=4, relief=RIDGE)
        table_frame.place(x=435, y=50, width=860, height=490)

        lbl_search_by = Label(table_frame, text="Search By", font=("arial", 12, " bold"), bg="red", fg="white")
        lbl_search_by.grid(row=0, column=0, sticky="w",padx=2)

        self.search_var=StringVar()

        combo_search = ttk.Combobox(table_frame,textvariable=self.search_var, font=("arial", 12, " bold"), width=24, state="readonly")
        combo_search["value"] = ("mobile", "ref", "Room No")
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()

        sreachtxt = ttk.Entry(table_frame,textvariable=self.txt_search, width=24, font=("arial", 13, " bold"))
        sreachtxt.grid(row=0, column=2,padx=2)

        btn_search = Button(table_frame,command=self.search, text="Search", font=("arial", 12, " bold"), bg="black", fg="gold", width=9)
        btn_search.grid(row=0, column=3, padx=1)

        btn_show_all= Button(table_frame,command=self.fetch_data, text="Show All", font=("arial", 12, " bold"), bg="black", fg="gold", width=9)
        btn_show_all.grid(row=0, column=4, padx=1)

        #Show Data Table
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","postcode","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref",text="Ref No.")
        self.cust_details_table.heading("name", text="Name")
        self.cust_details_table.heading("mother", text="Mother's Name")
        self.cust_details_table.heading("gender", text="Gender")
        self.cust_details_table.heading("postcode", text="PostCode")
        self.cust_details_table.heading("mobile", text="Mobile")
        self.cust_details_table.heading("email", text="E-mail")
        self.cust_details_table.heading("nationality", text="Nationality")
        self.cust_details_table.heading("idproof", text="Id Proof")
        self.cust_details_table.heading("idnumber", text="Id Number")
        self.cust_details_table.heading("address", text="Address")

        self.cust_details_table["show"]="headings"

        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name", width=100)
        self.cust_details_table.column("mother", width=100)
        self.cust_details_table.column("gender", width=100)
        self.cust_details_table.column("postcode", width=100)
        self.cust_details_table.column("mobile", width=100)
        self.cust_details_table.column("email", width=100)
        self.cust_details_table.column("nationality", width=100)
        self.cust_details_table.column("idproof", width=100)
        self.cust_details_table.column("idnumber", width=100)
        self.cust_details_table.column("address", width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def addData(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Neha39",database="Management")
                my_curser=conn.cursor()
                my_curser.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),self.var_cust_name.get(),self.var_mother.get(),
                    self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),
                    self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),
                    self.var_id_number.get(),self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added successfully",parent=self.root)
            except Exception as e:
                messagebox.showwarning("warning",f"Something went wrong:{str(e)}",parent=self.root)
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
        my_curser = conn.cursor()
        my_curser.execute("select * from customer")
        rows=my_curser.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    def get_cursor(self,event):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
            my_curser = conn.cursor()
            my_curser.execute("update customer set name=%s,mother=%s,gender=%s,postcode=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(
                 self.var_cust_name.get(), self.var_mother.get(),
                self.var_gender.get(), self.var_post.get(), self.var_mobile.get(),
                self.var_email.get(), self.var_nationality.get(), self.var_id_proof.get(),
                self.var_id_number.get(), self.var_address.get(),self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully.",parent=self.root)
    def delete(self):
        delete=messagebox.askquestion("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if delete:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
            my_curser = conn.cursor()
            #another methhod to run query
            query="delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_curser.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@Neha39", database="Management")
        my_curser = conn.cursor()
        my_curser.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_curser.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()





if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
