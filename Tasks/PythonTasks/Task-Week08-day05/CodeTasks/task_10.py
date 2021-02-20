myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def max(arr):
    arr.sort()
    return arr[len(arr)-1]

print(max(myList))