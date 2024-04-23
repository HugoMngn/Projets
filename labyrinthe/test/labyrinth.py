import random
import keyboard
import colorama
import numpy as np

# Dimensions du labyrinthe
hauteur = 10
largeur = 20

# Créer une matrice de cases
labyrinthe = [["°" for x in range(largeur)] for y in range(hauteur)]

# Ajouter des murs autour du labyrinthe
for x in range(largeur):
    labyrinthe[0][x] = "#"
    labyrinthe[hauteur - 1][x] = "#"
for y in range(hauteur):
    labyrinthe[y][0] = "#"
    labyrinthe[y][largeur - 1] = "#"


# Creuse un chemin dans le labyrinthe
def creuser_chemin(x, y):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 1 or ny < 1 or nx >= largeur - 1 or ny >= hauteur - 1:
            continue
        if labyrinthe[ny][nx] == " ":
            labyrinthe[y + dy // 2][x + dx // 2] = " "
            labyrinthe[ny][nx] = " "
            creuser_chemin(nx, ny)


# Creuse des chemins aléatoires dans le labyrinthe
creuser_chemin(largeur // 2, hauteur // 2)

# Position monstre aléatoire

rng = np.random.default_rng()
monstre_x, monstre_y = random.choice(
    [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
    + [(largeur - 2, y) for y in range(1, hauteur - 2)]
    + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
    + [(x, hauteur - 2) for x in range(1, largeur - 2)]
)
labyrinthe[monstre_y][monstre_x] = "M"
Minotaure = labyrinthe[monstre_y][monstre_x]

# Sortie aléatoire
sortie_x, sortie_y = random.choice(
    [(0, y) for y in range(1, hauteur - 1)]
    + [(largeur - 1, y) for y in range(1, hauteur - 1)]
    + [(x, 0) for x in range(1, largeur - 1)]
    + [(x, hauteur - 1) for x in range(1, largeur - 1)]
)
labyrinthe[sortie_y][sortie_x] = "S"
# Thésee entrée
entree_x, entree_y = random.choice(
    [(0, y) for y in range(1, hauteur - 1)]
    + [(largeur - 1, y) for y in range(1, hauteur - 1)]
    + [(x, 0) for x in range(1, largeur - 1)]
    + [(x, hauteur - 1) for x in range(1, largeur - 1)]
)
labyrinthe[entree_y][entree_x] = "T"
Thesee = labyrinthe[entree_y][entree_x]

# Afficher le labyrinthe
for ligne in labyrinthe:
    print(" ".join(ligne))

while True:
    while Thesee != Minotaure:
        if keyboard.is_pressed("z"):
            entree_y -= 1
            Thesee = labyrinthe[entree_y][entree_x]
            labyrinthe[entree_y][entree_x] = "T"
            print("")
            for ligne in labyrinthe:
                print(" ".join(ligne))
            break

        elif keyboard.is_pressed("q"):
            entree_x -= 1
            Thesee = labyrinthe[entree_y][entree_x]
            labyrinthe[entree_y][entree_x] = "T"
            print("")
            for ligne in labyrinthe:
                print(" ".join(ligne))
            break

        elif keyboard.is_pressed("s"):
            entree_y += 1
            Thesee = labyrinthe[entree_y][entree_x]
            labyrinthe[entree_y][entree_x] = "T"
            print("")
            for ligne in labyrinthe:
                print(" ".join(ligne))
            break

        elif keyboard.is_pressed("d"):
            entree_y += 1
            Thesee = labyrinthe[entree_y][entree_x]
            labyrinthe[entree_y][entree_x] = "T"
            print("")
            for ligne in labyrinthe:
                print(" ".join(ligne))
            break
