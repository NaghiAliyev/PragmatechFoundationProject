myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def decreasingRange(arr):
    arr.sort()
    arr.reverse()
    print(arr)
    
def decreasingRange_2(arr):
    array = sortingAlg(arr)
    reversedArray = reversingAlg(array)
    print(reversedArray)

def sortingAlg(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def reversingAlg(arr):
    reversedArr = []
    for i in range(len(arr)-1,-1,-1):
        reversedArr.append(arr[i])
    return reversedArr

# verilen massiv
print('Verilen massiv')
print(myList)

# hazir methoddan istifade ederek yazilib
decreasingRange(myList)

# siralama(buble sort ile) ve tersine cevirme algoritimleri ile yazilib
decreasingRange_2(myList)