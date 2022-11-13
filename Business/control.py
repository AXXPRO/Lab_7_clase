from Erori.erori import ParamsError
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
        self.__REPO = StudentRepo(self.__lista_studenti)
        COMANDA(self)
       
    

    def __id_pentru_afisare(self, student):
        """
        returneaza id-ul lui student
        """
        return student.get_id()
    def afisare_student_service(self):
        """
        Functia afiseazatoti studentii din lista_studenti
        """
    
        if self.__lista_studenti == []:
            print("Niciun student in lista!")
            input()
            return
        
        #FOR MY OCD :

        self.__lista_studenti.sort(key = self.__id_pentru_afisare)

        for __student in self.__lista_studenti:
            print(__student.get_id(), __student.get_nume())

        input()
    def sterge_student_id_service(self):
        """
        Functia sterge din lista de studenti studentul cu id-ul id
        param1: id-ul
        """
        if len(self.__params) !=1 :
            raise ParamsError("Numar de parametrii invalid!")
        self.__id_de_sters = self.__params[0]
        self.__REPO.delete_id_student_repo(self.__id_de_sters)
    def adaugare_student_service(self):
        """
        Functie responsabila pentru validare, si introducerea unui student in lista
        raises ValueError if element is not a student, or if id exists
        param1: id student
        param2: nume student
        """
        if len(self.__params) != 2:
            raise ParamsError("Numar de parametrii invalid!")
        self.__id = self.__params[0]
        self.__nume = self.__params[1]
        self.__student = Student(self.__id, self.__nume)
        self.__VALID = ValidareStudent(self.__student)
        self.__VALID.is_student_valid()
        self.__VALID.validare_id_student(self.__lista_studenti)
        
        self.__REPO.adauga_student_repo(self.__student)

        
    def modifica_student_service(self):
        """
        Funcita va modifca studentul cu id-ul id, cu un student dat de utilizator
        """
        if len(self.__params) != 2:
            raise ParamsError("Numar de parametrii invalid!")
        self.__id = self.__params[0]
        self.__nume = self.__params[1]
        self.__REPO.modificare_id_student_repo(self.__id, Student(self.__id, self.__nume))
    def cauta_student_id_service(self):
        """
        Va afisa numele studentului cu id-ul dat, sau va afisa ca nu exista acel id
        """

        if len(self.__params) !=1:
            raise ParamsError("Numar de parametrii invalid!")
        self.__id = self.__params[0]

        self.__student = self.__REPO.cauta_id_student_repo(self.__id)

        print("Studentul cu id-ul",self.__id, "este", self.__student.get_nume())
        input()