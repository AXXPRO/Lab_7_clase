from Erori.erori import ValidationError
from Infrastructura.Studenti.domain import *

class ValidareStudent:
    def __init__(self, Student):
        self.__nume = Student.get_nume()
        self.__id = Student.get_id()
    def get_id(self):
        """
        returneaza id-ul studentului
        """
        return self.__id
    def get_nume(self):
        """
        returneaza numele studentului
        """
        return self.__nume
    def is_student_valid(self):
        """
        Functia ridica o eroare daca parametrii unui student nu sunt valizi, cu mesaj corespunzator
        """
        __err = ""
        __id = self.get_id()
        __nume = self.get_nume()


        try:
            __id = float(__id)
            __id_copie = __id
            __id = int(__id)
            if __id < 0 or __id_copie != __id:
                raise ValueError
        except ValueError:
            __err+="Id invalid!\n"

        
        if __nume == "":
            __err+="Nume invalid!\n"
        
        if len(__err) > 0:
            raise ValidationError(__err)


    def validare_id_student(self, lista):
        """
        Valideaza daca id-ul studentului nu este existent deja in lista de studenti
        params: lista - lista de studenti
        TO BE TESTED"""
        __id = self.get_id()
        for student in lista:
            if student.get_id() == __id:
                raise ValidationError("Id deja existent!\n")
