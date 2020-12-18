import os,shutil
import os.path, time , datetime
from datetime import date
import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar
from tkinter import BooleanVar
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT , RIGHT, Listbox ,Checkbutton
from tkinter.ttk import Frame, Label, Entry ,Radiobutton
from shutil import copyfile

master = tk.Tk()
folder_path1 = StringVar()
folder_path2 = StringVar()
var = tk.StringVar()

master.title("Copy Files V18.12.63")

frame1 = tk.Frame(master, width=170, height=45,)
frame1.pack()

#ฟังชั่น

def getfiles1():

    global folder_path1
    filename = filedialog.askdirectory()
    folder_path1.set(filename)
    ent1.configure(text=folder_path1)

def getfiles2():

    global folder_path2
    filename = filedialog.askdirectory()
    folder_path2.set(filename)
    ent2.configure(text=folder_path2)
    foles_old()

#ค้นหาไฟล์ที่สร้างวันนี้
def foles_old():

    today = date.today()
    NowDate = today.strftime("%d/%m/%Y") #วันนี้
            
    res1 = ent1.get()
    #lbl3.configure(text=res1)
    with os.scandir(res1) as i:
        for entry in i:

            src = os.path.getmtime(entry.path)
            sctime = datetime.datetime.fromtimestamp(src)
            FileDate = sctime.strftime("%d/%m/%Y")

            if FileDate == NowDate:

                listbox.insert('end',FileDate + "   " + entry.path)
   

def datet():
    time1 = ''
    time2 = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        lbl3.config(text=time2)

    lbl3.after(200, datet)  


labelra = tk.Label(master)
tt = labelra.cget("text")
#tt = '22:33:00'

def Time_run():
    
    time1 = ''
    time2 = datetime.datetime.now().strftime('%H:%M:%S')
    
    
    if time2 != time1:
        time1 = time2
        timm = time2
 
    master.after(1000, Time_run)
    
    if tt == timm:
        #เมื่อถึงเวลาที่กำหนด 
        foles_old() #ค้นหาไฟล์ที่เก่ากว่าวันนี้
        foles_oldcc() #คัดลอกไฟล์ที่อยู่ใน Listbox แล้วลบข้อมูล
        
#คำสั่งให้ย้ายข้อมูลทันที
def Run_now():
    foles_old()
    foles_oldcc()
    

def radioCall1():
    labelra.config(text = '12:00:00')
    
def radioCall2():
    labelra.config(text = '24:00:00')

#Copy จาก
lbl1 = tk.Label(master=frame1,width=10, text="Copy From : ", anchor="e")
lbl1.grid(column=0,row=0)
ent1 = tk.Entry(master=frame1,width=60,state="disabled")
ent1.grid(column=1, row=0)
ent1.columnconfigure(0, weight=1)
btn1 = tk.Button(master=frame1,width=10,text="From",command=getfiles1)
btn1.grid(column=2, row=0)

#Copy ถึง
lbl2 = tk.Label(master=frame1,width=10, text="Copy To : ", anchor="e")
lbl2.grid(column=0,row=1)
ent2 = tk.Entry(master=frame1,width=60,state="disabled")
ent2.grid(column=1, row=1)
ent2.columnconfigure(0, weight=1)
btn2 = tk.Button(master=frame1,width=10,text="To",command=getfiles2)
btn2.grid(column=2, row=1)

#วันที่ เวลา
lbl3 = tk.Label(master=frame1 , fg='red')
lbl3.grid(column=1,row=3)

#radio เลือก

rad1 = tk.Radiobutton(master=frame1,text='Every day 12:00', value="12:00:00" , command=radioCall1)
rad1.grid(column=0,row=4) 
rad2 = tk.Radiobutton(master=frame1,text='Every day 24:00', value="24:00:00" , command=radioCall2)
rad2.grid(column=1,row=4)

radnow = tk.Button(master=frame1,width=10,text="RUN Now!",command=Run_now)
radnow.grid(column=2, row=4)

#ListFiles
listbox = tk.Listbox(master=frame1)
listbox.grid(columnspan = 6)
listbox['width'] = 95


#สแดงที่เสือก
labelra = tk.Label(master=frame1,width=10, text="24:00:00", fg='white')
labelra.grid(column=0,row=6)

#cr
labelra = tk.Label(master=frame1,width=10, text="@Nopparat.IT", fg='gray')
labelra.grid(column=2,row=6)

       
def foles_oldcc():
    
    today = date.today()
    NowDate = today.strftime("%d/%m/%Y") #วันนี้
            
    res1 = ent1.get()
    res2 = ent2.get()
    #lbl3.configure(text=res1)
    with os.scandir(res1) as i:
        for entry in i:

            src = os.path.getmtime(entry.path)
            sctime = datetime.datetime.fromtimestamp(src)
            FileDate = sctime.strftime("%d/%m/%Y")

            if FileDate == NowDate:
                #คำสั่ง Copy Files
                shutil.copy2(res1+"/"+entry.name, res2)
                listbox.delete(0,'end')
                listbox.delete(1,'end')
                listbox.delete(2,'end')
                listbox.delete(3,'end')
                listbox.delete(4,'end')
                listbox.delete(5,'end')
                listbox.delete(6,'end')
                listbox.delete(7,'end')
                listbox.delete(8,'end')
                listbox.delete(9,'end')
          

Time_run()
datet()
master.mainloop()