import tkinter
from tkinter import *
import tkinter as tk

root=Tk()
root.geometry('990x660')
root.title('Activite Parascolaire')
bg = PhotoImage(file="C:/Users/Salma Fannich/Downloads/amoooo.jpg.png")
label1 = Label(root, image=bg)
label1.place(x=0,y=0)

def login_page():
    root.destroy()
    import realacceuil

def club_data_page():
    club_data_frame=tk.Frame(main_frame)
    lb1=tk.Label(club_data_frame,text='Club data\n',font=('Bold',25))
    lb=tk.Label(club_data_frame,text='Objectifs du club :\n',font=('Bold',18))
    lb2=tk.Label(club_data_frame,text='Rassembler des personnes intéressées par les données pour créer des réseaux\n'
                                               ' et des partenariats qui peuvent favoriser la collaboration\n'
                                               ' l innovation et la croissance économique.\n'
                                               'Le cursus suivi au cycle préparatoire de l ENSA d Al-Hoceima ainsi que celui \n'
                                               ' cherchent à sensibiliser les gens à l importance des données dans notre monde moderne\n'
                                               ' et à limpact qu elles peuvent avoir sur les organisations et les communautés.\n',font=('Bold',12))
    lb3=tk.Label(club_data_frame,text='Nouveauté :\n',font=('Bold',18))
    lb4=tk.Label(club_data_frame,text='Membres du Data Club ! explorer les données de manière ludique et engageante\n'
                                               ' c est notre premier projet d ingénierie des données. \n'
                                               'Rejoignez-nous alors que nous plongeons dans le monde des données et acquérons de nouvelles compétences\n'
                                        
                                               ' pour analyser et interpréter les données plus efficacement',font=('Bold',12))
    lb1.pack()
    lb.pack()
    lb2.pack()
    lb3.pack()
    lb4.pack()

    club_data_frame.pack(pady=20)

def club_genie_civil_page():
    club_genie_civil_frame=tk.Frame(main_frame)
    lb1=tk.Label(club_genie_civil_frame,text='Génie Civil',font=('Bold',25))
    lb = tk.Label(club_genie_civil_frame, text='Objectifs de club :\n', font=('Bold', 18))
    lb2=tk.Label(club_genie_civil_frame,text='aider les membres à améliorer leurs compétences techniques, leur compréhension \n'
                                        'des principes de base du génie civil et à leur fournir des connaissances pratiques \n'
                                        'sur les différentes techniques et technologies utilisées dans ce domaine.\n'
                                        'chercher également à sensibiliser le grand public à limportance du génie civil dans la société moderne\n'
                                        '  en mettant laccent sur les avantages de l infrastructure civile pour la sécurité, la santé et le bien-être des citoyens. \n'
                                        'que la protection de l’environnement.\n'
                                        ,font=('Bold',12))
    lb3 = tk.Label(club_genie_civil_frame, text='Evénements  : \n', font=('Bold', 18))
    lb4=tk.Label(club_genie_civil_frame,text='ENSAH HACKATON 1.0\n'
                                        ' 3 clubs, 3 filières, distinctes les unes des autres mais pourtant complémentaires,\n '
                                             'se sont réunies pour créer la toute première édition de l évènement : \n'
                                        'Mettant en jeu les connaissances de chaque domaine,l évènement est sous forme de 3 mini compétitions mais avec \n'
                                        ' un seul but à prouver L harmonie entre les domaines de \n'
                                    ,font=('Bold',12))
    lb1.pack()
    lb.pack()
    lb2.pack()
    lb3.pack()
    lb4.pack()
    club_genie_civil_frame.pack(pady=20)

def club_cct_page():
    club_cct_frame=tk.Frame(main_frame)
    lb1 = tk.Label(club_cct_frame, text='Club CCT \n (since en 2010)',font=('Bold',25))
    lb2=tk.Label(club_cct_frame,text='Objectifs de club :',font=('Bold',18))
    lb=tk.Label(club_cct_frame,text='c est un club culturel et technologique   '
                                      'interssée tous ce qui en relation avec art,litterature,events,coaching.......\n'
                                      ' encourager les membres à développer leurs compétences en matière de technologie et d innovation, \n'
                                      ' et à mettre en place des projets entrepreneuriaux.\n'
                                      '  peut organiser des événements culturels pour permettre aux membres d exprimer \n'
                                    ' organiser des projets communautaires qui utilisent la technologie pour résoudre des problèmes locaux,'
                              ,font=('Bold',12))
    lb3 = tk.Label(club_cct_frame, text='Evénments :', font=('Bold', 18))
    lb4=tk.Label(club_cct_frame,text='* Glissa takafiya \n'
                                       '* Trip\n'
                                       '*Library \n'
                                       '* culturel forum'
                                ,font=('Bold',12))
    lb1.pack()
    lb2.pack()
    lb.pack()
    lb3.pack()
    lb4.pack()
    club_cct_frame.pack(pady=20)

def Club_01_page():
    Club_01_frame=tk.Frame(main_frame)
    lb1=tk.Label(Club_01_frame,text='Club 01 Science,technologie et genie civil : \n',font=('Bold',25))
    lb2 = tk.Label(Club_01_frame, text='Objectifs de club :', font=('Bold', 18))
    lb=tk.Label(Club_01_frame,text='aider les membres à développer leurs compétences scientifiques et technologiques \n'
                                           
                                             
                                               ' en organisant des ateliers, des conférences, des formations et des échanges de connaissances.\n'
                                               'encourager la recherche scientifique et technologique en offrant aux membres \n'
                                               ' l occasion de mener des projets de recherche et de développement, de présenter leurs résultats,\n'
                                               ' sensibiliser les membres et le grand public à l importance des sciences et de la technologie \n'
                                               ' dans la société moderne, en mettant en évidence les avantages de l innovation \n' 
                                               'technologique pour l industrie, l environnement et la société. '

                                               ,font=('Bold',12))
    lb3=tk.Label(Club_01_frame,text='Evénements et Objectifs  :',font=('Bold',18))
    lb4=tk.Label(Club_01_frame,text='* Web Dev Practise \n'
                                                '* Data Science and ML Essentials\n'
                                                '* 01 Python Competition\n'
                                                '* Web scraping Using python\n'
                                                '* Getting started with PHP Laravel\n'
                                                '* 01 Webinar\n'

                                                ,font=('Bold',12))
    lb1.pack()
    lb2.pack()
    lb.pack()
    lb3.pack()
    lb4.pack()
    Club_01_frame.pack(pady=20)





def hide_indicators():
    club_data_indicate.config(bg='white')
    club_genie_civil_indicate.config(bg='white')
    club_cct_indicate.config(bg='white')
    Club_01_indicate.config(bg='white')



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
head_frame.configure(height=50)

club_data_btn=tk.Button(options_frame,text='Club Data ',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(club_data_indicate,club_data_page))
club_data_btn.place(x=35,y=50)
club_data_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
club_data_indicate.place(x=3,y=50,width=5,height=40)


club_genie_civil_btn=tk.Button(options_frame,text='Club Génie civil',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(club_genie_civil_indicate,club_genie_civil_page))
club_genie_civil_btn.place(x=35,y=200)
club_genie_civil_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
club_genie_civil_indicate.place(x=3,y=250,width=5,height=40)

club_cct_btn=tk.Button(options_frame,text='Club CCT',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(club_cct_indicate,club_cct_page))
club_cct_btn.place(x=35,y=150)
club_cct_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
club_cct_indicate.place(x=3,y=200,width=5,height=40)

Club_01_btn=tk.Button(options_frame,text='Club 01',font=('Bold',15),fg='white',bd=0,bg='#12c4c0',command=lambda :indicate(Club_01_indicate,Club_01_page))
Club_01_btn.place(x=35,y=100)
Club_01_indicate=tk.Label(options_frame, text='',bg='#12c4c0')
Club_01_indicate.place(x=3,y=100,width=5,height=40)



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


root.mainloop()
