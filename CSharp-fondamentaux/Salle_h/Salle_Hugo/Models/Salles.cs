using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Salle_Hugo.Models
{
    public class Salles
    {
        public string Code { get; set; }
        public string Nom { get; set; }
        public int Nbplaces { get; set; }
        public Batiment Batiment { get; set; }
    }
}
