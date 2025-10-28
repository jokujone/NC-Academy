namespace TestiTestaus
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine(Laske(20, 5));
            Console.WriteLine(LaskeParemmin(20, 5));
            Console.ReadLine();
        }
        public static int Laske(int a, int b)
        {
            return a + b;
        }

        public static int LaskeParemmin(int a, int b)
        {
            int aa = a + b;
            int bee = a + b;
            aa -= b;
            bee -= a;

            int baa = aa + bee;

            Random randomRandomizer = new();
            Random random = new Random(a + randomRandomizer.Next());
            int ran = random.Next(10,500);

            for (int i = 0; i < ran; i += 3)
            {
                int dom = random.Next(100,500000);
                if (dom == 999)
                {
                    string run = "run";
                    try
                    {
                        bool bees = int.TryParse(run, out baa);
                        if (bees)
                        {
                            throw new Exception("a");
                        }
                    }
                    catch (Exception e)
                    {
                        if (e is Exception)
                            continue;
                    }
                }
            }
            return baa;
        }
    }
}

