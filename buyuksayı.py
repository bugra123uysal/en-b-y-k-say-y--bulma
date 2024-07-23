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
""" büyükden küçüğe """
def bdenkye():
    
      sayılar.sort(reverse=True) 
      gör.config(text=' '.join(map(str,sayılar)))

""" küçükden büyüğe """
def kdenbye():
     
     sayılar.sort()    
     gör.config(text=' '.join(map(str,sayılar)))
""" en büyüğü bulmak """ 
def byk():
     if sayılar:
          bınumbers=max(sayılar)
         

          gör.config(text=bınumbers)
                     
     else:
          gör.config(text="hatalı tekrar deneyiniz")
                                        
""" en küçük  olanı bulmak  """
def gck():
     if sayılar:
          guccuksayı=min(sayılar)

          gör.config(text=guccuksayı)
     else:
            gör.config(text="hatalı tekrar deneyin")
              
     

      
    
    
"""büyükden küçüğe  sonucu gösterme buttonu """
bas=tk.Button(a,text="b-k", command=bdenkye)
bas.place(x=140, y=50) 
    
""" küçükden büyüğe sıralama buttonu """
kb=tk.Button(a,text="k-b", command=kdenbye)
kb.place(x=250, y=50) 
     
"""  en büyük sayıyı bulmak """
big=tk.Button(a,text="büyük",command=byk)
big.place(x=350, y=50)

""" en küçük sayıyı bulma """
smaln=tk.Button(a,text="küçük", command=gck)
smaln.place(x=450, y=50)

a.mainloop()




