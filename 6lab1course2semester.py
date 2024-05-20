import numpy as np
import time
from scipy.stats import multivariate_normal
#1
readMatrix = np.loadtxt('matrix.txt', delimiter=',')

totalSum = np.sum(readMatrix)

maxElement = np.max(readMatrix)
minElement = np.min(readMatrix)

print("Матрица:")
print(readMatrix)
print("Сумма всех элементов:", totalSum)
print("Максимальный элемент:", maxElement)
print("Минимальный элемент:", minElement)

#2
x = np.array([2, 2, 2, 3, 3, 3, 5])

numbers = []
counts = []

uniqueValues, valueCounts = np.unique(x, return_counts=True)

numbers.extend(uniqueValues)
counts.extend(valueCounts)

numbers = np.array(numbers)
counts = np.array(counts)

print()
print("Кортеж уникальных чисел:", numbers)
print("Кортеж повторений уникальных чисел соответственно:",counts)

#3
array = np.random.randint(0, 20, size=(10, 4))

minValue = np.min(array)
maxValue = np.max(array)
meanValue = np.mean(array)
stdDeviation = np.std(array)

firstFiveRows = array[:5]

print()
print("Минимальное значение:", minValue)
print("Максимальное значение:", maxValue)
print("Среднее значение:", meanValue)
print("Стандартное отклонение:", stdDeviation)
print("Первые 5 строк:")
print(firstFiveRows)

#4
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

zeroIndices = np.where(x[:-1] == 0)
zeroIndices = zeroIndices[0]

maxValue = np.max(x[zeroIndices + 1])

print()
print("Максимальный элемент в векторе x среди элементов, перед которыми стоит нулевой:", maxValue)

#5
import numpy as np

def logpdf_custom(X, m, C):
    D = len(m)
    normСoeff = -0.5 * D * np.log(2 * np.pi)
    sign, logdet = np.linalg.slogdet(C) #вычисление знака и логарифма определителя матрицы C
    if sign != 1:
        return -np.inf
    CInverted = np.linalg.inv(C) #вычисление обратной матрицы для матрицы С
    diff = X - m
    exponent = -0.5 * np.sum(diff @ CInverted * diff, axis=1) #вычисление экспоненты для каждой строки массива diff с иcпользованием обратной матрицы
    return normСoeff + 0.5 * logdet + exponent

N, D = 1000, 3
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D) #генерирует случайные значения
C = np.dot(C, C.T) #обеспечение положительной определенности
startTime = time.time() #измерение скорости
logpdf_custom(X, m, C)
customDuration = time.time() - startTime

startTime = time.time() #измерение скорости
multivariate_normal.logpdf(X, m, C)
scipyDuration = time.time() - startTime

customResult = logpdf_custom(X, m, C)
scipyResult = multivariate_normal.logpdf(X, m, C)

print()
print(f"Скорость работы пользовательской функции: {customDuration:.6f} секунд")
print(f"Скорость работы функции из scipy: {scipyDuration:.6f} секунд")
print("Максимальное отклонение результатов:", np.max(np.abs(customResult - scipyResult)))


#6
a = np.arange(16).reshape(4, 4)
print()
print("Исходный массив:")
print(a)

# Поменять местами строки 1 и 3
a[[1, 3]] = a[[3, 1]]

print("Массив после замены строк 1 и 3:")
print(a)

#7
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

speciesColumn = iris[:, 4]

uniqueSpecies, counts = np.unique(speciesColumn, return_counts=True) #return_counts включает опцию возвращения колличества повторений уникальных значений

print()
for species, count in zip(uniqueSpecies, counts):
    print(f'{species.decode("utf-8")}: {count}') #декодирование species из-за записи строки в байтовом формате

#8
x = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
nonzeroIndices = np.nonzero(x)[0]

print()
print("Индексы ненулевых элементов:", nonzeroIndices)
