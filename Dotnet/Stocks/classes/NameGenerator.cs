using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace stocks.classes
{
    public static class NameGenerator
    {
        public static string Generate()
        {
            TextInfo ti = new CultureInfo("en-US", false).TextInfo;
            string name = "";

            Random rand = new Random();
            name += ti.ToTitleCase(nameparts[rand.Next(nameparts.Length)]);
            if (rand.NextDouble() < 0.3)
            {
                name += " ";
                name += ti.ToTitleCase(nameparts[rand.Next(nameparts.Length)]);
            }
            else
                name += nameparts[rand.Next(nameparts.Length)];

            if (rand.NextDouble() < 0.3) name += " " + suffixes[rand.Next(suffixes.Length)];

            return name;
        }

        static string[] nameparts =
        {
            "inter",
            "intra",
            "super",
            "techno",
            "tech",
            "tec",
            "bit",
            "byte",
            "glass",
            "club",
            "stock",
            "gen",
            "roof",
            "floor",
            "pizza",
            "pesto",
            "io",
            "down",
            "up",
            "par",
            "ninja",
            "nord",
            "cloud",
            "sole",
            "novo",
            "pack",
            "real",
            "full",
            "sum",
            "run",
            "start",
            "fuel",
            "field",
            "tree",
            "main",
            "master",
            "mini",
            "max",
            "soft",
            "micro",
            "wave",
            "idea",
            "day",
            "train",
            "twin",
            "turbo",
            "two",
            "one",
        };
        static string[] suffixes =
        {
            "Inc.",
            "Gmbh",
            "Co.",
            "Oy",
            "Ab",
            "Group",
            "Technologies",
        };
    }
}
