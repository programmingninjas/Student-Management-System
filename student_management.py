from tkinter import *

from PIL import Image,ImageTk

from tkinter import messagebox

import keyboard

import mysql.connector as ms

root=Tk()

root.title("Student Login System")

root.geometry("900x700+300+40")

root.resizable(False,False)

root.configure(bg="black")

#------VARIABLES-------
USERNAME=StringVar()
PASSWORD=StringVar()
student_name=StringVar()
father_name=StringVar()
mother_name=StringVar()
admission_number=StringVar()
attendance_percentage=StringVar()
fee=StringVar()


def show_admin():
        
	root1= Tk()

	root1.title("Student Management")

	root1.geometry("900x700+300+40")

	root1.resizable(False,False)

	root1.configure(bg="lavender")

	def clear_data():
		sname.delete(0,END)
		fname.delete(0,END)
		mname.delete(0,END)
		add_no.delete(0,END)
		attendance.delete(0,END)
		fee_entry.delete(0,END)

	def add_student(event=None):
		mydb=ms.connect(host="localhost",user="root",passwd="root",database="school") #set according to yours
		mycursor=mydb.cursor()
		mycursor.execute("CREATE TABLE IF NOT EXISTS students(Student_Name VARCHAR(30),Father_Name VARCHAR(30),Mother_Name VARCHAR(30),Admission_Number INT,Attendance INT,Fee_Status VARCHAR(20))")
		mycursor.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s)",
							   (sname.get(),
							   fname.get(),
							   mname.get(),
							   add_no.get(),
							   attendance.get(),
							   fee_entry.get()))
		mydb.commit()
		mydb.close()
		messagebox.showinfo("Success","Student Successfully Added!",parent=root1)
		clear_data()


	def delete_student():
		mydb=ms.connect(host="localhost",user="root",passwd="root",database="school")
		mycursor=mydb.cursor()
		sql="DELETE FROM students WHERE Student_Name=%s and Admission_Number=%s"
		val=(sname.get(),add_no.get())
		mycursor.execute(sql,val)
		mydb.commit()
		mydb.close()
		messagebox.showinfo("Success","Student Removed Successfully",parent=root1)
		clear_data()
		

	def close_window():
		exit=messagebox.askyesno("Student Management System","Are you sure you want to close the Window?",parent=root1)
		if exit>0:
			root1.destroy()

	head=Label(root1,text="Student  Management  System",fg="blueviolet",font=("Times",30,"bold"),bg="lavender")

	head.place(x=200,y=10)

	Name=Label(root1,text=" Student  Name",fg="crimson",font=("Times",16,"bold"),bg="lavender")

	Name.place(x=35,y=105)

	sname=Entry(root1,width=15,font=("Now",14,"bold"),relief=SUNKEN,textvariable=student_name)

	sname.place(x=200,y=105)

	Father=Label(root1,text="Father's  Name",fg="crimson",font=("Times",16,"bold"),bg="lavender")

	Father.place(x=39,y=150)

	fname=Entry(root1,width=15,font=("Now",14,"bold"),relief=SUNKEN,textvariable=father_name)

	fname.place(x=200,y=155)

	Mother=Label(root1,text="Mother's  Name",fg="crimson",font=("Times",16,"bold"),bg="lavender")

	Mother.place(x=39,y=200)

	mname=Entry(root1,width=15,font=("Now",14,"bold"),relief=SUNKEN,textvariable=mother_name)

	mname.place(x=200,y=202)

	Number=Label(root1,text="Admission No.",fg="crimson",font=("Times",16,"bold"),bg="lavender")

	Number.place(x=40,y=265)

	add_no=Entry(root1,width=15,font=("Now",14,"bold"),relief=SUNKEN,textvariable=admission_number)

	add_no.place(x=200,y=267)

	Attendance=Label(root1,text="Attendance %",fg="crimson",font=("Times",16,"bold"),bg="lavender")

	Attendance.place(x=40,y=335)

	attendance=Entry(root1,width=15,font=("Now",14,"bold"),relief=SUNKEN,textvariable=attendance_percentage)

	attendance.place(x=200,y=335)

	fee_status=Button(root1,text="Fee  Status",fg="red",font=("Times New Roman",16,"bold"),bd=1,bg="ghost white")

	fee_status.place(x=47,y=400)

	fee_entry=Entry(root1,width=12,font=("Now",14,"bold"),relief=SUNKEN,fg="green",bd=1,textvariable=fee)

	fee_entry.place(x=47,y=460)

	addstudent=Button(root1,text="Add Student",font=("Times New Roman",16,"bold"),bd=2,bg="thistle1",command=add_student)

	addstudent.place(x=50,y=550)

	removestudent=Button(root1,text="Delete Student",font=("Times New Roman",16,"bold"),bd=2,bg="thistle1",command=delete_student)

	removestudent.place(x=200,y=550)

	cleardata=Button(root1,text="Clear",font=("Times New Roman",16,"bold"),bd=2,bg="thistle1",width=10,command=clear_data)

	cleardata.place(x=370,y=550)

	closepage=Button(root1,text="Close",font=("Times New Roman",16,"bold"),bd=2,bg="thistle1",width=8,command=close_window)

	closepage.place(x=525,y=550)

	root1.bind("<Return>",add_student)

	root1.mainloop()






def show_student(student_name,father_name,mother_name,admission_number,attendance_percentage,fee):
	root.destroy()


	root2=Tk()

	root2.title("Student Information")

	root2.geometry("900x700+300+40")

	root2.resizable(False,False)

	bgimage=ImageTk.PhotoImage(Image.open("background3.jpg"))

	bgimage_label=Label(image=bgimage)

	bgimage_label.place(x=0,y=0,relwidth=1,relheight=1)

	b1=Canvas(root2,width=600,height=100,bg="light green")

	b1.place(x=1,y=10)

	b1.create_image(0,0,anchor=NW,image=bgimage)

	b1.place(x=0,y=0,relwidth=1,relheight=1)

	b1.create_text(450,30,text="Student  Management  System",fill="blueviolet",font=("Times",30,"bold"))

	b1.update()

	b1.create_text(112,120,text=" Student  Name",fill="crimson",font=("Times",16,"bold"))

	b1.create_text(115,175,text="Father's  Name",fill="crimson",font=("Times",16,"bold"))

	b1.create_text(116,230,text="Mother's  Name",fill="crimson",font=("Times",16,"bold"))

	b1.create_text(108,290,text="Admission No.",fill="crimson",font=("Times",16,"bold"))

	b1.create_text(110,350,text="Attendance %",fill="crimson",font=("Times",16,"bold"))

	b1.create_text(97,420,text="Fee Status",fill="crimson",font=("Times",16,"bold"))

	l1=Label(root2,fg="black",font=("Times",15,"bold"),relief=FLAT)

	l1.place(x=220,y=100)

	l2=Label(root2,fg="black",font=("Times",15,"bold"),relief=FLAT)

	l2.place(x=220,y=155)

	l3=Label(root2,fg="black",font=("Times",15,"bold"),relief=FLAT)

	l3.place(x=220,y=210)

	l4=Label(root2,fg="black",font=("Times",15,"bold"),relief=FLAT)

	l4.place(x=220,y=270)

	l5=Label(root2,fg="black",font=("Times",15,"bold"),relief=FLAT)

	l5.place(x=220,y=335)

	l6=Label(root2,fg="black",font=("Times",15,"bold"),relief=FLAT)

	l6.place(x=220,y=405)

	l1.config(text=student_name)

	l2.config(text=father_name)

	l3.config(text=mother_name)

	l4.config(text=admission_number)

	l5.config(text=(str(attendance_percentage)+"%"))

	if fee.lower()=="submitted":
		l6.config(text=fee,fg="green")
	else:
		l6.config(text=fee,fg="red")




	


	root2.mainloop()

def login_screen(event=None):
	if userentry.get()=="" or passentry.get()=="":
	 	messagebox.showerror("Error","Please Enter the Username and Password")
	else:
	 	try:
	 		mydb=ms.connect(host="localhost",user="root",passwd="root",database="school")

	 		mycursor=mydb.cursor()

	 		sql="SELECT * FROM students WHERE Student_Name=%s and Admission_Number=%s"

	 		val=(userentry.get(),passentry.get())

	 		mycursor.execute(sql,val)

	 		result=mycursor.fetchone()

	 		student_name=result[0]

	 		father_name=result[1]

	 		mother_name=result[2]

	 		admission_number=result[3]

	 		attendance_percentage=result[4]

	 		fee=result[5]

	 		show_student(student_name,father_name,mother_name,admission_number,attendance_percentage,fee)

	 	except Exception as es:
	 		messagebox.showerror("Error","Incorrect Username or Password")

	 		mydb.commit()
	 		mydb.close()
		




frame1=LabelFrame(root,bg="ghost white",width=400,height=280,relief=RIDGE,bd=0)

frame1.place(x=250,y=250)

image=ImageTk.PhotoImage(Image.open("user.jpg"))

l1=Label(root,image=image,width=190,height=170,anchor=NW)

l1.place(x=355,y=100)

loginlabel=Label(frame1,text="LOGIN",font=("Times New Roman",20,"bold"),fg="orange red",bg="ghost white")

loginlabel.place(x=152,y=30)

userlabel=Label(frame1,text="Username",font=("Times New Roman",15,"bold"),fg="orange red",bg="ghost white")

passlabel=Label(frame1,text="Password",font=("Times New Roman",15,"bold"),fg="orange red",bg="ghost white")

userlabel.place(x=50,y=85)

passlabel.place(x=50,y=155)

userentry=Entry(frame1,font=("Times New Roman",15,"bold"),fg="gray",bg="white")

userentry.place(x=50,y=120)

passentry=Entry(frame1,font=("Times New Roman",15,"bold"),fg="gray",bg="white",show="*")

passentry.place(x=50,y=190)

login_image=PhotoImage(file="button.png")

login_button=Button(root,image=login_image,bg="ghost white",bd=0,command=login_screen)

login_button.place(x=390,y=475)

keyboard.add_word_listener("007",show_admin) #here you can change secret code also


root.bind("<Return>",login_screen) #press enter to login


root.mainloop()
