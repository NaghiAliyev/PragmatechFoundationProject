def task_1(_num1,_num2):
    number1=_num1
    number2=_num2
    return (number1+number2)/2

def task_2():
    username=input('Istifadeci adini daxil edin : ')
    password=input('Istifadeci parolunu daxil edin : ')
    if username=='admin' and password=='123456':
        return 'duzdur'
    return 'sehvdir'

def task_3():
    results = []
    dostlar = ['Ehmed', 'Memmed', 'Sabir', 'Efsane', 'Qurban']
    index=0
    for dost in dostlar:
        index+=1
        if dost.find('a')!=-1:
            results.append(index)
    return results

def task_4():
    text = 'Baş nazir bildirib ki, müxtəlif sahələrdə əməkdaşlığımızı nəzərdə tutan bir çox sənədlər dünən keçirilən görüşlərdə imzalanıb: “Bu, çoxtərəfli platforma gələcək üçün böyük perspektivlər vəd edir. Əminəm ki, bu gün keçirilən iclasın nəticələri ikitərəfli münasibətlərin inkişafına da təkan verəcək. Prezident İlham Əliyev və Rəcəb Tayyib Ərdoğanın yorulmaz səyləri nəticəsində ölkələrimiz arasında münasibətlər ən yüksək səviyyəyə çatıb. Əməkdaşlığımız bütün sahələri əhatə edir. 2023-cü ilədək ticarət dövriyyəmizi 15 milyard dollara çatdırmaq əsas hədəflərimizdəndir'
    arrText = text.split()
    return len(arrText)


    
# -----------------------------------
# task 1
# print(task_1(5,6))

# task 2
# print(task_2())

# task 3
result = task_3()
print(f'siyahida {len(result)} sayda a herfi olan element var')
print(result)

# task 4
# print(task_4())

# task 5