using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Salle_Hugo.Services
{
    public class SaisieUser
    {
        public static InteractUser InteractU { get; set; } = new InteractUser();
        public virtual int DemandeInt(string message)
        {
            int result;
            while (true)
            {
                string userInput = DemandeString(message);
                if (int.TryParse(userInput, out result) == false)
                {
                    Console.WriteLine("Besoin nombre (c'est clair?)");
                }
                else
                {
                    break;
                }
            }
            return result;
        }

        public virtual string DemandeString(string message)
        {
            string result;
            while (true)
            {
                Console.WriteLine(message);
                string userInput = Console.ReadLine() ?? string.Empty;
                if (string.IsNullOrEmpty(userInput))
                {
                    Console.WriteLine("Pas laisser vide (assez simple non?)");
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
