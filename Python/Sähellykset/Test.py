import random
for i in range(10):
    success = False
    while not success:
        try:
            char = ""
            for i in range(500):
                    char += chr(random.randint(1, 2000))
            print(char)
            success = True
        except UnicodeEncodeError:
            pass