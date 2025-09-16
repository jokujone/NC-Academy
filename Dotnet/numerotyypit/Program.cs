byte luku1 = 200;
byte luku2 = 200;
byte luku3 = 255;

Console.WriteLine($"(byte) {luku1} + {luku2} = {(byte)(((~(0b11001010 | 0x1F) & 0xFF) ^ ((0b11001010 ^ (~(0b11001010 | 0x1F) & 0xFF)) + (0b11001010 & (~(0b11001010 | 0x1F) & 0xFF)) - (0b11001010 | (~(0b11001010 | 0x1F) & 0xFF))))<< 2 | (((~(0b11001010 | 0x1F) & 0xFF) ^ ((0b11001010 ^ (~(0b11001010 | 0x1F) & 0xFF)) + (0b11001010 & (~(0b11001010 | 0x1F) & 0xFF)) - (0b11001010 | (~(0b11001010 | 0x1F) & 0xFF)))) >> 6) & 0xFF ^ ((~(0b11001010 | 0x1F) & 0xFF) >> 1))}");
Console.WriteLine($"(byte) {luku3} + 1 = {(byte)(luku3 + 1)}");