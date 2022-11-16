from Infrastructura.Discipline.repo import DisciplinaRepo
from Infrastructura.Note.repo import NotaRepo
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
        self.__REPO_STUDENT = StudentRepo(self.__lista_studenti)
        self.__REPO_DISCIPLINA = DisciplinaRepo(self.__lista_discipline)
        self.__REPO_NOTA = NotaRepo(self.__lista_note) 
        COMANDA(self)


    def afisare_student_service(self):
        """
        Functia afiseazatoti studentii din lista_studenti
        """
    
        if self.__lista_studenti == {}:
            print("Niciun student in lista!")
            input()
            return
        
        #FOR MY OCD :

        #self.__lista_studenti.sort(key = self.__id_student_pentru_afisare)

        for __student in StudentRepo(self.__lista_studenti).get_list():
            print(__student.get_id(), __student.get_nume())

        input()

    def cauta_student_id_service(self):
        """
        Va afisa numele studentului cu id-ul dat, sau va afisa ca nu exista acel id
        """

        if len(self.__params) !=1:
            raise ParamsError("Numar de parametrii invalid!")
        self.__id = self.__params[0]

        self.__student = self.__REPO_STUDENT.cauta_id_student_repo(self.__id)

        print("Studentul cu id-ul",self.__id, "este", self.__student.get_nume())
        input()

##################################################################################


    def afisare_disciplina_service(self):
        """
        Functia afiseaza toate disciplinele din lista_discipline
        """
    
        if self.__lista_discipline == {}:
            print("Nicio disciplina in lista!")
            input()
            return
        
        #FOR MY OCD :

        #self.__lista_discipline.sort(key = self.__id_disciplina_pentru_afisare)

        for __disciplina in  DisciplinaRepo(self.__lista_discipline).get_list():
            print(__disciplina.get_id(), __disciplina.get_nume(), __disciplina.get_profesor())

        input()

    def cauta_disciplina_id_service(self):
        """
        Va afisa numele si profesorul disciplinei cu id-ul dat, sau va afisa ca nu exista acel id
        """

        if len(self.__params) !=1:
            raise ParamsError("Numar de parametrii invalid!")
        self.__id = self.__params[0]

        self.__disciplina = self.__REPO_DISCIPLINA.cauta_id_disciplina_repo(self.__id)

        print("Disciplina cu id-ul",self.__id, "este", self.__disciplina.get_nume(),"si are profesorul", self.__disciplina.get_profesor())
        input()
    def afisare_nota_service(self):
        """
        Functia afiseaza toate notele din lista_note
        """
    
        if self.__lista_note == {}:
            print("Nicio nota in lista!")
            input()
            return
        
        #FOR MY OCD :

        #self.__lista_discipline.sort(key = self.__id_disciplina_pentru_afisare)

        for __nota in  NotaRepo(self.__lista_note).get_list():
            print(__nota.get_id(), __nota.get_student().get_nume(), __nota.get_disciplina().get_nume(), __nota.get_valoare())

        input()
    def cauta_nota_id_service(self):
            """
            Va afisa numele studentului, materia si nota cu id-ul dat, sau va afisa ca nu exista acel id
            """

            if len(self.__params) !=1:
                raise ParamsError("Numar de parametrii invalid!")
            self.__id = self.__params[0]

            self.__nota = self.__REPO_NOTA.cauta_id_nota_repo(self.__id)

            print("Studentul",self.__nota.get_student().get_nume(), "are nota", self.__nota.get_valoare(),"la", self.__nota.get_disciplina().get_nume())
            input()
