using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace stocks.views
{
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
}
