from Infrastructura.Studenti.domain import *


def afisare_student_service(params):
    """
    Functia afiseazatoti studentii din lista_studenti
    """
    lista_studenti = params[-3]

    if lista_studenti == []:
        print("Niciun student in lista!")
        input()
        return
    
    for student in lista_studenti:
        print(type(student))
        print(student.get_id(), student.get_nume())

    input()