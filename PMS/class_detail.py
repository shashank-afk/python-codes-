import tkinter as tk
top=tk.Tk()
top.minsize(148,1)
top.maxsize(1924,1055)
top.resizable(0,0)
top.title("PMS")
top.geometry("926x625")
#----------------label----------------------------------
top_label=tk.Label(top,text='CLASS DETAIL',font=("Segoe UI Black", 22 , "bold"))
top_label.place(relx=0.248, rely=0.062, height=46, width=482)

Class=tk.Label(top,text='ENTER CLASS',font=("Times New Roman", 14 , "normal"))
Class.place(relx=0.043, rely=0.231, height=56, width=212)

section=tk.Label(top,text='ENTER SECTION',font=("Times New Roman", 14 , "normal"))
section.place(relx=0.054, rely=0.4, height=56, width=212)

student=tk.Label(top,text='ENTER NUMBER OF STUDENTS',font=("Times New Roman", 14 , "normal"))
student.place(relx=0.064, rely=0.554, height=56, width=342)

subject=tk.Label(top,text='ENTER NUMBER OF SUBJECTS',font=("Times New Roman", 14 , "normal"))
subject.place(relx=0.064, rely=0.692, height=56, width=342)

#-------------Entry-------------------------
clas=tk.Entry(top,font="TkFixedFont",background="white")
clas.place(relx=0.54, rely=0.262,height=44, relwidth=0.229)

sec=tk.Entry(top,font="TkFixedFont",background="white")
sec.place(relx=0.54, rely=0.4,height=44, relwidth=0.229)

stu=tk.Entry(top,font="TkFixedFont",background="white")
stu.place(relx=0.54, rely=0.554,height=44, relwidth=0.229)

sub=tk.Entry(top,font="TkFixedFont",background="white")
sub.place(relx=0.54, rely=0.708,height=44, relwidth=0.229)

cmessage=tk.Message(top,text='(WRITE IN DIGITS FROM 0 TO 9)')
cmessage.place(relx=0.788, rely=0.220, relheight=0.169,width=70)


smessage=tk.Message(top,text='(A or B)')
smessage.place(relx=0.775, rely=0.400, height=46,width=70)


