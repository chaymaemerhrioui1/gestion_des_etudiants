import tkinter
from tkinter import *
import tkinter as tk

root=Tk()
root.geometry('990x660')
root.title('Formation')
bg = PhotoImage(file="C:/Users/pc/Downloads/t1.png")
label1 = Label(root, image=bg)
label1.place(x=0,y=0)

def login_page():
    root.destroy()
    import realacceuil

def cycle_preparatoire_page():
    cycle_preparatoire_frame=tk.Frame(main_frame)
    lb1=tk.Label(cycle_preparatoire_frame,text='Cycle Préparatoire\n'
                                              '( Sciences & Techniques pour l’Ingénieur)\n',font=('Bold',25))
    lb=tk.Label(cycle_preparatoire_frame,text='Objectifs de la formation :\n',font=('Bold',18))
    lb2=tk.Label(cycle_preparatoire_frame,text='Préparer et donner à l élève ingénieur les bases scientifiques\n'
                                               ' et techniques, ainsi que les connaissances en langues et communications\n'
                                               ' indispensables à la poursuite des études dans une filière du cycle ingénieur.\n'
                                               'Le cursus suivi au cycle préparatoire de l ENSA d Al-Hoceima ainsi que celui \n'
                                               'suivi dans less filières accréditées par l ENSAH permettent de:\n'
                                               ' * Répondre à la demande régionale et nationale en matière de ressources humaines\n'
                                               ' qualifiées dans les domaines du Génie Civil, de l Environnement, de l Enérgitique\n'
                                               ' et de l Informatique.\n'
                                               '* Renforcer la compétitivité et le développement socio-économique régional et national.\n',font=('Bold',12))
    lb3=tk.Label(cycle_preparatoire_frame,text='Compétences à acquérir :\n',font=('Bold',18))
    lb4=tk.Label(cycle_preparatoire_frame,text='Le cycle préparatoire intégré de l’Ecole Nationale des Sciences Appliquées d Al-Hoceima\n'
                                               ' a pour objectif de préparer, sur quatre semestres, l intégration de l’une des filières \n'
                                               'du cycle ingénieur de l’ENSAH . Il est essentiel, pour l ingénieur de demain, d acquérir,\n'
                                               'En conséquence, ce cycle propose des bases très\n'
                                               ' sérieuses dans quatre disciplines scientifiques majeures et fondamentales pour la formation des ingénieurs :\n'
                                               ' * Physique, Mathématiques, Chimie, Informatique et Electronique. \n',font=('Bold',12))
    lb1.pack()
    lb.pack()
    lb2.pack()
    lb3.pack()
    lb4.pack()

    cycle_preparatoire_frame.pack(pady=20)

def genie_civil_page():
    genie_civil_frame=tk.Frame(main_frame)
    lb1=tk.Label(genie_civil_frame,text='Génie Civil',font=('Bold',25))
    lb = tk.Label(genie_civil_frame, text='Objectifs de la formation :\n', font=('Bold', 18))
    lb2=tk.Label(genie_civil_frame,text='* Doter les élèves ingénieurs d’un enseignement de très haut niveau correspondant à l’exigence des\n'
                                        ' entreprises du secteur bâtiment, des ouvrages d’art et des ouvrages hydrauliques.'
                                        '* Permettre aux élèves ingénieurs de maîtriser les techniques de la construction, la géotechnique,\n'
                                        ' l’hydraulique et l’énergie, la logistique et le management, la planification des transports ainsi \n'
                                        'que la protection de l’environnement.\n'
                                        '* Former les élèves à maîtriser les outils, les méthodes et les techniques du génie civil en général\n'
                                        '* Acquérir les capacités d’innover et d’entreprendre.\n'
                                        '* Intégrer les disciplines économiques, juridiques, financières et humaines, nécessaires à l’ingénieur.\n'
                                        '* inculquer aux élèves la technique d’apprendre à apprendre, les concepts de mondialisation et de globalisation',font=('Bold',12))
    lb3 = tk.Label(genie_civil_frame, text='Débouches et retombées de la formation: \n', font=('Bold', 18))
    lb4=tk.Label(genie_civil_frame,text='Les ingénieurs diplômés de la filière Génie Civil occupent rapidement des fonctions de responsabilités\n'
                                        ' dans les secteurs du Bâtiment et du Génie Civil : bureaux d’études, direction de chantiers, direction \n'
                                        'générale… La nature même de la formation permet aux diplômés de s’intégrer dans tous les types d’entreprises,\n'
                                        ' publiques et privées :\n'
                                        ' * Entreprises de BTP (bureaux d’études et chantiers) ;\n'
                                        ' * Bureaux d’Etudes et Sociétés d’Ingénierie \n'
                                        ' * Sociétés de Contrôle Technique ;\n'
                                        ' * Services Techniques des Administrations et des Villes (collectivités locales) ;',font=('Bold',12))
    lb1.pack()
    lb.pack()
    lb2.pack()
    lb3.pack()
    lb4.pack()
    genie_civil_frame.pack(pady=20)

def genie_info_page():
    genie_info_frame=tk.Frame(main_frame)
    lb1 = tk.Label(genie_info_frame, text='Génie Informatique \n (nouvelle accréditation en 2021)',font=('Bold',25))
    lb2=tk.Label(genie_info_frame,text='Objectifs de la formation :',font=('Bold',18))
    lb=tk.Label(genie_info_frame,text='La filière a pour vocation de former des ingénieurs polyvalents avec des  '
                                      'compétences principales\n'
                                      ' scientifiques et techniques, leur permettant de maîtriser'
                                      ' les concepts et\n'
                                      ' les technologies des '
                                      'grands domaines de l’informatique (modélisation \n'
                                      'et programmation,'
                                      'bases de données, systèmes '
                                      'et réseaux, conception et déploiement d’applications\n'
                                      ' d’entreprise, sécurité, prise de décision,'
                                      ' analyse de données,\n visualisation des données, …)'
                                      ' jusqu’aux applications les plus avancées qui '
                                      'se retrouvent réparties ',font=('Bold',12))
    lb3 = tk.Label(genie_info_frame, text='Compétences à acquérir :', font=('Bold', 18))
    lb4=tk.Label(genie_info_frame,text='* Modélisation \n'
                                       '* Programmation\n'
                                       '* Conception et déploiement d’applications d’entreprise\n'
                                       '* Bases de données\n'
                                       '* Qualité\n'
                                       '* Sécurité\n'
                                       '* Statistique et intelligence artificielle\n'
                                       '* Informatique et statistique décisionnelle\n'
                                       '* Big Data\n'
                                       '* Adaptation au milieu professionnel et aux évolutions futures.\n'
                                       '* Traitement du signal, Vision par ordinateur en OpenCV, Deep learnin',font=('Bold',12))
    lb1.pack()
    lb2.pack()
    lb.pack()
    lb3.pack()
    lb4.pack()
    genie_info_frame.pack(pady=20)

def ingenieur_de_donnee_page():
    ingenieur_de_donnee_frame=tk.Frame(main_frame)
    lb1=tk.Label(ingenieur_de_donnee_frame,text='Ingénierie des données : \n',font=('Bold',25))
    lb2 = tk.Label(ingenieur_de_donnee_frame, text='Objectifs de la formation :', font=('Bold', 18))
    lb=tk.Label(ingenieur_de_donnee_frame,text='Aujourd’hui, avec la connexion présente en tout lieu et à'
                                               ' tout instant, des données\n '
                                               'considérables naissent. Ces données ou data deviennent'
                                               ' un acteur clé pour la compréhension,\n'
                                               ' l’analyse, l’anticipation la prédiction'
                                               ' et la résolution des grands problèmes sanitaires,\n'
                                               ' économiques, politiques, sociaux et scientifiques de\n'
                                               ' notre pays le Maroc. En plus,'
                                               ' L’environnement de l’entreprise a radicalement changé. \n'
                                               'A la fois dans les informations\n'
                                               ' qu’elle requiert et les informations qu’elle doit fournir\n'
                                               ' pour exister dans un écosystème'
                                               ' économique et social où elle se doit d’être présente \n'
                                               'et réactive pour se développer.'
                                               ' La notion de proximité numérique avec les clients est inscrite dans la veille\n stratégique.'
                                               ' C’est une vraie rupture culturelle qui a bousculé les repères qu’ils soient dans\n'
                                               ' l’entreprise comme chez le client',font=('Bold',12))
    lb3=tk.Label(ingenieur_de_donnee_frame,text='Compétences à acquérir :',font=('Bold',18))
    lb4=tk.Label(ingenieur_de_donnee_frame,text='* Recherche d’Information : crawling et scraping\n'
                                                '* Acquisition des données (Data Ingestion)\n'
                                                '* Stockage des données (Data Storage)\n'
                                                '* Analyse de données (Data Analysis)\n'
                                                '* Visualisation des données (Data vizualisation)\n'
                                                '* Bases de données SQL et NoSQL\n'
                                                '* Architecture Big Data pour les entreprises\n'
                                                '* Transformation Digitale\n'
                                                '* Architecture Logicielle et Modélisation UML 2.0\n'
                                                '* Programmation Parallèle et Distribuée\n'
                                                '* Conception et déploiement d’applications d’entreprise\n'
                                                ,font=('Bold',12))
    lb1.pack()
    lb2.pack()
    lb.pack()
    lb3.pack()
    lb4.pack()
    ingenieur_de_donnee_frame.pack(pady=20)

def geer_page():
    geer_frame=tk.Frame(main_frame)
    lb=tk.Label(geer_frame,text='Génie énergétique et énergies renouvelables',font=('Bold',25))
    lb2 = tk.Label(geer_frame, text='Objectifs de la formation :', font=('Bold', 18))
    lb1=tk.Label(geer_frame,text='De nos jours, pour pouvoir satisfaire les besoins croissants en énergie \n'
                                 'de la population, plus de 60% de la production mondiale d’énergie provient \n'
                                 'des combustibles fossiles, environ 20% du nucléaire et le reste des sources \n'
                                 'd’énergie renouvelables. Toutefois, l’utilisation des ressources fossiles dans\n'
                                 ' de telles proportions pose, d’une part, des problèmes d’environnement, notamment\n'
                                 ' par l’émission de CO2 (gaz à effet de serre) et de gaz polluants (SO2, NOx, CO, CH4\n'
                                 ', chlorofluorocarbones, particules solides, etc.) et, d’autre part, entraînent \n'
                                 'l’augmentation des prix et l’épuisement de ces ressources. \n'
                                 'Les problèmes annoncés posent des questions essentielles pour le développement durable\n'
                                 ' de la planète. Les premières décisions politiques au niveau mondial ont été prises au\n'
                                 ' cours du sommet de Kyoto en 1997. Le but visé est de prendre des mesures de précaution\n'
                                 ' pour prévoir, prévenir ou atténuer les causes des changements climatiques. En parallèle,\n'
                                 ' la recherche de nouvelles technologies de production d’énergie dites propres et efficaces, \n'
                                 'a été encouragée et entreprise dans plusieurs pays\n'
                                 'Pour répondre aux besoins immédiats et futurs de nos sociétés, et réagir avec efficacité et rigueur aux défis\n'
                                 ' de ces mutations, nous devons former une nouvelle race d’ingénieur capable de produire, d’utiliser \n'
                                 'rationnellement l’énergie et gérer un environnement énergétique sain et vraiment durable.L’objectif \n'
                                 'principal de cette filière est de former des ingénieurs en Génie énergétique et énergies renouvelables \n'
                                 'possédant une formation polyvalente, adaptée, aux évolutions technologiques du monde de demain, et qui \n'
                                 'peuvent intervenir dans différents secteurs de l’énergie tout au long du processus de production et de \n'
                                 'distribution.Les enseignements proposés allient connaissances théoriques et techniques ainsi que des\n'
                                 ' réalisations concrètes, à travers des projets de fin d’étude et des stages au sein de l’industrie. \n'
                                 'Cette stratégie adoptée, permettra aux lauréats de s’adapter, répondre et réagir avec efficacité et \n'
                                 'rigueur aux défis des mutations et évolutions extrêmement rapides auxquels les entreprises sont confrontées,\n'
                                 ' aux nouveaux modes de management, aux pressions sans cesse croissantes de la concurrence, de la technologie \n'
                                 'et du client, ainsi qu’à la protection de l’environnement et des risques majeurs',font=('Bold',12))
    lb.pack()
    lb2.pack()
    lb1.pack()
    geer_frame.pack(pady=20)

def genie_mecanique_page():
    genie_mecanique_frame=tk.Frame(main_frame)
    lb1 = tk.Label(genie_mecanique_frame, text='Génie mécanique',font=('Bold',25))
    lb2=tk.Label(genie_mecanique_frame,text='Objectifs de la formation :',font=('Bold',18))
    lb=tk.Label(genie_mecanique_frame,text=' Cette formation a pour objectif de faire acquérir à ces lauréats les compétences suivantes :\n'
                                           '* Devenir un spécialiste autonome et compétent, qui pourra exercer une pratique professionnelle de \n'
                                           'haut niveau technique ;\n'
                                           '* Développer des aptitudes à la recherche en génie mécanique et de se préparer ainsi à une pratique \n'
                                           'professionnelle de \n'
                                           'haut niveau technique ;\n'
                                           '* Développer des aptitudes à la recherche en génie mécanique et de pouvoir se préparer à des \n'
                                           'études doctorales ;\n'
                                           '* Acquérir des connaissances approfondies dans une ou plusieurs spécialités du génie mécanique :\n'
                                           ' Conception, modélisation \n'
                                           'numérique, fabrication, design\n',font=('Bold',12))
    lb3 = tk.Label(genie_mecanique_frame, text='Compétences à acquérir :', font=('Bold', 18))
    lb4=tk.Label(genie_mecanique_frame,text='* Procédés de conception mécanique.\n'
                                            '* Procédés de production industrielle.\n'
                                            '* Méthodes de calcul et de simulation du comportement des structures et des systèmes mécaniques.\n'
                                            '* Automatisation et asservissement des systèmes de production industrielle.\n'
                                            '* Etudes énergétique et environnementale de procédés industriels.\n'
                                            '* Management de la qualité et métrologie.\n'
                                            '* Management et gestion de projet.\n'
                                            '* Communication en langues française et anglaise.',font=('Bold',12))
    lb1.pack()
    lb2.pack()
    lb.pack()
    lb3.pack()
    lb4.pack()
    genie_mecanique_frame.pack(pady=20)

def gee_page():
    gee_frame=tk.Frame(main_frame)
    lb1 = tk.Label(gee_frame, text='Génie de l’Eau et de l’Environnement',font=('Bold',25))
    lb2=tk.Label(gee_frame,text='Objectifs de la formation :',font=('Bold',18))
    lb=tk.Label(gee_frame,text='La filière Génie de l’Eau et de l’Environnement a été conçue en tenant compte des besoins\n'
                                   ' du tissu socio-économique en matière de compétences dans le domaine de l’eau de sa gestion\n'
                                   ' ainsi que l’assainissement liquide et solide à l’échelle nationale et régionale. En effet,\n'
                                   ' au cours des prochaines années, une mutation profonde est en progression se traduisant par :\n'
                                   '* La généralisation de l’accès à l’eau potable et au réseau d’assainissement (plan National \n'
                                   'd’Assainissement liquide),\n'
                                   '* La mise en place de décharges contrôlées (plan National de déchets ménagers et assimilés)\n'
                                   '* La protection de l’environnement et de développement durable (Charte Nationale de \n'
                                   '* l’environnement et du développement durable),\n'
                                   '* Les grands projets structurants au niveau de tout le Royaume',font=('Bold',12))
    lb1.pack()
    lb2.pack()
    lb.pack()
    gee_frame.pack(pady=20)

def hide_indicators():
    cycle_preparatoire_indicate.config(bg='white')
    genie_civil_indicate.config(bg='white')
    genie_info_indicate.config(bg='white')
    ingenieur_de_donnee_indicate.config(bg='white')
    geer_indicate.config(bg='white')
    genie_mecanique_indicate.config(bg='white')
    gee_indicate.config(bg='white')


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb,page):
    hide_indicators()
    lb.config(bg='#12c4c0')
    delete_pages()
    page()

options_frame=tk.Frame(root,bg='#12c4c0')

head_frame=tk.Frame(root,bg='#12c4c0',highlightthickness=1)
head_frame.pack(side=tk.TOP,fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=44)

cycle_preparatoire_btn=tk.Button(options_frame,text='Cycle prepara',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(cycle_preparatoire_indicate,cycle_preparatoire_page))
cycle_preparatoire_btn.place(x=35,y=50)
cycle_preparatoire_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
cycle_preparatoire_indicate.place(x=3,y=50,width=5,height=40)


genie_civil_btn=tk.Button(options_frame,text='Génie civil',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(genie_civil_indicate,genie_civil_page))
genie_civil_btn.place(x=35,y=250)
genie_civil_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
genie_civil_indicate.place(x=3,y=250,width=5,height=40)

genie_info_btn=tk.Button(options_frame,text='Génie Informatique',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(genie_info_indicate,genie_info_page))
genie_info_btn.place(x=35,y=200)
genie_info_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
genie_info_indicate.place(x=3,y=200,width=5,height=40)

ingenieur_de_donnee_btn=tk.Button(options_frame,text='Ingénieur données',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(ingenieur_de_donnee_indicate,ingenieur_de_donnee_page))
ingenieur_de_donnee_btn.place(x=35,y=100)
ingenieur_de_donnee_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
ingenieur_de_donnee_indicate.place(x=3,y=100,width=5,height=40)

geer_btn=tk.Button(options_frame,text='Génie énergétique',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(geer_indicate,geer_page))
geer_btn.place(x=35,y=150)
geer_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
geer_indicate.place(x=3,y=150,width=5,height=40)

genie_mecanique_btn=tk.Button(options_frame,text='Génie mecanique',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(genie_mecanique_indicate,genie_mecanique_page))
genie_mecanique_btn.place(x=35,y=300)
genie_mecanique_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
genie_mecanique_indicate.place(x=3,y=250,width=5,height=40)

gee_btn=tk.Button(options_frame,text='Génie de l eau',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(gee_indicate,gee_page))
gee_btn.place(x=35,y=350)
gee_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
gee_indicate.place(x=3,y=250,width=5,height=40)


options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=210,height=1000)

main_frame=tk.Frame(root,highlightbackground='black',highlightthickness=1)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1000,width=1400)


loginButton=Button(options_frame,text='Acceuil',font=('Open Sans','9','bold underline'),bg='white',fg='#12c4c0',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',
                   command=login_page)
loginButton.place(x=18,y=5)

#topp""""""""""""""""""""""""""""""""""""""""""
#Label(root,text="Email: chaymaemerhrioui@gmail.com",width=10,height=3,bg="#12c4c0",anchor='e').pack(side=TOP,fill=X)


root.mainloop()
