from Infrastructura.Studenti.repo import StudentRepo
from Erori.erori import ParamsError

class UI_functions:
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