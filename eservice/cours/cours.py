import os
import tkinter as tk
from tkinter import filedialog
import shutil

#fct
def eservicehome_page():
    root.destroy()
    import eservicehome


# Dictionnaire des filières et de leurs dossiers respectifs
FILIERES_DOSSIERS = {"Première Année Cycle Préparatoire": "C:/Users/pc/Documents/cours/Première Année Cycle Préparatoire",
                     "Deuxième Année Cycle Préparatoire": "C:/Users/pc/Documents/cours/Deuxième Année Cycle Préparatoire",
                      "Ingénierie des Données " :"C:/Users/pc/Documents/cours/ingenieurie des données",
                     "Génie Civil" : "C:/Users/pc/Documents/cours/Génie civil",
                     "Génie Informatique " : "C:/Users/pc/Documents/cours/genie informatique",
                     "Génie Energétique et Energie Renouvelable" :"C:/Users/pc/Documents/cours/Génie Energétique et Energie Renouvelable"
                    }
# Fonction pour animer le texte
def animate_text():
    x = 10  # Position initiale du texte en x
    y = 50  # Position initiale du texte en y
    dx = 5  # Valeur du déplacement en x
    dy = 0  # Valeur du déplacement en y
    while True:
        canvas.move(text_id, dx, dy)  # Déplacer le texte
        x += dx
        if x >= canvas.winfo_width() or x <= 0:
            dx *= -1  # Inverser la direction du déplacement en x si le texte atteint les bords du canevas
        canvas.update()
        canvas.after(20)  # Délai en millisecondes pour rafraîchir l'animation


def download_course():
    # Obtenir la filière sélectionnée dans la listebox
    selected_filiere = list_box_filieres.get(tk.ACTIVE)
    # Obtenir le cours sélectionné dans la listebox des cours
    selected_course = list_box_cours.get(tk.ACTIVE)
    # Obtenir le chemin complet du fichier du cours
    filiere_dossier = FILIERES_DOSSIERS[selected_filiere]
    course_file_path = os.path.join(filiere_dossier, selected_course)
    # Copier le fichier dans le dossier "Bureau"
    destination_path = os.path.expanduser("~/Desktop/" + selected_course)
    try:
        shutil.copy(course_file_path, destination_path)
        print("Le cours a été téléchargé dans votre Bureau.")
    except Exception as e:
        print("Erreur lors du téléchargement du cours :", str(e))


root = tk.Tk()
root.title("page des cours")


# Créer une listebox pour afficher les filières disponibles
list_box_filieres = tk.Listbox(root, width=60, height=40)
list_box_filieres.pack(side=tk.LEFT, padx=10, pady=10)

# Ajouter les filières à la listebox
for filiere in FILIERES_DOSSIERS.keys():
    list_box_filieres.insert(tk.END, filiere)

# Créer une listebox pour afficher les cours disponibles pour la filière sélectionnée
list_box_cours = tk.Listbox(root, width=60, height=40)
list_box_cours.pack(side=tk.LEFT, padx=10, pady=10)

def update_courses(event):
    # Effacer la listebox des cours
    list_box_cours.delete(0, tk.END)
    # Obtenir la filière sélectionnée
    selected_filiere = list_box_filieres.get(tk.ACTIVE)
    # Obtenir le chemin du dossier de la filière sélectionnée
    filiere_dossier = FILIERES_DOSSIERS[selected_filiere]
    # Lister les cours disponibles dans le dossier de la filière
    for file_name in os.listdir(filiere_dossier):
        if file_name.endswith(".pdf"):
            list_box_cours.insert(tk.END, file_name)

# Lier la mise à jour de la liste des cours à la sélection d'une filière
list_box_filieres.bind("<<ListboxSelect>>", update_courses)

# Créer un bouton pour télécharger un cours
download_button = tk.Button(root, text="Télécharger",cursor='hand2', command=download_course)
download_button.pack(pady=10)

# Créer un canevas pour afficher l'animation
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

# Afficher le texte dans le canevas
text_id = canvas.create_text(10, 50, text="Télecharger vos cours !!! ", fill="blue", font=("Helvetica", 16))



eservicehomeButton= tk.Button(root, text='Retour', cursor='hand2',command=eservicehome_page)
eservicehomeButton.place(x=1050,y=10)

animate_text()
root.mainloop()
