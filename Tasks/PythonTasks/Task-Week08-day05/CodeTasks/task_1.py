myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def method_1(arr):
    return len(arr)

def method_2(arr):
    counter = 0
    for element in arr:
        counter+=1

    return counter

# verilen massiv
print('Verilen massiv:')
print(myList)

print('Massivde olan elementleri sayi : ')

# hazir methoddan istifade ederek yazilib
print(method_1(myList))

# qismen algoritim istifade ederek yazilib
print(method_2(myList))