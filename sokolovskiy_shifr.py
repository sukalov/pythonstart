while True:
    stroka = input('впишите строку (чтобы завершить нажмите ENTER): ')
    if stroka != '':
        alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяаАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА  '
        alf = list(alf)
        stroka2 = ''
        stroka2 = list(stroka2)
        stroka3 = ''
        simvol_num = 0    
        while simvol_num != len(stroka):
            n = 0
            for symbol in alf:
                if stroka[simvol_num] == symbol:
                    stroka2.append(alf[n+1])
                    break
                else:
                    n += 1
            simvol_num += 1
        for sym in stroka2:
            stroka3 = stroka3 + sym
        print('зашифрованное слово (каждая буква следующая в алфавите): ', stroka3)
    else:
        break
