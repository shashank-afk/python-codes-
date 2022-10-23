import tkinter as tk
from tkinter import *
import mysql.connector as mc
#import report
import ctypes

try:
    
    from ttk import *
    py3=False
except ImportError:  # Python 3
    from tkinter.ttk import *
    py3=True

import sys
import os.path
'''
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk 
    py3 = True
'''

########################################################################
class MyApp(object):
    
    

    """"""
    

    #----------------------------------------------------------------------
    def __init__(self, parent):# frontpage
        
        top=tk.Tk()
        top.minsize(148,1)
        top.maxsize(1924,1055)
        top.resizable(0,0)
        top.title("PMS")
        user32 = ctypes.windll.user32
        screen_width=user32.GetSystemMetrics(0)
        screen_height=user32.GetSystemMetrics(1)
        x = screen_width//2 - 926//2
        y = screen_height//2 -625//2
        top.geometry('926x625+%d+%d' %(x,y))
        
    #-------------Label-----------
        label=tk.Label(top,text='PERFORMANCE MANAGEMENT SYSTEM',font=("Segoe UI Black", 14 , "bold"))
        label.place(relx=0.238, rely=0.08, height=86, width=542)




    #------------Button-----------
        entry=tk.Button(top,text='Entry',relief="groove",font=("Segoe UI Black", 24 , "bold"))
        entry.configure(foreground='black',highlightbackground="gray85")
        entry.place(relx=0.151,rely=0.32,height=123,width=306)
        entry.configure(pady="0")
        entry.configure(command=lambda:Entry(top))

        msheet=tk.Button(top,text='Generate Marksheet',relief="groove",font=("Segoe UI Black", 18 , "bold"))
        msheet.configure(foreground='black',highlightbackground="gray85")
        msheet.place(relx=0.551, rely=0.32, height=123, width=316)
        msheet.configure(pady="0")
        msheet.configure(command=lambda:ME(top))

        rport=tk.Button(top,text='Report',relief="groove",font=("Segoe UI Black", 18 , "bold"))
        rport.configure(foreground='black',highlightbackground="gray85")
        rport.place(relx=0.367, rely=0.576, height=123, width=306)
        rport.configure(pady="0")
        rport.configure(command=lambda:ReportEntry(top))
       
    #----------------------------------------------------------------------
    global Entry
        
    def Entry(ETP):
        ETP.withdraw()
        top=tk.Tk()
        top.minsize(148,1)
        top.maxsize(1924,1055)
        top.resizable(0,0)
        top.title("PMS")
        user32 = ctypes.windll.user32
        screen_width=user32.GetSystemMetrics(0)
        screen_height=user32.GetSystemMetrics(1)
        x = screen_width//2 - 926//2
        y = screen_height//2 -625//2
        top.geometry('926x625+%d+%d' %(x,y))

        Label=tk.Label(top,text="SELECT PAGE",font=("Segoe UI Black",22,"normal"))
        Label.place(relx=0.033, rely=0.222, height=46, width=262)

       

        s=["Class Detail","Student Entry"]
        var=tk.StringVar(top)
        var.set(s[0])

        dd=tk.OptionMenu(top, var, *s )
        dd.place(relx=0.55, rely=0.222, relheight=0.102, relwidth=0.362)
        dd.configure(background="white")
        dd.configure(disabledforeground="#a3a3a3")
        dd.configure(font=('Times New Roman',12,'bold'))
        dd.configure(foreground="#000000")
        
        def call():
            if var.get()=="Class Detail":
                CD(top)
            elif var.get()=="Student Entry":
                SE(top)

        Button=tk.Button(top,text="SUBMIT",font=("Segoe UI Black",18,"normal"),command=lambda:call())
        Button.place(relx=0.550, rely=0.667, height=53, width=166)

        bck=tk.Button(top,text="BACK",font=("Segoe UI Black",18,"normal"),command=lambda:back(ETP,top))
        bck.place(relx=0.350,rely=0.667,height=53,width=166)
        
        
    global ME
    def ME(mp):#exit gui command
        """"""
        mp.withdraw()
        top=tk.Tk()
        top.minsize(148,1)
        top.maxsize(1924,1055)
        top.resizable(0,0)
        top.title("PMS")
        user32 = ctypes.windll.user32
        screen_width=user32.GetSystemMetrics(0)
        screen_height=user32.GetSystemMetrics(1)
        x = screen_width//2 - 926//2
        y = screen_height//2 -625//2
        top.geometry('926x625+%d+%d' %(x,y))

        con=mc.connect(user="root",database="pms",host="localhost",password="root")
        cr=con.cursor()
        cr.execute("SELECT CLASS,SECTION FROM class_detail")
        f=cr.fetchall()
        L=[]
            
        for i in f:
            L.append(i[0])
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
        s=L
        var= tk.IntVar(top)
        var.set(s[0])

        cl=tk.OptionMenu(top  , var , *s)
        cl.place(relx=0.292, rely=0.15, relheight=0.058 , relwidth=0.062)
        cl.configure(background="white")
        cl.configure(disabledforeground="#a3a3a3")
        cl.configure(font=('Times New Roman',12,'bold'))
        cl.configure(foreground="#000000")

        k=["A","B"]
        v=tk.StringVar(top)
        v.set(k[0])
        
        sec=tk.OptionMenu(top  , v , *k)
        sec.place(relx=0.778, rely=0.144, relheight=0.058 , relwidth=0.062)
        sec.configure(background="white")
        sec.configure(disabledforeground="#a3a3a3")
        sec.configure(font=('Times New Roman',12,'bold'))
        sec.configure(foreground="#000000")

        sb=["MATHS","HINDI","ENGLISH","BIO","CS","EVS","SCIENCE","PHYSICS","CHEMISTRY","BIOLOGY","ECONOMICS","POLITICAL SCIENCE","HISTORY","GEOGRAPHHY","SSC"]
        V=tk.StringVar(top)
        V.set(sb[0])
        
        sub=tk.OptionMenu(top  , V , *sb)
        sub.place(relx=0.292, rely=0.256, relheight=0.058 , relwidth=0.120)
        sub.configure(background="white")
        sub.configure(disabledforeground="#a3a3a3")
        sub.configure(font=('Times New Roman',12,'bold'))
        sub.configure(foreground="#000000")

        exa=['PT-1/MT-1','PT-2/MT-2','PT-3/MT-3','HALF YEARLY','SESSION ENDING']
        vex=tk.StringVar(top)
        vex.set(exa[0])

        ex=tk.OptionMenu(top  , vex , *exa)
        ex.place(relx=0.778, rely=0.256, relheight=0.058 , relwidth=0.120)
        ex.configure(background="white")
        ex.configure(disabledforeground="#a3a3a3")
        ex.configure(font=('Times New Roman',12,'bold'))
        ex.configure(foreground="#000000")

        #------------Button-------------
        gm=tk.Button(top,text='Generate Marksheet',relief="groove",font=("Segoe UI Black", 12 , "bold"))
        gm.configure(foreground='black',highlightbackground="gray85")
        gm.place(relx=0.713, rely=0.352, height=43, width=206)
        gm.configure(pady="0")
        gm.configure(command=lambda:generate())

        submit=tk.Button(top,text='Submit',relief="raised",font=("Times New Roman",16,"bold"))
        submit.configure(foreground='black',highlightbackground="gray85")
        submit.place(relx=0.799, rely=0.896, height=53, width=126)
        submit.configure(pady="0")
        submit.configure(command=lambda:Submit())
        #-----------Frame-----------------
        frame=tk.Frame(top,relief='groove',borderwidth='2')
        frame.place(relx=0.065, rely=0.448, relheight=0.44, relwidth=0.869)
        

        def generate():
            check=0
            con=mc.connect(user="root",database="pms",host="localhost",password="root")
            cr=con.cursor()
            cr.execute("SELECT * FROM %d%s"%(int(var.get()),str(v.get())))
            t=cr.fetchall()
            global rn,name
            rn=[]
            nm=[]
            for i in t:
                rn.append(i[0])
                nm.append(i[1])
            
                
                
            for j in f:
                if int(var.get()) in j and str(v.get()) in j:
                    check=1

                
            if check==1:
                

                r=tk.Label(frame,text="ROLL NUMBER",width=24,relief=RIDGE,font=("Times New Roman",16,"normal"))
                r.grid(row=0,column=0,sticky=NSEW)
                n=tk.Label(frame,text="NAME",width=24,relief=RIDGE,font=("Times New Roman",16,"normal"))
                n.grid(row=0,column=1,sticky=NSEW)
                m=tk.Label(frame,text="MARKS",width=24,relief=RIDGE,font=("Times New Roman",16,"normal"))
                m.grid(row=0,column=2,sticky=NSEW)
                for i in range(0,len(rn)):
                    global cols
                    cols = []
                    for j in range(3):
                        if j==0:
                            p=tk.Label(frame,width=24,relief=RIDGE,text=rn[i])
                            p.grid(row=i+1, column=j, sticky=NSEW)
                        elif j==1:
                            p=tk.Label(frame,width=24,relief=RIDGE,text=nm[i])
                            p.grid(row=i+1, column=j, sticky=NSEW)
                    
                        elif(j==2):
                            e = tk.Entry(frame,width=24,relief=RIDGE)
                    
                            e.configure(font=("Times New Roman",16,"normal"))
                            e.grid(row=i+1, column=j, sticky=NSEW)
                            e.insert(END, '%d.%d' % (i, j))
                            cols.append(e)
                            
            else:
                w=tk.Tk("error")
                w.geometry("200x120")
                w.resizable(0,0)

                tk.Label(w,text="INVALID CLASS",font=("Times New Roman",16,"bold")).place(x=1,y=1,height=100,width=200)
                

            
        def Submit():
            exam=str(vex.get())
            op=[]
            for k in cols:
                op.append(k.get())
            for i in range(len(op)):
                con=mc.connect(user="root",database="pms",host="localhost",password="root")
                cr=con.cursor()
                cr.execute("UPDATE %s SET `%s`=%d WHERE RN=%d"%(str(V.get()).lower(),exam,int(op[i]),rn[i])) 
                con.commit()
                
                
                
        
     #===================================================Update in mysql=============================================#
    global show
    def show(ep):
        """"""
        ep.update()
        ep.deiconify()         

    #----------------------------------------------------------------------

    global CD
    def CD(cp):#entry gui command
        #entry gui
        """"""
        
        cp.withdraw()
        #This class configures and populates the toplevel window.
           #top is the toplevel containing window.
        
        top=tk.Tk()
        top.minsize(148,1)
        top.maxsize(1924,1055)
        top.resizable(0,0)
        top.title("PMS")
        user32 = ctypes.windll.user32
        screen_width=user32.GetSystemMetrics(0)
        screen_height=user32.GetSystemMetrics(1)
        x = screen_width//2 - 926//2
        y = screen_height//2 -625//2
        top.geometry('926x625+%d+%d' %(x,y))
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



        submit=tk.Button(top,text="SUBMIT",font=("Times New Roman",16,"bold"))
        submit.place(relx=0.747, rely=0.864, height=43, width=176)
        submit.configure(command=lambda:submit())
        

        bck=tk.Button(top,text="BACK",font=("Times New Roman",16,"bold"))
        bck.place(relx=0.498, rely=0.864, height=43, width=176)
        bck.configure(command=lambda:back(cp,top))
        def submit():
            if str(clas.get()).isdigit()== False or (int(clas.get())>12 and int(clas.get())<0):
                w=tk.Tk("error")
                w.geometry("200x120")
                w.resizable(0,0)

                tk.Label(w,text="INVALID CLASS",font=("Times New Roman",16,"bold")).place(x=1,y=1,height=100,width=200)

            elif len(str(sec.get()))>1:
                print(sec.get())
                w=tk.Tk("error")
                w.geometry("200x120")
                w.resizable(0,0)

                tk.Label(w,text="INVALID SECTION",font=("Times New Roman",16,"bold")).place(x=1,y=1,height=100,width=200)

            elif str(stu.get()).isdigit()==False :
                w=tk.Tk("error")
                w.geometry("400x120")
                w.resizable(0,0)

                tk.Label(w,text="INVALID NUMBER OF STUDENTS",font=("Times New Roman",16,"bold")).place(x=1,y=1,height=100,width=400)
            elif str(sub.get()).isdigit()==False:
                w=tk.Tk("error")
                w.geometry("400x120")
                w.resizable(0,0)

                tk.Label(w,text="INVALID NUMBER OF SUBJECTS",font=("Times New Roman",16,"bold")).place(x=1,y=1,height=100,width=400)
            else:
                con=mc.connect(user="root",host="localhost",password="root",database="pms")
                cr=con.cursor()
                cr.execute("SELECT CLASS,SECTION FROM class_detail")
                f=cr.fetchall()
                for i in f:
                    if i[0]==int(clas.get()) and i[1]==str(sec.get()):
                        w=tk.Tk("error")
                        w.geometry("400x120")
                        w.resizable(0,0)
                        tk.Label(w,text="CLASS ALREADY EXISTS",font=("Times New Roman",16,"bold")).place(x=1,y=1,height=100,width=400)
                        break
                else: 
                    cr.execute("INSERT INTO class_detail(`CLASS`,`SECTION`,`NUMBER OF SUBJECTS`,`NUMBER OF STUDENT`) VALUES('%d','%s','%d','%d')"%(int(clas.get()),str(sec.get()),int(stu.get()),int(sub.get())))
                    cr.execute("CREATE TABLE %d%s(`RN` INT,`NAME` VARCHAR(40),`SUBJECTS` VARCHAR(40))"%(int(clas.get()),str(sec.get())))
                    con.commit()
                    top.withdraw()
                    cp.update()
                    cp.deiconify()
    global back
    def back(ep,top):
        top.withdraw()
        ep.update()
        ep.deiconify()
    global SE
    def SE(sp):
        sp.withdraw()

        top=tk.Tk()
        top.minsize(148,1)
        top.maxsize(1924,1055)
        top.resizable(0,0)
        top.title("PMS")
        user32 = ctypes.windll.user32
        screen_width=user32.GetSystemMetrics(0)
        screen_height=user32.GetSystemMetrics(1)
        x = screen_width//2 - 926//2
        y = screen_height//2 -625//2
        top.geometry('926x625+%d+%d' %(x,y))

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
        

        #-----------------------entry and dropdowns----------------------------------------------
        con=mc.connect(user="root",password="root",host="localhost",database="pms")
        cr=con.cursor()
        cr.execute("select CLASS,SECTION from class_detail")
        f=cr.fetchall()
        C=[]
        S=[]
        for i in f:
            C.append(i[0])
            S.append(i[1])
        classes = C #etc
        variabl= tk.IntVar(top)
        variabl.set(classes[0]) 

        cl = tk.OptionMenu(top, variabl, *classes)
        cl.place(relx=0.313, rely=0.192, relheight=0.058,relwidth=0.060)
        cl.configure(background="white")
        cl.configure(disabledforeground="#a3a3a3")
        cl.configure(font=('Times New Roman',12,'bold'))
        cl.configure(foreground="#000000")

        secti = S #etc
        variable = tk.StringVar(top)
        variable.set(secti[0]) 

        sect= tk.OptionMenu(top, variable, *secti)
        sect.place(relx=0.832, rely=0.192, relheight=0.058, relwidth=0.060)
        sect.configure(background="white")
        sect.configure(disabledforeground="#a3a3a3")
        sect.configure(font=('Times New Roman',12,'bold'))
        sect.configure(foreground="#000000")

        r=tk.Entry(top,font=('Times New Roman',16,'bold'))
        r.place(relx=0.475, rely=0.448,height=44, relwidth=0.253)

        n=tk.Entry(top,font=('Times New Roman',16,'bold'))
        n.place(relx=0.475, rely=0.32,height=44, relwidth=0.253)

        s=['PHYSICS,CHEMISTRY,MATHS,CS,ENGLISH','PHYSICS,CHEMISTRY,MATHS,BIO,ENGLISH','PHYSICS,CHEMISTRY,HINDI,BIO,ENGLISH','HISTORY,POLITICAL SCIENCE,GEOGRAPHY,HINDI,ENGLISH','HISTORY,ECONOMICS,GEOGRAPHY,HINDI,ENGLISH','MATHS,SCIENCE,SSC,HINDI,ENGLISH,SANSKRIT','MATHS,SCIENCE,SSC,HINDI,ENGLISH','MATHS,ENGLISH,HINDI,EVS']
        var= tk.StringVar(top)
        var.set(s[0])

        su=tk.OptionMenu(top  , var , *s)
        su.place(relx=0.475, rely=0.56, relheight=0.074, relwidth=0.525)
        su.configure(background="white")
        su.configure(disabledforeground="#a3a3a3")
        su.configure(font=('Times New Roman',12,'bold'))
        su.configure(foreground="#000000")
        #-----------------------submit function--------------------------
        
        def sub():
            if str(r.get()).isdigit()==False  :
                w=tk.Tk("error")
                w.geometry("200x120")
                w.resizable(0,0)

                tk.Label(w,text="INVALID ROLL NUMBER",font=("Times New Roman",16,"bold")).place(x=1,y=1,height=100,width=200)

            elif len(str(n.get()))==0:
                
                w=tk.Tk("error")
                w.geometry("200x120")
                w.resizable(0,0)

                tk.Label(w,text="PLEASE ENTER NAME",font=("Times New Roman",16,"bold")).place(x=1,y=1,height=100,width=200)

            elif str(n.get()).isdigit()== True :
                w=tk.Tk("error")
                w.geometry("400x120")
                w.resizable(0,0)

                tk.Label(w,text="INVALID NAME",font=("Times New Roman",16,"bold")).place(x=1,y=1,height=100,width=400)
            
            else:
                
                con=mc.connect(user="root",host="localhost",password="root",database="pms")
                cr=con.cursor()
                cr.execute("INSERT INTO %d%s(`RN`,`NAME`,`SUBJECTS`) VALUES(%d,'%s','%s')"%(int(variabl.get()),str(variable.get()),int(r.get()),str(n.get()),str(var.get())))
                L=str(var.get()).split(",")
                for i in L:
                    cr.execute("INSERT INTO %s(`RN`,`CLASS`,`SECTION`,`NAME`) VALUES(%d,%d,'%s','%s')"%(i,int(r.get()),int(variabl.get()),str(variable.get()),str(n.get())))
                con.commit()
                                    
                    
            
       
        #--------------------Button----------------------------------------
        submit=tk.Button(top,text="SUBMIT",font=("Times New Roman",16,"bold"))
        submit.place(relx=0.713, rely=0.848, height=53, width=216)
        submit.configure(command=lambda:sub())

        bck=tk.Button(top,text="BACK",font=("Times New Roman",16,"bold"))
        bck.place(relx=0.41, rely=0.848, height=53, width=216)
        bck.configure(command=lambda:back(sp,top))

    global ReportEntry
    def ReportEntry(rp):
        rp.withdraw()
        top=tk.Tk()
        top.minsize(148,1)
        top.maxsize(1924,1055)
        top.resizable(0,0)
        top.title("PMS")
        user32 = ctypes.windll.user32
        screen_width=user32.GetSystemMetrics(0)
        screen_height=user32.GetSystemMetrics(1)
        x = screen_width//2 - 926//2
        y = screen_height//2 -625//2
        top.geometry('926x625+%d+%d' %(x,y))

        Label=tk.Label(top,text="PRE-REPORT",font=("Segoe UI Black",24,"normal"))
        Label.place(relx=0.324, rely=0.016, height=47, width=324)

        Class=tk.Label(top,text="SELECT CLASS",font=("Times New Roman",16,"normal"))
        Class.place(relx=0.032, rely=0.16, height=36, width=242)

        Sec=tk.Label(top,text="SELECT SECTION",font=("Times New Roman",16,"normal"))
        Sec.place(relx=0.032, rely=0.336, height=46, width=252)

        rn=tk.Label(top,text="ENTER ROLL NUMBER",font=("Times New Roman",16,"normal"))
        rn.place(relx=0.032, rely=0.544, height=46, width=342)
        
        con=mc.connect(user="root",password="root",database="pms",host="localhost")
        cr=con.cursor()
        cr.execute("select CLASS,SECTION from class_detail")
        f=cr.fetchall()
        C=[]
        S=[]
        for i in f:
            C.append(i[0])
            S.append(i[1])
        clas=C
        v=tk.IntVar(top)
        v.set(C[0])
        cl = tk.OptionMenu(top, v, *clas)
        cl.place(relx=0.497, rely=0.144, relheight=0.074, relwidth=0.256)
        cl.configure(background="white")
        cl.configure(disabledforeground="#a3a3a3")
        cl.configure(font=('Times New Roman',12,'bold'))
        cl.configure(foreground="#000000")

        sec=S
        var=tk.StringVar(top)
        var.set(S[0])
        s = tk.OptionMenu(top, var, *sec)
        s.place(relx=0.497, rely=0.336, relheight=0.074, relwidth=0.256)
        s.configure(background="white")
        s.configure(disabledforeground="#a3a3a3")
        s.configure(font=('Times New Roman',12,'bold'))
        s.configure(foreground="#000000")

        entry=tk.Entry(top,font=("Times New Roman",14,"normal"))
        entry.place(relx=0.497, rely=0.544,height=44, relwidth=0.253)

        button=tk.Button(top,text="SUBMIT",font=("Segoe UI Black",14,"normal"),command=lambda:Submit())
        button.place(relx=0.659, rely=0.816, height=63, width=196)

        bck=tk.Button(top,text="BACK",font=("Segoe UI Black",14,"normal"),command=lambda:back(rp,top))
        bck.place(relx=0.400, rely=0.816, height=63, width=196)

        def Submit():
            sub=[]
            nm=[]
            p1=[]
            p2=[]
            p3=[]
            h=[]
            se=[]
            
            con=mc.connect(user="root",password="root",database="pms",host="localhost")
            cr=con.cursor()
            cr.execute("SELECT * FROM %d%s"%(int(v.get()),str(var.get())))
            f=cr.fetchall()
            for i in f:
                if int(entry.get())==i[0]:
                    for j in i[2].split(","):
                        cr.execute("SELECT `NAME`,`PT-1/MT-1`,`PT-2/MT-2`,`PT-3/MT-3`,`HALF YEARLY`,`SESSION ENDING` FROM %s WHERE RN=%d"%(j,int(entry.get())))
                        k=cr.fetchall()
                        sub.append(j)
                        nm.append(k[0][0])
                        p1.append(k[0][1])
                        p2.append(k[0][2])
                        p3.append(k[0][3])
                        h.append(k[0][4])
                        se.append(k[0][5])
            report(top,int(v.get()),str(var.get()),int(entry.get()),nm,p1,p2,p3,h,se,sub)
                        
    global report       
    
    def report(rp,cl,sec,roll,nam,p1,p2,p3,h,se,sub):
        rp.withdraw()
        

        top=tk.Tk()
        top.minsize(148,1)
        top.maxsize(1924,1055)
        top.resizable(0,0)
        top.title("PMS")
        user32 = ctypes.windll.user32
        screen_width=user32.GetSystemMetrics(0)
        screen_height=user32.GetSystemMetrics(1)
        x = screen_width//2 - 926//2
        y = screen_height//2 -625//2
        top.geometry('926x625+%d+%d' %(x,y))
    
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

        cl=tk.Label(nf,text=cl,relief="groove",font=("Times New Roman",14,"normal"))
        cl.place(relx=0.173, rely=0.138, height=32, width=48)

        s=tk.Label(nf,text=sec,relief="groove",font=("Times New Roman",14,"normal"))
        s.place(relx=0.551, rely=0.138, height=32, width=30)

        rn=tk.Label(nf,text=roll,relief="groove",font=("Times New Roman",14,"normal"))
        rn.place(relx=0.897, rely=0.138, height=32, width=38)

        nm=tk.Label(nf,text=nam[0],relief="groove",font=("Times New Roman",14,"normal"))
        nm.place(relx=0.162, rely=0.621, height=32, width=230)

        button=tk.Button(top,text="HOME",font=("Times New Roman",16,"bold"),command=lambda:back(rp,top))
        button.place(relx=0.779, rely=0.912, height=43, width=176)

        marks=[p1,p2,p3,h,se]
        
        w1=[]
        w2=[]
        w3=[]
        wh=[]
        wse=[]
        for  i in p1:
            if i==None:
                i=0
            k=(i/80)*10
            w1.append(k)
        for j in p2:
            if j==None:
                j=0
            k=(j/80)*10
            w2.append(k)
        for l in p3:
            if l==None:
                l=0
            k=(k/80)*10
            w3.append(k)
        for m in h:
            if m== None:
                m=0
            k=(m/80)*20
            wh.append(k)
        for n in se:
            if n==None:
                n=0
            k=(n/80)*50
            wse.append(k)
        marks.append(w1)
        marks.append(w2)
        marks.append(w3)
        marks.append(wh)
        marks.append(wse)
        r=tk.Label(mf,text="SUBJECT",relief=RIDGE,font=("Times New Roman",10,"normal"))
        r.grid(row=0,column=0,sticky=NSEW)
        n=tk.Label(mf,text="PT-1",relief=RIDGE,font=("Times New Roman",10,"normal"))
        n.grid(row=0,column=1,sticky=NSEW)
        m=tk.Label(mf,text="PT-2",relief=RIDGE,font=("Times New Roman",10,"normal"))
        m.grid(row=0,column=2,sticky=NSEW)
        r1=tk.Label(mf,text="PT-3",relief=RIDGE,font=("Times New Roman",10,"normal"))
        r1.grid(row=0,column=3,sticky=NSEW)
        n1=tk.Label(mf,text="HY",relief=RIDGE,font=("Times New Roman",10,"normal"))
        n1.grid(row=0,column=4,sticky=NSEW)
        m1=tk.Label(mf,text="SEE",relief=RIDGE,font=("Times New Roman",10,"normal"))
        m1.grid(row=0,column=5,sticky=NSEW)
        r2=tk.Label(mf,text="WEIGHT. @ PT-1",relief=RIDGE,font=("Times New Roman",10,"normal"))
        r2.grid(row=0,column=6,sticky=NSEW)
        n2=tk.Label(mf,text="WEIGHT. @ PT-2",relief=RIDGE,font=("Times New Roman",10,"normal"))
        n2.grid(row=0,column=7,sticky=NSEW)
        m2=tk.Label(mf,text="WEIGHTAGE @ PT-3",relief=RIDGE,font=("Times New Roman",10,"normal"))
        m2.grid(row=0,column=8,sticky=NSEW)
        r3=tk.Label(mf,text="WEIGHTAGE @ HY",relief=RIDGE,font=("Times New Roman",10,"normal"))
        r3.grid(row=0,column=9,sticky=NSEW)
        n3=tk.Label(mf,text="WEIGHTAGE @ SEE",relief=RIDGE,font=("Times New Roman",10,"normal"))
        n3.grid(row=0,column=10,sticky=NSEW)
        
        for i in range(0,len(sub)):
                    
                    global cols
                    cols = []
                    for j in range(len(marks)):
                        if j==0:
                            p=tk.Label(mf,relief=RIDGE,text=sub[i])
                            p.grid(row=i+1, column=j, sticky=NSEW)
                            break
                    for j in range(len(marks)):
                        p=tk.Label(mf,relief=RIDGE,text=marks[j][i])
                        p.grid(row=i+1,column=j+1,sticky=NSEW)
                
                    

                            
                            

                        
                    
                        
        

        

                    

       
#----------------------------------------------------------------------


    
        

    
                
        
    
#----------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.withdraw()
    root.mainloop()

_init_(self,root)
    

