myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def evenIndex(arr):
    for i in range(0,len(arr),2):
        print(arr[i])

# verilen massiv
print('Verilen massiv:')
print(myList)

print('Massivde indeksi cut olan elementlerin cap edilmesi : ')

# hazir methoddan istifade ederek yazilib
evenIndex(myList)