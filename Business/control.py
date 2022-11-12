from Infrastructura.Studenti.domain import *
from Infrastructura.Studenti.repo import StudentRepo
from Validare.Student import ValidareStudent


class Business:
    def __init__(self,params, COMANDA):
        """
        Constructorul functiilor business
        param: params- listele + parametrii specifici fiecarei functii
        param: COMANDA- metoda clasei ce va fi executata
        
        """
        self.__lista_studenti = params[-3]
        self.__lista_discipline = params[-2]
        self.__lista_note = params[-1]
        self.__params = params[0:len(params)-3]
        COMANDA(self)
       
    def afisare_student_service(self):
        """
        Functia afiseazatoti studentii din lista_studenti
        """
        

        if self.__lista_studenti == []:
            print("Niciun student in lista!")
            input()
            return
        
        for __student in self.__lista_studenti:
            print(__student.get_id(), __student.get_nume())

        input()


    def adaugare_student_service(self):
        """
        Functie responsabila pentru validare, si introducerea unui student in lista
        raises ValueError if element is not a student, or if id exists
        param1: id student
        param2: nume student
        """
        if len(self.__params) != 2:
            raise ValueError("Incorect number of parameters!")
        self.__id = self.__params[0]
        self.__nume = self.__params[1]
        self.__student = Student(self.__id, self.__nume)
        self.__VALID = ValidareStudent(self.__student)
        self.__VALID.is_student_valid()
        self.__VALID.validare_id_student(self.__lista_studenti)
        self.__REPO = StudentRepo(self.__lista_studenti)
        self.__REPO.adauga_student_repo(self.__student)
