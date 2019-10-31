from tkinter import *


class App:
    def __init__(self, title):
        # self.start_frame = None
        # self.art_frame = None
        # self.visitor_frame = None

        self.root = Tk()
        self.root.title(title)
        self.root.geometry("800x740+500+110")

        self.frames = {
            'start': self.create_start_frame(),
            'visitor': self.create_visitor_frame(),
            'art': self.create_art_frame()
        }

    def hide_frames(self):
        for name, frame in self.frames.items():
            frame.pack_forget()

    # def show_frame(self, name):
    #     self.hide_frames()
    #     self.frames[name].pack()

    def show_visitor_frame(self):
        self.hide_frames()
        self.frames['visitor'].pack()

    def show_start_frame(self):
        self.hide_frames()
        self.frames['start'].pack()

    def show_art_frame(self):
        self.hide_frames()
        self.frames['art'].pack()

    def start(self):
        self.show_start_frame()
        self.root.mainloop()
    
    def create_start_frame(self):
        start_frame = Frame(master=self.root)
        start_frame.pack(fill="both", expand=True)
        Buttonone = Button(master=start_frame, text="Bezoeker", background='red', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=30, height=30,
                           command=self.show_visitor_frame)
        Buttonone.pack(side="left")

        Buttontwo = Button(master=start_frame, text="Gallery Holder", background='blue', foreground='black',
                           font=('Helvetica', 16, 'bold italic'), width=30, height=30,
                           command=self.show_visitor_frame)
        Buttontwo.pack(side="left")

        loginfield = Entry(master=start_frame)
        loginfield.pack(padx=20, pady=20)

        # loginbutton = Button(master=start_frame, text='login', command=logingh)
        # loginbutton.pack(padx=20, pady=20)

        return start_frame
    
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
        
        def handle_login_button():
            print(f"naam: {name_field.get()} email: {email_field.get()}")
            # if iets???
            self.show_art_frame()
        
        login_button = Button(master=visitor_frame, text='Aanmelden', command=handle_login_button)
        login_button.pack(padx=20, pady=20)

        return visitor_frame
        
    def create_art_frame(self):
        art_frame = Frame(master=self.root)
        art_frame.pack(fill="both", expand=True)

        backbutton = Button(master=art_frame, text='< Terug?', command=self.show_start_frame)
        backbutton.pack(padx=20, pady=20)

        return art_frame


app = App("Rijksmuseum")
app.start()
