#
# Version 2 Cleaner
#

from tkinter import *
import json
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
from api import request, maintain_items
from functools import partial


class App:
    def __init__(self, title):
        # self.start_frame = None
        # self.art_frame = None
        # self.visitor_frame = None

        """
           Here we define standard settings that wil be used through out the whole app
        """

        self.root = Tk()
        self.root.title(title)
        self.root.geometry("1200x768+500+110")
        self.root.resizable(FALSE, FALSE)
        request('artObjects')
        maintain_items()

        """
            Here we create a dictonairy for each frame we show in the app
        """

        self.frames = {
            'start': self.create_start_frame(),
            'visitor': self.create_visitor_frame(),
            'art': self.create_art_frame(),
            'houder': self.create_ghouder_frame(),
            'ghmenu': self.create_ghmenu_frame(),
            'bstukken': self.create_bstukken_frame(),
            'gcollectie': self.create_gcollectie_frame()
        }

    """
        Here we define for each screen you what action should be taken to be able to show the correct screen
    """

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

    """
        This is the first screen users will be able to see when they startup the app
        with 2 buttons one for the gallery holders and the other for the visitors
    """

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

    """
        Here we created the login page for the visitors where they have to fill in their Name and Email
    """

    def create_visitor_frame(self):
        visitor_frame = Frame(master=self.root)
        visitor_frame.grid()

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

        """
            This is the function for when the visitor presses login
        """

        def handle_login_button():
            print(f"naam: {name_field.get()} email: {email_field.get()}")
            # if iets???
            self.show_art_frame()

        login_button = Button(master=visitor_frame, text='Aanmelden', command=handle_login_button)
        login_button.grid(padx=20, pady=20)

        return visitor_frame

    """
        This is the function for when the visitor presses login
    """

    def create_art_frame(self):
        art_frame = Frame(master=self.root)
        art_frame.grid()

        backbutton = Button(master=art_frame, text='< Terug?', command=self.show_start_frame)
        backbutton.grid(padx=20, pady=20)

        return art_frame

    #
    # Dit is het login scherm van de gallerie houder
    #
    gh_id = 0

    def create_ghouder_frame(self):
        ghouder_frame = Frame(master=self.root)
        ghouder_frame.grid()

        backbutton = Button(master=ghouder_frame, text='<', command=self.show_start_frame)
        backbutton.grid(row=0, padx=20, pady=20)

        ID_label = Label(master=ghouder_frame, text="Uw gallerie ID")
        ID_label.grid(row=1)

        ID_field = Entry(master=ghouder_frame)
        ID_field.grid(padx=20, pady=20, row=1, column=1)

        """
            This is the function for when the gallary holder presses login
        """

        def handle_login_button():
            global gh_id
            gh_id = ID_field.get()
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

        """
            This is the function to reserve a art piece
        """

        def handle_reseveer_button(id):
            global gh_id
            with open('available.txt') as json_file:
                available = json.load(json_file)
            with open('reserved.txt') as json_file:
                reserved = json.load(json_file)

            temp = {}
            for key, value in available.items():
                if key == id:
                    temp[id] = available[key]
                    reserved[gh_id] = temp

                    with open('reserved.txt', 'w') as outfile:
                        json.dump(reserved, outfile)

        #self.show_gcollectie_frame()

        with open('available.txt') as json_file:
            reserved_pieces = json.load(json_file)

            for key, value in reserved_pieces.items():
                key = key

            c = 1
            r_img = 2
            r_button = 3
            titel_text = 4
            q = 0
            button_id = []
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

                    img = Button(master=bstukken_frame, image=photo, command=partial(handle_reseveer_button, item))
                    img.image = photo
                    img.grid(row=r_img, column=c)
                    button_id.append(img)
                    # titel = Label(master=bstukken_frame, text=f"{titel} van {artiest}")
                    # titel.grid(ipadx=2, ipady=2, row=titel_text, column=c)

                    c += 1
                    while c > 3:
                        r_img += 2
                        titel_text += 1
                        c = 1
        return bstukken_frame

    """
        This is to create the collection frame from a gallery holder
    """

    def create_gcollectie_frame(self):
        gcollectie_frame = Frame(master=self.root)
        gcollectie_frame.grid(row=2)

        backbutton = Button(master=gcollectie_frame, text='<', command=self.show_start_frame)
        backbutton.grid(row=0, ipadx=20, ipady=20)

        ID_label = Label(master=gcollectie_frame, text="Dit zijn jouw gereserveerde kunststukken.")
        ID_label.grid(row=0, column=2)

        """
            This is the function to gather the information to show to correct art pieces that the gallery holder reserved
        """

        global gh_id
        gh_id = "test1"
        with open('reserved.txt') as json_file:
            reserved_pieces = json.load(json_file)

            for key, value in reserved_pieces.items():
                kunst_id = value
                for key in kunst_id:
                    kunst_id = key

            r_img = 2
            c = 1
            for item in reserved_pieces:
                if item in reserved_pieces:
                    key = key
                    titel = reserved_pieces[item][kunst_id]['titel']
                    artiest = reserved_pieces[item][kunst_id]['artiest']
                    URL = reserved_pieces[item][kunst_id]['image']

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
