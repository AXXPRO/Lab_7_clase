from Erori.erori import RepoError, ValidationError
from Infrastructura.Discipline.repo import DisciplinaRepo
from Infrastructura.Studenti.domain import *

class ValidareDisciplina:
    def __init__(self, Disciplina):
        self.__nume = Disciplina.get_nume()
        self.__id = Disciplina.get_id()
        self.__profesor = Disciplina.get_profesor()
    def get_id(self):
        """
        returneaza id-ul Disciplinei
        """
        return self.__id
    def get_nume(self):
        """
        returneaza numele Disciplinei
        """
        return self.__nume
    def get_profesor(self):
        """
        returneaza numele profesorului
        """
    def is_disciplina_valid(self):
        """
        Functia ridica o eroare daca parametrii unei discipline nu sunt valizi, cu mesaj corespunzator
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

        
        if self.__nume == "":
            __err+="Nume invalid!\n"
        if self.__profesor == "":
            __err+="Profesor invalid!\n"
        
        if len(__err) > 0:
            raise ValidationError(__err)


    def validare_id_disciplina(self, lista):
        """
        Valideaza daca id-ul disciplinei nu este existent deja in lista de discipline
        params: lista - lista de discipline
        """
       
        try:
            __disciplina = DisciplinaRepo(lista).cauta_id_disciplina_repo(self.__id)
            raise ValidationError("Id deja existent!\n")
        except RepoError:
            pass
