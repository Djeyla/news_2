import json
from pprint import pprint


def find_words():
    words = {}
    for i in f:
        i = i.split()
        for x in i:
            if len(x) > 6:
                k = i.count(x)
                words[x] = k
    words = sorted(words.items(), key=lambda x: x[1], reverse=True)

    q = 1
    for z in words:
        if q > 5:
            break
        q = q + 1
        print(str(z))


print('Результаты файла newsafr')

with open('newsafr.json', 'r', encoding='utf-8') as f:
    find_words()


print('Результаты файла newscy')

with open('newscy.json', 'r', encoding='KOI8-R') as f:
    find_words()

print('Результаты файла newsfr')

with open('newsfr.json', 'r', encoding='ISO-8859-5') as f:
    find_words()

print('Результаты файла newsit')

with open('newsit.json', 'r', encoding='windows-1251') as f:
    find_words()
