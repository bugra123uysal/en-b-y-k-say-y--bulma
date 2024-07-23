import keyboard




from time import strftime



import tkinter as tk


sayılar=[]
a=tk.Tk()
a.title("büyük sayı")
a.geometry("600x800")

i=tk.Entry(a,text="")
i.place(x=10, y=50)
""" sayıların verilerini gönderir """


""" saati gösterir """
def nowtime():
     watch=strftime('%H:%M:%S %p')
     s.config(text=watch)
     s.after(1000,nowtime)
  

s=tk.Label(a,)
s.place(x=500,y=600, height=30,width=210)

""" sonuç gösterme """
gör=tk.Label(a, bd=2, relief="solid")
gör.place(x=350,y=20,height=30, width=300, )

   



nowtime()
def aaa():
     adg=i.get()
     try:

     
        """ int olarak eklemek """
        sayılar.append(int(adg))
        gör['text']=' '.join(map(str,sayılar))
     except ValueError:
          gör["text"]="hata oluştu"
     i.delete(0,tk.END)
    
    
     print("bitti")
    
""" sayıları girip verileri gönderme """
bs=tk.Button(a,text="gönder", command=aaa )
bs.place(x=140, y=250)
def bitti():
      
      sayılar.sort(reverse=True) 
      gör.config(text=' '.join(map(str,sayılar)))
     
      
""" sonucu gösterme buttonu """
bas=tk.Button(a,text="bittir", command=bitti  )
bas.place(x=140, y=50) 
    

     


a.mainloop()




