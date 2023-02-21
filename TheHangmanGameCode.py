word = input("Please enter the secret word: ").lower().strip()
for x in range(100):
    print()
typed = []
hits =[]
missed = 0
while True:
    password = ""
    for letter in word:
        password += letter if letter in hits else "."
    print(password)
    if password == word:
        print("You got it!" )
        break
    tentative = input("Type one letter: ").lower().strip()
    if tentative in typed:
        print("You already tried that one! ")
        continue
    else:
        typed += tentative
        if tentative in word:
            hits += tentative
        else:
            missed += 1
            print("You missed! ")
        print("|===|===\n|   | ")
        print("|   O  " if missed >= 1 else "|")
        line2 = ""
        if missed == 2:
            line2 = "  |  "
        elif missed == 3:
            line2 = " \|  "
        elif missed >= 4:
            line2 = "  \|/ "
            print(f"|{line2}")
            line3 = ""
            if missed == 5:
                line3 += "  /  "
            elif missed >=6:
                line3 += "  / \ "
                print(f"|{line3}")
                print("|\n==========")
                if missed == 6:
                    print("Hanged! ")
                    break
