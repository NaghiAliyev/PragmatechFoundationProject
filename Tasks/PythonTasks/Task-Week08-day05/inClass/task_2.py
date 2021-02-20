def task_2():
    username=input('Istifadeci adini daxil edin : ')
    password=input('Istifadeci parolunu daxil edin : ')
    if username=='admin' and password=='123456':
        return 'duzdur'
    return 'sehvdir'

print(task_2())