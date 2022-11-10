from Infrastructura.Studenti.domain import *

class ValidareStudent:
    def __init__(self, Student):
        self.nume = Student.get_nume()
        self.id = Student.get_id()
        
    def is_student_valid(self):
        """
        Functia ridica o eroare daca parametrii unui student nu sunt valizi, cu mesaj corespunzator
        """
        err = ""
        id = self.id
        nume = self.nume


        try:
            id = float(id)
            id_copie = id
            id = int(id)
            if id < 0 or id_copie != id:
                raise ValueError
        except ValueError:
            err+="Id invalid!\n"

        
        if nume == "":
            err+="Nume invalid!\n"
        
        if len(err) > 0:
            raise ValueError(err)


    def validare_id_student(self, lista):
        """TO BE TESTED"""
        id = self.id
        for student in lista:
            if student.get_id() == id:
                raise ValueError("Id deja existent!\n")
