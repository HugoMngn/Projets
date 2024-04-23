using Salle_Hugo.Models;
using Salle_Hugo.Services;
using System;
using System.Runtime.Serialization;


SaisieUser SaisieU = new SaisieUser();
InteractUser InteractU = new InteractUser();
BatimentServices BServices = new BatimentServices();
SallesServices Sservices = new SallesServices();
Sservices.BatServices = BServices;

while (true)
{
    int entreeMenu = SaisieU.DemandeInt(@"Que voulez vous faire ?
    1. Créer un batiment 
    2. Afficher tous les batiments
    3.Afficher un batiment

    4.Créer Salle
    5.Afficher les Salles
    6.Afficher une salle

    7.Compter toutes les places
    8.Compter les places par batiments

    10. Quitter");
    if (entreeMenu == 1)
    {
        Batiment b = BServices.CreerBat();
    }
    else if (entreeMenu == 2)
    {
        BServices.AfficherLesBats();
    }
    else if (entreeMenu == 3)
    {
        BServices.Afficher1Bat();
    }
    else if (entreeMenu == 4)
    {
        Salles s = Sservices.CreerSalle();
    }
    else if (entreeMenu == 5)
    {
        Sservices.AfficherLesSalles();
    }
    else if (entreeMenu == 6)
    {
        Sservices.Afficher1Salle();
    }
    else if (entreeMenu == 7)
    {
        Sservices.TotalPlacesGlobal();
    }
    else if (entreeMenu == 8)
    {
        Sservices.PlaceParBat();
    }
    else if (entreeMenu == 10)
    {
        break;
    }
    else
    {
        InteractU.AfficherMessages("entrée invalide");
    }

    InteractU.AttendrePourQuitter();
}