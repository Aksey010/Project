birthyear=0
birthday=0
while birthyear!=1799:
    print('В каком году родился Пушкин? Ответ:')
    birthyear=int(input())
    if birthyear==1799:
        print('Верный год')
        print('А в каком дне?')
        while birthday!=6:
            birthday = int(input())
            if birthday == 6:
                print('Верно')