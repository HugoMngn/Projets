import random
import time

nom_poke = ["Carapuce", "Salamèche", "Bulbizare", "Pikachu", "Ratata", "Roucoul"]
pv_poke = [
    random.randint(45, 60),
    random.randint(45, 60),
    random.randint(45, 60),
    random.randint(45, 60),
    random.randint(45, 60),
    random.randint(45, 60),
]

attaque_Salamèche = ["Flammèche", "Machouille", "déflagration", "roue de feu"]
degat_Salamèche = [
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
]

attaque_Carapuce = ["Pistolet à eau", "Groz'yeux", "vibraqua", "hydrocanon"]
degat_Carapuce = [
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
]

attaque_Bulbizare = ["Fouet liane", "Vampi'graine", "Mégafouet", "Giga-sangsue"]
degat_Bulbizare = [
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
]

attaque_Pikachu = ["Eclair", "Encore", "tonerre", "fatal foudre"]
degat_Pikachu = [
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
]

attaque_Ratata = ["Charge", "Mimi-queue", "Ecrasement", "Vive attaque"]
degat_Ratata = [
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
]

attaque_Roucoul = ["Cru-aile", "Jet de fumée", "tornade", "Regard doux"]
degat_Roucoul = [
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
    random.randint(5, 15),
]

choix_poke = [
    attaque_Carapuce,
    attaque_Salamèche,
    attaque_Bulbizare,
    attaque_Pikachu,
    attaque_Ratata,
    attaque_Roucoul,
]
choix_attack = [
    degat_Carapuce,
    degat_Salamèche,
    degat_Bulbizare,
    degat_Pikachu,
    degat_Ratata,
    degat_Roucoul,
]


def attack(n, v, m):
    print()
    print("Quelle attaque doit effectuer " + nom_poke[int(n)] + "? ")
    for i in range(0, 4):
        print(i + 1, ")-", choix_poke[int(n)][i])
    print()
    attaque_ref = 5
    while not (attaque_ref > -1 and attaque_ref < 4):
        attaque_ref = int(input("")) - 1
        print()
        if attaque_ref <= -1:
            print("Pas une attaque")
            print()
            print("Quelle attaque doit effectuer " + nom_poke[int(n)] + "? ")
            print()
        elif attaque_ref > 4:
            print("Pas une attaque")
            print()
            print("Quelle attaque doit effectuer " + nom_poke[int(n)] + "? ")
            print()
    print()
    degat = choix_attack[int(n)][attaque_ref]
    v = max(v - degat, 0)

    fight = (
        nom_poke[int(n)]
        + " utilise "
        + choix_poke[int(n)][attaque_ref]
        + " qui inflige "
        + str(degat)
        + " PV"
    )
    resultat = nom_poke[int(m)] + " a maintenant " + str(v) + " PV"
    max_taille = max(len(fight), len(resultat))
    fight += " " * (max_taille - len(fight))
    resultat += " " * (max_taille - len(resultat))
    print("+" * (max_taille + 4))
    print("+", fight, "+")
    print("+", resultat, "+")
    print("+" * (max_taille + 4))
    print()
    return v


def attackIA(n, v, m):
    attaque_ref = random.randint(0, 3)
    degat = choix_attack[int(n)][attaque_ref]
    v = max(v - degat, 0)

    fight = (
        nom_poke[int(n)]
        + " utilise "
        + choix_poke[int(n)][attaque_ref]
        + " qui inflige "
        + str(degat)
        + " PV"
    )
    resultat = nom_poke[int(m)] + " a maintenant " + str(v) + " PV"
    max_taille = max(len(fight), len(resultat))
    fight += " " * (max_taille - len(fight))
    resultat += " " * (max_taille - len(resultat))
    print("+" * (max_taille + 4))
    print("+", fight, "+")
    print("+", resultat, "+")
    print("+" * (max_taille + 4))
    print()
    return v


def fin_combat(n, m, v):
    end1 = nom_poke[int(n)] + " a été mis KO "
    print("+" * (len(end1) + 4))
    print("+", end1, "+")
    print("+" * (len(end1) + 4))
    print()

    msg_fin = "résultat du combat : "
    fin2 = nom_poke[int(m)] + " a gagner ce combat"
    fin1 = nom_poke[int(m)] + " a fini avec " + str(v) + " HP"
    max_fin = max(len(fin2), len(msg_fin))
    msg_fin += " " * (max_fin - len(msg_fin))
    fin2 += " " * (max_fin - len(fin2))
    fin1 += " " * (max_fin - len(fin1))
    print("+" * (max_fin + 4))
    print("+", msg_fin, "+")
    print("+", fin2, "+")
    print("+", fin1, "+")
    print("+" * (max_fin + 4))
    print()


def wait(steps, step_duration=0.1):
    print("[", end="", flush=True)
    for _ in range(steps):
        print(">", end="", flush=True)
        time.sleep(step_duration)
        print("\b#", end="", flush=True)
    print("]")
    print()


combat = ["PvP", "PvE"]
print("Que voulez-vous faire? ")
for i in range(0, 2):
    print(i + 1, ")-", combat[i])
choix_combat = int(input("")) - 1.0
print()
print(combat[int(choix_combat)], " à été sélectionné.")

if choix_combat == 0:
    print("J1, Choisissez votre pokemon parmi la liste suivante: ")
    for i in range(0, 6, 1):
        print(i + 1, ")-", nom_poke[i])
    pokemon1 = int(input("")) - 1.0
    print()
    print(nom_poke[int(pokemon1)], " à été sélectionné.")
    PV1 = pv_poke[int(pokemon1)]

    print("J2, Choisissez votre pokemon parmi la liste suivante: ")
    for i in range(0, 6, 1):
        print(i + 1, ")-", nom_poke[i])
    pokemon2 = int(input("")) - 1
    print()
    print(nom_poke[int(pokemon2)], " à été sélectionné.")
    PV2 = pv_poke[int(pokemon2)]
    print()

    start = (
        nom_poke[int(pokemon1)]
        + " ("
        + str(PV1)
        + " PV) affronte "
        + nom_poke[int(pokemon2)]
        + " ("
        + str(PV2)
        + " PV)"
    )
    print("+" * (len(start) + 4))
    print("+", start, "+")
    print("+" * (len(start) + 4))
    print()

    ok = input("Confirmez-vous ce duel? [o/n] ").lower()
    while not (ok == "o" or ok == "n"):
        print("t'as un choix parmi 2 possibilités et t'es pas capable de le faire...")
        print()
        ok = input("Confirmez-vous ce duel? [o/n] ").lower()

    if ok == "o":
        while PV2 > 0 and PV1 > 0:
            PV2 = attack(pokemon1, PV2, pokemon2)
            if PV2 <= 0:
                break
            PV1 = attack(pokemon2, PV1, pokemon1)

            endt1 = nom_poke[int(pokemon1)] + " a maintenant " + str(PV1) + " HP"
            endt2 = nom_poke[int(pokemon2)] + " a maintenant " + str(PV2) + " HP"
            msg = "résultat du tour : "
            max_end = max(len(endt1), len(endt2), len(msg))
            print("+" * (max_end + 5))
            print("+", msg, " " * (max_end - (len(msg))), "+")
            print("+", endt1, " " * (max_end - (len(endt1))), "+")
            print("+", endt2, " " * (max_end - (len(endt2))), "+")
            print("+" * (max_end + 5))
            print()

        if PV1 <= 0:
            fin_combat(pokemon1, pokemon2, PV2)

        elif PV2 <= 0:
            fin_combat(pokemon2, pokemon1, PV1)
    elif ok == "n":
        print("Vous avez pris vos jambes à vos cous et avez fui comme un lâche...")
        print()

elif choix_combat == 1:
    print("J1, Choisissez votre pokemon parmi la liste suivante: ")
    for i in range(0, 6, 1):
        print(i + 1, ")-", nom_poke[i])
    pokemon1 = int(input("")) - 1.0
    print()
    print(nom_poke[int(pokemon1)], " à été sélectionné.")
    PV1 = pv_poke[int(pokemon1)]

    pokemon2 = random.randint(0, 5)
    print()
    print(nom_poke[int(pokemon2)], " à été sélectionné par l'IA.")
    PV2 = pv_poke[int(pokemon2)]
    print()

    start = (
        nom_poke[int(pokemon1)]
        + " ("
        + str(PV1)
        + " PV) affronte "
        + nom_poke[int(pokemon2)]
        + " ("
        + str(PV2)
        + " PV)"
    )
    print("+" * (len(start) + 4))
    print("+", start, "+")
    print("+" * (len(start) + 4))
    print()

    ok = input("Confirmez-vous ce duel? [o/n] ").lower()
    while not (ok == "o" or ok == "n"):
        print("t'as un choix parmi 2 possibilités et t'es pas foutu de le faire...")
        print()
        ok = input("Confirmez-vous ce duel? [o/n] ").lower()

    if ok == "o":
        while PV2 > 0 and PV1 > 0:
            PV2 = attack(pokemon1, PV2, pokemon2)
            if PV2 <= 0:
                break
            wait(10)
            PV1 = attackIA(pokemon2, PV1, pokemon1)
            time.sleep(5)

            endt1 = nom_poke[int(pokemon1)] + " a maintenant " + str(PV1) + " PV"
            endt2 = nom_poke[int(pokemon2)] + " a maintenant " + str(PV2) + " PV"
            msg = "résultat du tour : "
            max_end = max(len(endt1), len(endt2), len(msg))
            print("+" * (max_end + 5))
            print("+", msg, " " * (max_end - (len(msg))), "+")
            print("+", endt1, " " * (max_end - (len(endt1))), "+")
            print("+", endt2, " " * (max_end - (len(endt2))), "+")
            print("+" * (max_end + 5))
            print()

        if PV1 <= 0:
            fin_combat(pokemon1, pokemon2, PV2)

        elif PV2 <= 0:
            fin_combat(pokemon2, pokemon1, PV1)
    elif ok == "n":
        print("Vous avez pris vos jambes à vos cous et avez fui comme un lâche...")
        print()
