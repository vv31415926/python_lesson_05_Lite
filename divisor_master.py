'''
Задание Lite
Необходимо реализовать модуль divisor_master. Все функции модуля принимают на
вход натуральные числа от 1 до 1000. Модуль содержит функции:
1. проверка числа на простоту (простые числа - это те числа у которых делители
единица и они сами);
2. выводит список всех делителей числа;
3. выводит самый большой простой делитель числа.
'''

def isSimple( n ):
    count=0
    for d in range( 1,n+1 ):
        if n % d == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

def getDivisor( n ):
    lst = []
    for d in range(1, n + 1):
        if n % d == 0:
            lst.append(  d  )
    return lst

def maxDivisor( n ):
    lst = getDivisor( n )
    lst2 = []
    nMax = 0
    for i in lst:
        if isSimple( i ):
            if i > nMax:
                nMax = i

    if nMax == 0:
        return None
    else:
        return nMax

if __name__ == '__main__':
    lst = [2,15,31,50,73,120,127,178,179,198,233,234,283,350,353,400,419 ]

    for i in lst:
        if isSimple(i) == True:
            print( f'число {i}- простое!!!' )
        else:
            print(f'число {i}- не простое...')

    for i in lst:
        l = getDivisor(i)
        print( f'делители числа {i}: {l}' )

    for i in lst:
        m = maxDivisor(i)
        print( f'максимальный простой делитель числа {i}: {m}' )