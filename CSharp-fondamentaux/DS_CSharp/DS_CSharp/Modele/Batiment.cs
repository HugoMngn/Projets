using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Salle-Hugo.Modele
{
    public class Batiment
    {
        public string Code { get; set; }
        public string Nom { get; set; }
        public int Adresse { get; set; }
        public int CodePostal { get; set; }
        public string Ville { get; set; }
    }
}
