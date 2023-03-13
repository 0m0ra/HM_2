number = int(input()) # вводим первое значение number            
max = number # приравниваем max к первому значению number
max_equal = 1 # используем в качестве счетчика и пока приравниваем к 1
while number != 0: # пока number не равно 0
    number = int(input()) # вводим значение number
    if (number == max): # если number равно max, то приравниваем max к max_equal
        max = max_equal 
    elif (max < number): # а если max меньше number, то приравниваем max к number и значение счетчика сбрасываем до 1
         max = number
         max_equal = 1
print(max_equal) # выводим количество
