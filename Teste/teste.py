from Erori.erori import RepoError
from Infrastructura.Studenti.domain import *
from Infrastructura.Discipline.domain import *
from Validare.Disciplina import *
from Validare.Student import *
from Infrastructura.Studenti.repo import *
from Infrastructura.Discipline.repo import *

class Teste:
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



    def __test_validare_student(self):

        self.__id_gresit = -5
        self.__nume_gresit = ""
        student = Student(self.__id_gresit, self.__nume_gresit)
        try:
            self.__valid = ValidareStudent(student)
            self.__valid.is_student_valid()
            assert False
        except ValueError as err:
            assert str(err) == "Id invalid!\nNume invalid!\n"

            
        self.__student = Student(0, "Marcel")
        self.__valid = ValidareStudent(self.__student)
        self.__valid.is_student_valid()

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
            assert str(err) == "Eroare repo!\n"
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
        input()


