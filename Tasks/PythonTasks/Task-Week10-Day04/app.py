import random
class Students():
    def __init__(self,_name,_article):
        self.name = _name
        self.article = _article
    def getStudentData(self):
        return self.name + '-' + self.article

studentsName=[
    'Pünhan Hüseynov',
    'Jalə Mirzayeva',
    'Hüseyn Ahmedzade',
    'Orxan Babazade',
    'İbrahim Hüseynov',
    'Orxan Mustafayev',
    'Fatimə Yaqubova',
    'Fərid Kərimli',
    'Toğrul Mardanov',
    'Nicat Gurbani',
    'Nağı Əliyev',
    'Elmir Səfərəliyev',
    'Elcan Quliyev',
    'Məhəmməd Sadıqzadə'
]

articles = [
    'article 1',
    'article 2',
    'article 3',
    'article 4',
    'article 5',
    'article 6',
    'article 7',
    'article 8',
    'article 9',
    'article 10',
    'article 11',
    'article 12',
    'article 13',
    'article 14'
]
# random.shuffle(studentsName)

students = []

def shufleAndAppendList():
    random.shuffle(articles)
    for i in range(len(articles)):
        studentName = studentsName[i]
        studentArticle = articles[i]
        student = Students(studentName,studentArticle)
        students.append(student)

shufleAndAppendList()


def printAllStudents():
    for student in students:
        print(student.getStudentData())

printAllStudents()
