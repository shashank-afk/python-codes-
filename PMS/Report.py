import tkinter as tk

top=tk.Tk()
top.minsize(148,1)
top.maxsize(1924,1055)
top.resizable(0,0)
top.title("PMS")
top.geometry("926x625")

#----------------Frames-----------------------
tf=tk.Frame(top,relief="groove",borderwidth="2")
tf.place(relx=0.0, rely=0.0, relheight=0.216, relwidth=1.001)


nf=tk.Frame(top,relief="groove",borderwidth="2")
nf.place(relx=0.0, rely=0.208, relheight=0.232, relwidth=1.001)

mf=tk.Frame(top,relief="groove",borderwidth="2")
mf.place(relx=0.0, rely=0.432, relheight=0.456, relwidth=1.001)

#--------------Labels---------------------------
kv=tk.Label(tf,text="KENDRIYA VIDYALAYA COOCHBEHAR",font=("Segoe UI Black",22,"normal"))
kv.place(relx=0.13, rely=0.074, height=46, width=700)

add=tk.Label(tf,text="ADRESS: NILKUTHI BABURHAT, COOCHBEHAR-PIN:736156")
add.place(relx=0.303, rely=0.37, height=26, width=407)

session=tk.Label(tf,text="SESSION:2020-2021",font=("Segoe UI Black",16,"normal"))
session.place(relx=0.357, rely=0.593, height=36, width=282)

clas=tk.Label(nf,text="CLASS :",font=("Times New Roman",14,"normal"))
clas.place(relx=0.032, rely=0.138, height=32, width=88)

section=tk.Label(nf,text="SECTION :",font=("Times New Roman",14,"normal"))
section.place(relx=0.368, rely=0.138, height=32, width=114)

roll_numbr=tk.Label(nf,text="ROLL NUMBER :",font=("Times New Roman",14,"normal"))
roll_numbr.place(relx=0.67, rely=0.138, height=32, width=174)

name=tk.Label(nf,text="NAME :",font=("Times New Roman",14,"normal"))
name.place(relx=0.032, rely=0.621, height=32, width=81)

cl=tk.Label(nf,text="12",relief="groove",font=("Times New Roman",14,"normal"))
cl.place(relx=0.173, rely=0.138, height=32, width=48)

s=tk.Label(nf,text="B",relief="groove",font=("Times New Roman",14,"normal"))
s.place(relx=0.551, rely=0.138, height=32, width=30)

rn=tk.Label(nf,text="21",relief="groove",font=("Times New Roman",14,"normal"))
rn.place(relx=0.897, rely=0.138, height=32, width=38)

nm=tk.Label(nf,text="HARSHEET SHARMA",relief="groove",font=("Times New Roman",14,"normal"))
nm.place(relx=0.162, rely=0.621, height=32, width=230)

Button=tk.Button(top,text="HOME",font=("Segoe UI Black",14,"normal"))
Button.place(relx=0.779, rely=0.912, height=43, width=176)
