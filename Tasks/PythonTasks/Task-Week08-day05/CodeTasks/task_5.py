myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def repeatedNumbers(arr):
    result = []
    for element in arr:
        repCount =arr.count(element)
        if repCount>1:
            if result.count(element)!=1:
                result.append(element)
    return result

print(repeatedNumbers(myList))