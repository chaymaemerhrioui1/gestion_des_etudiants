import tkinter as tk
import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(host='localhost', user='root', database='userdata')
cur = conn.cursor()

# Fonction pour récupérer les informations de l'étudiant
def recuperer_informations_etudiant(numero_etudiant):
    cur.execute('SELECT first_name, last_name, date_naissance FROM data WHERE id = ?', (numero_etudiant,))
    result = cur.fetchone()
    nom, prenom, date_naissance = result
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
    cur.execute('SELECT first_name, last_name, date_naissance FROM data WHERE id = ?', (numero_etudiant,))
    result = cur.fetchone()
    nom, prenom, date_naissance = result
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

    # Ajouter le nom de l'étudiant
    nom_label = tk.Label(canvas, text='Nom: {}'.format(nom), font=('Arial', 14))
    nom_label.place(x=100, y=10)

    # Ajouter le prénom de l'étudiant
    prenom_label = tk.Label(canvas, text='Prénom: {}'.format(prenom), font=('Arial', 12))
    prenom_label.place(x=100, y=40)

    # Ajouter la date de naissance de l'étudiant
    date_naissance_label = tk.Label(canvas, text='Date de naissance: {}'.format(date_naissance), font=('Arial', 10))
    date_naissance_label.place(x=100, y=70)

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