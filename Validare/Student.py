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



        try:
            self.__id = float(self.__id)
            self.__id_copie = self.__id
            self.__id = int(self.__id)
            if self.__id < 0 or self.__id_copie != self.__id:
                raise ValueError
        except ValueError:
            __err+="Id invalid!\n"

        
        if self.__nume == "":
            __err+="Nume invalid!\n"
        
        if len(__err) > 0:
            raise ValidationError(__err)


    def validare_id_student(self, lista):
        """
        Valideaza daca id-ul studentului nu este existent deja in lista de studenti
        params: lista - lista de studenti
        """
        
        for student in lista:
            if student.get_id() == self.__id:
                raise ValidationError("Id deja existent!\n")
