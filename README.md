# Introduction 
La gestion des étudiants est un aspect essentiel de tout établissement
d'enseignement, qu'il s'agisse d'une école, d'un collège ou d'une université. Lagestion efficace des étudiants implique la collecte et la mise à jour des donnéesdes étudiants telles que les informations personnelles, les notes, les absencesetlaperformance académique. Cela nécessite également une communicationfluideavec les étudiants et leurs parents ou tuteurs. Le projet de gestion des étudiants consiste à développer un systèmeautomatiséqui permettra de gérer toutes les activités liées aux étudiants de manièreefficace.Il s'agit notamment de la gestion des admissions, de la gestion des inscriptions, dela gestion des notes, de la gestion des absences, de la communicationaveclesparents et de la génération de rapports .

# Les pages de Projet développer avec Tkinter Pur 
Ce code est un programme GUI (graphical userinterface) écrit en Python avec l'utilisationdelabibliothèque Tkinter pour créer unefenêtreetunmenu de navigation. Le programmecomporteplusieurs fonctions qui définissent lesdifférentespages que l'utilisateur peut accéder encliquantsur les boutons du menu. La paged'accueil estdéfinie dans la fonction home_page(), lapagedeconnexion est définie dans la fonctionlogin_page(),la page de connexion en ligne est définiedanslafonction seconnecter_page() et lapagedecontactest définie dans la fonction contact_page()
![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/f16ecd32-11de-4579-8423-c6ac3cb16c04)

## Boutton home : 

 de la fenêtre. Les nouvelles sont stockéesdans une liste de dictionnaires contenant le titre et le chemin d'accès à l'image de chaquenouvelle. Des labels et des images sont utilisés pour afficher des informations sur l'école ENSA d'Al-Hoceima, tellesquelenom de l'école, une brève description, une image de fond, etc. Un bouton "Menu" pour rediriger l'utilisateur vers une autre page ("realacceuil" dans cecas)

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/f107dd52-0873-44ce-9411-38d4c49a79ae)

## Boutton formation : 

Les fonctions suivantes, "cycle_preparatoire_page" et "genie_civil_page","ingenieriededonnées"......,créent des cadres à l'intérieur de l'interface principale et ajoutent des étiquettes avec des informationssurlesprogrammes de formation en cycle préparatoire et en génie civil, respectivement.
![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/d1795010-d316-435a-b173-31afee25d8f0)

## Boutton Services en ligne

Il permetde créer une page de connexionpourunsiteweb en utilisant une base dedonnéesMySQL. 

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/ba0fc4e5-1cb2-452d-b2cc-3a2e5143f4d3)

En cliquant le bouton Créer un nouveau compte(pour s'inscrire)
La fonction `connect_database()` est appelée lorsque l'utilisateur appuie sur le bouton "S'inscrire". Ellevérifiequetous les champs requis sont remplis, que les mots de passe entrés correspondent et que l'utilisateur aacceptélestermes et conditions. Ensuite, elle essaie de se connecter à la base de données MySQL en utilisant les informations deconnexionprédéfinies. Si elle échoue, elle affiche un message d'erreur. Elle crée ensuite une base de données appelée "userdata" si elle n'existe pas déjà et crée une tableappelée"data"sielle n'existe pas déjà. Cette table contient les champs "id", "email", "first_name", "last_name" et "password".Ensuite, elle vérifie si l'utilisateur existe déjà dans la table en exécutant une requête SELECT sur la tableavecl'adressee-mail entrée par l'utilisateur. Si un utilisateur avec la même adresse e-mail est trouvé, un messaged'erreurestaffiché.
Sinon, elle insère les informations de l'utilisateur dans la table en utilisant une requête INSERT. Elleconfirmeensuitel'inscription de l'utilisateur en affichant un message de succès et en effaçant tous les champs de saisieparuneboutonappele OUI. La fenêtre d'inscription est ensuite créée, elle contient une image de fond et un cadre blanc pour les champsdesaisieet les étiquettes correspondantes. Chaque champ de saisie est précédé d'une étiquette pour indiquer lechampdesaisie attendu.
Enfin, la fenêtre est affichée à l'utilisateur et attend ses interactions jusqu'à ce que l'utilisateur fermelafenêtre.

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/c2fcc11b-f021-45d9-b9ea-5947d8bdf81b)

"Mot de passeoublié?".Elle affiche une nouvelle fenêtre dans laquelle l'utilisateur peut saisir son nom d'utilisateur et son nouveau mot de passe pour réinitialiser son mot de passe. La nouvelle information de mot de passe est stockéedanslabasededonnées MySQL. 
![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/ec2828cf-badb-473e-a9ad-58302a742f14)

un code de vérificationvanous envoyer vers notreemail : 

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/71f17c79-cde4-45cc-818d-1cd4b995466b)

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/4adc1b10-792a-41f6-80b8-1e9265267496)


En remplirlenouveaumot depasseEt Bon connexion

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/4a06bd90-b373-4521-9ed2-ae394a4f227e)

Et maintenant si l'utilisateur a saisie une email ou mot de passeincorrect.cemessage d'erreur va s'afficher: 

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/a7d508a8-9e54-486a-a8f6-6d4c1bbf322c)

Notre code lié avec base de données:
Lorsqu'on saisir notre informations dans SignUp il va liéer automatiquement dansnotrebase donnée

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/1d567d0c-1ded-47dc-af7b-ac6c6860773f)

et pour laffichage de l'utilisateur (cad lorsque l'utilisateur clique sur continuer le Signup ) , il va s'afficher cette interface : 
Ensuite, différentes fonctions sont définies pour gérer les actions de l'utilisateur dans l'interfacegraphique.Lafonction Exit() ferme la fenêtre. La fonction registrement_page() ferme la fenêtre actuelle et ouvreunenouvellefenêtre pour l'enregistrement d'un nouvel étudiant. La fonction registr() ferme la fenêtre actuelleet ouvreunenouvelle fenêtre pour se connecter. La fonction get_id_tab() ouvre une nouvelle fenêtre pour permettreàl'utilisateur de récupérer son ID en cas d'oubli. La fonction showimage() permet à l'utilisateur desélectionneruneimage pour l'afficher dans l'interface graphique. La fonction registration_no() génère un numérod'enregistrementunique pour chaque étudiant. La fonction clear() réinitialise tous les champs de la fenêtre. La fonctionverif(num)permet de vérifier que l'utilisateur entre le bon code avant de pouvoir sauvegarder ses modifications. Lafonctionsave() enregistre les données saisies par l'utilisateur dans un fichier Excel et dans une base dedonnéesMySQL.La fenêtre contient différents widgets, tels que des libellés (Labels), des entrées (Entry), des boutons(Button),desimages (Image) et des listes déroulantes (Combobox), pour permettre à l'utilisateur d'entrer des informationssurl'étudiant à enregistrer. Le programme utilise également une grille pour organiser les différents widgets dans la fenêtre. 

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/fcf778a1-c1c8-46a0-9529-dbf08a1e132c)

Si l'utilisateur veut modifier ses propres informations , il faut d'abordsaisirsoncode pour pouvoir acceder a ses données 

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/8c138dfe-49b6-4e69-8520-7d306f3d40a3)

Notre code lié avec base de données:
Lorsqu'on saisir notre informations dans Registration il va liéer automatiquementdansnotre base donnée

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/ace7c693-9c68-4100-8524-58a5db38f66d)

Lorsqu' on termine notre registration on retourne à la pagedeconnexionpour accéder à Myeservice

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/e98c2da8-1a2d-4277-878e-4982df75ca09)
### Notre première bouton cours affichera :

Le code commencepar définirundictionnaire nommé FILIERES_DOSSIERSquicontient les noms des filièrescommeclésetles chemins des dossierscontenantlescours pour chaque filièrecommevaleurs.Ensuite, une fonctionnommée"animate_text" est définiepouranimerletexte dans un canevas. Lafonction"download_course" est égalementdéfiniepour télécharger uncours.
Un bouton nommé "Télécharger" est créé pour télécharger le cours sélectionné. Lorsque ce boutonest cliqué, lafonction"download_course" est appelée.

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/c9afad38-fe5b-4850-ac61-40f350a2d8e8)

Lorsqu'on clique sur télécharger , le cour va telecharger sur le bureaude notre utilisateur

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/776a2751-3684-4171-9239-aa3ded5023da)

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/ebdf2fd2-43f4-414b-885a-7d301785481d)

### Notre deuxième bouton carteEtudiant affichera :

lorsque l'utilisateur saisie le "Numero d'etudiant" , une carte etudiant vacreerautomatiquement en liant sa code avec base de donnée

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/1c19ddd3-4bb1-43a4-94fa-7127c8b19f52)

### Notre troisième bouton marksheet affichera :

Ce code est un programme de calcul denotesetderésultats scolaires en utilisant la bibliothèqueTkinterde Python. Le programme contient desfonctionspour calculer la somme, le pourcentage, lanoteetlerésultat en fonction des notes des matièresentréespar l'utilisateur. Le programme comporteégalementdes fonctions pour vérifier les erreursetafficherlerésultat dans une fenêtreTkinter

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/1e3104a5-5e61-4b2e-a151-9125681283df)

Lorsque l'utilisateur entre ses propres notes , le programmevaafficher:

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/59d18cb6-183b-4150-bb65-8e9aff2cc14e)

Notre code lié avec base de données:
Lorsqu'on saisir notre notes dans Marksheet il va lier automatiquement dansnotrebasedonnéaavec les notes et id

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/89e74c4f-1e57-4ea0-bcbe-7566c2817a50)

### Notre quatrième bouton Clubs affichera :

Le programmecomptequatre clubs : le Club Data, leClubGénieCiviletle Club CCT,Club 01. Chaqueclubasaproprepage avec ses objectifs et ses événements

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/f2fc21d1-bd1d-4781-a74d-d4047493e1cf)

### Notre cinquiéme bouton Contacter nous affichera :

Ce code affiche une fenêtre principale, des labels et des boutons
pour afficher notre images et notre liens vers nos profils LinkedIn pour nous contacter au cas des problèmes.

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/a380b385-bb83-4719-800a-2c73eae3c7da)


## Boutton Contact : 

![image](https://github.com/chaymaemerhrioui1/gestion_des_etudiants/assets/128318349/32150861-0c7c-4585-957d-921340e7d814)

# FIN  , Mercii ❤️❤️









