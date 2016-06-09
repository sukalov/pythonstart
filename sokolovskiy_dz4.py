print("SOKOLOVSKIY MATVEY  GROUP: 152. VARIANT 1. HOMEWORK 3")
print("you type words until you just press enter twice")
print("after you enter nothing, you get all your words inversed back")
print("and then you can enter words again (you will get a new list of words)")
while True:
    vse_slova = []
    
    while True:
        slovo = input("enter a word: ")
        if slovo == '':
            print("")
            for element in vse_slova:
                print(element)
            print("")
            break
        else:
            slovo2 = ''
            i = len(slovo) - 1
            while i != -1:
                slovo2 = slovo2 + slovo[i]
                i = i - 1
            vse_slova.append(slovo2)
