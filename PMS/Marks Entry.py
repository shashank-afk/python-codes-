import tkinter as tk
top=tk.Tk()
top.minsize(148,1)
top.maxsize(1924,1055)
top.resizable(0,0)
top.title("PMS")
top.geometry("926x625")
#-------------Label-----------

label=tk.Label(top,text='Marks Entry',font=("Segoe UI Black", 22 , "bold"))
label.place(relx=0.335, rely=0.032, height=46, width=342)

sc=tk.Label(top,text='Select Class',font=("Times New Roman", 14 , "normal"))
sc.place(relx=0.065, rely=0.16, height=26, width=132)

ss=tk.Label(top,text='Select Section',font=("Times New Roman", 14 , "normal"))
ss.place(relx=0.551, rely=0.16, height=26, width=132)

ssub=tk.Label(top,text='Select Subject',font=("Times New Roman", 14 , "normal"))
ssub.place(relx=0.076, rely=0.272, height=26, width=132)

se=tk.Label(top,text='Select Examination',font=("Times New Roman", 14 , "normal"))
se.place(relx=0.551, rely=0.272, height=26, width=182)


#------------Entry & DropDownBox--------------
s=[11,12]
var= tk.IntVar(top)
var.set(s[0])

cl=tk.OptionMenu(top  , var , *s)
cl.place(relx=0.292, rely=0.15, relheight=0.058 , relwidth=0.062)
cl.configure(background="white")
cl.configure(disabledforeground="#a3a3a3")
cl.configure(font=('Times New Roman',12,'bold'))
cl.configure(foreground="#000000")

sec=tk.OptionMenu(top  , var , *s)
sec.place(relx=0.778, rely=0.144, relheight=0.058 , relwidth=0.062)
sec.configure(background="white")
sec.configure(disabledforeground="#a3a3a3")
sec.configure(font=('Times New Roman',12,'bold'))
sec.configure(foreground="#000000")

sub=tk.OptionMenu(top  , var , *s)
sub.place(relx=0.292, rely=0.256, relheight=0.058 , relwidth=0.094)
sub.configure(background="white")
sub.configure(disabledforeground="#a3a3a3")
sub.configure(font=('Times New Roman',12,'bold'))
sub.configure(foreground="#000000")

exa=[1,2,3,4,5,6,7]
vex=tk.IntVar(top)
vex.set(exa[0])

ex=tk.OptionMenu(top  , vex , *exa)
ex.place(relx=0.778, rely=0.256, relheight=0.058 , relwidth=0.072)
ex.configure(background="white")
ex.configure(disabledforeground="#a3a3a3")
ex.configure(font=('Times New Roman',12,'bold'))
ex.configure(foreground="#000000")

#------------Button-------------
gm=tk.Button(top,text='Generate Marksheet',relief="groove",font=("Segoe UI Black", 12 , "bold"))
gm.configure(foreground='black',highlightbackground="gray85")
gm.place(relx=0.713, rely=0.352, height=43, width=206)
gm.configure(pady="0")

submit=tk.Button(top,text='Submit',relief="raised",font=("Segoe UI Black", 12 , "bold"))
submit.configure(foreground='black',highlightbackground="gray85")
submit.place(relx=0.799, rely=0.896, height=53, width=126)
submit.configure(pady="0")
#-----------Frame-----------------
frame=tk.Frame(top,relief='groove',borderwidth='2')
frame.place(relx=0.065, rely=0.448, relheight=0.44, relwidth=0.869)



