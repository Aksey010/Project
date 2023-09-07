a=input('Введие числа через запятую')
a=a.split(',')
lst=[]
for number in a:
    if a.count(number) ==1:
        lst.append(number)
print(lst)