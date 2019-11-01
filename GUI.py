from tkinter import *
from api import request

request('artObjects')

def keuzeframe():
   hoofdframe.pack_forget() #Verberg
   startframe.pack() #Toon


def toonGHFrame():
   startframe.pack_forget() #Verberg
   hoofdframe.pack() #Toon


def logingh():
   if loginfield.get() == "admin":
       toonGHFrame()
   else:
       print('Verkeerde gebruikersnaam!')


root = Tk()
root.title("RijksMuseum")
root.geometry("800x740+500+110")
startframe = Frame(master=root)
startframe.pack(fill="both", expand=True)
Buttonone = Button(master=startframe, text="Bezoeker", background='red', foreground='black',
                    font=('Helvetica', 16, 'bold italic'), width=30, height=30,
                    command=toonGHFrame)
Buttonone.pack(side="left")

Buttontwo = Button(master=startframe, text="Gallery Holder", background='blue', foreground='black',
                    font=('Helvetica', 16, 'bold italic'), width=30, height=30,
                   command=toonGHFrame)
Buttontwo.pack(side="left")

loginfield = Entry(master=startframe)
loginfield.pack(padx=20, pady=20)


loginbutton = Button(master=startframe, text='login', command=logingh)
loginbutton.pack(padx=20, pady=20)


hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)


button = Button(master=hoofdframe, text="fuck you")
button.pack()
backbutton = Button(master=hoofdframe, text='<', command=keuzeframe)
backbutton.pack(padx=20, pady=20)


keuzeframe()
root.mainloop()











# startframe = Frame(master=root)
# startframe.pack(fill="both", expand=True)
# Buttonone = Button(text="Bezoeker", background='red', foreground='black',
#                    font=('Helvetica', 16, 'bold italic'), width=30, height=30,
#                    command=toonHoofdFrame)
# Buttonone.pack(side="left")
# Buttontwo = Button(text="Gallery Holder", background='blue', foreground='black',
#                    font=('Helvetica', 16, 'bold italic'), width=30, height=30)
# Buttontwo.pack(side="left")
#
#
# hoofdframe = Frame(master=root)
# hoofdframe.pack(fill="both", expand=True)
# backbutton = Button(master=hoofdframe, text='<', command=toonLoginFrame)
# backbutton.pack(padx=20, pady=20)
#
# root.mainloop()
# toonHoofdFrame()
