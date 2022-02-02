import random
for i in range(1,10):
    #wylosowane liczby oznaczjącej miesiąc
    month=random.randint(1,32)
    #wylosowane roku
    year=random.randint(0,99)
    #ponowne wylosowane miesiąca jeżeli została wylosowana liczba nie oznaczająca miesiąca
    while month >12 and month<21:
        month=random.randint(1,32)
        #jeśli został wylosowany luty to liczna dzień jest losowany maksymalnie do 28
    if month== 2 or month==22:
        day=random.randint(1,28)
        #analogicznie dla miesięcy
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        day=random.randint(1,31)
    elif month==21 or month==23 or month==25 or month==27 or month==28 or month==30 or month==32:
        day=random.randint(1,31)
    else:
        day=random.randint(1,30)
        #wylosowane pozostałych liczb peselu
    p=str(random.randint(1000, 9999))
    #jeżeli liczby są jedno cyfrowe to dodawane jest 0
    if year<10:
        year="0"+str(year)
    if day<10:
        day="0"+str(day)
    if month<10:
        month="0"+str(month)
        #wygenerowanie 10 liczb peselu i stworzenie z niego listy
    s=(str(year)+str(month)+str(day)+p)
    s1=list(s)
    #wygenerowanie sumy kontrolnej
    for i in range(0, len(s1)):
        s1[i] = int(s1[i])
    s2=[1,3,7,9,1,3,7,9,1,3]
    suma=0
    for i in range(0, len(s1)):
        s1[i]=s1[i]*s2[i]
        if s1[i]>9:
            s1[i]=s1[i]%10
        suma=suma+s1[i]
    if suma>9:
        kont=10-(suma%10)
        if not suma%10:
            kont=0
    else:
        kont=10-suma
    s=s+str(kont)
    print(s)
    
    
