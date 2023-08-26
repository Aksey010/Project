print('В каком году родился Пушкин? Ответ:')
birthyear=int(input())
if birthyear==1799:
    print('Верный год')
    print('А в каком дне?')
    birthday = int(input())
    if birthday == 6:
        print('Верно')
    else:
        print('Неверно')
else:print('Неверно')


