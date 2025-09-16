//First call needed to wake up the computer
Runloops(10000, 'a', false);

Runloops(10_000, 'a', true);
Runloops(500_000, 'a', true);
Runloops(600_000, 'a', true);

void Runloops(int amount, char symbol, bool verbose)
{
    string result = "";
    DateTime start = DateTime.Now;
    for (int i = 0; i < amount; i++)
    {
        result += symbol;
    }
    if (verbose)
        Console.WriteLine($"Time taken for {amount} of {symbol}: {Math.Round((DateTime.Now - start).TotalMilliseconds * 10) / 10}ms");
    Random rnd = new Random();
    if (rnd.NextDouble() > 0.95d)
        Console.WriteLine($"Here's your entire {result}");
}