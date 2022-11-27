class Medii:
    def __init__(self, id, nume, medie):
        self.__id = id
        self.__nume = nume
        self.__medie = medie
    def get_nume(self):
        return self.__nume
    def get_medie(self):
        return self.__medie

    def __eq__(self, other):
        equal = True
        if self.get_nume() == other.get_nume():
            equal = False
        if self.get_medie() == other.get_medie():
            equal = False
        return equal
    def __str__(self):
        return f"{self.__nume} are media {self.__medie}"

        
