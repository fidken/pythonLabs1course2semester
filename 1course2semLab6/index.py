import csv
import random

# show([string outputType, int count])
# АРГУМЕНТЫ outputType
# top - с начала (верха) таблицы (ПО УМОЛЧАНИЮ)
# bottom - с конца (низа) таблицы
# random - любые строки полей

# АРГУМЕНТЫ count
# 5 - (ПО УМОЛЧАНИЮ)
# любое число

with open('Titanic.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = [row for row in csvreader]
    title = rows[0]
    rows = rows[1:]


def show(count=5, outputType="top"):
    n = 0
    match outputType:
        case "top":
            print(title)
            for row in rows:
                if n < count:
                    print(row)
                    n += 1
                else:
                    break
        case "bottom":
            print(title)
            for row in reversed(rows):
                if n < count:
                    print(row)
                    n += 1
                else:
                    break
        case "random":
            print(title)
            random.shuffle(rows)
            for row in rows:
                if n < count:
                    print(row)
                    n += 1
                else:
                    break


# show(5, "random")


def columnRowCount():
    columnValues = []
    for columnNumber in range(len(title)):
        for row in rows:
            if row[columnNumber].strip() != '':
                columnValues.append(row[columnNumber])
        print(title[columnNumber])
        print("Колличество значений в столбце: " + str(len(columnValues)))
        columnValues = []

columnRowCount()