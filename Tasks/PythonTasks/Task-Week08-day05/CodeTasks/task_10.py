myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def max(arr):
    arr.sort()
    return arr[len(arr)-1]

def max_2(arr):
    maxElement = arr[0]

    for element in arr:
        if maxElement < element:
            maxElement = element
    return maxElement

# verilen massiv
print('Verilen massiv:')
print(myList)

print('Massivde olan en boyuk element : ')

# hazir methoddan istifade ederek yazilib
print(max(myList))


# qismen algoritim istifade ederek yazilib
print(max_2(myList))