using System;
using System.Globalization;

namespace Stocks
{
    class Program
    {
        public List<Stock> stockList = new List<Stock>();

        public static Program Game;

        static void Main(string[] args)
        {
            Game = new Program();
            Game.Run();
        }

        void Run()
        {
            GenerateStocks();

            IView currentView = new MainMenuView();
            while (currentView != null)
            {
                currentView.Display();
                currentView = currentView.HandleInput();
            }
            Console.WriteLine("Exiting application...");
        }

        void GenerateStocks()
        {
            for (int i = 0; i < 200; i++)
            {
                stockList.Add(Stock.Generate());
            }
        }
    }

    public class MainMenuView : IView
    {
        public void Display()
        {
            Console.Clear();
            Console.WriteLine("=== Main Menu ===");
            Console.WriteLine("1. View Stocks");
            Console.WriteLine("2. Go to Settings");
            Console.WriteLine("3. Exit");
        }

        public IView HandleInput()
        {
            var input = Console.ReadLine();
            return input switch
            {
                "1" => new StocksView(),
                "2" => new SettingsView(),
                "3" => null,
            };
        }
    }

    public class StocksView : IView
    {
        public void Display()
        {
            Console.Clear();
            Console.WriteLine("=== Stocks ===");
            Console.WriteLine("1. Browse Stocks");
            Console.WriteLine("2. My Stocks");
            Console.WriteLine("3. Back to Main Menu");
        }

        public IView HandleInput()
        {
            var input = Console.ReadLine();
            return input switch
            {
                "1" => new BrowseStocksView(0),
                "2" => new SettingsView(),
                "3" => new MainMenuView(),
                _ => this
            };
        }
    }

    public class BrowseStocksView : IView
    {
        int page = 0;

        public BrowseStocksView(int page)
        {
            this.page = page;
        }

        public void Display()
        {
            Console.Clear();
            Console.WriteLine($"=== Browse Stocks | Page {page + 1} ===");
            GenerateStockList();
            Console.WriteLine("7. Previous Page");
            Console.WriteLine("8. Next Page");
            Console.WriteLine("9. Back");
        }

        public IView HandleInput()
        {
            string? input = Console.ReadLine();
            switch (input)
            {
                case "7":
                    if (page != 0)
                        return new BrowseStocksView(page - 1);
                    else return new BrowseStocksView(page);
                case "8":
                    if (Program.Game.stockList.Count > (page + 1) * 6)
                        return new BrowseStocksView(page + 1);
                    else
                        return new BrowseStocksView(page);
                case "9":
                    return new StocksView();
                default:
                    return this;
            }
        }

        void GenerateStockList()
        {
            List<Stock> stocks = Program.Game.stockList;
            for (int i = 0; i < 6; i++)
            {
                int stockIndex = page * 6 + i;
                if (stocks.Count <= stockIndex)
                    break;
                Stock stock = stocks[stockIndex];
                Console.WriteLine($"{i + 1}. [{stockIndex + 1}] {stock.ToString()}");
            }
        }
    }


    public class SettingsView : IView
    {
        public void Display()
        {
            Console.Clear();
            Console.WriteLine("=== Settings ===");
            Console.WriteLine("1. Back to Main Menu");
        }

        public IView HandleInput()
        {
            var input = Console.ReadLine();
            return input == "1" ? new MainMenuView() : this;
        }
    }

    public interface IView
    {
        void Display();
        IView HandleInput();
    }

    public class Stock
    {
        string name;
        double cValue;
        double volatility;
        //add history

        public static Stock Generate()
        {
            Stock stock = new Stock();
            Random rand = new Random();

            stock.name = NameGenerator.Generate();
            stock.cValue = rand.Next(5, 500);
            stock.volatility = rand.NextDouble();

            return stock;
        }

        public override string ToString()
        {
            return $"{name}, {cValue}$";
        }
    }

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
        };
        static string[] suffixes =
        {
            "Inc",
            "Gmbh",
            "co",
            "Oy",
            "Ab",
            "Group",
            "Technologies",
        };
    }
}
