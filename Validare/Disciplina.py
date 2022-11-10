from Infrastructura.Discipline.domain import *

def is_disciplina_valid(Disciplina):
    """
    Functia ridica o eroare daca parametrii unuei discipline nu sunt valizi, cu mesaj corespunzator
    """
    err = ""
    id = get_id_disciplina(Disciplina)
    nume = get_nume_disciplina(Disciplina)
    profesor = get_profesor_disciplina(Disciplina)

    try:
        id_copie = id
        id = int(id)
        if id < 0 or id_copie != id:
            raise ValueError
    except ValueError:
        err+="Id invalid!\n"

    
    if nume == "":
        err+="Nume invalid!\n"

    if profesor == "":
        err+="Profesor invalid!\n"
    
    if len(err) > 0:
        raise ValueError(err)

# def validare_id_student(lista, id):
#     """TO BE TESTED"""
#     for student in lista:
#         if get_id_student(student) == id:
#             raise ValueError("Id deja existent!\n")