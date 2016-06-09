#сначала регулярное выражение было составлено иначе, но потом я решил,
#что проще перебрать падежные формы, нежели искать обходные пути
import re
def reading_str(way):
    text = open(way, 'r', encoding='utf-8')
    text_str = text.read()
    text.close
    
    return text_str

def several_resub(text):
    regex_upper = 'Комар(ы|ы́|у|(а((ми?)|х))|(о(м|в))|е)?[\.,\[\t\n -–"«»:;!?]'
    regex_lower = '([ \t«\n])комар(ы|ы́|у|(а((ми?)|х)?)|(о(м|в))|е)?[\.,\[\t\n -–"«»:;!?]'
    falsch = re.sub(regex_upper, r'Cлон\1',text)
    falsch = re.sub(regex_lower, r'\1cлон\2', falsch)
    return falsch

def writing_into_txt(what_to_write, where_to_write):
    doc = open(where_to_write, 'w', encoding='utf-8')
    doc.write(what_to_write)
    doc.close()

def main():
    val = reading_str('komar.txt')
    val1 = several_resub(val)
    val2 = writing_into_txt(val1, 'slon.txt')
    print('исправленный текст статьи в документе "slon.txt"')
    
if __name__ ==  '__main__':
    main()
