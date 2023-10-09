st = input("Введите строку: ")

pos1 = 0
pos2 = 0
index = 0
kol = 0

pst=st

pst = pst.replace(',', '')
pst = pst.replace('.', '')
pst = pst.replace(':', '')
pst = pst.replace('?', '')
pst = pst.replace('!', '')    
for letter in pst:    
    index += 1
    if (letter == ' '): 
        pos2 = index 
        if ((pos2 - pos1) % 2 != 0):
            kol +=1
        pos1 = pos2
    

pst = pst.replace(' ', '')
index += 1
pos2=index 
if ((pos2 - pos1) % 2 != 0):
    kol += 1         

print('Количество слов чётной длины =', kol)

while (len(pst) !=0):
    letter=pst[0] 
    print('Количество вхождений буквы', letter, '=', pst.count(letter))
    pst = pst.replace(letter, '')
        