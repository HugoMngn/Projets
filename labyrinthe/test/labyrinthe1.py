# -Librairies
import random
import keyboard
import colorama
import numpy as np

# -Dimensions du labyrinthe
hauteur = 10
largeur = 20

# -Créer une matrice de cases
labyrinthe = [
    [f"\x1b[8m{chr(9608)}\x1b[0m" for x in range(largeur)] for y in range(hauteur)
]

# -Ajouter des murs autour du labyrinthe
for x in range(largeur):
    labyrinthe[0][x] = "#"
    labyrinthe[hauteur - 1][x] = "#"
for y in range(hauteur):
    labyrinthe[y][0] = "#"
    labyrinthe[y][largeur - 1] = "#"


dead_m = False
# -Position monstre aléatoire
rng = np.random.default_rng()
monstre_x, monstre_y = random.choice(
    [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
    + [(largeur - 2, y) for y in range(1, hauteur - 2)]
    + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
    + [(x, hauteur - 2) for x in range(1, largeur - 2)]
)
labyrinthe[monstre_y][monstre_x] = "M"

# -Sortie aléatoire
sortie_x, sortie_y = random.choice(
    [(0, y) for y in range(1, hauteur - 1)]
    + [(largeur - 1, y) for y in range(1, hauteur - 1)]
    + [(x, 0) for x in range(1, largeur - 1)]
    + [(x, hauteur - 1) for x in range(1, largeur - 1)]
)
labyrinthe[sortie_y][sortie_x] = "S"

# -Thésee entrée
entree_x, entree_y = random.choice(
    [(0, y) for y in range(1, hauteur - 1)]
    + [(largeur - 1, y) for y in range(1, hauteur - 1)]
    + [(x, 0) for x in range(1, largeur - 1)]
    + [(x, hauteur - 1) for x in range(1, largeur - 1)]
)
labyrinthe[entree_y][entree_x] = "E"

# -Position de Thésée
thesee_x, thesee_y = entree_x, entree_y

# -Ajouter des "#" supplémentaires
nb_murs = 50
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
            labyrinthe[y][x] = "#"
            break

# -Faire avancer Thésée dans le labyrinthe
while True:
    # Ajouter une trace derrière Thésée à chaque mouvement
    labyrinthe[thesee_y][thesee_x] = "T"

    # Afficher le labyrinthe avec la position de Thésée
    for y in range(hauteur):
        for x in range(largeur):
            print(labyrinthe[y][x], end=" ")
        print()

    # -Demander à l'utilisateur de choisir une direction

    direction = input("Choisissez une direction (haut/bas/gauche/droite) : ")
    print("")
    print("")
    # -Ajouter la trace derrière Thésée

    if direction == "gauche" and labyrinthe != "#":
        labyrinthe[thesee_y][thesee_x] = "<"
    elif direction == "droite" and labyrinthe != "#":
        labyrinthe[thesee_y][thesee_x] = ">"
    elif direction == "haut" and labyrinthe != "#":
        labyrinthe[thesee_y][thesee_x] = "|"
    elif direction == "bas" and labyrinthe != "#":
        labyrinthe[thesee_y][thesee_x] = "|"

    # -Déplacer Thésée dans la direction choisie
    if direction == "haut" and labyrinthe[thesee_y - 1][thesee_x] != "#":
        thesee_y -= 1
    elif direction == "bas" and labyrinthe[thesee_y + 1][thesee_x] != "#":
        thesee_y += 1
    elif direction == "gauche" and labyrinthe[thesee_y][thesee_x - 1] != "#":
        thesee_x -= 1
    elif direction == "droite" and labyrinthe[thesee_y][thesee_x + 1] != "#":
        thesee_x += 1
    else:
        print("Y'a un mur")

    # Vérifier si Thésée a atteint le minautore
    if thesee_x == monstre_x and thesee_y == monstre_y:
        print("Bravo, vous avez atteint le minautore !")
        labyrinthe[monstre_y][monstre_x] = f"\x1b[8m{chr(9608)}\x1b[0m"
        dead_m = True

    # Vérifier si Thésée a atteint la sortie
    if thesee_x == sortie_x and thesee_y == sortie_y and dead_m:
        print("Bravo, vous avez réussi à sortir du labyrinthe !")
        break
    elif thesee_x == sortie_x and thesee_y == sortie_y and not dead_m:
        print("Vous n'avez pas tué le minautore !")

# -Afficher le labyrinthe
for ligne in labyrinthe:
    print(" ".join(ligne))
