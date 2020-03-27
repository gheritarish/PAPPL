from tkinter import *
from PIL import Image, ImageTk
from partie import Partie
from equipe import Equipe
from joueur import Joueur


def config():
    global partie
    partie = Partie()
    global equipe1
    equipe1 = Equipe()
    global equipe2
    equipe2 = Equipe()

    fenetre = Tk()
    fenetre.iconbitmap("./Ressources/logo.png")
    fenetre.title("Configuration de la partie")
    fenetre.geometry("1280x720+0+0")

    type_frame = LabelFrame(fenetre, text="Type de partie")
    type_frame.pack()

    def affiche(valeur):
        if valeur == "Points":
            slider_tours.pack_forget()
            slider_points.pack(side=TOP)

        elif valeur == "Tours":
            slider_points.pack_forget()
            slider_tours.pack(side=TOP)

    choix = StringVar()
    choix.set("Points")
    options = ("Points", "Tours")
    type = OptionMenu(type_frame, choix, *options, command=affiche)
    type.pack(side=TOP)

    points = IntVar()
    slider_points = Scale(type_frame, variable=points,
                          from_=1, to=1000, orient=HORIZONTAL)
    slider_points.pack(side=TOP)

    tours = IntVar()
    slider_tours = Scale(type_frame, variable=tours,
                         from_=1, to=20, orient=HORIZONTAL)

    diff_frame = Frame(type_frame)
    diff_frame.pack(side=BOTTOM)

    difficulte = Label(diff_frame, text="Difficulté")
    difficulte.pack(side=LEFT)

    diff = DoubleVar()
    slider_diff = Scale(diff_frame, variable=diff, from_=0.0,
                        to=1.0, resolution=0.2, orient=HORIZONTAL)
    slider_diff.pack(side=RIGHT)

    # EQUIPE 1
    equipe1_frame = LabelFrame(fenetre, text="Equipe 1")
    equipe1_frame.pack()

    equipe1_window = PanedWindow(equipe1_frame)
    equipe1_window.pack(fill=BOTH, expand=1)

    joueur11_window = PanedWindow(equipe1_window)
    equipe1_window.add(joueur11_window)

    nom11=StringVar()
    nom11.set("Jean")
    nom_joueur11 = Entry(joueur11_window, textvariable=nom11)
    nom_joueur11.pack(side=TOP)
    def Entry11_Callback(event):
        nom_joueur11.selection_range(0, END)
    nom_joueur11.bind("<FocusIn>", Entry11_Callback)

    choix11 = StringVar()
    choix11.set("Humain")
    options11 = ("Humain", "IA débile", "IA intelligente")
    type_joueur11 = OptionMenu(joueur11_window, choix11, *options11)
    type_joueur11.pack(side=BOTTOM)

    joueur12_window = PanedWindow(equipe1_window, orient=VERTICAL)
    equipe1_window.add(joueur12_window)

    nom12=StringVar()
    nom12.set("Pierre")
    nom_joueur12 = Entry(joueur12_window, textvariable=nom12)
    nom_joueur12.pack(side=TOP)
    def Entry12_Callback(event):
        nom_joueur12.selection_range(0, END)
    nom_joueur12.bind("<FocusIn>", Entry12_Callback)

    choix12 = StringVar()
    choix12.set("Humain")
    options12 = ("Humain", "IA débile", "IA intelligente")
    type_joueur12 = OptionMenu(joueur12_window, choix12, *options12)
    type_joueur12.pack(side=BOTTOM)

    # EQUIPE 2
    equipe2_frame = LabelFrame(fenetre, text="Equipe 2")
    equipe2_frame.pack()

    equipe2_window = PanedWindow(equipe2_frame)
    equipe2_window.pack(fill=BOTH, expand=1)

    joueur21_window = PanedWindow(equipe2_window)
    equipe2_window.add(joueur21_window)

    nom21=StringVar()
    nom21.set("Marie")
    nom_joueur21 = Entry(joueur21_window, textvariable=nom21)
    nom_joueur21.pack(side=TOP)
    def Entry21_Callback(event):
        nom_joueur21.selection_range(0, END)
    nom_joueur21.bind("<FocusIn>", Entry21_Callback)

    choix21 = StringVar()
    choix21.set("Humain")
    options21 = ("Humain", "IA débile", "IA intelligente")
    type_joueur21 = OptionMenu(joueur21_window, choix21, *options21)
    type_joueur21.pack(side=BOTTOM)

    joueur22_window = PanedWindow(equipe2_window, orient=VERTICAL)
    equipe2_window.add(joueur22_window)

    nom22=StringVar()
    nom22.set("Cécile")
    nom_joueur22 = Entry(joueur22_window, textvariable=nom22)
    nom_joueur22.pack(side=TOP)
    def Entry22_Callback(event):
        nom_joueur22.selection_range(0, END)
    nom_joueur22.bind("<FocusIn>", Entry22_Callback)

    choix22 = StringVar()
    choix22.set("Humain")
    options22 = ("Humain", "IA débile", "IA intelligente")
    type_joueur22 = OptionMenu(joueur22_window, choix22, *options22)
    type_joueur22.pack(side=BOTTOM)

    alerte = Label(fenetre, text="Veuillez remplir tous les champs.")

    def jouer():
        global alert
        if len(nom_joueur11.get()) > 0 and len(nom_joueur12.get()) > 0 and len(nom_joueur21.get()) > 0 and len(nom_joueur22.get()) > 0:
            if nom_joueur11.get() not in (nom_joueur12.get(), nom_joueur21.get(), nom_joueur22.get())\
                and nom_joueur12.get() not in (nom_joueur21.get(), nom_joueur22.get())\
                    and nom_joueur21.get() != nom_joueur22.get():
                joueur11 = Joueur(nom_joueur11.get(), choix11.get(), 1)
                joueur12 = Joueur(nom_joueur12.get(), choix12.get(), 1)
                joueur21 = Joueur(nom_joueur21.get(), choix21.get(), 2)
                joueur22 = Joueur(nom_joueur22.get(), choix22.get(), 2)

                equipe1_copie = Equipe(joueur11.nom, joueur12.nom)
                equipe2_copie = Equipe(joueur21.nom, joueur22.nom)

                if choix.get() == "Points":
                    partie_copie = Partie(choix.get(), points.get(), diff.get(), [
                                    joueur11, joueur21, joueur12, joueur22])
                elif choix.get() == "Tours":
                    partie_copie = Partie(choix.get(), tours.get(), diff.get(), [
                                    joueur11, joueur21, joueur12, joueur22])

                fenetre.destroy()

                global partie, equipe1, equipe2
                partie = partie_copie
                equipe1 = equipe1_copie
                equipe2 = equipe2_copie
            else:
                alerte.pack_forget()
                alerte["text"] = "Veuillez saisir des noms de joueur différents."
                alerte.pack()
        else:
            alerte.pack_forget()
            alerte["text"] = "Veuillez remplir tous les champs."
            alerte.pack()

    soumettre = Button(fenetre, text="Jouer", command=jouer)
    soumettre.pack()

    fenetre.mainloop()

    return partie, equipe1, equipe2
