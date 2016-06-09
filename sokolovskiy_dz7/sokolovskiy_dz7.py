# открытие CSV нами пройдено не было, поэтому первая функция местами нагуглена
import csv
import random
def making_dictionary_from_csv(way): # открываем CSV файл и выводим словарь
    bigramms = open(way, encoding = 'utf-8')
    csvreader = csv.reader(bigramms, delimiter='\t', quotechar='|')
    bigramm_dictionary = {}
    for row in csvreader:
        bigramm_dictionary[row[0]] = row[1]
    bigramms.close()
    return bigramm_dictionary

def random_bigramm(dictionary): #выбираем из словаря случайную пару key + word
    keys_list = []
    for key in dictionary:
        keys_list.append(key)
    word1 = random.choice(keys_list)
    word2 = dictionary[word1]
    random_bigramm = [word1, word2]
    return random_bigramm


def giving_task_level_2(random_bigramm): # разгадываем слово. уровень 2
    notes = random_bigramm[1].split(' ')
    n = 0
    while n < len(random_bigramm[0]):
        n += 1
        one_note = random.choice(notes)
        print('\nПОДСКАЗКА', n,':', one_note)
        notes.remove(one_note)
        attempt = input('ВАШ ВАРИАНТ : ')
        if attempt == random_bigramm[0]:
            print('\nПОЗДРАВЛЯЮ, СЛОВО УГАДАНО!')
            break
        elif n == len(random_bigramm[0]) - 1:
            print('\nВНИМАНИЕ, ОСТАЛАСЬ ОДНА ПОПЫТКА!')
    if n == len(random_bigramm[0]) and attempt != random_bigramm[0]:
        print('\nУВЫ, ПОРАЖЕНИЕ. ОТВЕТ:', random_bigramm[0])

def giving_task_level_1(random_bigramm): #разгадываем слово. уровень 1
    print('\nКОЛИЧЕСТВО ПОПЫТОК: ', len(random_bigramm[0]))
    notes = random_bigramm[1].split(' ')
    n = 0
    while n < len(random_bigramm[0]):
        n += 1
        one_note = random.choice(notes)
        print('\nПОДСКАЗКА', n, ':', one_note)
        notes.remove(one_note)
        attempt = input('ВАШ ВАРИАНТ : ')
        if attempt == random_bigramm[0]:
            print('\nПОЗДРАВЛЯЮ, СЛОВО УГАДАНО!')
            break
    if n == len(random_bigramm[0]) and attempt != random_bigramm[0]:
        print('\nУВЫ, ПОРАЖЕНИЕ. ОТВЕТ:', random_bigramm[0])

def main():
    val = making_dictionary_from_csv('sokolovskiy_bigramms.csv')
    print('SOKOLOVSKIY MATVEY   GROUP:152    HOMEWORK 7     VARIANT 1')
    print('количество попыток угадать слово равно количеству букв в слове')
    print('предлагаю два уровня сложности:')
    print(' уровень 1 – количество попыток дано сразу')
    print(' уровень 2 – длина слова известна только когда остаётся одна попытка\n')
    level = (input('выберите уровень(введите 1 или 2): ', ))
    while True:
        val1 = random_bigramm(val)
        if level == '1':
            val2 = giving_task_level_1(val1)
        elif level == '2':
            val2 = giving_task_level_2(val1)
        else:
            print('\nУРОВЕНЬ НЕ ВЫБРАН. ПРИДЁТСЯ ПЕРЕЗАПУСКАТЬ ПРОГРАММУ')
            break
        for_exit = input('\nДЛЯ ЗАВЕРШЕНИЯ НАЖМИТЕ  SPACE И ENTER \nДЛЯ ПРОДОЛЖЕНИЯ ЧТО УГОДНО (И ENTER)')
        if for_exit == ' ':
            break

if __name__ ==  '__main__':
    main()
