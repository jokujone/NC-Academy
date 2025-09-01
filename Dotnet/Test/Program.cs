using System;
using System.Threading;

class Program
{
    public static int TotalScore = 0;
    public static int[] upgrades = [0, 0, 0, 0];

    public static int lootAmount = 1;
    public static int moneyPerLoot = 1;

    public static int skin = 0;
    public static char[] skins = ['o', 'O', 'C', 'c', '0', '8', '^', ',', ' ', 'x', 'X', '@', '#', '$', '%', '&', '*', '+', '-', '=', '~', '?', '!', '|', '<', '>', '[', ']', '{', '}', '/', '\\', ':', ';', '_',
        '`', '(', ')', '1', '2', '3', '4', '5', '6', '7', '9', 'A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z'];

    public static int mountainmode = 0;

    static void Main(string[] args)
    {
        if (args.Count() > 0)
        {
            if (args.Contains("-money"))
            {
                TotalScore += 100000;
            }
            if (args.Contains("-cheats"))
            {
                TotalScore += 100000000;
                moneyPerLoot = 1000;
                lootAmount = 40;
            }
            if (args.Contains("-megacheats"))
            {
                TotalScore = int.MaxValue;
            }
            if (args.Contains("-g") || args.Contains("-godmode"))
            {
                Console.WriteLine("Invincibility enabled");
                Thread.Sleep(1500);
            }
            if (args.Contains("-mm") || args.Contains("-mountain") || args.Contains("-mountainmode"))
            {
                Console.WriteLine("Mountain mode enabled");
                mountainmode = 1;
                Thread.Sleep(1500);
            }
        }
        else
        {
            Console.WriteLine("Welcome");
            Thread.Sleep(500);
            Console.WriteLine("Pick up that loot");
            Thread.Sleep(1000);
            Console.WriteLine("Controls: WASD and E");
            Thread.Sleep(1500);
            Console.Clear();
        }

        while (true)
        {
            RunGame();
            RunStore();
        }
    }

    static void RunGame()
    {
        Console.Clear();
        MapManager map = new MapManager(10);
        Player player = new Player(map, 5, 5);
        player.score = TotalScore;
        map.GenerateLoot(lootAmount);

        while (true)
        {
            RenderEngine.Render(map, player);
            ConsoleKeyInfo keyInfo = Console.ReadKey(true);
            switch (keyInfo.Key)
            {
                case ConsoleKey.W:
                    player.Move(0, -1);
                    break;
                case ConsoleKey.S:
                    player.Move(0, 1);
                    break;
                case ConsoleKey.A:
                    player.Move(-1, 0);
                    break;
                case ConsoleKey.D:
                    player.Move(1, 0);
                    break;
                case ConsoleKey.E:
                    TotalScore = player.score;
                    return;
                default:
                    break;
            }
            if (map.GetTile(player.pos).lootOnTile)
            {
                player.score += moneyPerLoot;
                map.GetTile(player.pos).lootOnTile = false;
                map.GenerateLoot(1);
            }
        }
    }

    static void RunStore()
    {
        Store store = new Store(upgrades);
        while (true)
        {
            Console.Clear();
            Console.WriteLine("Welcome to the Store!");
            store.DisplayItems();
            ConsoleKeyInfo keyInfo = Console.ReadKey(true);
            switch (keyInfo.Key)
            {
                case ConsoleKey.E:
                    return;
                case ConsoleKey.D1:
                    store.Purchase(0);
                    break;
                case ConsoleKey.D2:
                    store.Purchase(1);
                    break;
                case ConsoleKey.D3:
                    store.Purchase(2);
                    break;
                default:
                    break;
            }
        }
    }
}

class Player
{
    public Pos pos;
    public int score = 0;
    MapManager map;

    public Player(MapManager map, int startX, int startY)
    {
        this.map = map;
        pos = new Pos(startX, startY);
        map.GetTile(pos).playerOnTile = true;
    }

    public void Move(int deltaX, int deltaY)
    {
        int newX = pos.x + deltaX;
        int newY = pos.y + deltaY;

        if (newX < 0 || newX >= map.size || newY < 0 || newY >= map.size)
        {
            return;
        }

        Tile targetTile = map.GetTile(newX, newY);
        if (targetTile.Type == TileType.Impassable)
        {
            return;
        }

        // Update current tile
        map.GetTile(pos.x, pos.y).playerOnTile = false;

        // Move player
        pos.x = newX;
        pos.y = newY;

        // Update new tile
        targetTile.playerOnTile = true;
    }
}

static class RenderEngine
{
    public static void Render(MapManager map, Player player)
    {
        Console.Clear();
        for (int y = 0; y < map.size; y++)
        {
            for (int x = 0; x < map.size; x++)
            {
                Tile tile = map.GetTile(x, y);
                Console.Write(tile.getSymbol() + " ");
            }
            Console.WriteLine();
        }
        Console.WriteLine("\nMoney: " + player.score);
        
    }
}

class MapManager
{
    public int size;
    Tile[] tiles;
    public MapManager(int size)
    {
        this.size = size;
        tiles = new Tile[size * size];
        Random random = new Random(69 + Program.lootAmount);
        for (int i = 0; i < tiles.Length; i++)
        {
            if (Program.mountainmode == 1) //MOUNTAIN MODE
            {
                if (random.Next(0, 100) < 20 && i != size * size / 2) // 20% chance to be impassable in MM
                    tiles[i] = new Tile(TileType.Impassable, i, i % size);
                else
                    tiles[i] = new Tile(TileType.Ground, i, i % size);
            }
            else
                tiles[i] = new Tile(TileType.Ground, i, i % size);
        }
    }

    public Tile GetTile(int x, int y)
    {
        return GetTile(new Pos(x, y));
    }

    public Tile GetTile(Pos pos)
    {
        if (pos.x < 0 || pos.x >= size || pos.y < 0 || pos.y >= size)
        {
            throw new ArgumentOutOfRangeException("out of bounds.");
        }
        return tiles[pos.y * size + pos.x];
    }

    public void GenerateLoot(int amount)
    {
        Random rand = new Random();
        for (int i = 0; i < amount; i++)
        {
            Pos lootPos = new Pos(rand.Next(size), rand.Next(size));
            while (GetTile(lootPos).Type != TileType.Ground || GetTile(lootPos).lootOnTile)
            {
                lootPos = new Pos(rand.Next(size), rand.Next(size));
            }
            Tile lootTile = GetTile(lootPos);
            lootTile.lootOnTile = true;
        }
    }

}

class Tile
{
    public TileType Type { get; set; }
    public bool playerOnTile = false;
    public bool lootOnTile = false;


    public Tile(TileType type, int x, int y)
    {
        Type = type;
    }

    public char getSymbol()
    {
        if (playerOnTile)
        {
            return Program.skins[Program.skin];
        } if (lootOnTile)
        {
            return '*';
        }
        switch (Type)
        {
            case TileType.Ground:
                return '.';
            case TileType.Impassable:
                return '#';
            default:
                return '?';
        }
    }
}

class Pos
{
    public int x { get; set; }
    public int y { get; set; }

    public Pos(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
    
    public static bool equals(Pos a, Pos b)
    {
        return a.x == b.x && a.y == b.y;
    }
}

enum TileType
{
    Ground,
    Impassable,
}

class Store
{
    public StoreItem[] items;

    public Store(int[] upgrades)
    {
        items =
        [
            new StoreItem("Efficient money", 10, "Increases money gain by 1 per loot",upgrades[0]),
            new StoreItem("More loot", 100, "Increases spawned loot amount by 1",upgrades[1]),
            new StoreItem("Purchase skin", 500, "Buy yourself a better skin from the battlepass store",upgrades[2]),
        ];
        foreach (var item in items)
        {
            item.CalculateCost();
        }
        
    }

    public void Purchase(int item)
    {
        if (Program.TotalScore >= items[item].Cost)
        {
            Program.TotalScore -= items[item].Cost;
            Program.upgrades[item]++;
            items[item].Owned++;
            items[item].CalculateCost();
            
            switch (item)
            {
                case 0:
                    Program.moneyPerLoot += 1;
                    break;
                case 1:
                    Program.lootAmount += 1;
                    break;
                case 2:
                    Program.skin = Random.Shared.Next(Program.skins.Length -1);
                    break;
            }
        }
    }

    public void DisplayItems()
    {
        for (int i = 0; i < items.Length; i++)
        {
            Console.WriteLine($"{i + 1}. {items[i].Name} - {items[i].Cost} money. {items[i].Description}");
        }
    }
}

class StoreItem
{
    public string Name { get; set; }
    private int BaseCost { get; set; }
    public int Cost { get; set; }
    public string Description { get; set; }
    public int Owned { get; set; }

    public StoreItem(string name, int cost, string description, int owned)
    {
        Name = name;
        BaseCost = cost;
        Description = description;
        Owned = owned;

        CalculateCost();
    }

    public void CalculateCost()
    {
        Cost = (int)(BaseCost * (1.2f * Owned + 1));
    }
}