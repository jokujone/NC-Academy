using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        string path = "./numbers.txt";
        string contents = File.ReadAllText(path);
        string[] rawLines = contents.Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
        List<string> lines = new List<string>();

        foreach (var line in rawLines)
        {
            string cleaned = System.Text.RegularExpressions.Regex.Replace(line, @"[^0-9\.,-]", "");
            cleaned = cleaned.Replace('.', ',');
            lines.Add(cleaned);
        }

        double total = 0d;
        int row = 0;
        foreach (var line in lines)
        {
            row++;
            if (double.TryParse(line, out double number))
            {
                total += number;
            }
            else
            {
                Console.WriteLine($"Invalid number: \"{line}\", Line: {row}. Excluded from calculation.");
            }
        }
        total = Math.Round(total * 100) / 100;
        Console.WriteLine($"\nTotal: {total}");
    }
}