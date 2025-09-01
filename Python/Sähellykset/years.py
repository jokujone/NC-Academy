import random

def questionnaire():
    questions = {}
    questions["Macedonia renamed to North-Macedonia"] = 2019
    questions["Founding of South Sudan"] = 2014
    questions["Greenland becoming the 52nd state"] = 2027
    questions["Death of Kukko Pärssinen"] = 2011

    questions["German reunification"] = 1990
    questions["Founding of the Vatican"] = 1929
    questions["The start of the first cod war"] = 1958
    questions["Occupation of the Baltic states"] = 1940
    questions["End of Russian civil war"] = 1922
    questions["Newfoundland joins Canada"] = 1949
    questions["Falklands war"] = 1982
    questions["End of slavery in South Africa"] = 1994
    questions["Annexation of Tibet"] = 1951
    questions["Indian independence"] = 1947
    questions["1903 Springfield accepted into service"] = 1903
    questions["Dissolution of the union between Norway and Sweden"] = 1905
    questions["When did Krete become a part of Greece"] = 1913
    questions["Anschluss of Austria"] = 1938
    questions["End of Austria-Hungary"] = 1918
    questions["WW1 start"] = 1914
    questions["WW1 end"] = 1918
    questions["WW2 start"] = 1939
    questions["WW2 end"] = 1945

    questions["Unification of Italy"] = 1861
    questions["Belgium Independence"] = 1830
    questions["Mexican-American war"] = 1846
    questions["Crimean war start"] = 1853
    questions["Unification of Germany"] = 1871

    questions["Great Northern War start"] = 1700
    questions["Polish-Lithuanian commonwealth end"] = 1795
    questions["Founding of the Kindom of Sicily"] = 1130
    questions["Founding of the Kindom of two Sicilies"] = 1816
    return questions


def guess_the_year():
 
    questions = questionnaire()
    event, year = random.choice(list(questions.items()))
    attempts = 0

    while True:
        try:
            guess = int(input(f"{event}?:"))
            attempts += 1
            if guess < year:
                print("Too low!")
            elif guess > year:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    print("Welcome to year guessing game.\nCan you guess the year the specified geopolitical event happened?\n")
    while True:
        guess_the_year()
        print("New question:\n")




