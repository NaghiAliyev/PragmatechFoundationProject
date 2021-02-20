myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def minimum(arr):
    arr.sort()
    return arr[0]

print(minimum(myList))