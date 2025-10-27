using Stocks;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace stocks.views
{
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
}
