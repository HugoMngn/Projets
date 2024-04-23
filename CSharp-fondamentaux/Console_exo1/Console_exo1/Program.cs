using System.ComponentModel.Design;
using System.Drawing;
using ANSIConsole;
using Console_exo1;
if (!ANSIInitializer.Init(false)) ANSIInitializer.Enabled = false;


/*
string user_prenom;
string user_gender;
int user_age;
int user_cours;

user_prenom = MesFonctions.Ask_name();
user_age = MesFonctions.Ask_age();
user_gender = MesFonctions.Ask_sex();
if (user_age > 10) { user_cours = MesFonctions.Ask_cours(); } else { user_cours = 0; };


Console.WriteLine(MesFonctions.Creermessage(user_prenom, user_age, user_gender, user_cours).GradientBackground(Color.Black, Color.Yellow, Color.Red, Color.Blue, Color.Cyan));
Console.ReadLine();

user_prenom = MesFonctions.Ask_and_VerifString("Prénom: ");
user_age = MesFonctions.Ask_and_VerifNumérique("Age: ");
user_gender = MesFonctions.Ask_and_VerifString("Genre: ");
if (user_age > 10) { user_cours = MesFonctions.Ask_and_VerifNumérique("Nombre de cours: "); } else { user_cours = 0; };

Console.WriteLine(MesFonctions.Creermessage(user_prenom, user_age, user_gender, user_cours).GradientBackground(Color.Black, Color.Yellow, Color.Red, Color.Blue, Color.Cyan));
Console.ReadLine();
*/

/*
Console.WriteLine("Donne le premier nombre?");
int n1 = int.Parse(Console.ReadLine());

Console.WriteLine("Donne le deuxième nombre?");
int n2 = int.Parse(Console.ReadLine());

Console.WriteLine("Donne le troisième nombre?");
int n3 = int.Parse(Console.ReadLine());

Console.WriteLine("Le plus grand nombre est: "+ MesFonctions.MaxofThree(n1, n2, n3));
Console.ReadLine();



List<int> L1 = new List<int> { 9, 4, 0 };
List<int> L2 = new List<int> { 8, 3 };

List<int> somme = MesFonctions.Somme2liste(L1, L2);

Console.WriteLine("Somme : ");
Console.Write("[");
for (int i = 0; i < somme.Count; i++)
{
    Console.Write(somme[i]);
    if (i != somme.Count - 1)
    {
        Console.Write(", ");
    }
}
Console.Write("]");
*/

/*
Console.WriteLine();
List<int> l1 = MesFonctions.ReadNumber();

Console.WriteLine();
List<int> l2 = MesFonctions.ReadNumber();

List<int> sum = MesFonctions.AddNumbers(l1, l2);

Console.WriteLine("Somme : ");
Console.Write("[");
for (int i = 0; i < sum.Count; i++)
{
    Console.Write(sum[i]);
    if (i != sum.Count - 1)
    {
        Console.Write(", ");
    }
}
Console.Write("]");*/

List<Personne> lesPersonnes = new List<Personne>();

while (true)
{
    int entreeMenu = MesFonctions.DemandeInt(@"Que voulez vous faire ?
1. Créer une personne, 
2. Afficher les personnes
3. Creer 10000 personnes");
    if (entreeMenu == 1)
    {
        Personne p = new Personne();
        p.Nom = MesFonctions.DemandeString("Veuillez indiquer votre nom : ");
        p.Age = MesFonctions.DemandeInt("Age : ");
        p.NbCours = MesFonctions.DemandeInt("Combien de cours : ");
        Personne p2 = p;
        // affichage du résultat

        Console.WriteLine(MesFonctions.CreerMessages(p2.Nom, p2.Age, p2.NbCours));
        lesPersonnes.Add(p);
    }
    else if (entreeMenu == 2)
    {
        Console.WriteLine("je sais pas faire");
    }
    else if (entreeMenu == 3)
    {
        for (int i = 0; i < 10000; i++)
        {
            Personne p = new Personne();
            p.Nom = "Polo";
            p.Age = 25;
            lesPersonnes.Add(p);
        }
        Console.WriteLine("je sais pas faire");
    }
    else
    {
        Console.WriteLine("entrée invalide");
    }
}

// pour attendre que l'utilisateur veuille bien quitter
Console.ReadLine();