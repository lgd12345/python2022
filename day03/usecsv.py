import csv
import re

# 파일을 연다. 함수로 만듬


def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

# ',', '' 이렇게 고치는 것 함수로 만듬


def switchcsv(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
    return listName
