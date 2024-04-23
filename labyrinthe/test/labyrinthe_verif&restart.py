# -Librairies
import random
import keyboard
from colorama import init, Fore, Style
import numpy as np

# Initialise la bibliothèque colorama
init()
banane = False
while True:
    # -Dimensions du labyrinthe
    hauteur = 16
    largeur = 22

    # -Créer une matrice de cases
    labyrinthe = [
        [f"\x1b[8m{chr(9608)}\x1b[0m" for x in range(largeur)] for y in range(hauteur)
    ]

    # -Ajouter des murs autour du labyrinthe
    for x in range(largeur):
        labyrinthe[0][x] = Fore.BLUE + "□" + Fore.RESET
        labyrinthe[hauteur - 1][x] = Fore.BLUE + "□" + Fore.RESET
    for y in range(hauteur):
        labyrinthe[y][0] = Fore.BLUE + "□" + Fore.RESET
        labyrinthe[y][largeur - 1] = Fore.BLUE + "□" + Fore.RESET

    dead_m = False

    # -Position monstre aléatoire
    rng = np.random.default_rng()
    monstre_x, monstre_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    labyrinthe[monstre_y][monstre_x] = Fore.MAGENTA + "M" + Fore.RESET

    # -TP aléatoire
    rng = np.random.default_rng()
    tp_x, tp_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    labyrinthe[tp_y][tp_x] = Fore.CYAN + "O" + Fore.RESET

    tp_y, tp_x != monstre_y, monstre_x

    tp2_x, tp2_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    labyrinthe[tp2_y][tp2_x] = Fore.CYAN + "o" + Fore.RESET

    tp2_y, tp2_x != monstre_y, monstre_x and tp2_y, tp2_x != tp_x, tp_y

    tp3_x, tp3_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    labyrinthe[tp3_y][tp3_x] = Fore.CYAN + "O" + Fore.RESET

    tp3_y, tp3_x != monstre_y, monstre_x

    tp4_x, tp4_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    labyrinthe[tp4_y][tp4_x] = Fore.CYAN + "o" + Fore.RESET

    tp4_y, tp4_x != monstre_y, monstre_x and tp4_y, tp4_x != tp3_x, tp3_y

    tp5_x, tp5_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    labyrinthe[tp5_y][tp5_x] = Fore.CYAN + "O" + Fore.RESET

    tp5_y, tp5_x != monstre_y, monstre_x

    tp6_x, tp6_y = random.choice(
        [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
        + [(largeur - 2, y) for y in range(1, hauteur - 2)]
        + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
        + [(x, hauteur - 2) for x in range(1, largeur - 2)]
    )
    labyrinthe[tp6_y][tp6_x] = Fore.CYAN + "o" + Fore.RESET

    tp6_y, tp6_x != monstre_y, monstre_x and tp6_y, tp6_x != tp5_x, tp5_y
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

    # -Ajouter des "#" supplémentaires
    nb_murs = 95
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

    score = ((((hauteur * largeur) - (2 * largeur)) - (2 * hauteur)) + 4) - nb_murs + 10

    # verifier faisabilité
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

    def is_finishable(
        labyrinthe, entree_y, entree_x, sortie_y, sortie_x, monstre_y, monstre_x
    ):
        verif = {(entree_y, entree_x)}
        verif2 = {(0, 0)}
        trouve_monstre = False
        trouve_sortie = False

        while verif and not (trouve_monstre and trouve_sortie):
            # choisir la prochaine case à tester
            a, b = verif.pop()

            # tester les cases voisines
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

        # Vérifier si le Minotaure et la sortie sont atteignables
        if is_accessible(
            labyrinthe, sortie_y, sortie_x, monstre_y, monstre_x
        ) and is_accessible(labyrinthe, entree_y, entree_x, sortie_y, sortie_x):
            return True
        else:
            return False

    jsp = True
    is_finishable(
        labyrinthe, entree_y, entree_x, sortie_y, sortie_x, monstre_y, monstre_x
    )
    if not is_finishable(
        labyrinthe, entree_y, entree_x, sortie_y, sortie_x, monstre_y, monstre_x
    ):
        print("labyrinthe impossible")
        jsp = False
    else:
        print("labyrinthe finissable")

    # -Faire avancer Thésée dans le labyrinthe
    while True:
        labyrinthe[thesee_y][thesee_x] = Fore.GREEN + "T" + Fore.RESET
        labyrinthe[monstre_y][monstre_x] = Fore.MAGENTA + "M" + Fore.RESET
        if not jsp:
            break
        # -Afficher le labyrinthe avec la position de Thésée
        for y in range(hauteur):
            for x in range(largeur):
                print(labyrinthe[y][x], end=" ")
            print()

        # -Demander à l'utilisateur de choisir une direction
        print("score:", score)
        direction = input("Choisissez une direction (Z/S/Q/D) : ")
        score -= 1
        print("")
        print("")

        # -Ajouter la trace derrière Thésée
        if direction == "Q" and labyrinthe != "#":
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "←" + Fore.RESET
        elif direction == "D" and labyrinthe != "#":
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "→" + Fore.RESET
        elif direction == "Z" and labyrinthe != "#":
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "↑" + Fore.RESET
        elif direction == "S" and labyrinthe != "#":
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "↓" + Fore.RESET

        if direction == "q" and labyrinthe != "#":
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "←" + Fore.RESET
        elif direction == "d" and labyrinthe != "#":
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "→" + Fore.RESET
        elif direction == "z" and labyrinthe != "#":
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "↑" + Fore.RESET
        elif direction == "s" and labyrinthe != "#":
            labyrinthe[thesee_y][thesee_x] = Fore.RED + "↓" + Fore.RESET

        # -Déplacer Thésée dans la direction choisie
        if direction == "Z" and labyrinthe[thesee_y - 1][thesee_x] != "#":
            thesee_y -= 1
        elif direction == "S" and labyrinthe[thesee_y + 1][thesee_x] != "#":
            thesee_y += 1
        elif direction == "Q" and labyrinthe[thesee_y][thesee_x - 1] != "#":
            thesee_x -= 1
        elif direction == "D" and labyrinthe[thesee_y][thesee_x + 1] != "#":
            thesee_x += 1
        elif direction == "":
            print((Fore.RED + "Veuillez selectioner une direction") + Fore.RESET)
        else:
            print((Fore.RED + "Vous ne pouvez pas passer le mur") + Fore.RESET)

        if direction == "z" and labyrinthe[thesee_y - 1][thesee_x] != "#":
            thesee_y -= 1
        elif direction == "s" and labyrinthe[thesee_y + 1][thesee_x] != "#":
            thesee_y += 1
        elif direction == "q" and labyrinthe[thesee_y][thesee_x - 1] != "#":
            thesee_x -= 1
        elif direction == "d" and labyrinthe[thesee_y][thesee_x + 1] != "#":
            thesee_x += 1
        elif direction == "":
            print((Fore.RED + "Veuillez selectioner une direction") + Fore.RESET)
        else:
            print((Fore.RED + "Vous ne pouvez pas passer le mur") + Fore.RESET)

        # -Vérifier si Thésée a atteint le minautore
        if thesee_x == monstre_x and thesee_y == monstre_y:
            print(
                (Fore.YELLOW + "Bravo, vous avez atteint le minautore !") + Fore.RESET
            )
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
                if minotaure_dir == 0 and (
                    labyrinthe[monstre_y - 1][monstre_x] != "□"
                    or labyrinthe[monstre_y - 1][monstre_x] != "#"
                ):
                    if (monstre_y - 1) >= 0 and (monstre_y - 1 < largeur):
                        monstre_y -= 1
                    else:
                        continue
                elif minotaure_dir == 1 and (
                    labyrinthe[monstre_y + 1][monstre_x] != "□"
                    or labyrinthe[monstre_y + 1][monstre_x] != "#"
                ):
                    if (monstre_y + 1) >= 0 and (monstre_y + 1 < largeur):
                        monstre_y += 1
                    else:
                        continue
                elif minotaure_dir == 2 and (
                    labyrinthe[monstre_y][monstre_x - 1] != "□"
                    or labyrinthe[monstre_y][monstre_x - 1] != "#"
                ):
                    if (monstre_x - 1) >= 0 and (monstre_x - 1 < largeur):
                        monstre_x -= 1
                    else:
                        continue
                elif minotaure_dir == 3 and (
                    labyrinthe[monstre_y][monstre_x + 1] != "□"
                    or labyrinthe[monstre_y][monstre_x + 1] != "#"
                ):
                    if (monstre_x + 1) >= 0 and (monstre_x + 1 < largeur):
                        monstre_x += 1
                    else:
                        continue

        labyrinthe[entree_y][entree_x] = Fore.YELLOW + "E" + Fore.RESET
        labyrinthe[sortie_y][sortie_x] = Fore.YELLOW + "S" + Fore.RESET
        # -Vérifier si Thésée a atteint la sortie
        if thesee_x == sortie_x and thesee_y == sortie_y and dead_m:
            print(
                (Fore.YELLOW + "Bravo, vous avez réussi à sortir du labyrinthe !")
                + Fore.RESET
            )
            print("Votre score final:", score)
            break
        elif thesee_x == sortie_x and thesee_y == sortie_y and not dead_m:
            print((Fore.RED + "Vous n'avez pas tué le minautore !") + Fore.RESET)

        # score game over
        if score == 0:
            print("Game over, vous êtes mort de soif")
            break

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

    # -Afficher le labyrinthe
    if jsp:
        for ligne in labyrinthe:
            print(" ".join(ligne))

    while True:
        choix = input("Voulez-vous relancer la partie ? (O/N) ")
        if choix.upper() == "O":
            break

        elif choix.upper() == "N":
            print("Merci d'avoir joué !")
            banane = True
            break

        else:
            print("Réponse invalide. Veuillez répondre par O ou N.")

    if banane == True:
        break
