using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Salle_Hugo.Models;

namespace Salle_Hugo.Services
{
    public class BatimentServices
    {
        public SaisieUser SaisieU = new SaisieUser();
        public InteractUser InteractU = new InteractUser();
        public List<Batiment> lesBats = new List<Batiment>();

        public Batiment CreerBat()
        {
            Batiment batiment = new Batiment();
            batiment.Nom = SaisieU.DemandeString("Le nom du batiment : ");
            batiment.Code = SaisieU.DemandeString($"Le code de {batiment.Nom} : ");
            batiment.Adresse = SaisieU.DemandeString($"L'adresse de {batiment.Nom} : ");
            batiment.Ville = SaisieU.DemandeString($"La ville de {batiment.Nom} : ");
            while (true)
            {
                string codePostal = SaisieU.DemandeString($"Le code postal de {batiment.Nom} : ");

                if (codePostal.Length == 5)
                {
                    if (int.TryParse(codePostal, out int codePostalInt) && codePostalInt >= 1000 && codePostalInt <= 98890)
                    {
                        batiment.CodePostal = codePostal;
                        break;
                    }
                    else
                    {
                        InteractU.AfficherMessages("Le code postal est censé être entre 01000 et 98890 en France (en tout cas en 2024) pour rappel...");
                    }
                }
                else
                {
                    InteractU.AfficherMessages("Le code postal est composé de 5 chiffres de base...");
                }
            }
            lesBats.Add(batiment);
            return batiment;
        }

        public void AfficherBat(Batiment batiment)
        {
            InteractU.AfficherMessages($"Nom : {batiment.Nom}");
            InteractU.AfficherMessages($"Code : {batiment.Code}");
            InteractU.AfficherMessages($"Adresse : {batiment.Adresse}");
            InteractU.AfficherMessages($"Code postal : {batiment.CodePostal}");
            InteractU.AfficherMessages($"Ville : {batiment.Ville}");
            InteractU.AfficherMessages(" ");
        }
         public void Afficher1Bat ()
        {
            InteractU.AfficherMessages("Liste des bâtiments existants : ");
            foreach (var b in lesBats)
            {
                InteractU.AfficherMessages($"- {b.Nom}");
            }
            string nomBatiment = SaisieU.DemandeString("Entrez le nom du bâtiment existant : ");
            Batiment batiment = lesBats.FirstOrDefault(b => b.Nom == nomBatiment);
            if (batiment != null)
            {
                InteractU.AfficherMessages(" ");
                InteractU.AfficherMessages("Détails du bâtiment sélectionné :");
                InteractU.AfficherMessages($"Nom : {batiment.Nom}");
                InteractU.AfficherMessages($"Code : {batiment.Code}");
                InteractU.AfficherMessages  ($"Adresse : {batiment.Adresse}");
                InteractU.AfficherMessages($"Code Postal : {batiment.CodePostal}");
                InteractU.AfficherMessages($"Ville : {batiment.Ville}");
            }
            else
            {
                InteractU.AfficherMessages("Le bâtiment sélectionné n'existe pas.");
            }
        }
        public void AfficherLesBats()
        {
            foreach (Batiment batiment in lesBats)
            {
                AfficherBat(batiment);
            }
        }

        public string RechercheBat()
        {
            InteractU.AfficherMessages("Liste des bâtiments existants : ");
            foreach (var b in lesBats)
            {
                InteractU.AfficherMessages($"- {b.Nom}");
            }

            string nomBatiment;
            do
            {
                nomBatiment = SaisieU.DemandeString("Entrez le nom du bâtiment existant : ");
            } while (!EstNomBatimentValide(nomBatiment));

            return nomBatiment;
        }

        private bool EstNomBatimentValide(string nom)
        {
            foreach (var b in lesBats)
            {
                if (b.Nom.Equals(nom))
                {
                    return true;
                }
            }
            return false;
        }
    }
}
