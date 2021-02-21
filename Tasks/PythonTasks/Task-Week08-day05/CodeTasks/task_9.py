myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def minimum(arr):
    arr.sort()
    return arr[0]

def minimum_2(arr):
    minimumElement = arr[0]

    for element in arr:
        if minimumElement > element:
            minimumElement = element
    return minimumElement

# verilen massiv
print('Verilen massiv:')
print(myList)

print('Massivde olan en kicik element : ')

# hazir methoddan istifade ederek yazilib
print(minimum(myList))

# qismen algoritim istifade ederek yazilib
print(minimum_2(myList))