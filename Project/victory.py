import random

days={'09':'девятое',
      '12':'двенадцатое',
      '02':'второе',
      "28":"двадцатьвосьмое",
      "25":"двадцатьпятое",
      "15":"пятнадцатое",
      "14":"четырнадцатое",
      "18":"восемнадцатое"}
months={"10":"октябрь",
        "06":"июнь",
        "11":"ноябрь",
        "05":"май",
        "04":"апрель",
        "08":"август",
        "03":"март",
        "12":"декабрь"}

t=random.randint(0,100)
true_answ=0
false_answ=0
answer='да'
while answer =='да':
    a=["Пабло Пикассо","Илон Маск","Райан Гослинг","Дуэйн Джонсон", "Джонни Депп","Алла Пугачёва","Леонардо да Винчи"
       ,"Наполеон Бонапарт","Альберт Эйнштейн","Иосиф Сталин"]
    data="25.10.1881","28.06.1971", "12.11.1980", "02.05.1972", "09.06.1963","15.04.1949","15.04.1452", "15.08.1769","14.03.1879","18.12.1878"
    random.seed(t)
    b=random.sample(a,5)
    random.seed(t)
    d=random.sample(data,5)
    print(b)
    print(d)
    for i in range(5):
        print(f"Когда родился(-ась){b[i]}")
        c=input()
        if c==d[i]:
            print("Верно")
            true_answ+=1
        else:
            print("Неверно")
            l=str(d[i])
            day= l.split(".")[0]
            month=l.split(".")[1]
            year=l.split(".")[2]
            print(days[day],months[month],year,"года")
            false_answ+=1




    print('Количество правильных ответов:',true_answ)
    print('Количество неправильных ответов:',false_answ)
    print('Процент правильных ответов:', true_answ*100/5)
    print('Процент неправильных ответов:', false_answ*100/5)
    print('Вы хотите попробовать ещё раз? (да, нет)')
    answer=str(input())