import keyboard




from time import strftime 



import tkinter as tk



a=tk.Tk()
a.title("büyük sayı")
a.geometry("600x800")

i=tk.Entry(a,text="")
i.place(x=10, y=50)
""" sayıların verilerini gönderir """
def aaa():
    adg=i.get()
    selam=", ".join(adg)
    gör.config(text=selam)
    
 

def fines():
    print("bitti")
    
def nowtime():
    watch=strftime('%H:%M:%S %p')
    s.config(text=watch)
    s.after(1000,nowtime)

s=tk.Label(a,)
s.place(x=500,y=600, height=30,width=210)

""" sayıları girip verileri gönderme """
bs=tk.Button(a,text="gönder", command=aaa )
bs.place(x=140, y=250)

gör=tk.Label(a)
gör.place(x=400,y=20,height=30, width=200)
   
""" sonucu göster """
bas=tk.Button(a,text="bittir", command=fines )
bas.place(x=140, y=50)



a.mainloop()





