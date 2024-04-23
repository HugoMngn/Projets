# # -Librairies
# import random
# import keyboard
# import colorama
# import numpy as np

# # -Dimensions du labyrinthe
# hauteur = 10
# largeur = 20

# # -Créer une matrice de cases
# labyrinthe = [["°" for x in range(largeur)] for y in range(hauteur)]

# # -Ajouter des murs autour du labyrinthe
# for x in range(largeur):
#     labyrinthe[0][x] = "#"
#     labyrinthe[hauteur - 1][x] = "#"
# for y in range(hauteur):
#     labyrinthe[y][0] = "#"
#     labyrinthe[y][largeur - 1] = "#"


# # -Creuse un chemin dans le labyrinthe
# def creuser_chemin(x, y, entree_x, entree_y, sortie_x, sortie_y):
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     random.shuffle(directions)
#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if nx < 1 or ny < 1 or nx >= largeur - 1 or ny >= hauteur - 1:
#             continue
#         if labyrinthe[ny][nx] == " ":
#             if (nx, ny) == (entree_x, entree_y) or (nx, ny) == (sortie_x, sortie_y):
#                 continue
#             labyrinthe[y + dy // 2][x + dx // 2] = " "
#             labyrinthe[ny][nx] = " "
#             creuser_chemin(nx, ny, entree_x, entree_y, sortie_x, sortie_y)


# # -Position monstre aléatoire
# rng = np.random.default_rng()
# monstre_x, monstre_y = random.choice(
#     [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
#     + [(largeur - 2, y) for y in range(1, hauteur - 2)]
#     + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
#     + [(x, hauteur - 2) for x in range(1, largeur - 2)]
# )
# labyrinthe[monstre_y][monstre_x] = "M"

# # -Sortie aléatoire
# sortie_x, sortie_y = random.choice(
#     [(0, y) for y in range(1, hauteur - 1)]
#     + [(largeur - 1, y) for y in range(1, hauteur - 1)]
#     + [(x, 0) for x in range(1, largeur - 1)]
#     + [(x, hauteur - 1) for x in range(1, largeur - 1)]
# )
# labyrinthe[sortie_y][sortie_x] = "S"

# # -Thésee entrée
# entree_x, entree_y = random.choice(
#     [(0, y) for y in range(1, hauteur - 1)]
#     + [(largeur - 1, y) for y in range(1, hauteur - 1)]
#     + [(x, 0) for x in range(1, largeur - 1)]
#     + [(x, hauteur - 1) for x in range(1, largeur - 1)]
# )


# # Trouver un point aléatoire à l'intérieur de la grille
# def trouver_point_interne():
#     return random.randint(1, largeur - 2), random.randint(1, hauteur - 2)


# # Déterminer si deux points sont voisins directs
# def sont_voisins(p1, p2):
#     return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) == 1


# # Créer un labyrinthe
# labyrinthe = [[1] * largeur for _ in range(hauteur)]

# # Ajouter les bords du labyrinthe
# for x in range(largeur):
#     labyrinthe[x][0] = 0
#     labyrinthe[x][hauteur - 1] = 0

# for y in range(hauteur):
#     labyrinthe[0][y] = 0
#     labyrinthe[largeur - 1][y] = 0

# # Créer des murs dans le labyrinthe en utilisant l'algorithme de Kruskal
# murs = []
# for x in range(1, largeur - 1):
#     for y in range(1, hauteur - 1):
#         if x % 2 == 1 or y % 2 == 1:
#             labyrinthe[x][y] = 0
#         else:
#             murs.append((x, y))

# # Mélanger les murs
# random.shuffle(murs)

# # Enlever les murs en utilisant l'algorithme de Kruskal
# ensemble = {entree_x, entree_y}
# for mur in murs:
#     p1 = mur
#     if p1[0] % 2 == 1:
#         p2 = (p1[0] + 1, p1[1])
#     else:
#         p2 = (p1[0], p1[1] + 1)
#     if find(p1[0] + p1[1] * largeur) != find(p2[0] + p2[1] * largeur):
#         ensemble.add(find(p1[0] + p1[1] * largeur))
#         fusion(p1[0] + p1[1] * largeur, p2[0] + p2[1] * largeur)
#         murs.remove(mur)
