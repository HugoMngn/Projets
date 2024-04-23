import math


class figure_geo:
    def perimetre(self):
        raise NotImplementedError("à spécialiser")

    def surface(self):
        raise NotImplementedError("à spécialiser")


class rectangle(figure_geo):
    def __init__(self, longueur: float, largeur: float):
        self.L = longueur
        self.l = largeur

    def perimetre(self):
        return round(2 * (self.L + self.l), 2)

    def surface(self):
        return round(self.L * self.l, 2)

    def is_carre(self):
        v = False
        if self.l == self.L:
            v = True
        return v


class carre(rectangle):
    def __init__(self, cote: float):
        self.L = cote
        self.l = cote


class cercle(figure_geo):
    def __init__(self, rayon: float):
        self.r = rayon
        self.pi = math.pi

    def perimetre(self):
        return round(2 * self.pi * self.r, 2)

    def surface(self):
        return round(self.pi * (self.r**2), 2)


r = rectangle(5, 5)
print(r.surface())
print("C'est un carré:", r.is_carre())
