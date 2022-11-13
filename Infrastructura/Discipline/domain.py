class Disciplina:
    def __init__(self, id, nume, profesor):
        self.__id = id
        self.__nume = nume
        self.__profesor = profesor
    def get_id(self):
        return self.__id
    def get_nume(self):
        return self.__nume
    def get_profesor(self):
        return self.__profesor
    def set_nume(self, nume):
        self.__nume = nume
    def set_profesor(self, profesor):
        self.__profesor = profesor
    def __eq__(self, other):
        self.__bool = True
        if self.get_id() != other.get_id():
            self.__bool = False
        if self.get_profesor() != other.get_profesor():
            self.__bool = False
        if self.get_nume() != other.get_nume():
            self.__bool = False
        return self.__bool