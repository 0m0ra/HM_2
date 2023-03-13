a = int(input())

# вспомогательный bool
isZero = False
for i in range(a): #наш цикл
    A = int(input()) #переменная
    if A == 0:  #проверка
        isZero = True
if isZero:
    print("YES")
else:
     print("NO")