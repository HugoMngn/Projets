# print("Question 1:")
fruits = {"pomme", "banane", "cerise"}
more_fruits = ["orange", "mangue", "raisins"]

fruits.update(more_fruits)
print(fruits)
print("")


# print("Question 2:")
X = {"a", "b", "c", "d"}
Y = {"s", "b", "d"}

print("X =", X, " & Y =", Y)
print("")
print("'c' est dans le set X :", "c" in X)
print("'a' est dans le set Y :", "a" in Y)
print("")
print("X - Y =", X.difference(Y))
print("Y - X =", Y.difference(X))
print("")
print("X ∪ Y =", Y.union(X))
print("X ∩ Y  =", Y.intersection(X))
print("")

# print("Question 3:")
fruits = ("pomme", "banane", "fraise")
vert, jaune, rouge = fruits
print(vert)
print(jaune)
print(rouge)
print("")

# print("Question 4:")
fruits = ("pomme", "banane", "cerise", "fraise", "framboise")
vert, jaune, *rouge = fruits
print(vert)
print(jaune)
print(rouge)
print("")

# print("Question 5:")
fruits = ("pomme", "mangue", "papaye", "ananas", "cerise")
vert, *tropical, rouge = fruits
print(vert)
print(tropical)
print(rouge)
print("")


# print("Question 6:")
entier = (5, 9, 3)
flottant = (0.296, 6.9, 3.46, 64.3, 9.6, 5.87)


def somme(*a):
    return sum(a)


x1 = somme(*entier)
print("Somme entiers:", x1)
x2 = somme(*flottant)
print("Somme flottants:", x2)
print("")


# print("Question 7:")
class ValeurNegativeError(Exception):
    def __init__(self, msg="Erreur: Valeur négative détectée."):
        self.msg = msg
        super().__init__(self.msg)


def verifier_valeur_positive(valeur):
    if valeur < 0:
        raise ValeurNegativeError()
    else:
        print(f"La valeur {valeur} est bien positive.")


try:
    verifier_valeur_positive(5)
    verifier_valeur_positive(-3)
except ValeurNegativeError as e:
    print(e)
print("")


# print("Question 9:")
class MaClasse:
    x = 23
    y = x + 5

    def affiche(self):
        self.z = 42
        print(f"y = {self.y}")
        print(f"z = {self.z}")


test = MaClasse()
test.affiche()
print("")


# print("Question 10:")
class Rectangle:
    def __init__(self, L=2, l=1):
        self.L = L
        self.l = l
        self.nom = "rectangle"

    def affichage(self):
        print(f"{self.nom} , longueur: {self.L}& largeur: {self.l}")

    def surface(self):
        return self.L * self.l


class Carre(Rectangle):
    def __init__(self, c=1):
        super().__init__(L=c, l=c)
        self.nom = "carré"


rectangle = Rectangle(L=8, l=4)
rectangle.affichage()
print("Surface rectangle:", rectangle.surface())

carre = Carre(c=4)
carre.affichage()
print("Surface carré:", carre.surface())
print("")


# print("Question 11:")
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, orig_x, orig_y, extrem_x, extrem_y):
        self.orig = Point(orig_x, orig_y)
        self.extrem = Point(extrem_x, extrem_y)

    def affichage(self):
        print(f"Origine: ({self.orig.x}, {self.orig.y})")
        print(f"Extrémité: ({self.extrem.x}, {self.extrem.y})")


segment_test = Segment(1, 2, 3, 4)
segment_test.affichage()
print("")


# print("Question 12:")
def amende(nb_victimes):
    points_init = 100
    cout_permis = 200

    valeur_poule = 1
    valeur_chien = 3
    valeur_vache = 5
    valeur_amis = 10

    total_pertes = (
        nb_victimes["poule"] * valeur_poule
        + nb_victimes["chien"] * valeur_chien
        + nb_victimes["vache"] * valeur_vache
        + nb_victimes["ami"] * valeur_amis
    )

    solde = points_init - total_pertes

    total = cout_permis + total_pertes
    amendes = total_pertes

    return solde, total, amendes


nb_victimes = {
    "poule": int(input("Nb de poules tuées: ")),
    "chien": int(input("Nb de chiens tués: ")),
    "vache": int(input("Nb de vaches tuées: ")),
    "ami": int(input("Nb d'amis sauvagement assassinés: ")),
}

solde, total, amendes = amende(nb_victimes)

print("")
if solde > 0:
    print(f"Point restants: {solde} point(s).")
    print(f"Somme du: {total} euros (amende: {amendes}€).")
else:
    print("Le chasseur a perdu son permis de chasse.")
    print(f"Somme du: {total} euros (amende: {amendes}€).")
