from Infrastructura.Studenti.domain import *

def adauga_student_repo(lista, Student):
    """
    Functie responsabila pentru a adauga un student in lista de studenti
    param: lista - lista de studenti
    param: Student - studentul pe care il adaugam
    return: 
    """
    lista.append(Student)

def size_student_repo(lista):
    """
    Functia responsabila pentru a returna numarul de studenti din lista
    param: lista - lista de studenti
    return: int, numarul de studenti din lista
    """
    return len(lista)

def cauta_id_student_repo(lista, id):
    """
    Functia responsabila pentru a returna Studentul cu id-ul id
    param: lista - lista de studenti
    param: id - id-ul unic al studentului pe care il cautam
    raises: TypeError - daca nu exista niciun student cu acel id in lista
    """    
    for student in lista:
        if student.get_id() == id:
            return student
    raise TypeError("Nu exista niciun student cu acel id!\n")

def modificare_id_student_repo(lista, id, student_change):
    """
    Functie responsabila pentru a modifica studentul cu id-ul id in Student
    param: lista - lista de Studenti
    param: id - id-ul studentului pe care il modificam
    param: Student - Studentul cu care vom modifica studentul caruia ii corespunde id
    """
    for student in lista:
        if student.get_id() == id:
            student.set_nume(student_change.get_nume())


def delete_id_student_repo(lista, id):
    """
    Functia sterge din lista studentul cu id-ul id
    param: lista - lista de studenti
    param: id - id-ul studentului pe care vrem sa il eliminam
    """
    lista_noua = []

    for student in lista:
        if student.get_id() != id:
            lista_noua.append(student)
    lista[:] = lista_noua