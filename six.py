p = 1 # задаем переменной значение 1. Она будет использоваться для расчета факториала
res = 1
N = int(input())
for i in range(N, 0, -1): # для i от N до 1
    p *= i # умножаем p на i для расчета факториала
    res += p # к результату прибавляем факториал
res /= p # результат делим на факториал
print(res) # по итогу получаем ответ на выражение вида 1 + 1/1! + 1/2! + ... + 1/N!
