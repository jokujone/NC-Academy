using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace stocks.classes
{
    public class StockValueEntry
    {
        public int Day { get; set; }
        public double Value { get; set; }

        public StockValueEntry(int day, double value)
        {
            Day = day;
            Value = value;
        }
    }
}
