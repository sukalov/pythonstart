import re
def reading_str(way):
    text = open(way, 'r', encoding='utf-8')
    text_str = text.read()
    text.close
    return text_str

def writing_into_txt(what_to_write, where_to_write):
    doc = open(where_to_write, 'w', encoding='utf-8')
    for part in what_to_write:
        doc.write(part + '\n')
    doc.close()

def main():
    val = reading_str('rur.txt')
    val1 = re.findall('(?:не )?(?:[^ .,:;?!"]*л(?:ъ|ся)|могъ) [^.,:;?!"]{0,15}[^ .,:;?!"]*ть(?:ся)?', val)
    val2 = writing_into_txt(val1, 'sokolovskiy_result.txt')

if __name__ ==  '__main__':
    main()
