using stocks.classes;
using stocks.views;
using System;
using System.Globalization;

//Keskeneräinen projekti

namespace Stocks
{
    class Program
    {
        public List<Stock> stockList = new List<Stock>();

        public static Program Game;

        public Stock? selectedStock = null;
        public int Day = 0;

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
            for (int i = 0; i < 50; i++)
            {
                stockList.Add(Stock.Generate());
            }
        }
    }
}
