from Infrastructura.Discipline.domain import *
from Infrastructura.Studenti.domain import *

def adauga_disciplina_repo(lista, Disciplina):
    """
    Functie responsabila pentru a adauga o disciplina in lista de discipline
    param: lista - lista de discipline
    param: Disciplina - disciplina pe care o adaugam
    return: 
    """
    lista.append(Disciplina)

def size_disciplina_repo(lista):
    """
    Functia responsabila pentru a returna numarul de discipline din lista
    param: lista - lista de discipline
    return: int, numarul de discipline din lista
    """
    return len(lista)

def cauta_id_disciplina_repo(lista, id):
    """
    Functia responsabila pentru a returna Disciplina cu id-ul id
    param: lista - lista de discipline
    param: id - id-ul unic al disciplinei pe care o cautam
    raises: TypeError - daca nu exista nicio disciplina cu acel id in lista
    """    
    for disciplina in lista:
        if get_id_disciplina(disciplina) == id:
            return disciplina
    raise TypeError("Nu exista nicio disciplina cu acel id!\n")

def modificare_id_disciplina_repo(lista, id, Disciplina):
    """
    Functie responsabila pentru a modifica disciplina cu id-ul id in Disciplina
    param: lista - lista de Discipline
    param: id - id-ul disciplinei pe care o modificam
    param: Disciplina - Disciplina cu care vom modifica disciplina caruia ii corespunde id
    """
    for disciplina in lista:
        if get_id_disciplina(disciplina) == id:
            set_nume_disciplina(disciplina, get_nume_disciplina(Disciplina))
            set_profesor_disciplina(disciplina, get_profesor_disciplina(Disciplina))

def delete_id_disciplina_repo(lista, id):
    """
    Functia sterge din lista disciplina cu id-ul id
    param: lista - lista de discipline
    param: id - id-ul disciplinei pe care vrem sa o eliminam
    """
    lista_noua = []

    for disciplina in lista:
        if get_id_disciplina(disciplina) != id:
            lista_noua.append(disciplina)
    lista[:] = lista_noua