print("SOKOLOVSKIY MATVEY  GROUP: 152. VARIANT 1. HOMEWORK 2")
print("you have to write any word, and the program will return every second letter.")
print("(spaces are also counted as symbols, so, please, don't use them)\n")
while True:
    slovo = input("type any word (if you want to break, just press 'enter'): ")
    if slovo != "":
        spaces = slovo.count(" ")
        even_letters = ''             
        if spaces == 1:
            print("you've typed a space. to get a nice result try not to repeat this mistake")
        elif spaces > 1:
            print("you've typed %s spaces. please try without them" % str(spaces))
        else:
            for i in range(len(slovo)):
                if i % 2 == 1:
                    even_letters = even_letters + slovo[i]
                else:
                    even_letters = even_letters
            print("here are even letters (every second letter): %s\n" % even_letters)
    else:
        break
