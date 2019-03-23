
'''we provide n value and please return array contains n number of elements example N = 5 [-1,2,1,-3,3] and sum of the list should be zero  '''
import random
import datetime
def solution(n):
    def func():
        num1 = 0
        lst = []
        for i in range(n):
            num = random.randint(-10,10)
            if num not in lst:
                lst.append(num)
            else:
                num = random.randint(-10,10)
                while num in lst:
                    num = random.randint(-10,10)
                lst.append(num)
        for num2 in lst:
            num1 += num2
        return func() if num1 !=0 else lst
    return func()

print(solution(random.randint(3,10)))

'''input (fri,45), today it is 'Fri' and tell after 45 days which day it is.'''
def solution1(S, K):
    days_in_week ={1:'Mon',2:'Tue',3:'Wed',4:'Thr',5:'Fri',6:'Sat',0:'Sun'}
    '''accessing the key by using value'''
    for key,value in days_in_week.items():
        if S==value:
            num = key+K
            break
    rem = num%7
    if rem<=6:
        return days_in_week[rem]

print(solution1('Fri',45))

''' we provide the day ex:'Mon' so please return the no. of the day from the dictionary'''
'''lst ={'Mon':1,'Tue':2,'Wed':3,'Thr':4,'Fri':5,'Sat':6,'Sun':7}'''
def solution2(S):
    lst ={'Mon':1,'Tue':2,'Wed':3,'Thr':4,'Fri':5,'Sat':6,'Sun':7}
    return lst[S]

print(solution2('Mon'))
