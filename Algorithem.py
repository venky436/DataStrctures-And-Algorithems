import math





# Liner_Search

def linear_serarch(data,target):
    length = len(data)
    for i in range(length):
        if data[i] == target:
           index = i
           return print('index is:',index)
          
           
    print('index not found')

linear_serarch([12,32,1,24,35,60,1,3,19,37],60
)



# Binary_Search

def binarySearch(arry,target):
    low = 0
    high = len(arry)-1

    while low <= high :
        mid = math.floor((low+high)//2)
        
        if arry[mid] == target :
            return mid
        
        elif arry[mid] < target:
            low = mid + 1
            
        else:
           high = mid -1
           
    return -1



a = [12,15,20,24,27,30,42,47,50]
target = 50
result = binarySearch(a,target)

if result != -1:
    print('index found at:',result)
else:
    print('no element found')




# To find factorial 

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))



# Bubble_sort

def Bubble_Sort(array):
    for i in range(0,len(array)-1):
        for j in range(i):
            if array[j+1] < array[j]:
                tem = array[j]
                array[j]=array[j+1]
                array[j+1]= tem

            
    return array

result = Bubble_Sort([3,1,4,2,6,8,7,9])
print(result)


# Selection_Sort

def SelectionSort(array):
    n = len(array)-1
    for i in range(n):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j] < array[min_index]:
                min_index = j
        tem = array[i]
        array[i]=array[min_index]
        array[min_index]=tem
    return array

result = SelectionSort([3,1,4,2,6,8,7,9,5])
print(result)

# Insertion_Sort

def InsertionSory(array):
    for i in range(1,len(array)):
        tem = array[i]
        j = i -1
        while tem < array[j] and j >= 0:
            array[j+1] = array[j]
            j -= 1
            array[j+1] = tem
            

    return array

print(InsertionSory([3,1,4,2,6,8,7,9,5,10]))






