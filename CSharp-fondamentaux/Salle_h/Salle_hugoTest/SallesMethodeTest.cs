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
    public class SallesMethodeTests
    {
        [Test]
        public void CreerSalle_WithValidInput_CreatesSalle()
        {
            // Arrange
            var mockSaisieU = new Mock<ISaisie>();
            mockSaisieU.SetupSequence(m => m.DemandeString(It.IsAny<string>()))
                       .Returns("Philadélie")  // Nom de la salle
                       .Returns("3B2");         // Code de la salle
            mockSaisieU.Setup(m => m.DemandeInt("Le nombre de place de Philadélie : "))
                       .Returns(290);          // Nombre de places

            var sallesService = new SallesServices();
            sallesService.SaisieU = mockSaisieU.Object;

            // Act
            var salle = sallesService.CreerSalle();

            // Assert
            Assert.AreEqual("Philadélie", salle.Nom);
            Assert.AreEqual("3B2", salle.Code);
            Assert.AreEqual(290, salle.Nbplaces);
        }


        [Test]
        public void AfficherSallesTest()
        {
            SallesServices SalService = new SallesServices();
            SalService.SaisieU = new SaisieMockCreaSalle();
            Salles s = new Salles { Nom = "Philadélie", Code = "3B2", Nbplaces = 290 };
            Assert.AreEqual("Philadélie", s.Nom);
            Assert.AreEqual("3B2", s.Code);
            Assert.AreEqual(290, s.Nbplaces);
        }
    }
    public class SaisieMockCreaSalle : SaisieUser
    {
        public override int DemandeInt(string message)
        {
            return 290;
        }
        public override string DemandeString(string message)
        {
            if (message == "Le nom de la salle : ") { return "Philadélie"; }
            else if (message == "Le code de Philadélie : ") { return "392"; }
            return string.Empty;
        }

    }
    public interface ISaisie
    {
        string DemandeString(string message);
        int DemandeInt(string message);
    }


}