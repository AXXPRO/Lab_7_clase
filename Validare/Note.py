from Erori.erori import RepoError, ValidationError
from Infrastructura.Note.repo import NotaRepo


class ValidareNota:
    def __init__(self, Nota):
        self.__id = Nota.get_id()
        self.__student = Nota.get_student()
        self.__disciplina = Nota.get_disciplina()
        self.__valoare= Nota.get_valoare()
   
    def is_nota_valid(self):
        """
        Functia ridica o eroare daca parametrii unei note nu sunt valizi, cu mesaj corespunzator
        """
        __err = ""
       
        self.__id_de_testat = self.__id
        try:
            self.__id_de_testat = float(self.__id_de_testat)
            self.__id_copie = self.__id_de_testat
            self.__id_de_testat = int(self.__id_de_testat)
            if self.__id_de_testat < 0 or self.__id_copie != self.__id_de_testat:
                raise ValueError
        except ValueError:
            __err+="Id invalid!\n"

        
        try:
            self.__valoare = float(self.__valoare)
            if self.__valoare <1 or self.__valoare >10:
                raise ValueError
        except ValueError:
            __err+="Nota invalida!\n"
        
        if len(__err) > 0:
            raise ValidationError(__err)


