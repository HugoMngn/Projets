using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Console_exo1Tests
{
    public class MesFonctionsTests
    {
        public static string CreermessageTests(string prenom, string age, string sexe)
        {
            if (age == "0")
            {
                return ("Bonjour " + prenom + ", tu es un tout jeune microbe de type: " + sexe +".");
            }
            else if (age == "1")
            {
                return ("Bonjour " + prenom + ", tu as " + age + " an et est de type: " + sexe +".");
            }
            else
            {
                return ("Bonjour " + prenom + ", tu as " + age + " ans. Et tu es GAY!");
            };
        }
    }
}
