using Stocks;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace stocks.views
{
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
}
