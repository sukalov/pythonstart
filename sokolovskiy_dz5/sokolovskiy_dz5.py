try:
    text = open('text.txt', 'r', encoding = "utf-8")
    da = 1
except:
    print("file isn't found")
    da = 0
if da == 1:
    print("name of the file: ", text.name)
    lines = 0
    textstr = ''
    for line in text:
        lines += 1
        textstr = textstr + ' ' + line
    slova = textstr.split(' ')
    text.close()
    print()
    print('the number of lines: ', lines)
    print('the number of words: ', len(slova))
    print()
    print('the average number of words in a line: ', round(len(slova)/lines, 2))
    
