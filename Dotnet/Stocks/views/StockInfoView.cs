using Stocks;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace stocks.views
{
    public class StockInfoView : IView
    {
        public void Display()
        {
            Console.WriteLine($"=== {Program.Game.selectedStock.Name()} ===");
            Console.WriteLine("1. Buy");
            Console.WriteLine("2. Price history");
            Console.WriteLine("3. Back");
        }

        public IView HandleInput()
        {
            throw new NotImplementedException();
        }
    }
}
