# лабораторная4
# задание1
# n = int(input("Колличество элементов?: "))
# mass = []
# for i in range(n):
#     mass.append(input(f'Введи переменную {i+1} '))
# print(len(set(mass)))

# задание2
# n1 = int(input("Количество элементов множества1?: "))
# n2 = int(input("Количество элементов множества2?: "))
# mass1 = set()
# mass2 = set()
#
# for i in range(n1):
#     mass1.add(input(f'Введите переменную {i+1} для множества1: '))
#
# for i in range(n2):
#     mass2.add(input(f'Введите переменную {i+1} для множества2: '))
#
# print("Является ли множество1 подмножеством множества2?: " + str(mass1 <= mass2))

# задание3

# n = int(input("Колличество ходов?:"))
# mass = set()
# city = ""
# for i in range(n):
#     if (i+1) % 2 == 0:
#         city = str(input("Ход Саши! Какой город?:"))
#         print("REPEAT") if city in mass else print("OK")
#         mass.add(city)
#     else:
#         city = str(input("Ход Маши! Какой город?:"))
#         print("REPEAT") if city in mass else print("OK")
#         mass.add(city)
# print(mass)

# задание4

# inputString = "lorem ipsum dolor amet lorem"
# words = inputString.split()
# wordСount = {}
# wordsMass = set()
# result = []
# for word in words:
#     if word in wordsMass:
#         result.append(str(wordСount[word]))
#     else:
#         result.append('0')
#     wordsMass.add(word)
#     wordСount[word] = wordСount.get(word, 0) + 1
#
# print(' '.join(result))

# задание5

# def count_units_purchased(n):
#     purchases = {}
#     for _ in range(n):
#         entry = input().split()
#         customer_id, item, quantity = int(entry[0]), entry[1], int(entry[2])
#
#         if customer_id in purchases:
#             purchases[customer_id].append((item, quantity))
#         else:
#             purchases[customer_id] = [(item, quantity)]
#
#     for customer_id, items in purchases.items():
#         print(f"Customer {customer_id} purchased:")
#         for item, quantity in items:
#             print(f"{quantity} units of {item}")
#
#
# n = int(input("Enter the number of entries: "))
# count_units_purchased(n)
#

# задание6

def count_words_frequency(text):
    words = text.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, _ in sorted_words:
        print(word)


text = input("Enter the text: ")
count_words_frequency(text)
