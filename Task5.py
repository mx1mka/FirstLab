list1 = ['Крышка для топливного бака.', 20, 10]
list2 = ['Основной элемент дисковой тормозной системы.', 70, 15]
list3 = ['Передние/задние фары', 40, 10]
list4 = ['Устройство для снижения шума от выходящих в атмосферу газов', 50, 10]

sp = {'Крышка': list1, 'Тормозные диски': list2, 'Фары': list3, 'Глушитель': list4}
def get_key (sp, val):
    for i,j in sp.items():
        if (j == val):
            return i
        
         

while True:
    print('1) Просмотр описания.')
    print('2) Просмотр цены.')
    print('3) Просмотр количества')
    print('4) Просмотр всей информации')
    print('5) Покупка')
    print('6) ВЫХОД.')
    print()
    ch=input('Выберите нужное вам действие: ')
    
    if (ch=='1'):
        for i in sp.values():
            print('Название:', get_key(sp, i))
            print('Описание:', i[0])
            print()

    if (ch=='2'):
        for i in sp.values():
            print('Название:', get_key(sp, i))
            print('Цена:', i[1])
            print()

    if (ch=='3'):
        for i in sp.values():
            print('Название:', get_key(sp, i))
            print('Количество:', i[2])
            print()        

    if (ch=='4'):
        for i in sp.values():
            print('Название:', get_key(sp, i))
            print('Описание:', i[0])
            print('Цена:', i[1])
            print('Количество:', i[2])
            print()

    if (ch=='5'):
        name = input("Введите название продукции: ")
        if (name!='n'):
           kol = input("Введите количество продукции: ")
           if kol.isdigit() == False:
               print('Введёное вами значение не является целым, положительным числом.')
           else:
            kol=int(kol)
            if (sp.get(name) == None):
                print('Введённого вами продукта нету в наличии.')
            else:
                i = sp.get(name)
                if (i[2]<kol):
                    print('Количество нужного вам товара превышает его количество у нас на складе.')
                else:
                    i[2] -= kol
                    print('Успешная покупка!')
    
    if (ch=='6'):
        print('До свидания!')
        exit()
                
