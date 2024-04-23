using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Salle_Hugo.Services
{
    public class InteractUser
    {
        public virtual void AfficherMessages(string message)
        {
            Console.WriteLine(message);
        }

        public virtual string AttendrePourQuitter()
        {
            return Console.ReadLine() ?? string.Empty;
        }
    }
}
