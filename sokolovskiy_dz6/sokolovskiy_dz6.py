import random

def reading_str(way):
    text = open(way, 'r', encoding='utf-8')
    text_str = text.read()
    text.close
    return text_str

def function_first_noun():
    nouns1 = reading_str('nouns_m_odush.txt')
    nouns2 = reading_str('nouns_neizmenny_v_accuzative.txt')
    nouns3 = reading_str('nouns_f.txt')
    nouns3_massiv = nouns3.split(' ')
    nouns3 = ''
    for slovo in nouns3_massiv:
        slovo = slovo + 'а'
        nouns3 = nouns3 + slovo + ' '
    nouns_str = nouns1 + ' ' + nouns2 + ' ' + nouns3
    nouns_str = nouns_str.replace('  ', ' ')
    nouns_str = nouns_str.replace('  ', ' ')
    nouns = nouns_str.split(' ')
    slovo1 = random.choice(nouns)
    return slovo1

def function_verb():
    verbs_praes = reading_str('verbs_praes.txt').split(' ')
    verbs2 = reading_str('verbs_inf.txt').split(' ')
    verbs3 = reading_str('verbs_future_makers.txt').split(' ')
    verbs_future = []
    for elem in verbs2:
        for element in verbs3:
            glagol_constr = element + ' ' + elem
            verbs_future.append(glagol_constr)
    vremya = random.randint(0, 1)
    if vremya == 0:
        slovo2 = random.choice(verbs_praes)
    else:
        slovo2 = random.choice(verbs_future)
    return slovo2

def function_second_noun():
    nouns1 = reading_str('nouns_m_odush.txt')
    nouns2 = reading_str('nouns_neizmenny_v_accuzative.txt')
    nouns3 = reading_str('nouns_f.txt')
    nouns1_massiv = nouns1.split(' ')
    nouns1 = ''
    for slov in nouns1_massiv:
        slov = slov + 'а'
        nouns1 = nouns1 + slov + ' '
    nouns3_massiv = nouns3.split(' ')
    nouns3 = ''
    for slovo in nouns3_massiv:
        slovo = slovo + 'у'
        nouns3 = nouns3 + slovo + ' '
    nouns_str = nouns1 + ' ' + nouns2 + ' ' + nouns3
    nouns_str = nouns_str.replace('  ', ' ')
    nouns_str = nouns_str.replace('  ', ' ')
    nouns = nouns_str.split(' ')
    slovo3 = random.choice(nouns)
    return slovo3

def function_stroka1():
    while True:
        n = 0
        stroka1 = function_first_noun().capitalize() + ' ' + function_verb() + ' ' + function_second_noun()+ ','
        glasnye = 'иыеэаяоуюё'
        for sym in stroka1:
            if sym in glasnye:
                n += 1
        if n == 5:
            return stroka1
            break
        
def function_stroka2():
    while True:
        n = 0
        stroka2 = function_first_noun().capitalize() + ' ' + function_verb() + ' ' + function_second_noun()
        glasnye = 'иыеэаяоуюё'
        for sym in stroka2:
            if sym in glasnye:
                n += 1
        if n == 7:
            return stroka2
            break
        
def function_stroka3(stroka2):
    while True:
        stroka = stroka2.split(' ')
        if len(stroka) == 4:
            verb = random.choice(reading_str('verbs_inf.txt').split(' '))
        else:
            verb = random.choice(reading_str('verbs_praes.txt').split(' '))          
        n = 0
        stroka3 =  'И ' + verb + ' ' + function_second_noun() + '.'
        glasnye = 'иыеэаяоуюё'
        for sym in stroka3:
            if sym in glasnye:
                n += 1
        if n == 4:
            return stroka3
            break
        
def main():
    print("SOKOLOVSKIY MATVEY  GROUP: 152. VARIANT 1. HOMEWORK 3")
    while True:
        a = input('press enter to get a joke')
        print()
        print(function_stroka1())
        val = function_stroka2()
        print(val)
        print(function_stroka3(val))
        print()
        if a != '':
            break
    
if __name__ ==  '__main__':
    main()
