import re
def reading_str(way):
    text = open(way, 'r', encoding = 'utf-8')
    text_str = text.read()
    text.close
    return text_str

def searching_smth(text):
    regexp = 'href="/wiki/%D0%A1%D1%82%D0%BE%D0%BB%D0%B8%D1%86%D0%B0" title="Столица"(.*\n.*)title="(.*)">(.*)</a>'
    res = re.search(regexp, text)
    try:
        capital = res.group(3)
    except AttributeError: # в статье про Ватикан столица не являлась ссылкой и была записана иначе
        regexp2 = 'href="/wiki/%D0%A1%D1%82%D0%BE%D0%BB%D0%B8%D1%86%D0%B0" title="Столица"(.*)\n<td>(.*)</td>'
        res2 = re.search(regexp2, text)
        capital = res2.group(2)
    return capital
    
def writing_into_txt(what_to_write, where_to_write):
    doc = open(where_to_write, 'a', encoding='utf-8')
    doc.write(what_to_write + '\n')
    
def main():
    val = reading_str('ovosh.html')
    val1 = searching_smth(val)
    val3 = writing_into_txt(val1, 'sokolovskiy_result.txt')

if __name__ ==  '__main__':
    main()
