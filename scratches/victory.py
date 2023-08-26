true_answ=0
false_answ=0
answer='да'
while answer =='да':
    print('В каком году родился Илон Маск?')
    Elon=int(input())                                      #1971
    if Elon==1971:
        print('Верно')
        true_answ +=1
    else: print('Неверно')
    print('В каком году родился Райан Гослинг?')
    Gosling=int(input())                                   #1980
    if Gosling==1980:
        print('Верно')
        true_answ += 1
    else: print('Неверно')
    print('В каком году родился Дуэйн Джонсон?')
    Dwayne=int(input())                                    #1972
    if Dwayne==1972:
        print('Верно')
        true_answ += 1
    else: print('Неверно')
    print('В каком году родился Джонни Депп?')
    Johny=int(input())                                    #1963
    if Johny==1963:
        print('Верно')
        true_answ += 1
    else: print('Неверно')
    print('В каком году родилась Алла Пугачева?')
    Alla=int(input())                                      #1949
    if Alla==1949:
        print('Верно')
        true_answ += 1
    else: print('Неверно')
    print('Количество правильных ответов:',true_answ)
    print('Количество неправильных ответов:',false_answ)
    print('Процент правильных ответов:', true_answ*100/5)
    print('Процент неправильных ответов:', false_answ*100/5)
    print('Вы хотите попробовать ещё раз? (да, нет)')
    answer=str(input())