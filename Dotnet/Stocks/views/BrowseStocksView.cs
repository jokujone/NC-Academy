using stocks.classes;
using Stocks;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace stocks.views
{
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
}
