myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def totalAmount(arr):
    total=0
    for element in arr:
        total+=element
    return total

# verilen massiv
print('Verilen massiv:')
print(myList)

print('Massivde olan elementlerin ceminin cap edilmesi : ')

# hazir methoddan istifade ederek yazilib
print(sum(myList))

# qismen algoritim istifade ederek yazilib
print(totalAmount(myList))