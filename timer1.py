from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox


root=Tk()
root.title("timer")
root.configure(bg="grey")
root.geometry("220x200")

sec=StringVar()
min=StringVar()
hours=StringVar()

hours_combo=ttk.Combobox(root,width=5,textvariable=hours)
hours_combo["values"] =("00","01","02","03","04","05","06","07","08","09","10","11","12")
hours_combo["state"]="readonly"
hours_combo.current(0)
hours_combo.place(x=20,y=30)

min_combo=ttk.Combobox(root,width=5,textvariable=min)
min_combo["values"] =("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")  
min_combo["state"]="readonly"
min_combo.current(0)
min_combo.place(x=80,y=30)

sec_combo=ttk.Combobox(root,width=5,textvariable=sec)
sec_combo["values"] =("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")  
sec_combo["state"]="readonly"
sec_combo.current(0)
sec_combo.place(x=140,y=30)

enthours=StringVar()
entmin=StringVar()
entsec=StringVar()

enthours.set('00')
entmin.set('00')
entsec.set('00')
frame=Frame(root,width=20).pack()

ent1=Label(frame,textvariable=enthours,font=("Arial",30),fg="red",bg="grey").place(x=13,y=160)
ent1=Label(frame,textvariable=entmin,font=("Arial",30),fg="red",bg="grey").place(x=87,y=160)
ent1=Label(frame,textvariable=entsec,font=("Arial",30),fg="red",bg="grey").place(x=160,y=160)



def start():

    try:
        usre_input=int(hours.get())*3600+int(min.get())*60+int(sec.get())
    except:
        messagebox.showwarning("warning","invalid option")
    while usre_input>=0:
        hours1=usre_input//3600
        extasec=usre_input-3600*hours1
        min1=extasec//60
        sec1=extasec%60

        enthours.set(hours1)
        entmin.set(min1)
        entsec.set(sec1)
        
        root.update()
        time.sleep(1)

        usre_input-=1

btn=Button(text="START",width=10,height=2,bg="red",fg="white",command=start).place(x=65,y=70)
root.mainloop()
