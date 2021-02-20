def task_3():
    results = []
    dostlar = ['Ehmed', 'Memmed', 'Sabir', 'Efsane', 'Qurban']
    index=0
    for dost in dostlar:
        index+=1
        if dost.find('a')!=-1:
            results.append(index)
    return results

result = task_3()
print(f'siyahida {len(result)} sayda a herfi olan element var')
print(result)
