myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def reversing(arr):
    arr.reverse()
    for element in arr:
        print(element)

def reverseAlg(arr):
    reversedArray = []
    for i in range(len(arr)-1,-1,-1):
        reversedArray.append(arr[i])
    return reversedArray

# verilen massiv
print('Verilen massiv:')
print(myList)

print('Massivdeki elementlerin tersine cevrilmis veziyetde cap edilmesi : ')

# hazir methoddan istifade ederek yazilib
reversing(myList)

# qismen algoritim istifade ederek yazilib
print(reverseAlg(myList))