#
# Version 2 Cleaner
#

from tkinter import *
import json
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
from api import request, maintain_items



class App:
    def __init__(self, title):
        # self.start_frame = None
        # self.art_frame = None
        # self.visitor_frame = None

        self.root = Tk()
        self.root.title(title)
        self.root.geometry("1200x768+500+110")
        self.root.resizable(FALSE, FALSE)
        request('artObjects')
        maintain_items()

        self.frames = {
            'start': self.create_start_frame(),
            'visitor': self.create_visitor_frame(),
            'art': self.create_art_frame(),
            'houder': self.create_ghouder_frame(),
            'ghmenu': self.create_ghmenu_frame(),
            'bstukken': self.create_bstukken_frame(),
            'gcollectie': self.create_gcollectie_frame()
        }

    def hide_frames(self):
        for name, frame in self.frames.items():
            frame.grid_forget()

    def show_start_frame(self):
        self.hide_frames()
        self.frames['start'].grid()

    def show_visitor_frame(self):
        self.hide_frames()
        self.frames['visitor'].grid()

    def show_art_frame(self):
        self.hide_frames()
        self.frames['art'].grid()

    def show_ghouder_frame(self):
        self.hide_frames()
        self.frames['houder'].grid()

    def show_ghmenu_frame(self):
        self.hide_frames()
        self.frames['ghmenu'].grid()

    def show_bstukken_frame(self):
        self.hide_frames()
        self.frames['bstukken'].grid()

    def show_gcollectie_frame(self):
        self.hide_frames()
        self.frames['gcollectie'].grid()

    def start(self):
        self.show_start_frame()
        self.root.mainloop()

#
# Begin scherm bezoeker of gallerie houder
#
    def create_start_frame(self):
        start_frame = Frame(master=self.root)
        start_frame.grid()
        Buttonone = Button(master=start_frame, text="Bezoeker", background='red', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=30, height=30,
                           command=self.show_visitor_frame)
        Buttonone.grid(row=0)

        Buttontwo = Button(master=start_frame, text="Gallerie Houder", background='blue', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=30, height=30,
                           command=self.show_ghouder_frame)
        Buttontwo.grid(row=0, column=1)

        return start_frame

#
# Dit is het login scherm van de bezoeker
#
    def create_visitor_frame(self):
        visitor_frame = Frame(master=self.root)
        visitor_frame.grid()

        # button = Button(master=visitor_frame, text="fuck you")
        # button.grid()

        backbutton = Button(master=visitor_frame, text='<', command=self.show_start_frame)
        backbutton.grid(padx=20, pady=20)

        name_label = Label(master=visitor_frame, text="Uw naam:")
        name_label.grid(row=1)

        name_field = Entry(master=visitor_frame)
        name_field.grid(padx=20, pady=20, row=1, column=1)

        email_label = Label(master=visitor_frame, text="Uw email:")
        email_label.grid(row=2)

        email_field = Entry(master=visitor_frame)
        email_field.grid(padx=20, pady=20, row=2, column=1)

#
# Hier moet de werkende funcite die voor de login van de bezoeker is
#
        def handle_login_button():
            print(f"naam: {name_field.get()} email: {email_field.get()}")
            # if iets???
            self.show_art_frame()
        
        login_button = Button(master=visitor_frame, text='Aanmelden', command=handle_login_button)
        login_button.grid(padx=20, pady=20)

        return visitor_frame

#
# Hier moet alle stukken komen waar ze naar toe kunnen
#
    def create_art_frame(self):
        art_frame = Frame(master=self.root)
        art_frame.grid()

        backbutton = Button(master=art_frame, text='< Terug?', command=self.show_start_frame)
        backbutton.grid(padx=20, pady=20)

        return art_frame

#
# Dit is het login scherm van de gallerie houder
#
    def create_ghouder_frame(self):
        ghouder_frame = Frame(master=self.root)
        ghouder_frame.grid()

        backbutton = Button(master=ghouder_frame, text='<', command=self.show_start_frame)
        backbutton.grid(row=0, padx=20, pady=20)

        ID_label = Label(master=ghouder_frame, text="Uw gallerie ID")
        ID_label.grid(row=1)

        ID_field = Entry(master=ghouder_frame)
        ID_field.grid(padx=20, pady=20, row=1, column=1)

#
# Hier moet de werkende funcite die voor de login van de gallerie houder is1
#
        def handle_login_button():
            print(f"ID: {ID_field.get()}")
            # if iets???
            self.show_ghmenu_frame()

        login_button = Button(master=ghouder_frame, text='Login', command=handle_login_button)
        login_button.grid(padx=20, pady=20)

        return ghouder_frame

#
# Menu voor de gallerie houder
#
    def create_ghmenu_frame(self):
        ghmenu_frame = Frame(master=self.root)
        ghmenu_frame.grid()
        Buttonone = Button(master=ghmenu_frame, text="Beschikbare stukken", background='green', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=20, height=30,
                           command=self.show_bstukken_frame)
        Buttonone.grid(row=0)

        Buttontwo = Button(master=ghmenu_frame, text="Mijn stukken", background='yellow', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=20, height=30,
                           command=self.show_gcollectie_frame)
        Buttontwo.grid(row=0, column=1)

        Buttonthree = Button(master=ghmenu_frame, text="Bezoekers", background='orange', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=20, height=30,
                           command=self.show_ghouder_frame)
        Buttonthree.grid(row=0, column=2)

        return ghmenu_frame

    def create_bstukken_frame(self):
        bstukken_frame = Frame(master=self.root)
        bstukken_frame.grid(row=2)

        backbutton = Button(master=bstukken_frame, text='<', command=self.show_start_frame)
        backbutton.grid(row=0, ipadx=20, ipady=20)

        ID_label = Label(master=bstukken_frame, text="Hier kan je reserveren")
        ID_label.grid(row=0, column=2)


        #
        # Hier moet de werkende funcite die voor de reservatie van een kunst stuk is
        #
        def handle_reseveer_button():

            self.show_gcollectie_frame()

        with open('available.txt') as json_file:
            reserved_pieces = json.load(json_file)

            for key, value in reserved_pieces.items():
                key = key

            c = 1
            r_img = 2
            r_button = 3
            titel_text = 4
            for item in reserved_pieces:
                if item in reserved_pieces:
                    key = key
                    titel = reserved_pieces[item]['titel']
                    artiest = reserved_pieces[item]['artiest']
                    URL = reserved_pieces[item]['image']

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
                    img.grid(row=r_img, column=c)
                    reserveer_button = Button(master=bstukken_frame, text=f"Reserveer", command=handle_reseveer_button)
                    reserveer_button.grid(ipadx=2, ipady=2, row=r_button, column=c)
                    titel = label(master=bstukken_frame, text=f"{titel} van {artiest}")
                    titel.grid(ipadx=2, ipady=2, row=titel_text, column=c)

                    c = c + 1
                    while c > 3:
                        r_img = r_img + 2
                        r_button = r_button + 2
                        titel_text = titel_text + 2
                        c = 1
        return bstukken_frame

    def create_gcollectie_frame(self):
        gcollectie_frame = Frame(master=self.root)
        gcollectie_frame.grid(row=2)

        backbutton = Button(master=gcollectie_frame, text='<', command=self.show_start_frame)
        backbutton.grid(row=0, ipadx=20, ipady=20)

        ID_label = Label(master=gcollectie_frame, text="Dit zijn jouw gereserveerde kunststukken.")
        ID_label.grid(row=0, column=2)


        #
        # Hier moet de werkende funcite die voor de reservatie van een kunst stuk is
        #

        with open('reserved.txt') as json_file:
            reserved_pieces = json.load(json_file)

            for key, value in reserved_pieces.items():
                key = key

            r_img = 2
            c = 1
            for item in reserved_pieces:
                if item in reserved_pieces:
                    key = key
                    titel = reserved_pieces[item]['titel']
                    artiest = reserved_pieces[item]['artiest']
                    URL = reserved_pieces[item]['image']

                    u = urllib.request.urlopen(URL)
                    raw_data = u.read()
                    u.close()

                    im = Image.open(BytesIO(raw_data))
                    width = 80
                    height = 80
                    im2 = im.resize((width, height))
                    photo = ImageTk.PhotoImage(im2)

                    img = Label(master=gcollectie_frame, image=photo)
                    img.image = photo
                    img.grid(row=r_img, column=c)

                    c = c + 1
                    while c > 3:
                        r_img = r_img + 2
                        c = 1
        return gcollectie_frame


app = App("Rijksmuseum")
app.start()
