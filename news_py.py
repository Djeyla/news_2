import chardet

print('Результаты файла newsafr')
with open('newsafr.txt', 'r', encoding='utf-8') as f:
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

print('Результаты файла newscy')
with open('newscy.txt', 'rb') as f:
    data = f.read()
    result = chardet.detect(data)
    print(result)

with open('newscy.txt', 'r', encoding='KOI8-R') as f:
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

print('Результаты файла newsfr')
with open('newsfr.txt', 'rb') as f:
    data = f.read()
    result = chardet.detect(data)
    print(result)

with open('newsfr.txt', 'r', encoding='ISO-8859-5') as f:
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

print('Результаты файла newsit')

with open('newsit.txt', 'rb') as f:
    data = f.read()
    result = chardet.detect(data)
    print(result)

with open('newsit.txt', 'r', encoding='windows-1251') as f:
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
