class Student:
    def __init__(self, id, nume):
        self.id = id
        self.nume = nume
    def get_id(self):
        return self.id
    def get_nume(self):
        return self.nume
    def set_nume(self, nume):
        self.nume = nume        


# def creaza_student(id, nume):
#     """
#     Functia creaza si returneaza un student, caracterizat printr-un id si un nume
#     param: id - id unic pentru fiecare studemt
#     param: nume - Numele studentului
#     return: Student
#     """
#     return {id:nume}

# def get_id_student(Student):
#     """
#     Functia returneaza id-ul unui Student
#     param: Student - un student caracterizat prin id si nume
#     return: id-ul studentului
#     """
#     for i in Student:
#      return i

# def get_nume_student(Student):
#     """
#     Functia returneaza numele unui Student
#     param: Student - un student caracterizat prin id si nume
#     return: numele studentului
#     """
#     return Student[get_id_student(Student)]

# def set_nume_student(Student, nume):
#     """
#     Functia schimba numele studentului in nume
#     param: Student - un student
#     param: nume - string, noul nume pe care il atribuim studentului
#     return: 
#     """

#     Student[get_id_student(Student)] = nume
    