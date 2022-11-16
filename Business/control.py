from Erori.erori import ParamsError, RepoError
from Infrastructura.Discipline.domain import Disciplina
from Infrastructura.Discipline.repo import DisciplinaRepo
from Infrastructura.Note.domain import Nota
from Infrastructura.Note.repo import NotaRepo
from Infrastructura.Studenti.domain import *
from Infrastructura.Studenti.repo import StudentRepo
from Validare.Disciplina import ValidareDisciplina
from Validare.Note import ValidareNota
from Validare.Student import ValidareStudent


class BusinessStudent:
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


class BusinessDisciplina:
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
        self.__REPO = DisciplinaRepo(self.__lista_discipline)
        COMANDA(self)

    def sterge_disciplina_id_service(self):
        """
        Functia sterge din lista de discipline disciplina cu id-ul id
        param1: id-ul
        """
        if len(self.__params) !=1 :
            raise ParamsError("Numar de parametrii invalid!")
        self.__id_de_sters = self.__params[0]
        self.__REPO.delete_id_disciplina_repo(self.__id_de_sters)

    def adaugare_disciplina_service(self):
        """
        Functie responsabila pentru validare, si introducerea unei discipline in lista
        raises ValueError if element is not a disciplina, or if id exists
        param1: id Disciplina
        param2: nume Disciplina
        param3: profesor Disciplina
        """
        if len(self.__params) != 3:
            raise ParamsError("Numar de parametrii invalid!")
        self.__id = self.__params[0]
        self.__nume = self.__params[1]
        self.__profesor = self.__params[2]

        self.__disciplina = Disciplina(self.__id, self.__nume, self.__profesor)
        self.__VALID = ValidareDisciplina(self.__disciplina)
        self.__VALID.is_disciplina_valid()
        self.__VALID.validare_id_disciplina(self.__lista_discipline)
        
        self.__REPO.adauga_disciplina_repo(self.__disciplina)


    def modifica_disciplina_service(self):
        """
        Funcita va modifca disciplina cu id-ul id, cu o disciplina data de utilizator
        """
        if len(self.__params) != 3:
            raise ParamsError("Numar de parametrii invalid!")
        self.__id = self.__params[0]
        self.__nume = self.__params[1]
        self.__profesor = self.__params[2]
        self.__REPO.modificare_id_disciplina_repo(self.__id, Disciplina(self.__id, self.__nume, self.__profesor))



class BusinessNota:
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
        self.__REPO_Nota = NotaRepo(self.__lista_note)
        self.__REPO_Student = StudentRepo(self.__lista_studenti)
        self.__REPO_Disciplina = DisciplinaRepo(self.__lista_discipline)
        COMANDA(self)

    def sterge_nota_id_service(self):
        """
        Functia sterge din lista de notele cu cu id-ul id
        param1: id-ul
        """
        if len(self.__params) !=1 :
            raise ParamsError("Numar de parametrii invalid!")
        self.__id_de_sters = self.__params[0]
        self.__REPO_Nota.delete_id_nota_repo(self.__id_de_sters)

    def __check_ids(self, __student_id, __disciplina_id):
        """
        Functia verifica daca exista sau nu student si disciplina cu id-ul dat
        TEETTETETETSSSSSSSTTTTTT
        """
        self.__err = ""
        self.__student_id = __student_id
        self.__disciplina_id = __disciplina_id

        try:
            self.__REPO_Student.cauta_id_student_repo(self.__student_id)
        except RepoError as err:
            self.__err += str(err)
        try:
            self.__REPO_Disciplina.cauta_id_disciplina_repo(self.__disciplina_id)
        except RepoError as err:
            self.__err += str(err)
        
        if len(self.__err) > 0:
            raise RepoError(self.__err)
             
            
        
    def adaugare_nota_service(self):
        """
        Functie responsabila pentru validare, si introducerea unei note in lista
        raises ValueError if element is not a nota, or if id exists
        param1: id Nota
        param2: id Student
        param3: id Disciplina
        param4: id Valoare
        """
        if len(self.__params) != 4:
            raise ParamsError("Numar de parametrii invalid!")
        self.__id = self.__params[0]
        self.__student_id = self.__params[1]
        self.__disciplina_id = self.__params[2]
        self.__valoare = self.__params[3]

        self.__check_ids(self.__student_id, self.__disciplina_id)

        self.__nota = Nota(self.__id,  self.__REPO_Student.cauta_id_student_repo(self.__student_id), self.__REPO_Disciplina.cauta_id_disciplina_repo(self.__disciplina_id), self.__valoare )
        
        
        self.__VALID = ValidareNota(self.__nota)
        self.__VALID.is_nota_valid()
        self.__VALID.validare_id_nota(self.__lista_note)
        
        self.__REPO_Nota.adauga_nota_repo(self.__nota)


    def modifica_nota_service(self):
        """
        Funcita va modifca nota cu id-ul id, cu o nota data de utilizator
        """
        if len(self.__params) != 4:
            raise ParamsError("Numar de parametrii invalid!")

        self.__id = self.__params[0]
        self.__student_id = self.__params[1]
        self.__disciplina_id = self.__params[2]
        self.__valoare = self.__params[3]

        self.__check_ids(self.__student_id, self.__disciplina_id)

        self.__REPO_Nota.modificare_id_nota_repo(self.__id, Nota(self.__id, self.__REPO_Student.cauta_id_student_repo(self.__student_id), self.__REPO_Disciplina.cauta_id_disciplina_repo(self.__disciplina_id), self.__valoare))