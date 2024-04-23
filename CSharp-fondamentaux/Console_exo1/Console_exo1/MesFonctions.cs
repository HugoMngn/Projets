using ANSIConsole;
using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.Json.Serialization;

namespace Console_exo1
{
    public class MesFonctions
    {
        public static string Creermessage(string prenom, int age, string sexe, int cours)
        {
            if (age == 0)
            {
                return ("Bonjour " + prenom + ", tu es un tout jeune microbe de type: " + sexe + ".");
            }
            else if (age == 1)
            {
                return ("Bonjour " + prenom + ", tu as " + age + " an et est de type: " + sexe + ".");
            }
            else
            {
                return ("Bonjour " + prenom + ", tu as " + age + " ans. Et tu es une LICORNE! Qui a " + cours + " cours. Ca fait beaucoup la nan? ");
            };
        }

        public static int Ask_and_VerifNumérique(string question)
        {
            while (true)
            {
                Console.Write(question.GradientBackground(Color.Black, Color.Yellow, Color.Red, Color.Blue, Color.Cyan) + " ");
                string nbInput = Console.ReadLine() ?? string.Empty;

                bool nbIsNumeric = int.TryParse(nbInput, out int nb);

                if (nbIsNumeric)
                {
                    return nb;
                    break;
                }
                else
                {
                    Console.WriteLine("espèce d'assisté bordel, met un C-H-I-F-F-R-E !");
                }
            }
        }

        public static string Ask_and_VerifString(string question)
        {
            while (true)
            {
                Console.Write(question.GradientBackground(Color.Black, Color.Yellow, Color.Red, Color.Blue, Color.Cyan) + " ");
                string strInput = Console.ReadLine() ?? string.Empty;

                bool strIsString = string.IsNullOrEmpty(strInput);

                if (strIsString == false)
                {
                    return strInput;
                    break;
                }
                else
                {
                    Console.WriteLine("espèce d'assisté bordel, met des L-E-T-T-R-E-S!");
                }
            }
        }
        public static string Ask_name()
        {
            Console.Write("Ton nom?".GradientBackground(Color.Black, Color.Yellow, Color.Red, Color.Blue, Color.Cyan)+" ");
            string nameInput = Console.ReadLine() ?? string.Empty;
            return nameInput;
        }

        public static string Ask_sex()
        {
            while (true)
            {
                Console.Write("Ton genre?".GradientBackground(Color.Black, Color.Yellow, Color.Red, Color.Blue, Color.Cyan) + " ");
                string sexInput = Console.ReadLine() ?? string.Empty;
                if (sexInput == "homme" || sexInput=="femme") {
                    return sexInput;
                }
                else
                {
                    Console.WriteLine("J'suis scientifique, pas attardé, donc y'a que 2 genre Karen, 'homme' ou 'femme'. C'est clair?");
                }
            }
        }

        public static int Ask_age()
        {
            while (true)
            {
                Console.Write("Ton age?".GradientBackground(Color.Black, Color.Yellow, Color.Red, Color.Blue, Color.Cyan)+" ");
                string ageInput = Console.ReadLine() ?? string.Empty;

                bool ageIsNumeric = int.TryParse(ageInput, out int age);

                if (ageIsNumeric)
                {
                    return age;
                    break;
                }
                else
                {
                    Console.WriteLine("espèce d'assisté bordel, met un C-H-I-F-F-R-E !");
                }
            }
        }

        public static int Ask_cours()
        {
            while (true)
            {
                Console.Write("Ton nombre de cours? ".GradientBackground(Color.Black, Color.Yellow, Color.Red, Color.Blue, Color.Cyan));
                string coursInput = Console.ReadLine() ?? string.Empty;

                bool coursIsNumeric = int.TryParse(coursInput, out int cours);

                if (coursIsNumeric && cours <= 20 && cours >= 1)
                {
                    return cours;
                    break;
                }
                else if (cours < 1)
                {
                    Console.WriteLine("T'es vraiment un branleur ou au chômage bordel, mais t'es censé avoir au moins 1 heure");
                }
                else if (cours> 20)
                {
                    Console.WriteLine("T'es addict ou tu sais pas lire, parce que le maximum c'est 20 cours mon reuf...");
                }
                else
                {
                    Console.WriteLine("Le NOMBRE de cours est censé être NUMERIQUE,donc rentre un NOMBRE...");
                }
            }
        }

        public static int MaxofThree(int n1, int n2, int n3)
        {
            if ((n1 >= n2) && (n1 >= n3))
            {
                return n1;
            }
            else if (n2 >= n3)
            {
                return n2;
            }
            else
            {
                return n3;
            };
        }



        public static List<int> Somme2liste(List<int> n1, List<int> n2)
        {
            n1.Reverse();
            n2.Reverse();

            List<int> somme = new List<int>();

            int retenue = 0; 

            int i = 0;
            while (i < n1.Count || i < n2.Count || retenue != 0)
            {
                int sum = retenue;

                if (i < n1.Count)
                    sum += n1[i];

                if (i < n2.Count)
                    sum += n2[i];

                somme.Add(sum % 10); 
                retenue = sum / 10; 

                i++;
            }
            somme.Reverse();

            return somme;
        }


        public static List<int> AddNumbers(List<int> l1, List<int> l2)
        {
            l1.Reverse();
            l2.Reverse();

            List<int> s = new List<int>();

            int retenue = 0;

            int i = 0;
            while (i < l1.Count || i < l2.Count || retenue != 0)
            {
                int sum = retenue;
                if (i < l1.Count)
                    sum += l1[i];
                if (i < l2.Count)
                    sum += l2[i];

                s.Add(sum % 10);
                retenue = sum / 10;

                i++;
            }
            s.Reverse();
            return s;
        }

        public static List<int> ReadNumber()
        {
            List<int> number = new List<int>();
            Console.WriteLine("Entrez les chiffres du nombre (terminer avec une ligne vide) :");
            while (true)
            {
                string input = Console.ReadLine();
                if (string.IsNullOrWhiteSpace(input))
                {
                    break;
                }
                if (!int.TryParse(input, out int digit) || digit < 0 || digit > 9)
                {
                    Console.WriteLine("Veuillez entrer un chiffre valide (0-9) ou une ligne vide pour terminer.");
                    continue;
                }
                number.Add(digit);
            }
            return number;
        }
    


        public static string CreerMessages(string nom, int age, int nbCours = -1)
        {
            var message1 = "";
            if (age == 0)
            {
                message1 = $"Bonjour {nom.Trim()}, tu es un bébé. ";
            }
            else if (age == 1)
            {
                message1 = $"Bonjour {nom.Trim()}, tu as un an.";
            }
            else
            {
                message1 = $"Bonjour {nom.Trim()}, tu as {age} ans.";
            }

            if (nbCours > 0)
            {
                message1 = message1 + $" Tu suis {nbCours} cours.";
            }
            return message1;
        }

        public static int DemandeInt(string message)
        {
            int result;
            while (true)
            {
                string userInput = DemandeString(message);
                if (int.TryParse(userInput, out result) == false)
                {
                    Console.WriteLine("Idiot, saisie incorrecte");
                }
                else
                {
                    break;
                }
            }
            return result;
        }

        public static string DemandeString(string message)
        {
            string result;
            while (true)
            {
                Console.WriteLine(message);
                string userInput = Console.ReadLine() ?? string.Empty;
                if (string.IsNullOrEmpty(userInput))
                {
                    Console.WriteLine("Idiot, saisie incorrecte");
                }
                else
                {
                    result = userInput;
                    break;
                }
            }
            return result;
        }
    }
}

