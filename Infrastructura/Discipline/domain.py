def creaza_disciplina(id, nume, profesor):
    """
    Functia creaza si returneaza o disciplina, caracterizata printr-un id, nume si profesor
    param: id - id unic pentru fiecare disciplina
    param: nume - Numele disciplinei
    param: profesor - Numele profesorului
    return: Disciplina
    """
    return {id:[nume,profesor]}

def get_id_disciplina(Disciplina):
    """
    Fuinctia returneaza id-ul unei discipline
    param: Disciplina - obiect caracterizat prin id, nume si profesor
    return: numar natural, id
    """
    for i in Disciplina:
        return i
    

def get_profesor_disciplina(Disciplina):
    """
    Functia returneaza profesorul unei discipline
    param: Disciplina - obiect caracterizat prin id, nume si profesor
    return: string, profesor
    """
    return Disciplina[get_id_disciplina(Disciplina)][1]

def get_nume_disciplina(Disciplina):
    """
    Functia returneaza numele unei discipline
    param: Disciplina - obiect caracterizat prin id, nume si profesor
    return: string, nume
    """
    return Disciplina[get_id_disciplina(Disciplina)][0]
def set_profesor_disciplina(Disciplina,profesor):
    """
    Functia returneaza profesorul unei discipline
    param: Disciplina - obiect caracterizat prin id, nume si profesor
    return: string, profesor
    """
    Disciplina[get_id_disciplina(Disciplina)][1] = profesor

def set_nume_disciplina(Disciplina,nume):
    """
    Functia returneaza numele unei discipline
    param: Disciplina - obiect caracterizat prin id, nume si profesor
    return: string, nume
    """
    Disciplina[get_id_disciplina(Disciplina)][0] = nume
    