a = input("Введите список чисел, разделенных пробелом: ").split()
counter = 0
for i in a:
    if i.isnumeric()==False:
        if i.startswith('-') == True:
            j=i[1:]
            if j.isnumeric()==True:
                continue
        print("Введённое вами значение не является целым, положительным числом.")
        exit()

a = list(map(int, a))  
pa = a
for i in range(len(pa)):
    for j in range(i + 1, len(pa)):
        if pa[i] == pa[j]:
            counter += 1
            pa.pop(j)
            break 
                
print('Количество пар элементов, равыных друг другу =', counter)