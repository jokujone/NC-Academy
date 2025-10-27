using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace stocks.views
{
    public interface IView
    {
        void Display();
        IView HandleInput();
    }
}
