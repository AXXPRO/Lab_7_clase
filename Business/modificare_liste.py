from Infrastructura.Studenti.domain import *
from Infrastructura.Studenti.repo import *
from Validare.Student import *

#TTEEEEEEEEEEEEST
def adaugare_student_service(params):
    """
    Functie responsabila pentru validare, si introducerea unui student in lista
    raises ValueError if element is not a student, or if id exists
    param1: id student
    param2: nume student
    """
    if len(params) != 5:
        raise ValueError("Incorect number of parameters!")
    id = params[0]
    nume = params[1]
    lista_studenti = params[-3]
    student = Student(id, nume)
    valid = ValidareStudent(student)
    valid.is_student_valid()
    valid.validare_id_student(lista_studenti)
    adauga_student_repo(lista_studenti, student)
        
