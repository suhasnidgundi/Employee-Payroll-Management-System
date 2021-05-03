from tkinter import*
from tkinter import ttk, messagebox
import pymysql

class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("EMPLOYEE PAYROLL MANAGEMENT SYSTEM | DEVELOPED BY SUHAS NIDGUNDI |")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="lightgrey")
        title = Label(self.root, text="Employee Payroll Management System", font=("calibri", 30, "bold"), bg="#262626", fg="white").place(x=0, y=0, relwidth=1)

        # ========================== Frame 1 ============================= #
        # ========================== All Variables ============================= #
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_hr_location = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_proof_id = StringVar()
        self.var_contact = StringVar()
        self.var_status = StringVar()
        self.var_experience = StringVar()

        # ========================== Frame 2 ============================= #
        # ========================== All Variables ============================= #
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_t_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net_salary = StringVar()

        # ========================== Frame 1 ============================= #
        Frame1 = Frame(self.root, bd=3, bg="white", relief=RIDGE)
        Frame1.place(x=10, y=70, width=750, height=620)

        title1 = Label(Frame1, text="Employee Details", font=("comicsans", 20, "bold"), bg="#607d8b", fg="white", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        lbl_code = Label(Frame1, text="Employee Code", font=("times new roman", 20), fg="black", bg="white").place(x=10, y=60)
        txt_code = Entry(Frame1, textvariable=self.var_emp_code, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=220, y=65, width=200)
        btn_code = Button(Frame1, text="Search", activebackground="#2196f3", activeforeground="white", font=("consolos", 15, "bold"), bg="#262626", fg="white", cursor="hand2", bd=0).place(x=440, y=62, height=30, width=100)
        btn_delete = Button(Frame1, text="Delete", activebackground="lightgreen", activeforeground="red", font=("consolos", 15, "bold"), bg="red", fg="white", cursor="hand2", bd=0).place(x=550, y=62, height=30, width=100)
        
        # ========================== Row 1 ============================= #
        lbl_designation = Label(Frame1, text="Designation", font=("times new roman", 20), fg="black", bg="white").place(x=10, y=120)
        txt_designation = Entry(Frame1, textvariable=self.var_designation, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=170, y=130, width=200)

        lbl_dob = Label(Frame1, text="D.O.B", font=("times new roman", 20), fg="black", bg="white").place(x=390, y=120)
        txt_dob = Entry(Frame1, textvariable=self.var_dob, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=520, y=130)

        # ========================== Row 2 ============================= #
        lbl_name = Label(Frame1, text="Name", font=("times new roman", 20), fg="black", bg="white").place(x=10, y=170)
        txt_name = Entry(Frame1, textvariable=self.var_name, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=170, y=175, width=200)

        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 20), fg="black", bg="white").place(x=390, y=170)
        txt_doj = Entry(Frame1, textvariable=self.var_doj, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=520, y=175)

        # ========================== Row 3 ============================= #
        lbl_age = Label(Frame1, text="Age", font=("times new roman", 20), fg="black", bg="white").place(x=10, y=220)
        txt_age = Entry(Frame1, textvariable=self.var_age, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=170, y=225, width=200)

        lbl_experience = Label(Frame1, text="Experience", font=("times new roman", 20), fg="black", bg="white").place(x=390, y=220)
        txt_experience = Entry(Frame1, textvariable=self.var_experience, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=520, y=225)

        # ========================== Row 4 ============================= #
        lbl_gender = Label(Frame1, text="Gender", font=("times new roman", 20), fg="black", bg="white").place(x=10, y=270)
        cmb_gender = ttk.Combobox(Frame1, cursor="hand2", textvariable=self.var_gender, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
        cmb_gender['values'] = ['Male', 'Female']
        cmb_gender.place(x=170, y=275, width=200)

        lbl_proof_id = Label(Frame1, text="Proof ID", font=("times new roman", 20), fg="black", bg="white").place(x=390, y=270)
        cmb_proof_id = ttk.Combobox(Frame1, cursor="hand2", textvariable=self.var_proof_id, font=("calibri", 13, "bold"), justify=CENTER, state="readonly")
        cmb_proof_id['values'] = ['AADHAR CARD', 'PAN CARD', 'DRIVING LIENCE']
        cmb_proof_id.place(x=520, y=275)

        # ========================== Row 5 ============================= #
        lbl_email = Label(Frame1, text="Email", font=("times new roman", 20), fg="black", bg="white").place(x=10, y=320)
        txt_email = Entry(Frame1, textvariable=self.var_email, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=170, y=325, width=200)

        lbl_contact = Label(Frame1, text="Contact", font=("times new roman", 20), fg="black", bg="white").place(x=390, y=320)
        txt_contact = Entry(Frame1, textvariable=self.var_contact, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=520, y=325)

        # ========================== Row 6 ============================= #
        lbl_hired = Label(Frame1, text="Hired Location", font=("times new roman", 18), fg="black", bg="white").place(x=10, y=370)
        txt_hired = Entry(Frame1, textvariable=self.var_hr_location, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=170, y=375, width=200)

        lbl_status = Label(Frame1, text="Status", font=("times new roman", 20), fg="black", bg="white").place(x=390, y=370)
        txt_status = Entry(Frame1, textvariable=self.var_status, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=520, y=375)

        # ========================== Row 7 ============================= #
        lbl_address = Label(Frame1, text="Address", font=("times new roman", 20), fg="black", bg="white").place(x=10, y=420)
        self.txt_address = Text(Frame1, font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
        self.txt_address.place(x=170, y=425, width=500, height=150)


        # ========================== Frame 2 ============================= #
        Frame2 = Frame(self.root, bd=3, bg="white", relief=RIDGE)
        Frame2.place(x=770, y=70, width=580, height=300)

        title2 = Label(Frame2, text="Employee Salary Details", font=("comicsans", 20, "bold"), bg="#607d8b", fg="white", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        lbl_month = Label(Frame2, text="Month", font=("calibri", 18), fg="black", bg="white").place(x=10, y=60)
        txt_designation = Entry(Frame2, textvariable=self.var_month, font=("consolos", 15, "bold"), bg="lightyellow", fg="black").place(x=90, y=64, width=100)

        lbl_year = Label(Frame2, text="Year", font=("calibri", 18), fg="black", bg="white").place(x=210, y=60)
        txt_year = Entry(Frame2, textvariable=self.var_year, font=("consolos", 15, "bold"), bg="lightyellow", fg="black").place(x=270, y=64, width=100)

        lbl_b_salary = Label(Frame2, text="Salary", font=("calibri", 18), fg="black", bg="white").place(x=385, y=60)
        txt_b_salary = Entry(Frame2, textvariable=self.var_salary, font=("consolos", 15, "bold"), bg="lightyellow", fg="black").place(x=460, y=64, width=100)

        # ========================== Row 2 ============================= #
        lbl_days = Label(Frame2, text="Total Days", font=("calibri", 18), fg="black", bg="white").place(x=10, y=110)
        txt_days = Entry(Frame2, textvariable=self.var_t_days, font=("consolos", 15, "bold"), bg="lightyellow", fg="black").place(x=160, y=112, width=120)

        lbl_absent = Label(Frame2, text="Absents", font=("calibri", 18), fg="black", bg="white").place(x=310, y=110)
        txt_absent = Entry(Frame2, textvariable=self.var_absent, font=("consolos", 15, "bold"), bg="lightyellow", fg="black").place(x=440, y=112, width=120)

        # ========================== Row 3 ============================= #
        lbl_medical = Label(Frame2, text="Medical", font=("calibri", 18), fg="black", bg="white").place(x=10, y=140)
        txt_medical = Entry(Frame2, textvariable=self.var_medical, font=("consolos", 15, "bold"), bg="lightyellow", fg="black").place(x=160, y=145, width=120)

        lbl_pf = Label(Frame2, text="PF", font=("calibri", 20), fg="black", bg="white").place(x=310, y=140)
        txt_pf = Entry(Frame2, textvariable=self.var_pf, font=("consolos", 15, "bold"), bg="lightyellow", fg="black").place(x=440, y=145, width=120)

        # ========================== Row 4 ============================= #
        lbl_convence = Label(Frame2, text="Convence", font=("calibri", 18), fg="black", bg="white").place(x=10, y=170)
        txt_convence = Entry(Frame2, textvariable=self.var_convence, font=("consolos", 15, "bold"), bg="lightyellow", fg="black").place(x=160, y=175, width=120)

        lbl_n_salary = Label(Frame2, text="Net Salary", font=("calibri", 20), fg="black", bg="white").place(x=310, y=170)
        txt_n_salary = Entry(Frame2, textvariable=self.var_net_salary, font=("consolos", 15, "bold"), bg="lightyellow", fg="black").place(x=440, y=175, width=120)

        btn_calculate = Button(Frame2, text="Calculate", command=self.calculate, font=("arial", 15, "bold"), bg="#262626", fg="white", bd=0, activebackground="#607d8b", activeforeground="white", cursor="hand2").place(x=40, y=240, height=30, width=120)
        btn_save = Button(Frame2, text="Save", font=("arial", 15, "bold"), bg="#262626", fg="white", activebackground="#607d8b", bd=0, activeforeground="white", cursor="hand2").place(x=170, y=240, height=30, width=120)
        btn_clear = Button(Frame2, command=self.Clear, text="Clear", font=("arial", 15, "bold"), bg="#262626", fg="white", bd=0, activebackground="#607d8b", activeforeground="white", cursor="hand2").place(x=300, y=240, height=30, width=120)
        btn_update = Button(Frame2, text="Update", font=("arial", 15, "bold"), bg="#262626", fg="white", bd=0, activebackground="#607d8b", activeforeground="white", cursor="hand2").place(x=430, y=240, height=30, width=120)
    
        # ========================== Frame 3 ============================= #
        Frame3 = Frame(self.root, bd=3, bg="white", relief=RIDGE)
        Frame3.place(x=770, y=380, width=580, height=310)

        # ========================== Frame 3 ============================= #
        self.var_txt = StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator = self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''

        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''

        Cal_Frame = Frame(Frame3, bd=2, bg="black", relief=RIDGE)
        Cal_Frame.place(x=2, y=2, width=245, height=300)

        txt_Result = Entry(Cal_Frame, textvariable=self.var_txt, font=("arial", 25, "bold"), bg="lightgrey", justify=LEFT).place(x=0, y=2, relwidth=1, height=45)

        # ========================== Row 1 ============================= #
        btn_7 = Button(Cal_Frame, text="7", command=lambda:btn_click(7), font=("consolos", 15, "bold"), cursor="hand2").place(x=0, y=52, width=60, height=60)
        btn_8 = Button(Cal_Frame, text="8", command=lambda:btn_click(8), font=("consolos", 15, "bold"), cursor="hand2").place(x=61, y=52, width=60, height=60)
        btn_9 = Button(Cal_Frame, text="9", command=lambda:btn_click(9), font=("consolos", 15, "bold"), cursor="hand2").place(x=122, y=52, width=60, height=60)
        btn_div = Button(Cal_Frame, text="/", command=lambda:btn_click('/'), font=("consolos", 15, "bold"), cursor="hand2").place(x=183, y=52, width=60, height=60)

        # ========================== Row 2 ============================= #
        btn_4 = Button(Cal_Frame, text="4", command=lambda:btn_click(4), font=("consolos", 15, "bold"), cursor="hand2").place(x=0, y=112, width=60, height=60)
        btn_5 = Button(Cal_Frame, text="5", command=lambda:btn_click(5), font=("consolos", 15, "bold"), cursor="hand2").place(x=61, y=112, width=60, height=60)
        btn_6 = Button(Cal_Frame, text="6", command=lambda:btn_click(6), font=("consolos", 15, "bold"), cursor="hand2").place(x=122, y=112, width=60, height=60)
        btn_7 = Button(Cal_Frame, text="*", command=lambda:btn_click('*'), font=("consolos", 15, "bold"), cursor="hand2").place(x=183, y=112, width=60, height=60)

        # ========================== Row 3 ============================= #
        btn_1 = Button(Cal_Frame, text="1", command=lambda:btn_click(1),font=("consolos", 15, "bold"), cursor="hand2").place(x=0, y=172, width=60, height=60)
        btn_2 = Button(Cal_Frame, text="2", command=lambda:btn_click(2),font=("consolos", 15, "bold"), cursor="hand2").place(x=61, y=172, width=60, height=60)
        btn_3 = Button(Cal_Frame, text="3", command=lambda:btn_click(3),font=("consolos", 15, "bold"), cursor="hand2").place(x=122, y=172, width=60, height=60)
        btn_mul = Button(Cal_Frame, text="-", command=lambda:btn_click('-'), font=("consolos", 15, "bold"), cursor="hand2").place(x=183, y=172, width=60, height=60)

        # ========================== Row 3 ============================= #
        btn_0 = Button(Cal_Frame, text="0", command=lambda:btn_click(0),font=("consolos", 15, "bold"), cursor="hand2").place(x=0, y=232, width=60, height=60)
        btn_clear_cal = Button(Cal_Frame, text="C", command=clear_cal, font=("consolos", 15, "bold"), cursor="hand2").place(x=61, y=232, width=60, height=60)
        btn_sum = Button(Cal_Frame, text="+", command=lambda:btn_click('+'), font=("consolos", 15, "bold"), cursor="hand2").place(x=122, y=232, width=60, height=60)
        btn_equal = Button(Cal_Frame, text="=", command=result, font=("consolos", 15, "bold"), cursor="hand2").place(x=183, y=232, width=60, height=60)

        # ========================== Row 3 ============================= #
        sal_Frame = Frame(Frame3, bd=3, bg="white", relief=RIDGE)
        sal_Frame.place(x=250, y=2, width=320, height=300)
        title3 = Label(sal_Frame, text="Salary Reciept", font=("comicsans", 20, "bold"), bg="#607d8b", fg="white", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        sal_Frame2 = Frame(sal_Frame, bd=2, bg="white", relief=RIDGE)
        sal_Frame2.place(x=0, y=40, relwidth=1, height=220)

        scroll_y = Scrollbar(sal_Frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_reciept = Text(sal_Frame2, font=("calibri", 15), bg="lightyellow", yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fil=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_reciept.yview)

        btn_print = Button(sal_Frame, command=self.print, text="Print", font=("consolos", 15, "bold"), bg="#262626", fg="white", activebackground="#3f51b5", activeforeground="white", cursor="hand2").place(x=170, y=262, height=30, width=120)

        self.check_connection()

    def calculate(self):
        if self.var_month.get()=="" or self.var_year.get()=="" or self.var_salary.get()=="" or self.var_t_days.get()=="" or self.var_absent.get()=="" or self.var_medical.get()=="" or self.var_pf.get()=="" or self.var_convence.get()=="":
            messagebox.showerror("!!! ERROR 404 !!!", "!!! *** EMPLOYEE SALARY DETAILS ARE REQUIRED *** !!!")
        else:
            # self.var_net_salary.set("RESULT")
            # 35000/31==1752
            # 31-10=21*1752
            per_day = int(self.var_salary.get())/int(self.var_t_days.get())
            work_day = int(self.var_t_days.get())-int(self.var_absent.get())
            sal_ = per_day*work_day
            deduct = int(self.var_medical.get())+int(self.var_pf.get())
            addition = int(self.var_convence.get())
            net_sal = sal_-deduct+addition  
            self.var_net_salary.set(str(round(net_sal, 2)))

    def check_connection(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="ems")
            cur = con.cursor()
            cur.execute("SELECT * FROM emp_salary")
            rows = cur.fetchall()
            print(rows)

        except Exception as ex:
            messagebox.showerror("!!! ERROR 404 !!!", f"!!! ERROR DUE TO : {str(ex)} !!!")

    def print(self):
        if self.var_emp_code.get()=="":
            messagebox.showerror("!!! ERROR 404 !!!", "!!! *** PLEASE ENTER EMPLOYEE ID *** !!!")
        else:
            op = messagebox.askyesno("!!! SAVE RECIEPT !!!", "DO YOU WANT TO RECIEPT BILL ?")
            if op>0:
                self.reciept_data = self.txt_salary_reciept.get('1.0', END)
                f1 = open("reciepts/" + str(self.var_emp_code.get())+".txt","w")
                f1.write(self.reciept_data)
                f1.close
                messagebox.showinfo("!!! SAVED !!!", f"RECIEPT NO : {self.var_emp_code.get()} SAVED SUCCESSFULLY")
                self.txt_salary_reciept.delete('1.0', END)
            else:
                return

    def Clear(self):
        if self.var_emp_code.get()=="" or self.var_name.get()=="" or self.var_age.get()=="" or self.var_gender.get()=="":
            messagebox.showerror("!!! ERROR 404 !!!", "PLEASE FILL THE FORM OR SELECT THE EMPLOYEE TO EDIT")
        else:
            # ========================== Frame 1 ============================= #
            # ========================== All Variables ============================= #
            self.var_emp_code.set("")
            self.var_designation.set("")
            self.var_name.set("")
            self.var_age.set("")
            self.var_gender.set("")
            self.var_email.set("")
            self.var_hr_location.set("")
            self.var_doj.set("")
            self.var_dob.set("")
            self.var_experience.set("")
            self.var_proof_id.set("")
            self.var_contact.set("")
            self.var_status.set("")
            self.txt_address.delete('1.0', END)

            # ========================== Frame 2 ============================= #
            # ========================== All Variables ============================= #
            self.var_month.set("")
            self.var_year.set("")
            self.var_t_days.set("")
            self.var_absent.set("")
            self.var_medical.set("")
            self.var_pf.set("")
            self.var_convence.set("")
            self.var_salary.set("")
            self.var_net_salary.set("")
            self.txt_salary_reciept.delete('1.0', END)

root = Tk()
obj = EmployeeSystem(root)
root.mainloop()