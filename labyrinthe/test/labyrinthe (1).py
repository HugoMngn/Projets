# -Librairies
import random
import keyboard
from colorama import init, Fore, Back, Style
import numpy as np
import pickle


# definition des couleurs
def blanc(text):
    newtext = Fore.LIGHTWHITE_EX + text
    return newtext + Style.RESET_ALL


def blue(text):
    newtext = Fore.LIGHTBLUE_EX + text
    return newtext + Style.RESET_ALL


# -Nom joueur
joueur = "defaulname1"
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
print(
    Fore.LIGHTYELLOW_EX
    + "Pour poursuivre sa quete, Thésée doit franchir le labyrinthe en terrasant le minautore afin de trouver la sortie "
    + Fore.RESET
)
print("")
print(
    blue("□"),
    Fore.LIGHTYELLOW_EX + "= Mur magique incassable par le minautore" + Fore.RESET,
)
print(
    blanc("#"),
    Fore.LIGHTYELLOW_EX + "= Mur du labyrinthe cassable par le minautore" + Fore.RESET,
)
print(
    Fore.LIGHTMAGENTA_EX + "M" + Fore.RESET,
    Fore.LIGHTYELLOW_EX + "= Minautore" + Fore.RESET,
)
print(
    Fore.LIGHTBLUE_EX + "O - o" + Fore.RESET,
    Fore.LIGHTYELLOW_EX + " = Portails de teleportations" + Fore.RESET,
)
print(
    Fore.LIGHTGREEN_EX + "T" + Fore.RESET, Fore.LIGHTYELLOW_EX + "= Thésée" + Fore.RESET
)
print(
    Fore.LIGHTYELLOW_EX + "S" + Fore.RESET,
    Fore.LIGHTYELLOW_EX + "= Sortie" + Fore.RESET,
)
print("")
print(
    Fore.LIGHTYELLOW_EX
    + "l'emplacement des murs interieurs, minautore, portails de téléportations, sortie et Thésée change a chaque partie"
    + Fore.RESET
)
print("")

# Initialise la bibliothèque colorama
init()

# boucle permettant de relancer une partie
banane = False
while True:
    # -Dimensions du labyrinthe
    hauteur = 16
    largeur = 22

    # variable utilisé plus tard:
    dead_m = False  # verifier mort du minotaure
    jsp = True  # variable servant à redémarrer

    # -Créer une matrice de cases
    labyrinthe = [
        [f"\x1b[8m{chr(9608)}\x1b[0m" for x in range(largeur)] for y in range(hauteur)
    ]

    #  -Ajouter des murs autour du labyrinthe
    for x in range(largeur):
        labyrinthe[0][x] = blue("□")
        labyrinthe[hauteur - 1][x] = blue("□")
    for y in range(hauteur):
        labyrinthe[y][0] = blue("□")
        labyrinthe[y][largeur - 1] = blue("□")

    # -Position monstre aléatoire
    rng = np.random.default_rng()
    monstre_x, monstre_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    while not (
        ((monstre_y) >= 1)
        and ((monstre_y) <= (hauteur - 1))
        and ((monstre_x) >= 1)
        and ((monstre_x) <= (largeur - 1))
    ):
        monstre_x, monstre_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )

    labyrinthe[monstre_y][monstre_x] = Fore.MAGENTA + "M" + Fore.RESET

    # -TP aléatoire, à faire par couple entrée/sortie
    rng = np.random.default_rng()
    tp_x, tp_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    while not (
        ((tp_y) >= 1)
        and ((tp_y) <= (hauteur - 1))
        and ((tp_x) >= 1)
        and ((tp_x) <= (largeur - 1))
    ):
        tp_x, tp_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
    labyrinthe[tp_y][tp_x] = Fore.CYAN + "O" + Fore.RESET

    tp2_x, tp2_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    while not (
        ((tp2_y) >= 1)
        and ((tp2_y) <= (hauteur - 1))
        and ((tp2_x) >= 1)
        and ((tp2_x) <= (largeur - 1))
    ):
        tp2_x, tp2_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
    labyrinthe[tp2_y][tp2_x] = Fore.CYAN + "o" + Fore.RESET

    tp3_x, tp3_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    while not (
        ((tp3_y) >= 1)
        and ((tp3_y) <= (hauteur - 1))
        and ((tp3_x) >= 1)
        and ((tp3_x) <= (largeur - 1))
    ):
        tp3_x, tp3_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
    labyrinthe[tp3_y][tp3_x] = Fore.CYAN + "O" + Fore.RESET

    tp4_x, tp4_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    while not (
        ((tp4_y) >= 1)
        and ((tp4_y) <= (hauteur - 1))
        and ((tp4_x) >= 1)
        and ((tp4_x) <= (largeur - 1))
    ):
        tp4_x, tp4_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
    labyrinthe[tp4_y][tp4_x] = Fore.CYAN + "o" + Fore.RESET

    tp5_x, tp5_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    while not (
        ((tp5_y) >= 1)
        and ((tp5_y) <= (hauteur - 1))
        and ((tp5_x) >= 1)
        and ((tp5_x) <= (largeur - 1))
    ):
        tp5_x, tp5_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
    labyrinthe[tp5_y][tp5_x] = Fore.CYAN + "O" + Fore.RESET

    tp6_x, tp6_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    while not (
        ((tp6_y) >= 1)
        and ((tp6_y) <= (hauteur - 1))
        and ((tp6_x) >= 1)
        and ((tp6_x) <= (largeur - 1))
    ):
        tp6_x, tp6_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
    labyrinthe[tp6_y][tp6_x] = Fore.CYAN + "o" + Fore.RESET

    # -Sortie aléatoire
    sortie_x, sortie_y = random.choice(
        [(0, y) for y in range(1, hauteur - 1)]
        + [(largeur - 1, y) for y in range(1, hauteur - 1)]
        + [(x, 0) for x in range(1, largeur - 1)]
        + [(x, hauteur - 1) for x in range(1, largeur - 1)]
    )
    labyrinthe[sortie_y][sortie_x] = Fore.YELLOW + "S" + Fore.RESET

    # -Thésee entrée
    entree_x, entree_y = random.choice(
        [(0, y) for y in range(1, hauteur - 1)]
        + [(largeur - 1, y) for y in range(1, hauteur - 1)]
        + [(x, 0) for x in range(1, largeur - 1)]
        + [(x, hauteur - 1) for x in range(1, largeur - 1)]
    )
    labyrinthe[entree_y][entree_x] = Fore.YELLOW + "E" + Fore.RESET

    # -Position de Thésée
    thesee_x, thesee_y = entree_x, entree_y

    # afficher les murs / Ajouter des "#" supplémentaires
    nb_murs = 89
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

    # -Compteur de score de la partie
    score = (
        ((((hauteur * largeur) - (2 * largeur)) - (2 * hauteur)) + 4) - nb_murs - 101
    )

    # verifier accessibilité entre 2 points
    def is_accessible(labyrinthe, y1, x1, y2, x2):
        verif = {(y1, x1)}
        verif2 = {(y1, x1)}

        while verif:
            a, b = verif.pop()

            for da, db in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                na, nb = a + da, b + db
                if na == y2 and nb == x2:
                    return True
                if (
                    na >= 0
                    and na < len(labyrinthe)
                    and nb >= 0
                    and nb < len(labyrinthe[0])
                ):
                    cell = labyrinthe[na][nb]
                    if cell in ("\x1b[8m█\x1b[0m", "O", "o") and (na, nb) not in verif2:
                        verif.add((na, nb))
                        verif2.add((na, nb))
        return False

    # fonction pour vérifier si c'est finissable
    def is_finishable(
        labyrinthe, entree_y, entree_x, sortie_y, sortie_x, monstre_y, monstre_x
    ):
        verif = {(entree_y, entree_x)}
        verif2 = {(0, 0)}
        trouve_monstre = False
        trouve_sortie = False

        while verif and not (trouve_monstre and trouve_sortie):
            # choisir next case à test
            a, b = verif.pop()

            # test des cases voisines
            for da, db in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                na, nb = a + da, b + db
                if (
                    na >= 0
                    and na < len(labyrinthe)
                    and nb >= 0
                    and nb < len(labyrinthe[0])
                ):
                    cell = labyrinthe[na][nb]
                    if cell in ("\x1b[8m█\x1b[0m", "O", "o") and (na, nb) not in verif2:
                        verif.add((na, nb))
                        verif2.add((na, nb))
                    elif cell == labyrinthe[monstre_y][monstre_x]:
                        trouve_monstre = True
                    elif cell == labyrinthe[sortie_y][sortie_x]:
                        trouve_sortie = True

            # vérifier les conditions d'arrêt
            if not verif:
                return False

        # Vérifier si minotaure et la sortie sont atteignables
        if is_accessible(
            labyrinthe, sortie_y, sortie_x, monstre_y, monstre_x
        ) and is_accessible(labyrinthe, entree_y, entree_x, sortie_y, sortie_x):
            return True
        else:
            return False

    # usage fonction is_finishable pour le savoir et potentiellement redémarrer
    is_finishable(
        labyrinthe, entree_y, entree_x, sortie_y, sortie_x, monstre_y, monstre_x
    )

    if not is_finishable(
        labyrinthe, entree_y, entree_x, sortie_y, sortie_x, monstre_y, monstre_x
    ):
        jsp = False

    # -Faire avancer Thésée dans le labyrinthe
    while True:
        # -Ajouter des murs autour du labyrinthe

        for x in range(largeur):
            labyrinthe[0][x] = blue("□")
            labyrinthe[hauteur - 1][x] = blue("□")
        for y in range(hauteur):
            labyrinthe[y][0] = blue("□")
            labyrinthe[y][largeur - 1] = blue("□")

        # afficher entrée et sortie en permanence
        labyrinthe[entree_y][entree_x] = Fore.YELLOW + "E" + Fore.RESET
        labyrinthe[sortie_y][sortie_x] = Fore.YELLOW + "S" + Fore.RESET

        labyrinthe[thesee_y][thesee_x] = Fore.GREEN + "T" + Fore.RESET

        # arreter la génération en cours pour redémarrer
        if not jsp:
            break

        # -regénérer le labyrinthe avec la position de Thésée en cas de dysfonctionnement sur l'apparition d'objet
        for y in range(hauteur):
            for x in range(largeur):
                print(labyrinthe[y][x], end=" ")
            print()

        # -Demander à l'utilisateur de choisir une direction
        print("score:", score)
        direction = input("Choisissez une direction (Z/Q/S/D) : ")
        score -= 1
        print("")
        print("")
        print("")
        print("")
        print("")

        # -Ajouter la trace derrière Thésée
        if direction.upper() == "Q" and labyrinthe != blanc("#"):
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "←" + Fore.RESET
        elif direction.upper() == "D" and labyrinthe != blanc("#"):
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "→" + Fore.RESET
        elif direction.upper() == "Z" and labyrinthe != blanc("#"):
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "↑" + Fore.RESET
        elif direction.upper() == "S" and labyrinthe != blanc("#"):
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "↓" + Fore.RESET

        # -Déplacer Thésée dans la direction choisie
        if (
            direction.upper() == "Z"
            and labyrinthe[thesee_y - 1][thesee_x] != blanc("#")
            and labyrinthe[thesee_y - 1][thesee_x] != blue("□")
        ):
            thesee_y -= 1
        elif (
            direction.upper() == "S"
            and labyrinthe[thesee_y + 1][thesee_x] != blanc("#")
            and labyrinthe[thesee_y + 1][thesee_x] != blue("□")
        ):
            thesee_y += 1
        elif (
            direction.upper() == "Q"
            and labyrinthe[thesee_y][thesee_x - 1] != blanc("#")
            and labyrinthe[thesee_y][thesee_x - 1] != blue("□")
        ):
            thesee_x -= 1
        elif (
            direction.upper() == "D"
            and labyrinthe[thesee_y][thesee_x + 1] != blanc("#")
            and labyrinthe[thesee_y][thesee_x + 1] != blue("□")
        ):
            thesee_x += 1
        elif direction == "":
            print(
                (Fore.LIGHTRED_EX + "Veuillez selectioner une direction") + Fore.RESET
            )
        else:
            print((Fore.LIGHTRED_EX + "Vous ne pouvez pas passer le mur") + Fore.RESET)

        # -Vérifier si Thésée a atteint le minautore
        if thesee_x == monstre_x and thesee_y == monstre_y:
            dead_m = True
            labyrinthe[monstre_y][monstre_x] = f"\x1b[8m{chr(9608)}\x1b[0m"

        # déplacement du minotaure dans le cadre
        if not dead_m:
            labyrinthe[monstre_y][monstre_x] = f"\x1b[8m{chr(9608)}\x1b[0m"
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
                if (
                    minotaure_dir == 0
                    and ((monstre_y - 1) >= 1)
                    and ((monstre_y - 1) < (hauteur - 1))
                ):
                    if labyrinthe[monstre_y - 1][monstre_x] != blanc("#"):
                        monstre_y -= 1
                        labyrinthe[monstre_y][monstre_x] = (
                            Fore.MAGENTA + "M" + Fore.RESET
                        )
                    else:
                        labyrinthe[monstre_y][monstre_x] = (
                            Fore.MAGENTA + "M" + Fore.RESET
                        )
                        continue

                elif (
                    minotaure_dir == 1
                    and ((monstre_y + 1) >= 1)
                    and ((monstre_y + 1) < (hauteur - 1))
                ):
                    if labyrinthe[monstre_y + 1][monstre_x] != blanc("#"):
                        monstre_y += 1
                        labyrinthe[monstre_y][monstre_x] = (
                            Fore.MAGENTA + "M" + Fore.RESET
                        )
                    else:
                        labyrinthe[monstre_y][monstre_x] = (
                            Fore.MAGENTA + "M" + Fore.RESET
                        )
                        continue

                elif (
                    minotaure_dir == 2
                    and ((monstre_x - 1) >= 1)
                    and ((monstre_x - 1) < (largeur - 1))
                ):
                    if labyrinthe[monstre_y][monstre_x - 1] != blanc("#"):
                        monstre_x -= 1
                        labyrinthe[monstre_y][monstre_x] = (
                            Fore.MAGENTA + "M" + Fore.RESET
                        )
                    else:
                        labyrinthe[monstre_y][monstre_x] = (
                            Fore.MAGENTA + "M" + Fore.RESET
                        )
                        continue

                elif (
                    minotaure_dir == 3
                    and ((monstre_x + 1) >= 1)
                    and ((monstre_x + 1) < (largeur - 1))
                ):
                    if labyrinthe[monstre_y][monstre_x + 1] != blanc("#"):
                        monstre_x += 1
                        labyrinthe[monstre_y][monstre_x] = (
                            Fore.MAGENTA + "M" + Fore.RESET
                        )
                    else:
                        labyrinthe[monstre_y][monstre_x] = (
                            Fore.MAGENTA + "M" + Fore.RESET
                        )
                        continue
                else:
                    labyrinthe[monstre_y][monstre_x] = Fore.MAGENTA + "M" + Fore.RESET

        # -Vérifier si Thésée a atteint le minautore
        if thesee_x == monstre_x and thesee_y == monstre_y:
            print(
                (Fore.LIGHTYELLOW_EX + "Bravo, vous avez atteint le minautore !")
                + Fore.RESET
            )

        # -Vérifier si Thésée a atteint un portail de téléportation
        if thesee_x == tp_x and thesee_y == tp_y:
            print(
                (Fore.YELLOW + "Bravo vous avez trouver un portail de teleportation !")
                + Fore.RESET
            )
            thesee_x, thesee_y = tp2_x, tp2_y
        elif thesee_x == tp2_x and thesee_y == tp2_y:
            print(
                (Fore.YELLOW + "Bravo vous avez trouver un portail de teleportation !")
                + Fore.RESET
            )
            thesee_x, thesee_y = tp_x, tp_y

        if thesee_x == tp3_x and thesee_y == tp3_y:
            print(
                (Fore.YELLOW + "Bravo vous avez trouver un portail de teleportation !")
                + Fore.RESET
            )
            thesee_x, thesee_y = tp4_x, tp4_y
        if thesee_x == tp4_x and thesee_y == tp4_y:
            print(
                (Fore.YELLOW + "Bravo vous avez trouver un portail de teleportation !")
                + Fore.RESET
            )
            thesee_x, thesee_y = tp3_x, tp3_y

        if thesee_x == tp5_x and thesee_y == tp5_y:
            print(
                (Fore.YELLOW + "Bravo vous avez trouver un portail de teleportation !")
                + Fore.RESET
            )
            thesee_x, thesee_y = tp6_x, tp6_y
        elif thesee_x == tp6_x and thesee_y == tp6_y:
            print(
                (Fore.YELLOW + "Bravo vous avez trouver un portail de teleportation !")
                + Fore.RESET
            )
            thesee_x, thesee_y = tp5_x, tp5_y

        # -Vérifier si Thésée a atteint la sortie
        if thesee_x == sortie_x and thesee_y == sortie_y and dead_m:
            print(
                (
                    Fore.LIGHTYELLOW_EX
                    + "Bravo, vous avez réussi à sortir du labyrinthe !"
                )
                + Fore.RESET
            )
            print("Votre score final:", score)
            break
        elif thesee_x == sortie_x and thesee_y == sortie_y and not dead_m:
            print(
                (Fore.LIGHTRED_EX + "Vous n'avez pas tué le minautore !") + Fore.RESET
            )

        # score game over
        if score == 0:
            print((Fore.LIGHTRED_EX + "GAME OVER, VOUS ETES MORT DE SOIF") + Fore.RESET)
            break
        print("")

    # -Afficher le labyrinthe
    if jsp:
        for ligne in labyrinthe:
            print(" ".join(ligne))

    # Enregistrement de la partie
    partie = {
        "joueur": joueur,
        "score final du joueur :": score,
    }

    with open("partie_labyrinthe_pickle.txt", "wb") as f:
        pickle.dump(partie, f)

    while jsp:
        choix = input("Voulez-vous relancer la partie ? (O/N) ")
        if choix.upper() == "O":
            break

        elif choix.upper() == "N":
            print("Merci d'avoir joué !")
            banane = True
            break

        else:
            print("Réponse invalide. Veuillez répondre par O ou N.")

    if banane:
        break
