import tkinter as tk
from tkinter import messagebox

import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(host='localhost', user='root', database='userdata')
cur = conn.cursor()

# Fonction pour récupérer les informations de l'étudiant
def recuperer_informations_etudiant(numero_etudiant):
    cur.execute(f'SELECT * FROM data WHERE id = {numero_etudiant}')
    row = cur.fetchone()
    if row is None:
        messagebox.showerror('Error', "ID doesn't exist, verify your ID")
    #    elif row>1:
    #       messagebox.showerror('Error', "there has been an error in our database.\nerror number: 69 ")
    else:
        date_naissance= row[5]
        nom= row[2]
        prenom= row[3]
    return nom, prenom, date_naissance
# Fonction pour créer la carte étudiant
def creer_carte_etudiant():
    # Récupérer les informations de l'étudiant
    numero_etudiant = numero_etudiant_entry.get()
    nom, prenom, date_naissance = recuperer_informations_etudiant(numero_etudiant)

    # Créer une fenêtre Tkinter
    carte_etudiant = tk.Toplevel()

    # Créer un canevas pour dessiner la carte
    canvas = tk.Canvas(carte_etudiant, width=300, height=200)
    canvas.pack()

    # Dessiner un rectangle pour la carte
    canvas.create_rectangle(10, 10, 290, 190, fill='white')

    # Ajouter une image de l'étudiant
    etudiant_image = tk.PhotoImage(file='t1.png')
    canvas.create_image(50, 50, image=etudiant_image)



import tkinter as tk


# Connexion à la base de données
conn = mysql.connector.connect(host='localhost', user='root', database='userdata')
cur = conn.cursor()


# Fonction pour récupérer les informations de l'étudiant
def recuperer_informations_etudiant(numero_etudiant):
    cur.execute(f'SELECT * FROM data WHERE id = {numero_etudiant}')
    result = cur.fetchone()
    nom, prenom, date_naissance, classe= result[2], result[3], result[5], result[7]
    return nom, prenom, date_naissance,classe


# Fonction pour créer la carte étudiant
def creer_carte_etudiant():
    # Récupérer les informations de l'étudiant
    numero_etudiant = numero_etudiant_entry.get()
    nom, prenom, date_naissance, classe = recuperer_informations_etudiant(numero_etudiant)

    # Créer une fenêtre Tkinter
    carte_etudiant = tk.Toplevel()

    # Créer un canevas pour dessiner la carte
    canvas = tk.Canvas(carte_etudiant, width=300, height=200)
    root.title('carte etudiant')

    canvas.pack()

    # Dessiner un rectangle pour la carte
    canvas.create_rectangle(10, 10, 290, 190, fill='white')

    # Ajouter une image de l'étudiant
    etudiant_image = tk.PhotoImage(file='t1.png')
    canvas.create_image(50, 50, image=etudiant_image)

    # Ajouter le nom de l'étudiant
    nom_label = tk.Label(canvas, text="Ecole national Des Sciences Appliquees\nd'AlHoceima",bg='WHITE', font=('Arial', 7))
    nom_label.place(x=100, y=10)

    # Ajouter le prénom de l'étudiant
    prenom_label = tk.Label(canvas, text='Prénom: {}'.format(prenom),bg='WHITE', font=('Arial', 12))
    prenom_label.place(x=100, y=40)

    nom_label = tk.Label(canvas, text='nom: {}'.format(nom),bg='WHITE', font=('Arial', 10))
    nom_label.place(x=100, y=70)

    # Ajouter la date de naissance de l'étudiant
    date_naissance_label = tk.Label(canvas, text='Date de naissance: {}'.format(date_naissance),bg='WHITE', font=('Arial', 10))
    date_naissance_label.place(x=100, y=100)

    if(str(classe)=='i.d' or str(classe)=='id'):
        x= "ingenieurie des données"
    elif(str(classe)=='cp1' or str(classe)=='cp2'):
        x= "cycle preparatoire"
    elif(str(classe)=='g.i'):
        x = "genie informatique"
    elif(str(classe)=='g.c'):
        x = "genie civil"
    elif (str(classe) == 'g.m'):
        x = "genie mecaniue"
    elif (str(classe) == 'geer'):
        x = "genie energitique et energie renouvlable"
    elif (str(classe) == 'gee'):
        x = "genie de l'eau et l'environnement"

    date_naissance_label = tk.Label(canvas, text='élève ingenieur en\n {}'.format(x),bg='WHITE', font=('Arial', 10))
    date_naissance_label.place(x=100, y=130)


    # Afficher la fenêtre Tkinter
    carte_etudiant.mainloop()


# Création de l'interface graphique
root = tk.Tk()
root.geometry('400x400')

# Champ de saisie pour le numéro d'étudiant
numero_etudiant_label = tk.Label(root, text='Numéro étudiant:')
numero_etudiant_label.pack()
numero_etudiant_entry = tk.Entry(root)
numero_etudiant_entry.pack()

# Bouton pour créer la carte étudiant
creer_carte_etudiant_bouton = tk.Button(root, text='Créer carte étudiant', command=creer_carte_etudiant)
creer_carte_etudiant_bouton.pack()

root.mainloop()