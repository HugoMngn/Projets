using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Salle_Hugo.Models;

namespace Salle_Hugo.Services
{
    public class SallesServices
    {
        public SaisieUser SaisieU = new SaisieUser();
        public InteractUser InteractU = new InteractUser();
        public BatimentServices BatServices = new BatimentServices();
        public List<Salles> lesSalles = new List<Salles>();

        public Salles CreerSalle()
        {
            Salles salles = new Salles();
            salles.Nom = SaisieU.DemandeString("Le nom de la salle : ");
            salles.Nbplaces = SaisieU.DemandeInt($"Le nombre de place de {salles.Nom} : ");
            while (true)
            {
                string code = SaisieU.DemandeString($"Le code de {salles.Nom} : ");

                if (code.Length == 3)
                {
                    salles.Code = code;
                    break;
                }
                else
                {
                    InteractU.AfficherMessages("Le code est composé de 3 caractères...");
                }
            }


            string nomBatiment = BatServices.RechercheBat();
            salles.Batiment = BatServices.lesBats.FirstOrDefault(b => b.Nom == nomBatiment);

            lesSalles.Add(salles);
            return salles;
        }

        public void AfficherSalles(Salles salles)
        {
            InteractU.AfficherMessages($"Nom : {salles.Nom}");
            InteractU.AfficherMessages($"Code : {salles.Code}");
            InteractU.AfficherMessages($"Nombre de place : {salles.Nbplaces}");
            InteractU.AfficherMessages($"Batiment : {salles.Batiment.Nom}");
            InteractU.AfficherMessages(" ");
        }
        public void Afficher1Salle()
        {
            InteractU.AfficherMessages("Liste des salles existantes : ");
            foreach (var salle in lesSalles)
            {
                InteractU.AfficherMessages($"- {salle.Nom}");
            }
            string nomSal = SaisieU.DemandeString("Entrez le nom de la salle : ");
            Salles salles = lesSalles.FirstOrDefault(b => b.Nom == nomSal);
            if (salles != null)
            {
                InteractU.AfficherMessages(" ");
                InteractU.AfficherMessages($"Nom : {salles.Nom}");
                InteractU.AfficherMessages($"Code : {salles.Code}");
                InteractU.AfficherMessages($"Nombre de place : {salles.Nbplaces}");
                InteractU.AfficherMessages($"Batiment : {salles.Batiment.Nom}");
            }
            else
            {
                Console.WriteLine("La salle sélectionnée n'existe pas.");
            }
        }
        public void AfficherLesSalles()
        {
            foreach (Salles salles in lesSalles)
            {
                AfficherSalles(salles);
            }
        }

        public void TotalPlacesGlobal()
        {
            int totalPlaces = 0;
            foreach (var salle in lesSalles)
            {
                totalPlaces += salle.Nbplaces;
            }
            InteractU.AfficherMessages($"Le nombre de place total est de {totalPlaces}");
        }

        public void PlaceParBat()
        {
            Dictionary<string, int> totalPlacesParBatiment = new Dictionary<string, int>();

            foreach (var salle in lesSalles)
            {
                string nomBatiment = salle.Batiment.Nom;
                if (!totalPlacesParBatiment.ContainsKey(nomBatiment))
                {
                    totalPlacesParBatiment[nomBatiment] = 0;
                }
                totalPlacesParBatiment[nomBatiment] += salle.Nbplaces;
            }

            foreach (var kvp in totalPlacesParBatiment)
            {
                string nomBatiment = kvp.Key;
                int totalPlaces = kvp.Value;

                Batiment batiment = BatServices.lesBats.FirstOrDefault(b => b.Nom == nomBatiment);

                if (batiment != null)
                {
                    InteractU.AfficherMessages($"Bâtiment : {batiment.Nom}");
                    InteractU.AfficherMessages($"Code postal : {batiment.CodePostal}");
                    InteractU.AfficherMessages($"Total des places : {totalPlaces}");
                    InteractU.AfficherMessages(" ");
                }
            }
        }
    }
}
