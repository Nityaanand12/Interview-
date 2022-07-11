def pivot(mylist, pivot_index, end_index):
    swap = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if mylist[pivot_index] < mylist[i]:
            swap += 1
            mylist[swap], mylist[i] = mylist[i], mylist[swap]
    mylist[pivot_index], mylist[swap] = mylist[swap], mylist[pivot_index]
    return swap
    
def quick_sort_helper(mylist, left, right):
    if left < right:
        pivot_index = pivot(mylist, left, right)
        quick_sort_helper(mylist, left, pivot_index-1)
        quick_sort_helper(mylist, pivot_index+1, right)
    return mylist

def quick_sort(mylist):
    return quick_sort_helper(mylist, 0, len(mylist)-1)

mylist = quick_sort([11, 3, 2, 1, 15, 5, 4,45, 88, 96, 50, 45])
print(mylist)
def first_largest(k, mylist):
    for i in range(k):
        print(mylist[i])
    print("====")

def last_smallest(k, mylist):
    n = len(mylist)
    for i in range(-k,0):
        print(mylist[i])

first_largest(3,mylist)
last_smallest(3,mylist)






