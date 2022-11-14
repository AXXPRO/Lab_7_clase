
from Business.control import BusinessDisciplina, BusinessStudent
from Erori.erori import RepoError
from Infrastructura.Studenti.domain import *
from Infrastructura.Discipline.domain import *
from Validare.Disciplina import *
from Validare.Student import *
from Infrastructura.Studenti.repo import *
from Infrastructura.Discipline.repo import *

class Teste:


    def __test_domain_disciplina(self):
        """
        Testele pentru functiile domain asociate disciplina
        """
        self.__id = 0
        self.__nume = "Mate"
        self.__profesor = "Cotfas"
        self.__prima_materie = Disciplina(self.__id, self.__nume, self.__profesor)

        assert self.__prima_materie.get_id() == 0
        assert self.__prima_materie.get_nume() == "Mate"
        assert self.__prima_materie.get_profesor() == "Cotfas"

        self.__nume_nou = "Romana"
        self.__profesor_nou = "Ghinea"
        self.__prima_materie.set_nume(self.__nume_nou)
        self.__prima_materie.set_profesor(self.__profesor_nou)

        assert self.__prima_materie.get_nume() == "Romana"
        assert self.__prima_materie.get_profesor() == "Ghinea"

        self.__prima_materie = Disciplina(self.__id, self.__nume, self.__profesor)
        self.__a_doua_materie = Disciplina(self.__prima_materie.get_id(),self.__prima_materie.get_nume(),self.__prima_materie.get_profesor())
        assert self.__prima_materie == self.__a_doua_materie

        self.__a_doua_materie = Disciplina(self.__prima_materie.get_id()+1,self.__prima_materie.get_nume(),self.__prima_materie.get_profesor())
        assert (self.__prima_materie == self.__a_doua_materie) == False

    def __test_domain_student(self):
        """
        Testele pentru functiile domain asociate student
        """
        self.__id = 0
        self.__nume = "Carol"
        self.__primul_student = Student(self.__id, self.__nume)

        assert self.__primul_student.get_id() == 0
        assert self.__primul_student.get_nume() == "Carol"

        self.__nume_nou = "Gabi"
        self.__primul_student.set_nume(self.__nume_nou)
        assert self.__primul_student.get_nume()== "Gabi"

        self.__primul_student = Student(self.__id, self.__nume)
        self.__al_doilea_student = Student(self.__primul_student.get_id(), self.__primul_student.get_nume())
        assert self.__primul_student == self.__al_doilea_student
        self.__al_doilea_student = Student(self.__primul_student.get_id()+1, self.__primul_student.get_nume())
        assert (self.__primul_student == self.__al_doilea_student) == False

    def __test_validare_disciplina(self):
        self.__id_valid = 0
        self.__nume_valid = "Mate"
        self.__profesor_vaild = "Cotfas"
        self.__prima_disciplina = Disciplina(self.__id_valid, self.__nume_valid, self.__profesor_vaild)
        self.__valid = ValidareDisciplina(self.__prima_disciplina)
        self.__lista = []
        self.__valid.validare_id_disciplina(self.__lista)
        self.__lista = [self.__prima_disciplina]   
        try:
            self.__valid.validare_id_disciplina(self.__lista)
            assert False
        except ValidationError as err:
             assert (str(err)=="Id deja existent!\n")


        self.__id_gresit = -5
        self.__nume_gresit = ""
        self.__profesor_gresit = ""
        self.__disciplina = Disciplina(self.__id_gresit, self.__nume_gresit, self.__profesor_gresit)
        try:
            self.__valid = ValidareDisciplina(self.__disciplina)
            self.__valid.is_disciplina_valid()
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNume invalid!\nProfesor invalid!\n"

            
        self.__disciplina = Disciplina(0, "Mate", "Delia")
        self.__valid = ValidareDisciplina(self.__disciplina)
        self.__valid.is_disciplina_valid()        


    def __test_validare_student(self):

        self.__id_valid = 0
        self.__nume_valid = "Cram"

        self.__primul_student_valid = Student(self.__id_valid, self.__nume_valid)
        
        self.__valid = ValidareStudent(self.__primul_student_valid)
        self.__lista = []
        self.__valid.validare_id_student(self.__lista)
        self.__lista = [self.__primul_student_valid]
        try:
            self.__valid.validare_id_student(self.__lista)
            assert False
        except ValidationError as err:
            assert (str(err)=="Id deja existent!\n")

        
        self.__id_gresit = -5
        self.__nume_gresit = ""
        student = Student(self.__id_gresit, self.__nume_gresit)
        try:
            self.__valid = ValidareStudent(student)
            self.__valid.is_student_valid()
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNume invalid!\n"

            
        self.__student = Student(0, "Marcel")
        self.__valid = ValidareStudent(self.__student)
        self.__valid.is_student_valid()

    def __test_repo_disciplina(self):
        self.__lista = []
        self.__repo_disciplina = DisciplinaRepo(self.__lista)
        self.__primua_disciplina = Disciplina(0, "Mate", "Cotfas")
        self.__a_doua_disciplina = Disciplina(1, "Romana", "Ghinea")
        assert self.__repo_disciplina.size_disciplina_repo() == 0
        self.__repo_disciplina.adauga_disciplina_repo(self.__prima_disciplina)
        assert self.__repo_disciplina.size_disciplina_repo() == 1
        self.__repo_disciplina.adauga_disciplina_repo(self.__a_doua_disciplina)

        self.__disciplina_gasit = self.__repo_disciplina.cauta_id_disciplina_repo(0)
        assert self.__disciplina_gasit == self.__prima_disciplina

        try:
            self.__disciplina_gasit = self.__repo_disciplina.cauta_id_disciplina_repo(3)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Disciplina inexistenta!\n"

        self.__disciplina_modificare = Disciplina(3, "Muzica", "Grosar")
        self.__repo_disciplina.modificare_id_disciplina_repo(self.__disciplina_modificare.get_id(), self.__disciplina_modificare)
        assert self.__prima_disciplina == self.__lista[0]
        assert self.__a_doua_disciplina == self.__lista[1]

        self.__disciplina_modificare = Disciplina(0, "Muzica", "Grosar")
        self.__repo_disciplina.modificare_id_disciplina_repo(self.__disciplina_modificare.get_id(), self.__disciplina_modificare)
        assert self.__disciplina_modificare == self.__lista[0]
        assert self.__a_doua_disciplina == self.__lista[1]

        self.__repo_disciplina.delete_id_disciplina_repo(3)
        assert self.__repo_disciplina.size_disciplina_repo() == 2
        self.__repo_disciplina.delete_id_disciplina_repo(1)
        assert self.__repo_disciplina.size_disciplina_repo() == 1
        assert self.__lista[0] == self.__prima_disciplina
        self.__repo_disciplina.delete_id_disciplina_repo(0)
        assert self.__repo_disciplina.size_disciplina_repo() == 0

    def __test_repo_student(self):
        self.__lista = []
        self.__repo_student = StudentRepo(self.__lista)
        self.__primul_student = Student(0, "Marc")
        self.__al_doilea_student = Student(1, "Ionel")
        assert self.__repo_student.size_student_repo() == 0
        self.__repo_student.adauga_student_repo(self.__primul_student)
        assert self.__repo_student.size_student_repo() == 1
        self.__repo_student.adauga_student_repo(self.__al_doilea_student)

        self.__student_gasit = self.__repo_student.cauta_id_student_repo(0)
        assert self.__student_gasit == self.__primul_student

        try:
            self.__student_gasit = self.__repo_student.cauta_id_student_repo(3)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Student inexistent!\n"
        self.__student_modificare = Student(3, "Mircel")
        self.__repo_student.modificare_id_student_repo(self.__student_modificare.get_id(), self.__student_modificare)
        assert self.__primul_student == self.__lista[0]
        assert self.__al_doilea_student == self.__lista[1]

        self.__student_modificare = Student(0, "Mircel")
        self.__repo_student.modificare_id_student_repo(self.__student_modificare.get_id(), self.__student_modificare)
        assert self.__student_modificare == self.__lista[0]
        assert self.__al_doilea_student == self.__lista[1]

        self.__repo_student.delete_id_student_repo(3)
        assert self.__repo_student.size_student_repo() == 2
        self.__repo_student.delete_id_student_repo(1)
        assert self.__repo_student.size_student_repo() == 1
        assert self.__lista[0] == self.__primul_student
        self.__repo_student.delete_id_student_repo(0)
        assert self.__repo_student.size_student_repo() == 0


    def __test_control_disciplina(self):
        self.__lista_studenti = []
        self.__lista_discipline = []
        self.__lista_note = []

        self.__disciplina_control = Disciplina(0, "Mate", "Cotfas")
        self.__params = [0, "Mate", "Cotfas",self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessDisciplina = BusinessDisciplina(self.__params, BusinessDisciplina.adaugare_disciplina_service)
        assert self.__lista_discipline[0] == self.__disciplina_control

        self.__disciplina_not_sters = Disciplina(1, "Romana", "Ghinea")
        self.__params = [1, "Romana", "Ghinea", self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessDisciplina = BusinessDisciplina(self.__params, BusinessDisciplina.adaugare_disciplina_service)
        self.__params = [0 ,self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessDisciplina = BusinessDisciplina(self.__params, BusinessDisciplina.sterge_disciplina_id_service)
        assert self.__lista_discipline[0] == self.__disciplina_not_sters


        self.__lista_discipline =[]
        self.__disciplina_mate = Disciplina(0, "Mate", "Cotfas")
        self.__disciplina_modificat= Disciplina(0, "Romana", "Ghinea")
        self.__params = [0, "Mate", "Cotfas", self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessDisciplina = BusinessDisciplina(self.__params, BusinessDisciplina.adaugare_disciplina_service)
        self.__params = [1, "Romana", "Ghinea",self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessDisciplina = BusinessDisciplina(self.__params, BusinessDisciplina.modifica_disciplina_service)
        assert self.__lista_discipline[0] == self.__disciplina_mate
        self.__params = [0, "Romana", "Ghinea",self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessDisciplina = BusinessDisciplina(self.__params, BusinessDisciplina.modifica_disciplina_service)
        assert self.__lista_discipline[0] == self.__disciplina_modificat

    def __test_control_student(self):
        self.__lista_studenti = []
        self.__lista_discipline = []
        self.__lista_note = []
        self.__student_control = Student(0, "Andrei")
        self.__params = [0, "Andrei",self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessStudent = BusinessStudent(self.__params, BusinessStudent.adaugare_student_service)
        assert self.__lista_studenti[0] == self.__student_control

        self.__student_not_sters = Student(1, "Marc")
        self.__params = [1, "Marc", self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessStudent = BusinessStudent(self.__params, BusinessStudent.adaugare_student_service)
        self.__params = [0 ,self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessStudent = BusinessStudent(self.__params, BusinessStudent.sterge_student_id_service)
        assert self.__lista_studenti[0] == self.__student_not_sters


        self.__lista_studenti =[]
        self.__student_marc = Student(0, "Marc")
        self.__student_modificat = Student(0, "Cram")
        self.__params = [0, "Marc", self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessStudent = BusinessStudent(self.__params, BusinessStudent.adaugare_student_service)
        self.__params = [1, "Cram",self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessStudent = BusinessStudent(self.__params, BusinessStudent.modifica_student_service)
        assert self.__lista_studenti[0] == self.__student_marc
        self.__params = [0, "Cram",self.__lista_studenti, self.__lista_discipline, self.__lista_note]
        self.__BusinessStudent = BusinessStudent(self.__params, BusinessStudent.modifica_student_service)
        assert self.__lista_studenti[0] == self.__student_modificat

        






    def ruleaza_toate_testele(self):
        """
        Functia responsabila pentru a rula testele, apelata in main
        """
        self.__test_domain_student()
        print("Teste domain student trecute!")
        self.__test_validare_student()
        print("Teste validare trecute!")
        self.__test_repo_student()
        print("Teste repo student trecute!")
        self.__test_control_student()
        print("Teste control student trecute!")

        self.__test_domain_disciplina()
        print("Teste de domain disciplina trecute!")
        self.__test_validare_disciplina()
        print("Teste de validare disciplina trecute!")
        self.__test_repo_disciplina()
        print("Teste repo disciplina trecute!")
        self.__test_control_disciplina()
        print("Teste control disciplina trecute!")

        input()
        

