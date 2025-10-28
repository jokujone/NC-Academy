using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// VSTest.Console.exe on työkalu testien suorittamiseen

namespace TestiTestaus
{
    [TestClass]
    public class TestiTestausTests
    {
        [TestMethod]
        public void TestaaLaskemista()
        {
            int a = 5;
            int b = 10;
            int expected = 15;

            int actual = Program.Laske(a, b);
            Assert.AreEqual(expected, actual, "Laskeminen ei toimi :(");
        }

        [TestMethod]
        public void TestaaParempaaLaskemista()
        {
            int a = 5;
            int b = 10;
            int expected = 15;

            int actual = Program.Laske(a, b);
            Assert.AreEqual(expected, actual, "Parempi laskeminen toimii huonommin:(");
        }
    }
}
