using Salle_Hugo.Models;
using Salle_Hugo.Services;
using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Salle_hugoTest
{
    public class BatimentMethodeTests
    {

        [Test]
        public void CreerBatTest()
        {
            BatimentServices BatServices = new BatimentServices();
            BatServices.SaisieU = new SaisieMock();
            var b = BatServices.CreerBat();
            Assert.AreEqual("Les aur�lias", b.Nom);
            Assert.AreEqual("AAAAA", b.Code);
            Assert.AreEqual("19 rue des loriet", b.Adresse);
            Assert.AreEqual("Cecilie", b.Ville);
            Assert.AreEqual("09229", b.CodePostal);
        }

        [Test]
        public void AfficherBatTest()
        {
            BatimentServices BatServices = new BatimentServices();
            BatServices.SaisieU = new SaisieMock();
            var b = BatServices.CreerBat();
            Assert.AreEqual("Les aur�lias", b.Nom);
            Assert.AreEqual("AAAAA", b.Code);
            Assert.AreEqual("19 rue des loriet", b.Adresse);
            Assert.AreEqual("Cecilie", b.Ville);
            Assert.AreEqual("09229", b.CodePostal);
        }


    }
    public class SaisieMock : SaisieUser
    {
        public override int DemandeInt(string message)
        {
            return 1;
        }
        public override string DemandeString(string message)
        {
            if (message == "Le nom du batiment : ") { return "Les aur�lias"; }
            else if (message == "Le code de Les aur�lias : ") { return "AAAAA"; }
            else if (message == "L'adresse de Les aur�lias : ") { return "19 rue des loriet"; }
            else if (message == "La ville de Les aur�lias : ") { return "Cecilie"; }
            else if (message == "Le code postal de Les aur�lias : ") { return "09229"; }
            return string.Empty;
        }

    }
    public class SaisieMockPrint : SaisieUser
    {
        public override int DemandeInt(string message)
        {
            return 1;
        }
        public override string DemandeString(string message)
        {
            if (message == "Le nom du batiment : ") { return "Les aur�lias"; }
            else if (message == "Le code de Les aur�lias : ") { return "AAAAA"; }
            else if (message == "L'adresse de Les aur�lias : ") { return "19 rue des loriet"; }
            else if (message == "La ville de Les aur�lias : ") { return "Cecilie"; }
            else if (message == "Le code postal de Les aur�lias : ") { return "09229"; }
            return string.Empty;
        }

    }

}