#30. Количество чисел, равных минимальному
def kek(sf): # имя функции sf- локальная переменная
    try:
        err=0
        minimum = None
        f=open(sf,"r")
        s=None #элемент последовательности
        for str in f: 
            try:
                for sx in [sx for s1 in str.split(' ') for s2 in s1.split('\t') for s3 in s2.split('\n') for sx in s3.split(',') if sx!='']: #split  - функция разбиения
                    try:
                        if(s == None): #первый проход
                            s=int(sx) # отделяем целочисленный тип
                            minimum=s
                            num=1
                            continue
                        s = int(sx)
                        if(s<minimum):
                            num=0 # количество min эл-в
                            minimum=s
                        if(s==minimum):
                            num+=1 #счётчик +1
                    except: # исключения try
                        print("ignored",sx)
            except ValueError:
                err=-2 
                print("Bad value:", str)
        f.close()
        return err,minimum, num
    except FileNotFoundError:
        err=-3
        print("Can't open file")
        return err,minimum, num
err,minimum,num=kek("in.txt") #запускает функцию
if(err<0):
    print("Error")
else :
    print("Количество чисел, равных минимальному =",num)
    print("Минимальный элемент равен",minimum)
