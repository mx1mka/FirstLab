a = input("Введите список, разделенный пробелом: ").split()
for i in a:
    if i.isnumeric()==False:
        if i.startswith('-') == True:
            j=i[1:]
            if j.isnumeric()==True:
                continue
        print("Введённое вами значение не является целым, положительным числом.")
        exit()
a = tuple(map(int, a)) 
m = a[0]
if (m%2 == 0):
    fl=True
else:
    fl=False
for i in a:
    if (fl == False and i%2==0):
        m=i
        fl=True
    else:
       if (i<m and i%2==0):
          m=i

print(m)

