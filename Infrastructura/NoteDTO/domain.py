class NotaDTO:
    def __init__(self, id_nota, id_student, id_disciplina, valoare):
        self.__id_nota = id_nota
        self.__id_student = id_student
        self.__id_disciplina = id_disciplina
        self.__valoare = valoare
    def get_id_nota(self):
        return self.__id_nota
    def get_id_student(self):
        return self.__id_student
    def get_id_disciplina(self):
        return self.__id_disciplina
    def get_valoare(self):
        return self.__valoare

    def set_id_student(self, id_nou):
        self.__id_student = id_nou

        
    def set_id_disciplina(self, id_nou):
        self.__id_disciplina = id_nou
        
    def set_valoare(self, valoare_noua):
        self.__valoare = valoare_noua

    def __eq__(self, other):
        """
        Functia compara egalitatea intre doua note
        """
        egale = True
        if self.__id_nota != other.__id_nota:
            egale = False
        if self.__id_student != other.__id_student:
            egale = False
        if self.__id_disciplina != other.__id_disciplina:
            egale = False
        if self.__valoare != other.__valoare:
            egale = False
        return egale

    