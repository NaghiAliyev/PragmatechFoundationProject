myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def evenIndex(arr):
    for element in arr:
        if arr.index(element)%2==0:
            print(element)

evenIndex(myList)