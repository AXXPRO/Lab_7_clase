class Student:
    def __init__(self, id, nume):
        self.__id = id
        self.__nume = nume
    def get_id(self):
        return self.__id
    def get_nume(self):
        return self.__nume
    def set_nume(self, nume):
        self.__nume = nume
    """
    Definim relatia de egalitate intre 2 studenti
    """
    def __eq__(self, other):
        self.__bool = True
        if self.get_id() != other.get_id():
            self.__bool = False
        if self.get_nume() != other.get_nume():
            self.__bool = False
        return self.__bool




