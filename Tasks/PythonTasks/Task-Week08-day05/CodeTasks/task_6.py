myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def arrPrinter(arr):
    for element in arr:
        if arr.index(element)%2==1:
            arr.remove(element)
    return arr

print(arrPrinter(myList))