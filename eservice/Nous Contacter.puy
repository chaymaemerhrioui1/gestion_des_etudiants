import tkinter as tk
from PIL import ImageTk, Image
import webbrowser

#Création de la fenêtre principale
root = tk.Tk()
root.geometry("600x600")
root.title("About")

#Création des images
img1 = Image.open("salma2.png")
img1 = img1.resize((200, 200), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(img1)

img2 = Image.open("chaymae2.png")
img2 = img2.resize((200, 200), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(img2)

img3 = Image.open("chadi.png")
img3 = img3.resize((200, 200), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(img3)

img4 = Image.open("israe.png")
img4 = img4.resize((200, 200), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(img4)

# Création des labels pour afficher les images
label1 = tk.Label(root, image=photo1)
label1.grid(row=0, column=0, padx=20, pady=20)
button1 = tk.Button(root, text="Salma Fannich \n Linkedin", command=lambda: webbrowser.open_new_tab("https://www.linkedin.com/in/salma-fannich-019992252"))
button1.grid(row=1, column=0)

label2 = tk.Label(root, image=photo2)
label2.grid(row=0, column=1, padx=20, pady=20)
button2 = tk.Button(root, text="Chaymae Merhrioui \n Linkedin", command=lambda: webbrowser.open_new_tab("https://www.linkedin.com/in/chaymae-merhrioui-4458081a5"))
button2.grid(row=1, column=1)

label3 = tk.Label(root, image=photo3)
label3.grid(row=2, column=0, padx=20, pady=20)
button3 = tk.Button(root, text="Chadi Mountassir \n Linkedin", command=lambda: webbrowser.open_new_tab("https://www.linkedin.com/in/chadi-mountassir-542779231"))
button3.grid(row=3, column=0)

label4 = tk.Label(root, image=photo4)
label4.grid(row=2, column=1, padx=20, pady=20)
button4 = tk.Button(root, text="Salma Kellali \n Linkedin", command=lambda: webbrowser.open_new_tab("https://www.linkedin.com/in/salma-kellali-538339268"))
button4.grid(row=3, column=1)

root.mainloop()
