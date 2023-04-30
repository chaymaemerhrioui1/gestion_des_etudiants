from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import time


def login_page():
    root.destroy()
    import realacceuil





class NewsTicker(tk.Frame):
    def __init__(self, master, news_items):
        super().__init__(master)

        # Set up the news items
        self.news_items = news_items
        self.current_item = 0

        # Create the label for displaying news items
        self.news_label = tk.Label(self, font=("Arial", 16), wraplength=600)
        self.news_label.place(x=100,y=0)

        # Create the label for displaying images
        self.image_label = tk.Label(self)
        self.image_label.pack(ipady=150, padx=120,pady=120)
        #self.image_label.place(x=100,y=100)

        # Start the ticker animation
        self.animate()

    def animate(self):
        # Get the current news item and update the labels
        item = self.news_items[self.current_item]
        self.news_label.config(text=item["title"])

        # Load the image for the current news item and update the label
        image = Image.open(item["image"])
        image = image.resize((400, 450), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Increment the current item counter
        self.current_item += 1
        if self.current_item >= len(self.news_items):
            self.current_item = 0

            # Schedule the next animation
        self.after(3000, self.animate)

 # Define the news items
news_items = [
    {
        "title": "\n\n\n  Le Roi ouvert ENSAH en 2008 avec 50 MDH",
        "image": "le-roi.png"
    },
    {
        "title": "\n\n\n  Sortie pedagogique par le culb génit civil ",
        "image": "genie-civil.png"
    },
    {
        "title": "\n\n\n L'ENSA d'Al Hoceima abrite l'Entrepreneurial Exchange 1.0",
        "image": "exchang-01.png"
    },
    {
        "title":"\n\n\n\t Activité universale ",
        "image": "activity.png"
    }
]

# Create the main window
root = tk.Tk()
root.geometry("990x660")
root.resizable(0, 0)
root.title("Home")
# Create the news ticker widget
news_ticker = NewsTicker(root, news_items)
news_ticker.pack()

"""Label(root,text="Email: chaymaemerhrioui@gmail.com",width=10,height=3,
      bg="#12c4c0",anchor='e').pack(side=TOP,fill=X)"""

l1 = Label(root, text='                                                                                                                               \n'
           ,fg='white', bg='#12c4cf')
l1.config(font=('Arial', 22))
l1.pack(expand=True)
l1.place(x=0,y=0)

bg1 = PhotoImage(file="t1.png")
label1 = Label(root, image=bg1)
label1.place(x=90,y=25)


loginButton=Button(root,text='Menu',font=('Open Sans','9','bold underline'),bg='white',fg='#12c4c0',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',
                   command=login_page)
loginButton.place(x=18,y=5)

l1 = Label(root, text='ENSA d Al-Hoceima \n', fg='white', bg='goldenrod2')
l1.config(font=('Arial', 20))
l1.pack(expand=True)
l1.place(x=0,y=550)

l2=Label(root,text='L Ecole Nationale des Sciences Appliquées d Al hoceima est un établissement public d enseignement\n'
                   ' supérieur relevant de l université Abdelmalek Essaadi. Sa création s inscrit dans l optique de \n'
                   'favoriser la formation des ingénieurs d Etat hautement qualifiés dans les spécialités les plus ouvertes\n'
                   ' et susceptibles de connaître d importants développements au sein du tissu socio-économique \n'
                   'régional et'
                   'national. Le positionnement de l Ecole contribuera à lui conférer une dimension \n'
                   'euro-méditerranéenne et à'
                   ' répondre aux besoins régionaux et nationaux en matière de formation en ingénierie . \n')
l2.config(font=('Arial', 10))
l2.pack(expand=True)
l2.place(x=250,y=550)




root.mainloop()
