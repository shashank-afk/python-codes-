import tkinter as tk
#from ttk import *

top=tk.Tk()
top.minsize(148,1)
top.maxsize(1924,1055)
top.resizable(0,0)
top.title("PMS")
top.geometry("926x625")

#------------------------Labels-----------------------------------------------------
Label=tk.Label(top,text="STUDENT ENTRY",font=("Segoe UI Black",22,"bold"))
Label.place(relx=0.238, rely=0.048, height=56, width=502)

clas=tk.Label(top,text="Select Class",font=("Times New Roman",14,"normal"))
clas.place(relx=0.043, rely=0.192, height=36, width=182)

section=tk.Label(top,text="Select Section",font=("Times New Roman",14,"normal"))
section.place(relx=0.562, rely=0.192, height=36, width=182)

Name=tk.Label(top,text="Enter Student's Name",font=("Times New Roman",14,"normal"))
Name.place(relx=0.018, rely=0.336, height=36, width=302)

rn=tk.Label(top,text="Enter Student's Roll No.",font=("Times New Roman",14,"normal"))
rn.place(relx=0.025, rely=0.464, height=36, width=312)

sub=tk.Label(top,text="Select Subject Group",font=("Times New Roman",14,"normal"))
sub.place(relx=0.025, rely=0.576, height=46, width=292)

#-------------------------buttons-------------------------------------------------------
submit=tk.Button(top,text="SUBMIT",font=("Times New Roman",16,"bold"))
submit.place(relx=0.713, rely=0.848, height=53, width=216)

back=tk.Button(top,text="BACK",font=("Times New Roman",16,"bold"))
back.place(relx=0.41, rely=0.848, height=53, width=216)

#-----------------------entry and dropdowns----------------------------------------------
classes = [1,2,3,4,5,6,7,8,9,10,11,12] #etc
variabl= tk.IntVar(top)
variabl.set(classes[0]) 

cl = tk.OptionMenu(top, variabl, *classes)
cl.place(relx=0.313, rely=0.192, relheight=0.058,relwidth=0.060)
cl.configure(background="white")
cl.configure(disabledforeground="#a3a3a3")
cl.configure(font=('Times New Roman',12,'bold'))
cl.configure(foreground="#000000")

secti = ['A','B'] #etc
variable = tk.StringVar(top)
variable.set(secti[0]) 

sect= tk.OptionMenu(top, variable, *secti)
sect.place(relx=0.832, rely=0.192, relheight=0.058, relwidth=0.060)
sect.configure(background="white")
sect.configure(disabledforeground="#a3a3a3")
sect.configure(font=('Times New Roman',12,'bold'))
sect.configure(foreground="#000000")

n=tk.Entry(top,font=('Times New Roman',16,'bold'))
n.place(relx=0.475, rely=0.448,height=44, relwidth=0.253)

r=tk.Entry(top,font=('Times New Roman',16,'bold'))
r.place(relx=0.475, rely=0.32,height=44, relwidth=0.253)

s=['PCMC','PCMB']
var= tk.StringVar(top)
var.set(s[0])

su=tk.OptionMenu(top  , var , *s)
su.place(relx=0.475, rely=0.56, relheight=0.074, relwidth=0.256)
su.configure(background="white")
su.configure(disabledforeground="#a3a3a3")
su.configure(font=('Times New Roman',12,'bold'))
su.configure(foreground="#000000")






