def Prime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False 
    return True

count = 0 
rez = []
maxdel = []
maxrez = 0
for i in range(631632, 684935):
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            if Prime(d):
                if Prime(int(i // d)):
                    if int(i // d) - d > maxrez:
                        maxrez = int(i // d) - d
                        maxdel = [d, int(i // d)]
                        rez.append(i)
print(len(rez), rez[0], maxrez, maxdel)




#with open ("26-j9.txt") as f:
#    a, b = [int(elem) for elem in f.readline()]
#    value = []
#    for line in f:
#        value.append(int(line))
#    value.sort()
#    summ = 0
#    i = 0
#    while summ <= a:
#        summ += value[i]
#        i += 1
#    print(summ, i)




#with open ("27-8b.txt") as f:
#    value = []
#    n = int(f.readline())
#    for line in f:
#        value.append(int(line))
#    minindex = value.index(min(value))
#    mini = value.pop(minindex)
#    minindex2 = value.index(min(value))
#    mini2 = value.pop(minindex2)
#    if minindex2 - minindex <= 5:
#        minindex2 = value.index(min(value))
#        mini2 = value.pop(minindex2)
#    print(minindex, mini, minindex2, mini2, mini ** 2 + mini2 ** 2)





#for m in range(2, 100, 2):
#    for n in range(3, 100, 2):
#        num = (2 ** m) * (7 ** n)
#        if num >= 100000000 and num <= 300000000:
#            print(num, m + n, m, n)




#dif1, dif2, dif3, dif4 = [], [], [], []
#sum, mini = 0, 1000000000
#with open ("13b.txt") as f:
#    n = f.readline()
#    for line in f:
#        a, b  = [int(elem) for elem in line.split()]
#        sum += min(a, b)
#        if max(a, b) - min(a, b) == 1:
#            dif1.append([min(a,b), max(a,b)])
#        if max(a, b) - min(a, b) == 2:
#            dif2.append([min(a,b), max(a,b)])
#        if max(a, b) - min(a, b) == 3:
#            dif3.append([min(a,b), max(a,b)])
#        if max(a, b) - min(a, b) == 4:
#            dif4.append([min(a,b), max(a,b)])
#    if sum % 5 == 4:
#        for i in dif1:
#            if sum - i[0] + i[1] < mini:
#                mini = sum - i[0] + i[1]
#    if sum % 5 == 3:
#        for i in dif2:
#            if sum - i[0] + i[1] < mini:
#                mini = sum - i[0] + i[1]
#    if sum % 5 == 2:
#        for i in dif3:
#            if sum - i[0] + i[1] < mini:
#                mini = sum - i[0] + i[1]
#    if sum % 5 == 1:
#        for i in dif4:
#            if sum - i[0] + i[1] < mini:
#                mini = sum - i[0] + i[1]
#    print(sum)
#    print(mini)
#    #print(dif1, dif2, dif3, dif4, sep = '\n')
        


##27
#min, s = 1000000000, []
#with open("27B.txt") as f:
#    n = int(f.readline())
#    for line in f:
#        s.append(int(line))
#    s.sort()
#    for a in range(50):
#        for b in range(50):
#            for c in range(50):
#                if s[a] + s[b] + s[c] < min and (s[a] + s[b] + s[c]) % 3 == 0 and s[a] != s[b] and s[a] != s[c] and s[b] != s[c]:
#                    min = s[a] + s[b] + s[c]
#print(min)


#def delitel(a):
#    flag = False
#    for i in range(2, a // 2):
#        if a % i == 0:
#            flag = True
#            #print(i)
#            if a % 13 != 0:
#                return False
#                break
#    return flag


##print(delitel(208))
#count = 0
#i = 350300
#while count <= 6:
#    i += 1
#    if delitel(i):
#        count += 1
#        print(i)


##Не рабочая 27
#ChetMax, ChetMin = 100000, 1000000
#sumMax, sumMin = 0, 0
#with open ("27-B__5nim.txt") as f:
#    n = int(f.readline())
#    for line in f:
#        a, b = [int(elem) for elem in line.split()]
#        if b % 2 != 0:
#            sumMax += max(a, b)
#            sumMin += min(a, b)
#            if max(a, b) % 2 != 0:
#                if ChetMax > a + b:
#                    ChetMax = a + b
#                    ChetMaxValue = max(a, b)
#            if min(a, b) % 2 != 0:
#                if ChetMin > a + b:
#                    ChetMin = a + b
#                    ChetMinValue = min(a, b)
#    res = sumMax + sumMin
#    while sumMax % 2 != 0 and sumMin % 2 == 0:
#        if sumMax % 2 != 0:
#            sumMax
#        else:
#            res -= ChetMax
#        if sumMin % 2 == 0:
#            continue
#        else:
#            res -= ChetMin
#print(res)





##27 с тремя парами
#def nechet(a, b):
#    return (a - b) % 2 != 0

#group1, group2, group3 = 0, 0, 0 
#arrg1, arrg1 = [], [] 
#maxi, mini = 0, 100000
#dif = 100000
#with open("14.txt") as f:
#    n = int(f.readline())
#    for line in f:
#        a, b, c = [int(elem) for elem in line.split()]
#        maxi = max(a, b, c)
#        mini = min(a, b, c) 
#        mid = a + b + c - mini - maxi
#        group3 += maxi
#        dif = maxi - mid if nechet(maxi, mid) and ((maxi - mid) < dif) else dif
#        dif = maxi - mini if nechet(maxi, mini) and ((maxi - mini) < dif) else dif
#        dif = mid - mini if nechet(mid, mini) and ((mid - mini) < dif) else dif
#        group1 += mid
#        group2 += mini
#    if group1 % 2 + group2 % 2 == 1:
#        print(group1, group2, group3)
#    else:
#        print(group1, group2, group3 - dif)

        



#def f(n):
#    if n < 14:
#        return 0
#    elif n == 14:
#        return 1
#    elif n % 2 == 0:
#        return f(n // 2) + f(n - 1)
#    else:
#        return f(n - 1)
#print(f(63))



#def f(n):
#    if n < 14:
#        return 0
#    elif n == 14:
#        return 1
#    else:
#        return f(n // 2) + f(n - 1)
#print(f(63))


#for i in range(700459, 730463):
#    if list(str(hex(i)))[2:][0] == "b" and list(str(hex(i)))[2:][-1] == "b" and i % 7 != 0:
#        res = i
#print(res)

##25 статград 4
#def isPrime(n):
#    if n % 2 == 0:
#        return n == 2
#    d = 3
#    while d * d <= n and n % d != 0:
#        d += 2
#    return d * d > n

#deli, count, min = [], 0, 1000000
#for i in range(10001, 50001):
#    j = 2
#    while j ** 2 <= i:
#        if i % j == 0:
#            if isPrime(j):
#                deli.append(j)
#            if isPrime(i // j) and j ** 2 != i:  
#                deli.append(i // j)
#        j += 1
#    if len(deli) == 3:
#        count += 1
#        if i < min:
#            min = i
#    deli = []
#print(count, min)



#def f(x, A):
#    return ((not(x%A==0 and x%6!=0))<=(x%3!=0))
#flag = True
#for A in range(1, 10000):
#    for x in range(1, 10000):
#        if not f(x, A):
#            flag = False
#            break
#    if flag:
#        print(A, x)
#    flag = True


#import time

#start_time = time.time()
#import math
#def simple(n):
#    for d in range(2, round(math.sqrt(n)+1)):
#        if n % d == 0:
#            return False
#            break
#    return True
#print(simple(99971))
#print("--- %s seconds ---" % (time.time() - start_time))

#start_time1 = time.time()
#def simple1(x):
#    if x <= 1: return False
#    d = 2
#    while d*d <= x:
#        if x % d == 0:
#            return False
#        d += 1
#    return True
#print(simple(99971))
#print("--- %s seconds ---" % (time.time() - start_time1))

#def isPrime(n):
#    if n % 2 == 0:
#        return n == 2
#    d = 3
#    while d * d <= n and n % d != 0:
#        d += 2
#    return d * d > n

#deli, res = [], {}
#count, mini = 0, 1000000
#for i in range(478392, 502440):
#    flag = True
#    j = 2
#    while (j ** 2 <= i and flag):
#        if i % j == 0:
#            if isPrime(j) and isPrime(i // j) and j ** 2 != i:
#                deli.append(j)
#                deli.append(i // j)
#            else:
#                flag = False
#        j += 1
#    if len(deli) == 2 and flag:
#        count += 1
#        if deli[1] - deli[0] < mini:
#            mini = deli[1] - deli[0]
#            minires = [i, *deli, deli[1] - deli[0]]
#    deli = []
#print(count, minires)



#a=[]
#for i in range(300000, 333001):
#    for j in range(1, i//2+1):
#        if i%j==0:
#            a.append(j)
#    if len(a)>2:
#        break
#    if len(a)==2:
#        print(a, i)
#        a=[]


#def CC(num, base):
#    res = ""
#    while num > 0:
#        res = str(num % base) + res
#        num //= base
#    return res
#num = 729 ** 7 + 3 ** 16 - 18
#print(CC(num, 9).count("0"))


#for i in range(int((106000000 // 2) ** 0.5), int((107000000 // 2) ** 0.5)):
#    deli = []
#    for tmp in range(1, i +     1):
#        if i % tmp == 0:
#            deli.append(tmp)
#            if len(deli) > 2:
#                break
#    if len(deli) == 2:
#        print(deli[1] ** 2 * 2)


#def f(n):
#    if n < 2:
#        return 0
#    if n == 2:
#        return 1
#    else:
#        return f(n - 1) + f(n - 3) + f(n // 3)
#print(f(22))


#def f(n):
#    if n<10:
#        return n
#    if n>10 and n%10==0:
#        return f(n%5)+1
#    if n>10 and n%10!=0:
#        return n*f(n-1)
#def g(n):
#    if n>=21:
#        return n*n+n+3
#    if n%2==0 and n<21:
#        return 2*g(n-2)*g(n-4)
#    if n%2!=0 and n<21:
#        return 2*g(n-1)*g(n-3)
#print(sum(map(int, str(f(g(f(g(22))))))))


#with open("18na100.txt") as f:                                  
#    arr, maxi, count, summ = [], 0, 0, 0                    
#    arr = f.read().replace(',', '.').splitlines()              
#    for i in range(len(arr)-1):                                
#        if abs((float(arr[i]) - float(arr[i+1])) <= 8):         
#            if summ == 0:
#                summ = float(arr[i]) + float(arr[i+1]) 
#            else:
#                summ += float(arr[i+1])
#            if summ > maxi:
#                maxi = summ
#                count = i
#        else:                                                   
#            summ =  0                                           
#print(maxi, count) 


#arr = []
#with open ("24.txt") as f:
#    s = f.read()
#    for i in range(len(s) - 2):
#        if s[i] == s[i+1]:
#            arr.append(s[i+2])
#    print(dict((i, arr.count(i)) for i in arr))


##num = ((66 + (6 ** 2019)) * 6 ** 2019) + 66 + (6 ** 6)
#num = 66 * (6 ** 2019 + 1) + 6 ** 6 + 6 ** 4038 
#rez = ""
#while num > 0:
#    rez = str(num % 6) + rez
#    num //= 6
#print(rez)
#rez2 = 0
#for i in list(rez):
#    rez2 += int(i)
#print(rez2) 


#s = "1" + "0" * 75
#while "10" in s or "1" in s:
#    if ("10") in s:
#        s = s.replace("10", "001", 1)
#    else:
#        s = s.replace("1", "00", 1)
#print(s.count("0"))


#def f(x, y, z, w):
#    return ((x <= y) == (z <= w)) or (x and w)

#for i in range(16):
#    mask = []
#    tmp = i
#    for j in range(4):
#        mask.append(tmp % 2)
#        tmp //= 2
#    for j in reversed(range(4)):
#        print(mask[j], end = '')
#    print('', int (f(mask[3],mask[2],mask[1],mask[0])))


#with open ("input1.txt") as f:
#    a = int(f.readline())
#    b = int(f.readline())
#    print(a + b)



#dump, queue = [], []      
#count, ans, sv8, sv2, sv4 = 0, 0, 0, 0, 0
#with open ("B") as f:
#    n = int(f.readline())
#    for i in range(6):
#        queue.append(int(f.readline()))
#    for i in range(6, n):
#        x = int(f.readline())
#        if x % 185 == 0:
#            ans += count
#        elif x % 37 == 0:
#            ans += sv185 + sv5
#        elif x % 5 == 0:
#            ans += sv185 + sv37
#        if (queue[0] % 185) == 0:
#            sv185 += 1
#        elif x % 37 == 0:
#            sv37 += 1
#        elif x % 5 == 0:
#            sv37 += 1
#        count += 1
#        queue.append(x)
#        dump.append(queue.pop(0))
#print(ans)
#Ответ: 246886329

##27
#dump, queue = [], []      
#count, ans, sv185, sv37, sv5 = 0, 0, 0, 0, 0
#with open ("B") as f:
#    n = int(f.readline())
#    for i in range(6):
#        queue.append(int(f.readline()))
#    for i in range(6, n):
#        x = int(f.readline())
#        if x % 185 == 0:
#            ans += count
#        elif x % 37 == 0:
#            ans += sv185 + sv5
#        elif x % 5 == 0:
#            ans += sv185 + sv37
#        if (queue[0] % 185) == 0:
#            sv185 += 1
#        elif x % 37 == 0:
#            sv37 += 1
#        elif x % 5 == 0:
#            sv37 += 1
#        count += 1
#        queue.append(x)
#        dump.append(queue.pop(0))
#print(ans)
#Ответ: 246886329

##27
#dump, queue = [], []      
#count, ans, sv107 = 0, 0, 0
#with open ("B") as f:
#    n = int(f.readline())
#    for i in range(4):
#        queue.append(int(f.readline()))
#    for i in range(4, n):
#        x = int(f.readline())
#        if x % 107 == 0:
#            ans += count
#        else:
#            ans += sv107
#        if (queue[0] % 107) == 0:
#            sv107 += 1
#            count += 1
#        else:
#            count += 1
#        queue.append(x)
#        dump.append(queue.pop(0))
#print(ans)
##ответ: 94639752




#26
#summ, count, maxi, i, arr = 0, 0, 0, 0, []                  #
#with open ("27881.txt") as f:                               #читаем файл  
#    n, m = [int(elem) for elem in f.readline().split()]     #читаем первые два значения из файла 
#    for line in f:                                          #добавляем каждую линию в список
#        arr.append(int(line))                               #добавляем каждую линию в список
#    arr.sort()                                              #соритирем список от меньшего к большему
#    while summ < n:                                         #пока объем данных не превышает заданную сумму, добавляем значения в ответ 
#        summ += arr[i]                                      #
#        count += 1                                          #
#        if arr[i] > maxi:                                   #ищем максимум  
#            maxi = arr[i] 
#        i += 1
#    summ -= arr[i]
#    summ -= arr[i-1]
#    for i in reversed(arr):
#        if i <= n - summ:
#            if i > maxi:
#                maxi = i
#print(count-1, maxi, summ)  


#arr = []
#for i in range(210235, 210300):
#    for j in range(1, i//2+1):
#        if i % j == 0:
#            arr.append(j)
#    if len(arr) == 5:
#        print(*arr)
#    arr = []


#def f(x, y, a):
#    return (2*x + 3*y > 30) or (x + y <= a)

#for a in range(0, 50):
#    for x in range(0, 50):
#        for y in range(0, 50):
#            if not f(x, y, a):
#                print(x, y, a, f(x, y, a))
    


#f = open('tsB.txt')
#a = int(f.readline())
#sv31 = 0
#sv2 = 0
#sv62 = 0
#ans = 0
#for i in range(0, a, 1):
#    line = int(f.readline())
#    if line%62==0:
#        ans += i
#        sv62 += 1
#    elif line%31==0:
#        ans = ans + sv62 + sv2
#        sv31 += 1
#    elif line%2==0:
#        ans = ans + sv31 + sv62
#        sv2 += 1
#    else:
#        ans += sv62
#f.close()
#print(ans)

#import math
#def f(x):
#    return (((x**2)*(math.log(3-2*x), 64)) >= (math.log((2*x-3)**2, 2)))
#for x in range(-10, 10, 1):
#    print(x, f(x))
    


##Задание 5 файл 2
#with open('Z24_5.txt') as f:
#    s=f.read()
#    sum = 0
#    for i in s:
#        if i.isdigit():
#            sum += int(i)
#print(sum, (len(s)+1)//2)
##Ответ: 47524, 1 


##6
#with open('18new.txt') as f:
#    s="1+2+3+4-1"
#    res=int(s[0])
#    for i in range(1, len(s)):
#        if s[i]=='-':
#            res-=int(s[i+1])
#        if s[i]=='+':
#            res+=int(s[i+1])
#print(res)

##4
#with open('18new.txt') as f:
#    s="1+2+3+4"
#    c=0
#    sum=0
#    for i in s:
#        if i.isdigit():
#            sum+=int(i)
#print(c)

#count = 0
#with open("your_file.txt") as f:
#    s = f.read()
#    for  i in range(2, len(s)):
#        if s[i] == s[i-2] and s[i] == "V":
#            count += 1
#print(count)


#deli = []
#for i in range(100):
#    if (i ** 4>244143) and (i ** 4<1367821):
#        for j in range(1, i ** 4 // 2 + 1):
#            if (i ** 4) % j == 0:
#                deli.append(j)
#        if len(deli) == 4:
#            print(*deli, i ** 4)
#        deli = []


#deli = []
#for i in range(10000, 11000):
#    if (i ** 2>101000000) and (i ** 2<102000000):
#        for j in range(1, i ** 2 // 2 + 1):
#            if (i ** 2) % j == 0:
#                deli.append(j)
#        if len(deli) == 2:
#            print(*deli, i ** 2)
#        deli = []



#arr = []
#count= 0
#min = 100000
#j = 1
#for i in range(10001, 50001):
#    while len(arr) < 19 and j < 50001:
#        if i%j==0:
#            arr.append(j)
#        j += 1
#    if len(arr) > 17:
#        count += 1
#        if i<min:
#            min=i
#    arr = []
#    j = 1
#print(count, min)


#def f(n):
#    if n == 0:
#        return 0
#    elif n > 0 and n % 2 == 0:
#        return f(n // 2)
#    elif  n % 2 != 0:
#        return 1 + f(n - 1)
#for n in range(10000):
#    if f(n) == 12:
#        print(n)


#def f(a, x):
#    return (70 % a == 0) and ((x % 28 == 0) <= (not (x % a != 0) or (x % 21 != 0)))
#for a in range(1,1000):
#     for x in range(1,1000):
#         if  f(a, x):
#             print(a, x)


#26
#summ, count, maxi, i, arr = 0, 0, 0, 0, []                  #
#with open ("27886.txt") as f:                               #читаем файл  
#    n, m = [int(elem) for elem in f.readline().split()]     #читаем первые два значения из файла 
#    for line in f:                                          #добавляем каждую линию в список
#        arr.append(int(line))                               #добавляем каждую линию в список
#    arr.sort()                                              #соритирем список от меньшего к большему
#    while summ < n:                                         #пока объем данных не превышает заданную сумму, добавляем значения в ответ 
#        summ += arr[i]                                      #
#        count += 1                                          #
#        if arr[i] > maxi:                                   #ищем максимум  
#            maxi = arr[i] 
#        i += 1
#    summ -= arr[i]
#    summ -= arr[i-1]
#    for i in reversed(arr):
#        if i <= n - summ:
#            if i > maxi:
#                maxi = i
#print(count-1, maxi, summ)                                    



#for x in range(450):
#    res = ""
#    num = 343**5+7**3-1-x
#    while num > 0:
#        res = str(num % 7) + res
#        num //= 7
#    if res.count("6") == 12:
#        print(res, x)




#for temp in range(1, 10000000):
#    num=temp
#    res=''
#    while num>0:
#        res=str(num%4)+res
#        num//=4
#    s='0'+res
#    while '01' in s or '02' in s or '03' in s:
#        s=s.replace('01', '30', 1)
#        s=s.replace('02', '101', 1)
#        s=s.replace('03', '202', 1)
#    if s=='1'*15+'2'*10+'3'*60:
#        print(res)


#s = "0"+15*"1"+10*"2"+60*"3"
#while ("30" in s) and ("101" in s) and ("202" in s):
#    s = s.replace("30", "01", 1)
#    s = s.replace("101", "02", 1)
#    s = s.replace("202", "03", 1)
#print(s, s.count("1"))

#bin(99)
#int("110001", 2)

#for s in range(10, 1000):
#    sr = s
#    s = (s+1) // 7
#    n = 36
#    while s < 2050:
#        s = s * 2
#        n = n + 3
#    if n == 60:
#        print(sr, n)


#def f(x, y, z, w):
#    return ((x == (not y)) <= (y and not z)) or (z and (not w))

#for i in range(16):
#    mask = []
#    tmp = i
#    for j in range(4):
#        mask.append(tmp % 2)
#        tmp //= 2
#    for j in reversed(range(4)):
#        print(mask[j], end = '')
#    print('', int (f(mask[3],mask[2],mask[1],mask[0])))




#summ, count, maxi, i, arr = 0, 0, 0, 0, []                  #
#with open ("27886.txt") as f:                               #читаем файл  
#    n, m = [int(elem) for elem in f.readline().split()]     #читаем первые два значения из файла 
#    for line in f:                                          #добавляем каждую линию в список
#        arr.append(int(line))                               #добавляем каждую линию в список
#    arr.sort()                                              #соритирем список от меньшего к большему
#    while summ < n:                                         #пока объем данных не превышает заданную сумму, добавляем значения в ответ 
#        i += 1                                              #
#        summ += arr[i]                                      #
#        count += 1                                          #
#        if arr[i] > maxi:                                   #ищем максимум  
#            maxi = arr[i]                                   #
#print(count, maxi, summ)                                    #


#arr = []
#for i in range(201455, 201470):
#    for j in range(1, i//2+1):
#        if i % j == 0:
#            arr.append(j)
#    if len(arr) == 3:
#        print(*arr, i)
#    arr = []


#count, maxi = 1, 0
#with open ("zadanie24_2 (1).txt") as f:
#    s = f.read()
#    for i in range(len(s)):
#        if s[i] == "L" and s[i-1] == "L":
#            count +=1
#            if maxi < count:
#                maxi = count
#        else:
#            count = 1
#print(maxi)




#def f(bit):                                  #
#    rez = 2                                         #начальное число 
#    for i in bit:                                   #перебираем каждую возможную итерацию комбинацию
#        if i == 0:                                  #
#            rez += 2                                #
#        else:                                       #
#            rez *= 3                                #
#    return rez                                      #

#bit, sett, col =[], set(), 0                        #
#for i in  range(8):                                 #начало создания двоичной маски
#    tmp = i                                         #
#    mask, bit = [], []                              #
#    for j in range(3):                              #
#        mask.append(tmp % 2)                        #
#        tmp //= 2                                   #
#        bit.append(mask[j])                         #записываем маску в список bit
#        print(mask[j], end = '')                    #выводим маску
#    print("", f(bit))                               #выводим полученное расшифрованное число 
#    sett.add(f(bit))                                #добавляем найденное занчение в множество 
#print(sett, len(sett), sep = '\n')                  #выводим множество и количество его эл-тов

#for x in range(1,100000):
#    xr = x
#    a = 0
#    b = 0
#    while x > 0:
#        y = x % 10
#        if y > 3:
#            a = a+1
#        if y < 8:
#            b = b+1
#        x = x // 10
#    if (len(list(str(xr))) == 5) and (a == 4) and (b == 2):
#        print(xr, a, b)

#count, min = 0, 10000000
#for i in range(4668, 10414):
#    if ((i%3==0) or (i%11==0)) and ((i % 2 != 0) and (i % 13 != 0) and (i % 22 != 0) and (i % 33 != 0)):
#        count +=1 
#        if min > i:
#            min = i
#print(count, min)

#def F(n):
#    if n > 0:
#        G(n - 1)
#def G(n):
#    print("*")
#    if n > 1:
#        F(n - 3)

#print(F(11))


#count = 0
#def f(a, x, y):
#    return ((x < a) <= (x**2 < 81)) and ((y**2 <= 36) <= (y <= a))
#print(f(6,10000,10000),f(7,10000,10000),f(8,10000,10000))
#for a in range(100):
#    for y in range(100):
#        for x in range(100):
#            if not f(a, x, y):
#                count +=1
#                print(a, x, y, count)


#str(bin(8**2020+4**2017+26-1)).count("1")


#hex(int("1000100111001101", 2))


#summ, count, maxi, i, arr = 0, 0, 0, 0, []
#with open ("28139.txt") as f:
#    n, m = [int(elem) for elem in f.readline().split()]
#    for line in f:
#        arr.append(int(line))
#    arr.sort()
#    while summ < n:
#        i += 1
#        summ += arr[i]
#        count += 1
#        if arr[i] > maxi:
#            maxi = arr[i]
#print(count, maxi, summ)



#findd = False
#summ, count, maxi, i, arr = 0, 0, 0, 0, []
#with open ("28138.txt") as f:
#    n, m = [int(elem) for elem in f.readline().split()]
#    for line in f:
#        arr.append(int(line))
#    arr.sort()
#    while summ < n:
#        i += 1
#        summ += arr[i]  
#        count += 1
#        if arr[i] > maxi:
#            maxi = arr[i]
#    count -= 1
#    summ -= arr[i]
#    for j in range(i + 1, len(arr)):

#print(count, maxi, summ)





#arr = []
#for i in range(489421, 489440):
#    for j in range(1, i//2+1):
#        if i % j == 0:
#            arr.append(j)
#    if len(arr) == 3:
#        print(*arr, i)
#    arr = []    


#maxi, count = 0, 1
#with open ('zadanie24_1.txt') as f:
#    s = f.read()
#    for i in range(1, len(s)):
#        if (s[i] == 'C') and (s[i-1] == 'C'):
#            count += 1
#            if maxi < count:
#                maxi = count
#        else:
#            count = 1
#print(count, maxi)


#def f(n):
#    if n > 10:
#        return 0 
#    elif n == 10:
#        return 1
#    else:
#        return f(n + 1) + f(n * 2)
#def fx(n):
#    if n > 20:
#        return 0 
#    elif n == 20:
#        return 1
#    else:
#        return fx(n + 1) + fx(n * 2)
#print(f(1), fx(10), f(1) * fx(10))


#for x in range(1, 10000):
#    xr = x
#    a = 0
#    b = 10
#    while x > 0:
#        c = x % 10
#        a += c
#        if c < b:
#            b = c
#        x //= 10
#    if (a == 11) and (b == 5):
#        print(xr, a, b)
        


#def F(n):
#    print(n)
#    if n < 5:
#        F(n + 3)
#        F(2 * n)
#print(F(1))

#count, maxi = 0, 0
#for i in range(7487, 10006):
#    if (i % 13 == 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 17 != 0) and (i % 22 != 0):
#        count += 1
#        if maxi < i:
#            maxi = i
#print(count, maxi)

#def  f(a, x, y):
#    return ((x + 3*y > a) or (y < 30) or (x < 30))

#for a in range(1, 150):
#    for x in range(1, 150):
#        for y in range(1, 150):
#            if not f(a, x, y):
#                print(a, x, y)

#int('0111101000100011', 2)
#oct(31267)


#def f(x, y, z, w):
#    return ((not z or w) and (not x == y)) <= (x and z)

#for i in  range(16):
#    tmp = i
#    mask = []
#    for j in range(4):
#        mask.append(tmp % 2)
#        tmp //= 2
#    for j in reversed(range(4)):
#        print(mask[j], end='')
#    print('', int(f(mask[3],mask[2],mask[1],mask[0])))

#def f(x, y, z):
#    return (x == y) or (not y and x)

#print(f(0,1,0))


#count = 0
#for i in range(10000, 90001):
#    i = str(i)
#    if (int(i[1]) + int(i[3])) == (int(i[0]) + int(i[2]) + int(i[4])):
#        count += 1
#print(count)

#count = 0
#with open ("Задание_24__2sbx.txt") as f:
#    s = f.read()
#    for i in range(len(s)//2+1):
#        if s[i] == s[-i]:
#            count +=1
#print(count)



#def f(n):
#    if n > 5:
#        return 0 
#    elif n == 5:
#        return 1
#    else:
#        return f(n + 1) + f(n + 5) + f(n**2)
#def fx(n):
#    if n > 26:
#        return 0 
#    elif n == 26:
#        return 1
#    else:
#        return fx(n + 1) + fx(n + 5) + fx(n**2)
#print(f(2), fx(5), f(2) * fx(5))


#for x in range(30001):
#    xr = x
#    l = 0
#    m = 0
#    while x > 0:
#        m += 1
#        if x % 2 == 0:
#            l += m
#        x //= 10
#    if (l == 9) and (m == 5):
#        print(xr)

#with open("18new.txt") as f:                                    #считываем файл 
#    arr, mini, count, summ = [], 10000, 0, 0                    #
#    arr = f.read().replace(',', '.').splitlines()               #считываем построчно значения
#    for i in range(1, len(arr)):                                #
#        if (abs(float(arr[i]) - float(arr[i-1])) <= 7):         #разность между значениями рядом стоящими значениями 
#            summ += float(arr[i]) + float(arr[i-1])             #суммируем, если их разность меньше  7
#            if (summ > 20) and (summ < mini):                   #если сумма больше 20 - добавляем в минимум 
#                mini = summ                                     #
#        else:                                                   #
#            summ =  0                                           #
#print(mini)                                                     #


#count, mini = 0, 100000
#for i in range(6858, 13620):
#    if (i % 13 == 0) and (i % 11 != 0) and (i % 25 != 0) and (i % 56 != 0) and (i % 143 != 0) and (i % 512 != 0) and (i % 380 != 0):
#        count += 1
#        if mini >2 i:
#            mini = i
#print(count, mini)

#def f(n):
#    if n <= 2:
#        return n * 2
#    else:
#        return f(n - 2) + g(n - 2)
#def g(n):
#    if n <= 3:
#        return n
#    else:
#        return g(n - 1) + f(n - 2) * f(n - 2)
#print(f(6)+g(8))

#def  f(a, x):
#    return (x % a == 0) <= ((not (x % 21 == 0)) or (x % 35 == 0))
#for a in range(1, 100):
#    for x in range(1, 100):
#        if not f(a, x):
#            print(a, x)
#f(1, 21)
#42 % 4 == 0



#def f(a, x, y):
#    return (5 * y + 4 * x > a) or (2 * x + 3 * y < 90) or (y - 2 * x < -150)
#found = False
#i = 500
#while(not found):
#    x = 0 
#    ew = False
#    while (x < 500) and (not ew):
#        y = 0 
#        while (y < 500) and (not ew):
#            if (not f(i, x, y)):
#                ew = True 
#            y += 1 
#        x += 1
#    if (ew == False):
#        a = i 
#        found = True
#    i -= 1
#print(a)


#num = 5 ** 14 + 25 ** 3 - 117
#rez = ''
#while num > 0:
#    rez = str(num % 5) + rez
#    num //= 5
#print(rez)

#import math; math.gcd(21, 35)


#s = 100 * "8"
#while ('999' in s) or ('888' in s):
#    if '888' in s:
#        s = s.replace('888', '9', 1)
#    else:
#        s = s.replace('999', '8', 1)
#print(s)

#import math
#math.gcd(48, 72)

#def lcm(a, b):
#    import math
#    return (a * b) // math.gcd(a, b)
#lcm(a,b)

#bin(29)
#int("100000", 2)

#for n in range(10000):
#    s = 1
#    k = 0   
#    while s + n < 155:
#        s = 4*s
#        k += n
#    if k == 88:
#        print(k, n)

#def f(x, y, z, w):
#    return ((x == (not y)) <= ((x and w) == z))

#for i in range(16):
#    tmp = i
#    mask = []
#    for j in range(4):
#        mask.append(tmp%2)
#        tmp //= 2
#    for j in reversed(range(4)):
#        print(mask[j], end='')
#    print('', int(f(mask[3],mask[2],mask[1],mask[0])))


#arr = []
#max, count = 0, 0
#for i in range(120115, 120201):
#    for j in range(1, i//2+1 ):
#        if i % j == 0:
#            arr.append(j)
#    if len(arr) > max:
#        max = len(arr)
#        count = i
#    arr = []
#print(max+1, count)
        

#summ, count, maxi, i, arr = 0, 0, 0, 0, []
#with open ("27887.txt") as f:
#    n, m = [int(elem) for elem in f.readline().split()]
#    for line in f:
#        arr.append(int(line))
#    arr.sort()
#    while summ < n:
#        i += 1
#        summ += arr[i]
#        count += 1
#        if arr[i] > maxi:
#            maxi = arr[i]
#print(arr.index(45))
#print(count, maxi, summ)

    


#def f(n):
#    if (n > 15):
#        return 0
#    elif (n == 15):
#        return 1
#    else:
#        return f(n + 1) + f(n * 2) + f(n * 3)
        
#def fx(n):
#    if (n > 30):
#        return 0
#    elif (n == 30):
#        return 1
#    else:
#        return fx(n + 1) + fx(n * 2) + fx(n * 3)
#print(f(2))     
#print(fx(15))

#count = 0
#for x in range(1000):
#    xr = x
#    a=0
#    b=1
#    while x>0:
#        a=a+1
#        b=b*(x%10)
#        x=x//10
#    if (a == 2) and (b == 24):
#        count += 1
#        print(a, b, xr, count)

#str(bin(4**1014+2**1012-7)).count('1')

#def F(n):
#    if n < 10:
#        F(3 * n)
#        print(n)
#        F(n + 3)
#print(F(1))

#s = '2' + 100 *'9'
#while ('19' in s) or ('299' in s) or ('3999' in s):
#    s = s.replace('19', '2', 1)
#    s = s.replace('299', '3', 1)
#    s = s.replace('3999', '1', 1)
#print(s)

#bin(92)
#int('10101', 2)
#hex(int('1101001110100110', 2))



##def f(x, y, z, w):
#    return ((x and y and (not z)) == (y or z or (not w)))

#for i in  range(16):
#    tmp = i
#    mask = []
#    for j in range(4):
#        mask.append(tmp % 2)
#        tmp //= 2
#    for j in reversed(range(4)):
#        print(mask[j], end='')
#    print('', int(f(mask[3],mask[2],mask[1],mask[0])))


#def f(n):
#    if (n == 42):
#        return 1
#    elif n > 40:
#        return 0
#    else:
#        return f(n + 3) + f(n * 2)
    
#print(f(3))


#for x in range(100, 500):
#    xr = x
#    L = x - 12
#    M = x + 12
#    while L != M:
#        if L > M:
#            L = L - M
#        else:
#            M = M - L
#    if M == 2:
#        print(M, xr)


#count = 0
#for i in range(1056, 7564):
#    if ((i % 3 == 0) or (i % 11 == 0)) and (i % 13 != 0) and (i % 17 != 0) and (i % 19 != 0) and (i % 23 != 0):
#        count += 1
#        print(i)
#print(count)

#def f(n):
#    if n <= 1:
#        return 1
#    elif n > 1 and n % 2 == 0:
#        return n + f(n - 1)
#    else:
#        return n * n + f(n - 2)

#print(f(80))


#deli = []
#for i in range(100):
#    if (i ** 4>244143) and (i ** 4<1367821):
#        for j in range(1, i ** 4 // 2 + 1):
#            if (i ** 4) % j == 0:
#                deli.append(j)
#        if len(deli) == 4:
#            print(*deli, i ** 4)
#        deli = []



#import math
#def lcm(a, b):
#    return (a * b) // math.gcd(a, b)

#print(23, 16, lcm(23, 16), math.gcd(23, 16))


#num, rez = 9 ** 22 + 3 ** 66 - 18, ''
#while num > 0:
#    rez = str(num % 3) + rez
#    num //= 3
#print(rez.count('2'))



#s = '563' * 121
#while '56' in s or '3333' in s:
#    s = s.replace('56', '3', 1)
#    s = s.replace('3333', '3', 1)
#print(s)


#num, rez = 126, ''
#while num > 0:
#    rez = str(num % 2) + rez
#    num //= 2
#print(rez)
#print(int('1111', 2))


#def f(x, y, z):
#    return (z or y) <= (x == z)

#for i in range(8):
#    tmp = i
#    mask = []
#    for j in range(3):
#        mask.append(tmp%2)
#        tmp //= 2
#    for j in reversed(range(3)):
#        print(mask[j], end='')
#    print('', int(f(mask[2],mask[1],mask[0])))




#num = 9 ** 8 + 3 ** 24 - 18
#rez = ""
#while num > 0:
#    rez = str(num % 3) + rez
#    num //=  3
#print(rez.count("2"))

#import math

#def deli(n):
#    Ldev = []
#    for i in range(1, int(math.sqrt(n) + 1)):
#        if n % i == 0:
#            yield i
#            if i*i != n:
#                Ldev.append(n / i)
#    for i in reversed(Ldev):
#        yield i

#for i in range(1820348, 2880928):
#    if len(list(deli(i))) == 5:
#        print(list(deli(i)))



#import math

#arr=[]
#for i in range(1820348, 2880928):
#    for j in range(1, i // 2 + 1):
#        if (i % j == 0):
#            arr.append(j)
#    if len(arr) == 4:
#        print(*arr, i)
#        arr=[]
#    else:
#        arr=[]

#def factors(n):
#    for x in range(2,n):
#        if n%x == 0:
#            return (x,) + factors(n/x)
#    return (n,1)
#print(factors(1820348))

#s = 147 * "7"
#while "777" in s:
#    s = s.replace("777", "2", 1)
#    s = s.replace("222", "7", 1)
#print(s)


#for s in range (100000):
#    sr = s
#    n = 127
#    while s - n > 0:
#        s = s + 15
#        n = n + 20
#    if (s < 10000) and (s > 999):
#        print(s, sr)



#def f(n):
#    if n <= 1:
#        return 1
#    elif n % 2 == 0:
#        return n * f(n - 1)
#    else: 
#        return n + f(n - 2)

#print(f(84))

#count = 0
#for n in range(10**8):
#    if f(n) < 10**8:
#        count += 1
#print(count) 




#num = 9**20+3**60-25
#rez = ''
#while num > 0:
#    rez = str(num % 3) + rez
#    num //= 3
#print(rez.count("2"))


#s = "1" * 198
#while "1111" in s:
#    s= s.replace("1111", "33", 1)
#    s= s.replace("333", "1", 1)
#print(s)




#for s in range(1000000):
#    sr = s
#    n = 200
#    while s // n >= 2:
#        s = s + 5
#        n = n + 5
#    if s > 99 and s < 1000:
#        print(sr, s)


#a=[0]*20
#a[0]=0
#a[1]=1
#for i in range(2, 12):
#    a[i]=a[i-1]+a[i-2]
#print(a[11])

#c=0
#min=15000
#for i in range(7525, 13487):
#    if i%7==0 and i%6!=0 and i%9!=0 and i%14!=0 and i%21!=0:
#        c+=1
#        if i<min:
#            min=i
#print(c, min)