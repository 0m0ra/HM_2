n0 = -1 #предположим, что предыдущий элемент = -1
l1 = 0 # текущая длина послед. повторяющихся
max_l = 0 # Искомая длина послед. повторяющихся
n = int(input())
while n != 0:
    if n == n0:
        l1 += 1
    else:
        n0 = n
        max_l = max(max_l, l1)
        l1 = 1
    n = int(input())
max_l = max(max_l, l1)
print(max_l)
