#
# Version 2 Cleaner
#

from tkinter import *
import json
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
from api import request, keep_reserved



class App:
    def __init__(self, title):
        # self.start_frame = None
        # self.art_frame = None
        # self.visitor_frame = None

        self.root = Tk()
        self.root.title(title)
        self.root.geometry("800x730+500+110")
        request('artObjects')
        keep_reserved()

        self.frames = {
            'start': self.create_start_frame(),
            'visitor': self.create_visitor_frame(),
            'art': self.create_art_frame(),
            'houder': self.create_ghouder_frame(),
            'ghmenu': self.create_ghmenu_frame(),
            'bstukken': self.create_bstukken_frame()
        }

    def hide_frames(self):
        for name, frame in self.frames.items():
            frame.pack_forget()

    def show_start_frame(self):
        self.hide_frames()
        self.frames['start'].pack()

    def show_visitor_frame(self):
        self.hide_frames()
        self.frames['visitor'].pack()

    def show_art_frame(self):
        self.hide_frames()
        self.frames['art'].pack()

    def show_ghouder_frame(self):
        self.hide_frames()
        self.frames['houder'].pack()

    def show_ghmenu_frame(self):
        self.hide_frames()
        self.frames['ghmenu'].pack()

    def show_bstukken_frame(self):
        self.hide_frames()
        self.frames['bstukken'].pack()

    def start(self):
        self.show_start_frame()
        self.root.mainloop()

#
# Begin scherm bezoeker of gallerie houder
#
    def create_start_frame(self):
        start_frame = Frame(master=self.root)
        start_frame.pack(fill="both", expand=True)
        Buttonone = Button(master=start_frame, text="Bezoeker", background='red', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=30, height=30,
                           command=self.show_visitor_frame)
        Buttonone.pack(side="left")

        Buttontwo = Button(master=start_frame, text="Gallerie Houder", background='blue', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=30, height=30,
                           command=self.show_ghouder_frame)
        Buttontwo.pack(side="left")

        return start_frame

#
# Dit is het login scherm van de bezoeker
#
    def create_visitor_frame(self):
        visitor_frame = Frame(master=self.root)
        visitor_frame.pack(fill="both", expand=True)

        # button = Button(master=visitor_frame, text="fuck you")
        # button.pack()

        backbutton = Button(master=visitor_frame, text='<', command=self.show_start_frame)
        backbutton.pack(padx=20, pady=20)

        name_label = Label(master=visitor_frame, text="Uw naam:")
        name_label.pack(side="left")

        name_field = Entry(master=visitor_frame)
        name_field.pack(padx=20, pady=20, side="left")

        email_label = Label(master=visitor_frame, text="Uw email:")
        email_label.pack(side="left")

        email_field = Entry(master=visitor_frame)
        email_field.pack(padx=20, pady=20, side="left")

#
# Hier moet de werkende funcite die voor de login van de bezoeker is
#
        def handle_login_button():
            print(f"naam: {name_field.get()} email: {email_field.get()}")
            # if iets???
            self.show_art_frame()
        
        login_button = Button(master=visitor_frame, text='Aanmelden', command=handle_login_button)
        login_button.pack(padx=20, pady=20)

        return visitor_frame

#
# Hier moet alle stukken komen waar ze naar toe kunnen
#
    def create_art_frame(self):
        art_frame = Frame(master=self.root)
        art_frame.pack(fill="both", expand=True)

        backbutton = Button(master=art_frame, text='< Terug?', command=self.show_start_frame)
        backbutton.pack(padx=20, pady=20)

        return art_frame

#
# Dit is het login scherm van de gallerie houder
#
    def create_ghouder_frame(self):
        ghouder_frame = Frame(master=self.root)
        ghouder_frame.pack(fill="both", expand=True)

        backbutton = Button(master=ghouder_frame, text='<', command=self.show_start_frame)
        backbutton.pack(padx=20, pady=20)

        ID_label = Label(master=ghouder_frame, text="Uw gallerie ID")
        ID_label.pack(side="left")

        ID_field = Entry(master=ghouder_frame)
        ID_field.pack(padx=20, pady=20, side="left")

#
# Hier moet de werkende funcite die voor de login van de gallerie houder is1
#
        def handle_login_button():
            print(f"ID: {ID_field.get()}")
            # if iets???
            self.show_ghmenu_frame()

        login_button = Button(master=ghouder_frame, text='Login', command=handle_login_button)
        login_button.pack(padx=20, pady=20)

        return ghouder_frame

#
# Menu voor de gallerie houder
#
    def create_ghmenu_frame(self):
        ghmenu_frame = Frame(master=self.root)
        ghmenu_frame.pack(fill="both", expand=True)
        Buttonone = Button(master=ghmenu_frame, text="Beschikbare stukken", background='green', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=20, height=30,
                           command=self.show_bstukken_frame)
        Buttonone.pack(side="left")

        Buttontwo = Button(master=ghmenu_frame, text="Mijn stukken", background='yellow', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=20, height=30,
                           command=self.show_ghouder_frame)
        Buttontwo.pack(side="left")

        Buttonthree = Button(master=ghmenu_frame, text="Bezoekers", background='orange', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=20, height=30,
                           command=self.show_ghouder_frame)
        Buttonthree.pack(side="left")

        return ghmenu_frame

    def create_bstukken_frame(self):
        bstukken_frame = Frame(master=self.root)
        bstukken_frame.grid(row=2)

        backbutton = Button(master=bstukken_frame, text='<', command=self.show_start_frame)
        backbutton.grid(row=0, column=1, ipadx=20, ipady=20)

        ID_label = Label(master=bstukken_frame, text="Hier kan je reserveren")
        ID_label.grid(row=0)


        #
        # Hier moet de werkende funcite die voor de reservatie van een kunst stuk is
        #
        def handle_reseveer_button():

            self.show_gcollectie_frame()

        with open('available.txt') as json_file:
            art_pieces = json.load(json_file)

            for key, value in art_pieces.items():
                key = key

            n = 0
            for item in art_pieces:
                if item in art_pieces:
                    key = key
                    titel = art_pieces[item]['titel']
                    artiest = art_pieces[item]['artiest']
                    URL = art_pieces[item]['image']

                    u = urllib.request.urlopen(URL)
                    raw_data = u.read()
                    u.close()

                    im = Image.open(BytesIO(raw_data))
                    width = 80
                    height = 80
                    im2 = im.resize((width, height))
                    photo = ImageTk.PhotoImage(im2)

                    img = Label(master=bstukken_frame, image=photo)
                    img.image = photo
                    img.grid(row=n)
                    login_button = Button(master=bstukken_frame, text="Reserveer", command=handle_reseveer_button)
                    login_button.grid(ipadx=20, ipady=20, row=n)
                    n = n + 1
        return bstukken_frame


app = App("Rijksmuseum")
app.start()
