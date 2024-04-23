# -Librairies
import random
import keyboard
from colorama import init, Fore, Back, Style
import numpy as np
import pickle


def blanc(text):
    newtext = Fore.LIGHTWHITE_EX + text
    return newtext + Style.RESET_ALL


def blue(text):
    newtext = Fore.LIGHTBLUE_EX + text
    return newtext + Style.RESET_ALL


# -Nom joueur
joueur = 'defaulname1'
while not (len(joueur) < 10 and len(joueur) > 0):
    joueur = input(blue("Entrez le nom du joueur : ")).capitalize()
    if len(joueur) >= 10:
        print(Fore.RED + "Le nom ne doit pas comporter plus de 9 lettres" + Fore.RESET)
    if len(joueur) <= 0:
        print(Fore.RED + "Le nom doit au minimum contenir 1 lettre" + Fore.RESET)

    print("")
    print("")
    print("")
# -Histoire du jeu

print(Fore.LIGHTGREEN_EX + "Bienvenue sur le LABY-ESCAPE" + Fore.RESET)

print("")
print(Fore.LIGHTYELLOW_EX + "Pour poursuivre sa quete, Thésée doit franchir le labyrinthe en terrasant le minautore afin de trouver la sortie " + Fore.RESET)
print("")
print(blue("□"), Fore.LIGHTYELLOW_EX +
      "= Mur magique incassable par le minautore" + Fore.RESET)
print(blanc("#"), Fore.LIGHTYELLOW_EX +
      "= Mur du labyrinthe cassable par le minautore" + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "M" + Fore.RESET,
      Fore.LIGHTYELLOW_EX + "= Minautore" + Fore.RESET)
print(Fore.LIGHTBLUE_EX + "O - o" + Fore.RESET, Fore.LIGHTYELLOW_EX +
      " = Portails de teleportations" + Fore.RESET)
print(Fore.LIGHTGREEN_EX + "T" + Fore.RESET,
      Fore.LIGHTYELLOW_EX + "= Thésée" + Fore.RESET)
print(Fore.LIGHTYELLOW_EX + "S" + Fore.RESET,
      Fore.LIGHTYELLOW_EX + "= Sortie" + Fore.RESET)
print("")
print(Fore.LIGHTYELLOW_EX + "l'emplacement des murs interieurs, minautore, portails de téléportations, sortie et Thésée change a chaque partie" + Fore.RESET)

# -Initialise la bibliothèque colorama
init()

# -Dimensions du labyrinthe
hauteur = 16
largeur = 22

# -Créer une matrice de cases
labyrinthe = [
    [f"\x1b[8m{chr(9608)}\x1b[0m" for x in range(largeur)] for y in range(hauteur)
]

# -Ajouter des murs autour du labyrinthe
for x in range(largeur):
    labyrinthe[0][x] = blue("□")
    labyrinthe[hauteur - 1][x] = blue("□")
for y in range(hauteur):
    labyrinthe[y][0] = blue("□")
    labyrinthe[y][largeur - 1] = blue("□")

dead_m = False

# -Position monstre aléatoire
rng = np.random.default_rng()
monstre_x, monstre_y = random.choice(
    [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
    + [(largeur - 2, y) for y in range(1, hauteur - 2)]
    + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
    + [(x, hauteur - 2) for x in range(1, largeur - 2)]
)
labyrinthe[monstre_y][monstre_x] = (Fore.LIGHTMAGENTA_EX + "M" + Fore.RESET)

# -TP aléatoire
rng = np.random.default_rng()
tp_x, tp_y = random.choice(
    [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
    + [(largeur - 2, y) for y in range(1, hauteur - 2)]
    + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
    + [(x, hauteur - 2) for x in range(1, largeur - 2)]
)
labyrinthe[tp_y][tp_x] = (Fore.LIGHTCYAN_EX + "O" + Fore.RESET)

tp_y, tp_x != monstre_y, monstre_x

tp2_x, tp2_y = random.choice(
    [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
    + [(largeur - 2, y) for y in range(1, hauteur - 2)]
    + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
    + [(x, hauteur - 2) for x in range(1, largeur - 2)]
)
labyrinthe[tp2_y][tp2_x] = (Fore.LIGHTCYAN_EX + "o" + Fore.RESET)

tp2_y, tp2_x != monstre_y, monstre_x and tp2_y, tp2_x != tp_x, tp_y

tp3_x, tp3_y = random.choice(
    [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
    + [(largeur - 2, y) for y in range(1, hauteur - 2)]
    + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
    + [(x, hauteur - 2) for x in range(1, largeur - 2)]
)
labyrinthe[tp3_y][tp3_x] = (Fore.LIGHTCYAN_EX + "O" + Fore.RESET)

tp3_y, tp3_x != monstre_y, monstre_x

tp4_x, tp4_y = random.choice(
    [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
    + [(largeur - 2, y) for y in range(1, hauteur - 2)]
    + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
    + [(x, hauteur - 2) for x in range(1, largeur - 2)]
)
labyrinthe[tp4_y][tp4_x] = (Fore.LIGHTCYAN_EX + "o" + Fore.RESET)

tp4_y, tp4_x != monstre_y, monstre_x and tp4_y, tp4_x != tp3_x, tp3_y

tp5_x, tp5_y = random.choice(
    [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
    + [(largeur - 2, y) for y in range(1, hauteur - 2)]
    + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
    + [(x, hauteur - 2) for x in range(1, largeur - 2)]
)
labyrinthe[tp5_y][tp5_x] = (Fore.LIGHTCYAN_EX + "O" + Fore.RESET)

tp5_y, tp5_x != monstre_y, monstre_x

tp6_x, tp6_y = random.choice(
    [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
    + [(largeur - 2, y) for y in range(1, hauteur - 2)]
    + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
    + [(x, hauteur - 2) for x in range(1, largeur - 2)]
)
labyrinthe[tp6_y][tp6_x] = (Fore.LIGHTCYAN_EX + "o" + Fore.RESET)

tp6_y, tp6_x != monstre_y, monstre_x and tp6_y, tp6_x != tp5_x, tp5_y

# -Sortie aléatoire
sortie_x, sortie_y = random.choice(
    [(0, y) for y in range(1, hauteur - 1)]
    + [(largeur - 1, y) for y in range(1, hauteur - 1)]
    + [(x, 0) for x in range(1, largeur - 1)]
    + [(x, hauteur - 1) for x in range(1, largeur - 1)]
)
labyrinthe[sortie_y][sortie_x] = (Fore.LIGHTYELLOW_EX + "S" + Fore.RESET)

# -Thésee entrée
entree_x, entree_y = random.choice(
    [(0, y) for y in range(1, hauteur - 1)]
    + [(largeur - 1, y) for y in range(1, hauteur - 1)]
    + [(x, 0) for x in range(1, largeur - 1)]
    + [(x, hauteur - 1) for x in range(1, largeur - 1)]
)
labyrinthe[entree_y][entree_x] = (Fore.LIGHTYELLOW_EX + "E" + Fore.RESET)


# -Position de Thésée
thesee_x, thesee_y = entree_x, entree_y

# -Ajouter des "#" supplémentaires
nb_murs = 88
for i in range(nb_murs):
    while True:
        x, y = random.randint(1, largeur - 2), random.randint(1, hauteur - 2)
        if labyrinthe[y][x] == f"\x1b[8m{chr(9608)}\x1b[0m":
            if (x, y) in [
                (entree_x + dx, entree_y + dy)
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            ] or (x, y) in [
                (sortie_x + dx, sortie_y + dy)
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            ]:
                continue
            labyrinthe[y][x] = blanc("#")
            break
# Compteur de score de la partie
score = ((((hauteur * largeur) - (2 * largeur)) -
         (2 * hauteur)) + 4) - nb_murs - 142

# -Faire avancer Thésée dans le labyrinthe
while True:
    # Ajouter une trace derrière Thésée à chaque mouvement
    labyrinthe[thesee_y][thesee_x] = (Fore.LIGHTGREEN_EX + "T" + Fore.RESET)
    labyrinthe[monstre_y][monstre_x] = (
        Fore.LIGHTMAGENTA_EX + "M" + Fore.RESET)

    # -Afficher le labyrinthe avec la position de Thésée
    for y in range(hauteur):
        for x in range(largeur):
            print(labyrinthe[y][x], end=" ")
        print()

    print(Fore.GREEN + "score:" + Fore.RESET)
    print(score)

    # -Demander à l'utilisateur de choisir une direction
    direction = input("Choisissez une direction (Z/Q/S/D) : ")
    score -= 1
    print("")
    print("")
    print("")
    print("")
    print("")

    # -Ajouter la trace derrière Thésée
    if direction == "Q" and labyrinthe != blanc("#"):
        labyrinthe[thesee_y][thesee_x] = (Fore.RED + "←" + Fore.RESET)
    elif direction == "D" and labyrinthe != blanc("#"):
        labyrinthe[thesee_y][thesee_x] = (Fore.RED + "→" + Fore.RESET)
    elif direction == "Z" and labyrinthe != blanc("#"):
        labyrinthe[thesee_y][thesee_x] = (Fore.RED + "↑" + Fore.RESET)
    elif direction == "S" and labyrinthe != blanc("#"):
        labyrinthe[thesee_y][thesee_x] = (Fore.RED + "↓" + Fore.RESET)

    if direction == "q" and labyrinthe != blanc("#"):
        labyrinthe[thesee_y][thesee_x] = (Fore.RED + "←" + Fore.RESET)
    elif direction == "d" and labyrinthe != blanc("#"):
        labyrinthe[thesee_y][thesee_x] = (Fore.RED + "→" + Fore.RESET)
    elif direction == "z" and labyrinthe != blanc("#"):
        labyrinthe[thesee_y][thesee_x] = (Fore.RED + "↑" + Fore.RESET)
    elif direction == "s" and labyrinthe != blanc("#"):
        labyrinthe[thesee_y][thesee_x] = (Fore.RED + "↓" + Fore.RESET)

    # -Déplacer Thésée dans la direction choisie
    if (
            direction == "Z"
            and labyrinthe[thesee_y - 1][thesee_x] != blanc("#")
            and labyrinthe[thesee_y - 1][thesee_x] != blue("□")):
        thesee_y -= 1
    elif (direction == "S" and labyrinthe[thesee_y + 1][thesee_x] != blanc("#") and labyrinthe[thesee_y + 1][thesee_x] != blue("□")):
        thesee_y += 1
    elif (direction == "Q" and labyrinthe[thesee_y][thesee_x - 1] != blanc("#") and labyrinthe[thesee_y][thesee_x - 1] != blue("□")):
        thesee_x -= 1
    elif (direction == "D" and labyrinthe[thesee_y][thesee_x + 1] != blanc("#") and labyrinthe[thesee_y][thesee_x + 1] != blue("□")):
        thesee_x += 1
    elif direction == "":
        print((Fore.LIGHTRED_EX + "Veuillez selectioner une direction") + Fore.RESET)
    elif direction == "z" or direction == "q" or direction == "s" or direction == "d":
        pass
    else:
        print((Fore.LIGHTRED_EX + "Vous ne pouvez pas passer le mur") + Fore.RESET)

    if (
            direction == "z"
            and labyrinthe[thesee_y - 1][thesee_x] != blanc("#")
            and labyrinthe[thesee_y - 1][thesee_x] != blue("□")):
        thesee_y -= 1
    elif (direction == "s" and labyrinthe[thesee_y + 1][thesee_x] != blanc("#") and labyrinthe[thesee_y + 1][thesee_x] != blue("□")):
        thesee_y += 1
    elif (direction == "q" and labyrinthe[thesee_y][thesee_x - 1] != blanc("#") and labyrinthe[thesee_y][thesee_x - 1] != blue("□")):
        thesee_x -= 1
    elif (direction == "d" and labyrinthe[thesee_y][thesee_x + 1] != blanc("#") and labyrinthe[thesee_y][thesee_x + 1] != blue("□")):
        thesee_x += 1
    elif direction == "":
        print((Fore.LIGHTRED_EX + "Veuillez selectioner une direction") + Fore.RESET)
    elif direction == "Z" or direction == "Q" or direction == "S" or direction == "D":
        pass
    else:
        print((Fore.LIGHTRED_EX + "Vous ne pouvez pas passer le mur") + Fore.RESET)

    # -Vérifier si Thésée a atteint le minautore
    if thesee_x == monstre_x and thesee_y == monstre_y:
        print((Fore.LIGHTYELLOW_EX +
              "Bravo, vous avez atteint le minautore !") + Fore.RESET)
        labyrinthe[monstre_y][monstre_x] = f"\x1b[8m{chr(9608)}\x1b[0m"
        dead_m = True

    labyrinthe[monstre_y][monstre_x] = f"\x1b[8m{chr(9608)}\x1b[0m"
    if not dead_m:
        if (
            direction == "Z"
            or direction == "Q"
            or direction == "S"
            or direction == "D"
            or direction == "z"
            or direction == "q"
            or direction == "s"
            or direction == "d"
        ):
            minotaure_dir = random.randint(0, 3)
            if minotaure_dir == 0 and labyrinthe[monstre_y - 1][monstre_x] != blue("□"):
                monstre_y -= 1
            elif minotaure_dir == 1 and labyrinthe[monstre_y + 1][monstre_x] != blue("□"):
                monstre_y += 1
            elif minotaure_dir == 2 and labyrinthe[monstre_y][monstre_x - 1] != blue("□"):
                monstre_x -= 1
            elif minotaure_dir == 3 and labyrinthe[monstre_y][monstre_x + 1] != blue("□"):
                monstre_x += 1

    # -Vérifier si Thésée a atteint le minautore
    if thesee_x == monstre_x and thesee_y == monstre_y:
        print((Fore.LIGHTYELLOW_EX +
              "Bravo, vous avez atteint le minautore !") + Fore.RESET)
        labyrinthe[monstre_y][monstre_x] = f"\x1b[8m{chr(9608)}\x1b[0m"
        dead_m = True

    # -Vérifier si Thésée a atteint la sortie
    if thesee_x == sortie_x and thesee_y == sortie_y and dead_m:
        print(
            (Fore.LIGHTYELLOW_EX + "Bravo, vous avez réussi à sortir du labyrinthe !")
            + Fore.RESET
        )
        print("Votre score final:", score)
        break
    elif thesee_x == sortie_x and thesee_y == sortie_y and not dead_m:
        print((Fore.LIGHTRED_EX + "Vous n'avez pas tué le minautore !") + Fore.RESET)

    # score game over
    if score == 0:
        print((Fore.LIGHTRED_EX + "GAME OVER, VOUS ETES MORT DE SOIF") + Fore.RESET)
        break
    print("")
    # Demander au joueur s'il souhaite relancer la partie
while True:
    choix = input("Voulez-vous relancer la partie ? (O/N) ")
    if choix.upper() == "O":
        # Code pour relancer la partie
        break
    elif choix.upper() == "N":
        print("Merci d'avoir joué !")
        break
    else:
        print("Réponse invalide. Veuillez répondre par O ou N.")
    # -Vérifier si Thésée a atteint un portail de téléportation
    if thesee_x == tp_x and thesee_y == tp_y:
        print(
            (Fore.LIGHTYELLOW_EX + "Bravo vous avez trouver un portail de teleportation !")
            + Fore.RESET
        )
        thesee_x, thesee_y = tp2_x, tp2_y
    elif thesee_x == tp2_x and thesee_y == tp2_y:
        print(
            (Fore.LIGHTYELLOW_EX + "Bravo vous avez trouver un portail de teleportation !")
            + Fore.RESET
        )
        thesee_x, thesee_y = tp_x, tp_y

    if thesee_x == tp3_x and thesee_y == tp3_y:
        print(
            (Fore.LIGHTYELLOW_EX + "Bravo vous avez trouver un portail de teleportation !")
            + Fore.RESET
        )
        thesee_x, thesee_y = tp4_x, tp4_y
    if thesee_x == tp4_x and thesee_y == tp4_y:
        print(
            (Fore.LIGHTYELLOW_EX + "Bravo vous avez trouver un portail de teleportation !")
            + Fore.RESET
        )
        thesee_x, thesee_y = tp3_x, tp3_y

    if thesee_x == tp5_x and thesee_y == tp5_y:
        print(
            (Fore.LIGHTYELLOW_EX + "Bravo vous avez trouver un portail de teleportation !")
            + Fore.RESET
        )
        thesee_x, thesee_y = tp6_x, tp6_y
    elif thesee_x == tp6_x and thesee_y == tp6_y:
        print((Fore.LIGHTYELLOW_EXk + "Bravo vous avez trouver un portail de teleportation !")
              + Fore.RESET
              )
        thesee_x, thesee_y = tp5_x, tp5_y

# -Afficher le labyrinthe
for ligne in labyrinthe:
    print(" ".join(ligne))

# Enregistrement de la partie
partie = {
    "joueur": joueur,
    "score final du joueur :": score,
}

with open("partie_labyrinthe_pickle.txt", "wb") as f:
    pickle.dump(partie, f)

# Demander au joueur s'il souhaite relancer la partie
while True:
    choix = input("Voulez-vous relancer la partie ? (O/N) ")
    if choix.upper() == "O":
        # Code pour relancer la partie
        break
    elif choix.upper() == "N":
        print("Merci d'avoir joué !")
        break
    else:
        print("Réponse invalide. Veuillez répondre par O ou N.")
