import re
def reading_list(way):
    text = open(way, 'r', encoding = 'utf-8')
    text1 = text.read()
    text1 = text1.lower()
    text1 = text1.replace('\n', ' ')
    text1 = text1.replace('\t', ' ')
    for smth in range(0,10):
        text2 = text1.replace('  ', ' ')
    text_list = text2.split(' ')
    text.close()
    text_list1 = []
    for sym in text_list:
        sym = sym.strip('!.,?;:{}[]()<>:+_-"–=*/\ ' )
        if sym != '' or sym != ' ':
            text_list1.append(sym)
    return text_list1

def searching_forms(words):
    forms = []
    for element in words:
        word_bordered = '<'+element+'>' #в этом месте я предпринял все попытки заставить программу находить ТОЛЬКО правильные формы
        if re.search('<откр((((о(й|ют|е(шь|м|т))|ы((ть|л)\
|(вш((и(е|й|х|ми?))|(е(е|го|му?))|ую|ая))))(ся)?)|(((о(ю|\
(й|е)те))|(ыл(а|и|о)))(сь)?)|(ыв(шись)?))|((ыт(ы(й|е|х|ми?\
)|ая|о(й|е|го|му?)|ую))))>', word_bordered):
            if element not in forms:
                forms.append(element)
    return forms

def main():
    print('\nMATVEY SOKOLOVSKIY   GROUP:152   HOMEWORK 8   VARIANT:1\n')
    way = input('введите название текстового файла (после этого желательно скопировать): ')
    try:
        val = reading_list(way)
        val1 = searching_forms(val)
        print('формы глагола "открыть" встречающиеся в документе:\n')
        for element in val1:
            print(element)
    except FileNotFoundError:
        print('извините, файл не найден')

if __name__ == '__main__':
    main()
