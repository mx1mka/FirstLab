spisok = "Год Обезьяны", "Год Петуха", "Год Собаки", "Год Свиньи", "Год Крысы", "Год Быка", "Год Тигра", "Год Кролика", "Год Дракона", "Год Змеи", "Год Лошади", "Год Козы"
a = 1
while True:
    a = input("Введите число: ")
    if (a == "0"):
        break

    if a.isdigit() == True:
        year = int(a)
        print(spisok[year % 12])
    else:
        print("Введённое вами значение не является целым, положительным числом.")