class Client:
    def __init__(self, nom: str, prenom: str, numero_de_carte_vitale: int):
        self.nom = nom
        self.prenom = prenom
        self.carte_vitale = numero_de_carte_vitale

    def __str__(self):
        return f"{self.prenom} {self.nom} (numéro de carte vitale: {self.carte_vitale})"


class Produit:
    def __init__(self, reference: str, prix: float, quantite: int):
        self.reference = reference
        self.prix = prix
        self.quantite = quantite

    def __str__(self):
        return f"référence: {self.reference} (prix: {self.prix} €, quantité en stock: {self.quantite})"


class Medicament(Produit):
    def __init__(
        self,
        reference: str,
        prix: float,
        quantite: int,
        generique: bool,
        ordonnance: bool,
    ):
        super().__init__(reference, prix, quantite)
        self.generique = generique
        self.ordonnance = ordonnance

    def __str__(self):
        if self.ordonnance and self.generique:
            return super().__str__() + f", générique: oui, délivré sans ordonnance: oui"
        elif self.ordonnance and not self.generique:
            return super().__str__() + f", générique: non, délivré sans ordonnance: oui"
        elif self.generique and not self.ordonnance:
            return super().__str__() + f", générique: oui, délivré sans ordonnance: non"
        else:
            return super().__str__() + f", générique: non, délivré sans ordonnance: non"


class Parapharmacie(Produit):
    def __init__(
        self,
        reference: str,
        prix: float,
        quantite: int,
        type_produit: str,
    ):
        if (
            type_produit == "produit de beauté"
            or type_produit == "diététique"
            or type_produit == "cosmétique"
        ):
            super().__init__(reference, prix, quantite)
            self.type_produit = type_produit
        else:
            print("pas le bon type de produit")
            pass

    def __str__(self):
        return super().__str__() + f", type: {self.type_produit}"


class Pharmacie:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.clients = []
        self.produits = []

    def ajouter_client(self, client: Client):
        self.clients.append(client)

    def ajouter_produit(self, produit: Produit):
        self.produits.append(produit)

    def achat(self, produit: Produit, client: Client, quantite: int):
        if produit.quantite >= quantite:
            produit.quantite -= quantite
            print(f"{quantite} x {produit} acheté(s) par {client}")
        else:
            print(f"Impossible d'acheter {quantite} x {produit}. Stock insuffisant.")

    def approvisionnement(self, produit: Produit, quantite: int):
        produit.quantite += quantite
        print(f"Approvisionnement de {quantite} x {produit}")

    def afficher_clients(self):
        print("Liste des clients de la pharmacie:")
        for client in self.clients:
            print(client)

    def afficher_produits(self):
        print("Liste des produits de la pharmacie:")
        for produit in self.produits:
            print(produit)


Belle_etoile = Pharmacie("Belle_etoile", "18 avenue de Belledone")

Michel = Client("Dutron", "Michel", 123456789101213)
Jacquie = Client("De Montazac", "Jacquie", 263741938204726)

Suppositoire = Medicament("Suppositoire", 69.69, 69, True, False)
Mascara = Parapharmacie("Mascara", 99.99, 3, "produit de beauté")

Belle_etoile.ajouter_client(Michel)
Belle_etoile.ajouter_client(Jacquie)
print("")
Belle_etoile.ajouter_produit(Suppositoire)
Belle_etoile.ajouter_produit(Mascara)
print("")
Belle_etoile.afficher_clients()
print("")
Belle_etoile.afficher_produits()
print("")
print(Mascara)
print(Suppositoire)
print(Michel)
print(Jacquie)
print("")
Belle_etoile.achat(Mascara, Jacquie, 7)
Belle_etoile.achat(Suppositoire, Michel, 7)
print("")
print(Mascara)
print(Suppositoire)
print("")
Belle_etoile.achat(Suppositoire, Jacquie, 109)
print(Mascara)
print(Suppositoire)
print("")
Belle_etoile.approvisionnement(Suppositoire, 29)
print("")
print(Mascara)
print(Suppositoire)
