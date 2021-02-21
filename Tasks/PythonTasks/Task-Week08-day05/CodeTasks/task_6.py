myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def arrPrinter(arr):
    oddIndex = []
    for i in range(1,len(arr),2):
        element = arr[i]
        oddIndex.append(element)
    for i in range(1,len(oddIndex),2):
        arr.pop(i)
    return arr

# verilen massiv
print('Verilen massiv:')
print(myList)

print('Verilen massivde tek indeksde duranlarin silindiyi massiv : ')

# hazir methoddan istifade ederek yazilib
print(arrPrinter(myList))