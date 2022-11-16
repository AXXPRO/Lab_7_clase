class Nota:
    def __init__(self, id, student, disciplina, valoare):
        self.__id = id
        self.__student = student
        self.__disciplina = disciplina
        self.__valoare= valoare
    def get_id(self):
        return self.__id
    def get_student(self):
        return self.__student
    def get_disciplina(self):
        return self.__disciplina
    def get_valoare(self):
        return self.__valoare
    def set_student(self, student):
        self.__student = student
    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina
    def set_valoare(self, valoare):
        self.__valoare = valoare 

    def __eq__(self, other):
        """
        Definim relatia de egalitate intre 2 note
        """
        self.__bool = True
        if self.get_id() != other.get_id():
            self.__bool = False
        if self.get_student() != other.get_student():
            self.__bool = False
        if self.get_disciplina() != other.get_disciplina():
            self.__bool = False
        if self.get_valoare() != other.get_valoare():
            self.__bool = False
        return self.__bool

