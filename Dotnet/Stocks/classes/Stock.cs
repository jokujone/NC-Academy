using Stocks;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace stocks.classes
{
    public class Stock
    {
        string name;
        double cValue;
        double volatility;
        public List<StockValueEntry> ValueHistory;

        public static Stock Generate()
        {
            Stock stock = new Stock();
            Random rand = new Random();

            stock.name = NameGenerator.Generate();
            stock.cValue = rand.Next(5, 500);
            stock.volatility = rand.NextDouble();
            stock.ValueHistory = new List<StockValueEntry>();

            return stock;
        }

        public override string ToString()
        {
            return $"{name}, {cValue}$";
        }

        public string Name() 
        {
            return name; 
        }

        public double Value()
        {
            return Math.Round(cValue * 100) / 100;
        }

        public void Progress()
        {
            ValueHistory.Add(new StockValueEntry(Program.Game.Day, cValue));
            Random r = new();
            volatility *= 1 + ((r.NextDouble() - 0.5d) / 10d);
        }
    }
}
