import os
import re

def walking():
    all_roots = []
    for root, dirs, files in os.walk('.'):
        all_roots.append(root)
    return all_roots

def find_deepest_root(roots):
    deepest = 0
    for root in roots:
        how_many = re.findall('[\/]', root)
        if deepest < len(how_many):
            deepest = len(how_many)
    return deepest

def main():
    val = walking()
    val1 = find_deepest_root(val)
    print('максимальная глубина папки:', val1)

if __name__ ==  '__main__':
    main()
