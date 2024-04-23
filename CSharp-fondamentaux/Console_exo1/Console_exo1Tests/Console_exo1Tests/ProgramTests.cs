using Console_exo1;
using NUnit.Framework.Internal;

namespace Console_exo1Tests
{
    public class ProgramTests
    {
        [Test]
        public void CreerMessageTests0()
        {
            var result = MesFonctionsTests.CreermessageTests("HUGO", "0", "homme");
            Assert.AreEqual("Bonjour HUGO, tu es un tout jeune microbe de type: homme.", result);

            var result2 = MesFonctionsTests.CreermessageTests("HUGO", "1", "homme");
            Assert.AreEqual("Bonjour HUGO, tu as 1 an et est de type: homme.", result2);

            var result3 = MesFonctionsTests.CreermessageTests("HUGO", "18", "homme");
            Assert.AreEqual("Bonjour HUGO, tu as 18 ans. Et tu es GAY!", result3);
        }
    }
}