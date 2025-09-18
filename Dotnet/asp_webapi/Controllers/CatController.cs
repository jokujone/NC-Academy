using Microsoft.AspNetCore.Mvc;
using System.Text.Json;

namespace asp_webapi.Controllers
{
    [ApiController]
    [Route("api/cat")]
    public class CatController : ControllerBase
    {
        [HttpGet("test")]
        public string Test()
        {
            return "Cat says meow";
        }

        [HttpGet("")]
        public string Pet(string? action)
        {
            if (action == "pet")
            {
                Random random = new Random();
                if (random.NextDouble() > 0.1d)
                    return "*hapy cat noises*";
                else
                    return "*angry cat noises*";
            }
            if (action == "a")
            {
                // AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa
                Random random = new Random();
                string aAAAAAAA = "";
                bool AaaAAAAA = true;
                while (AaaAAAAA)
                {
                    bool aaAaaAAAaaa, aAAAAAaa = false;
                    bool AAAAAAAaaaa;
                    if (aaAaaAAAaaa = random.NextDouble() > 0.5)
                    {aAAAAAAA += "A";}
                    else
                    {aAAAAAAA += "a";}

                    ///AAAAAAAAH
                    if (aAAAAAaa = random.NextDouble() < 0.0001 * (aAAAAAAA.Length / 10))
                    {AaaAAAAA = true;
                        AAAAAAAaaaa = AaaAAAAA;
                        Console.WriteLine("a" + AAAAAAAaaaa + AaaAAAAA + "a");
                        break;}
                }
                return aAAAAAAA + "a";
            }
            if (action == "smalltalk")
            {
                return Talk();
            }
            if (action == "steal")
            {
                return new Cat(DateTime.Now).ToString();
            }


            string help = "Cat says: ERROR INCORRECT ACTION. NO RESPONSE\nAVAILABLE ACTIONS:\n";

            help += "\n'pet' - pet the cat";
            help += "\n'a' - say 'a' to the cat";
            help += "\n'smalltalk' - start a conversation with the cat";
            help += "\n'steal' - take the cat";
            return help;
        }

        //random cat responses
        string Talk()
        {
            Random random = new Random();
            string[] responses = new string[]
            {
                "meow",
                "purr",
                "hiss",
                "mew",
                "chirp",
                "mrrp",
                "prrr",
                "meow meow",
                "meow purr",
                "hiss meow",
                "Is your location?\n\n62°53'16.0\"N 27°37'44.4\"E",
                "you are stupid idiot",
                "moew",
                "meow",
                "meow",
                "meow",
                "m",
                "\nWouldn't it be funny if\n\nforeach(cat in cats)\n{\n   foreach(child in cat.children)\n   {\n      child.Dispose(DisposeType.DestroyAndBlowUp);\n   }\n   cat.Dispose(DisposeType.DestroyAndRemoveAllKnowledge);\n   EvidenceCenter.BurnAll(EvidenceCenter.GetAllEvidence());\n   EvidenceCenter.Dispose(DisposeType.BurnDown);\n}",
            };
            return "Cat says: " + responses[random.Next(responses.Length)];
        }
    }

   public class Cat
    {
        public string Name { get; set; }
        public string CurrentBrainActivity { get; set; }
        public bool Soul { get; set; }
        public DateTime LastInhaleTime { get; set; }
        public DateTime BirthTime { get; set; }
        public Cat[] ?Children { get; set; }
        public Cat(DateTime minBirthDate)
        {
            Random r = new Random();
            Name = GenerateName(3, 15);
            CurrentBrainActivity = GenerateName(5, 120);
            Soul = r.NextDouble() > 0.5d;
            LastInhaleTime = DateTime.Now - TimeSpan.FromMilliseconds(r.Next(0, 4000));
            BirthTime = DateTime.Now - TimeSpan.FromSeconds(r.Next(100000, 500000000));
            if (r.NextDouble() > 0.6d)
                Children = SpawnThem();
        }

        static string GenerateName(int min, int max)
        {
            string name = "";

            Random rnd = new Random();

            int size = rnd.Next(min, max);

            for (int i = 0; i < size; i++)
            {
                name += (char)rnd.Next('A', 'Z' + 1);
            }

            return name;
        }

        public override string ToString()
        {
            var options = new JsonSerializerOptions
            {
                WriteIndented = true
            };
            return $"You have stolen the cat you were just connected to. This action cannot be undone. Cat data:\n\n{JsonSerializer.Serialize(this, options)}\n\nERROR: You do not have enough space to store this cat. Cat {Name} and it's descendants {GetAllChildNames()}have been permanently destroyed.\nA total of {GetDescendantCount() + 1} cat(s) have been destroyed.";
        }

        public Cat[] SpawnThem()
        {
            List<Cat> childs = new List<Cat>();
            Random r = new Random();
            int count = r.Next(1, 5);
            for (int i = 0; i < count; i++)
            {
                childs.Add(new Cat(BirthTime));
            }
            return childs.ToArray();
        }

        public string GetAllChildNames()
        {
            string childNames = "";
            if (Children == null) return childNames;
            foreach(Cat cat in Children)
            {
                childNames += cat.Name + ", ";
                childNames += cat.GetAllChildNames();
            }
            return childNames;
        }

        public int GetDescendantCount()
        {
            int count = 0;
            if (Children == null) return count;
            foreach (Cat cat in Children)
            {
                count++;
                count += cat.GetDescendantCount();
            }
            return count;
        }
    }
}
