import tkinter as tk
my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window 

l1 = tk.Listbox(my_w)
l1.grid(row=1,column=1) 

l1.insert(1,'PHP')   # Adding one element to Listbox 
l1.insert(2,'Python')
l1.insert(3,'MySQL')

print(l1.get(0))  # Output PHP
print(l1.get(2))  # Output MySQL
ll = l1.get(0)
lb = tk.Label(my_w,width=10, text=ll, fg='blue')
lb.grid(row=2,column=1) 
my_w.mainloop()  # Keep the window open