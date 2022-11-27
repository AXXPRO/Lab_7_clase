
from Business.control import ServiceDisciplina, ServiceNota, ServiceStudent
from Erori.erori import RepoError
from Infrastructura.Medii.domain import Medii
from Infrastructura.Note.domain import Nota
from Infrastructura.Note.repo import NotaRepo
from Infrastructura.Studenti.domain import *
from Infrastructura.Discipline.domain import *
from Validare.Disciplina import *
from Validare.Note import ValidareNota
from Validare.Student import *
from Infrastructura.Studenti.repo import *
from Infrastructura.Discipline.repo import *

class Teste:

    def __test_domain_nota(self):
        """
        Testele pentru functiile domain asociate note
        """
        self.__id = 0
        self.__student= Student(0, "Eu")
        self.__disciplina = Disciplina(0, "Mate", "Cotfas")
        self.__valoare = 10
        self.__prima_nota = Nota(self.__id, self.__student, self.__disciplina, self.__valoare)


        assert self.__prima_nota.get_id() == 0
        assert self.__prima_nota.get_student() == self.__student
        assert self.__prima_nota.get_disciplina() == self.__disciplina
        assert self.__prima_nota.get_valoare() == self.__valoare

        self.__student_nou= Student(1, "Tu")
        self.__disciplina_nou = Disciplina(0, "Rom", "Ghinea")
        self.__valoare_nou = 5
        self.__a_doua_nota = Nota(self.__id, self.__student_nou, self.__disciplina_nou, self.__valoare_nou)



        self.__prima_nota.set_student(self.__student_nou)
        self.__prima_nota.set_disciplina(self.__disciplina_nou)
        self.__prima_nota.set_valoare(self.__valoare_nou)
        
        assert self.__prima_nota.get_student() == self.__student_nou
        assert self.__prima_nota.get_disciplina() == self.__disciplina_nou
        assert self.__prima_nota.get_valoare() == self.__valoare_nou

        self.__prima_nota = Nota(self.__id, self.__student, self.__disciplina, self.__valoare)
        self.__a_doua_nota = Nota(self.__prima_nota.get_id(),self.__prima_nota.get_student(),self.__prima_nota.get_disciplina(),self.__prima_nota.get_valoare())
        assert self.__prima_nota == self.__a_doua_nota

        #self.__a_doua_materie = Disciplina(self.__prima_materie.get_id()+1,self.__prima_materie.get_nume(),self.__prima_materie.get_profesor())


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



    def __test_validare_nota(self):
        self.__id_valid = 0
        self.__valoare_valid = 7
        self.__student_valid = Student(0, "Marius")
        self.__disciplina_valid = Disciplina(0, "Mate", "Cotfas")
        self.__prima_nota = Nota(self.__id_valid, self.__student_valid, self.__disciplina_valid, self.__valoare_valid)
        self.__valid = ValidareNota(self.__prima_nota)
        self.__valid.is_nota_valid()


        self.__id_gresit = -5
        self.__valoare_gresit = "f"
        self.__nota = Nota(self.__id_gresit, self.__student_valid, self.__disciplina_valid, self.__valoare_gresit)
        try:
            self.__valid = ValidareNota(self.__nota)
            self.__valid.is_nota_valid()
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNota invalida!\n"





    def __test_validare_disciplina(self):
      

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
        self.__valid = ValidareStudent(self.__primul_student_valid)
        
        self.__id_gresit = -5
        self.__nume_gresit = ""
        student = Student(self.__id_gresit, self.__nume_gresit)
        try:
            self.__valid = ValidareStudent(student)
            self.__valid.is_student_valid()
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNume invalid!\n"

            


    def __test_repo_nota(self):
   
        self.__REPO_Nota = NotaRepo()
        self.__prima_nota = Nota(0, Student(0, "Marc"), Disciplina(0, "Mate", "Cotfas"), 8)
        self.__a_doua_nota = Nota(1, Student(1, "George"), Disciplina(0, "Romana", "Ghinea"), 2)

        assert self.__REPO_Nota.size_nota_repo() == 0
        self.__REPO_Nota.adauga_nota_repo(self.__prima_nota)
        assert self.__REPO_Nota.size_nota_repo() == 1
        self.__REPO_Nota.adauga_nota_repo(self.__a_doua_nota) 

        self.__lista_note = self.__REPO_Nota.get_list()
        assert self.__lista_note[0] == self.__prima_nota
        assert self.__lista_note[1] == self.__a_doua_nota

        self.__nota_gasit = self.__REPO_Nota.cauta_id_nota_repo(0)
        assert self.__nota_gasit == self.__prima_nota

        try:
            self.__nota_gasit = self.__REPO_Nota.cauta_id_nota_repo(3)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Nota inexistenta!\n"
        
        self.__nota_modificare = Nota(0, Student(3, "Simeon"), Disciplina(4, "Informatica", "Stefan"), 10)
        self.__REPO_Nota.modificare_id_nota_repo(self.__nota_modificare.get_id(), self.__nota_modificare)

        self.__nota_cautata = self.__REPO_Nota.cauta_id_nota_repo(self.__prima_nota.get_id())
        assert self.__nota_cautata == self.__nota_modificare

        self.__nota_cautata = self.__REPO_Nota.cauta_id_nota_repo(self.__a_doua_nota.get_id())
        assert self.__nota_cautata == self.__a_doua_nota

        self.__REPO_Nota.delete_id_nota_repo(3)
        assert self.__REPO_Nota.size_nota_repo() == 2
        self.__REPO_Nota.delete_id_nota_repo(1)
        assert self.__REPO_Nota.size_nota_repo() == 1

        try:
            self.__REPO_Nota.cauta_id_nota_repo(1)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Nota inexistenta!\n"
        
        self.__REPO_Nota.delete_id_nota_repo(0)
        assert self.__REPO_Nota.size_nota_repo() == 0

        
    def __test_repo_disciplina(self):
       
        self.__repo_disciplina = DisciplinaRepo()
        self.__prima_disciplina = Disciplina(0, "Mate", "Cotfas")
        self.__a_doua_disciplina = Disciplina(1, "Romana", "Ghinea")
        assert self.__repo_disciplina.size_disciplina_repo() == 0
        self.__repo_disciplina.adauga_disciplina_repo(self.__prima_disciplina)
        assert self.__repo_disciplina.size_disciplina_repo() == 1
        self.__repo_disciplina.adauga_disciplina_repo(self.__a_doua_disciplina)


        self.__lista_discipline = self.__repo_disciplina.get_list()
        assert self.__lista_discipline[0] == self.__prima_disciplina
        assert self.__lista_discipline[1] == self.__a_doua_disciplina

        self.__disciplina_gasit = self.__repo_disciplina.cauta_id_disciplina_repo(0)
        assert self.__disciplina_gasit == self.__prima_disciplina

        try:
            self.__disciplina_gasit = self.__repo_disciplina.cauta_id_disciplina_repo(3)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Disciplina inexistenta!\n"


        self.__disciplina_modificare = Disciplina(0, "Muzica", "Grosar")
        self.__repo_disciplina.modificare_id_disciplina_repo(self.__disciplina_modificare.get_id(), self.__disciplina_modificare)
        
        self.__disciplina_cautata = self.__repo_disciplina.cauta_id_disciplina_repo(self.__prima_disciplina.get_id())
        assert self.__disciplina_cautata == self.__disciplina_modificare

        self.__disciplina_cautata = self.__repo_disciplina.cauta_id_disciplina_repo(self.__a_doua_disciplina.get_id())
        assert self.__disciplina_cautata == self.__a_doua_disciplina


        self.__repo_disciplina.delete_id_disciplina_repo(3)
        assert self.__repo_disciplina.size_disciplina_repo() == 2
        self.__repo_disciplina.delete_id_disciplina_repo(1)
        assert self.__repo_disciplina.size_disciplina_repo() == 1
        try:
            self.__repo_disciplina.cauta_id_disciplina_repo(1)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Disciplina inexistenta!\n"
        
        self.__repo_disciplina.delete_id_disciplina_repo(0)
        assert self.__repo_disciplina.size_disciplina_repo() == 0

    def __test_repo_student(self):
        self.__repo_student = StudentRepo()
        self.__primul_student = Student(0, "Marc")
        self.__al_doilea_student = Student(1, "Ionel")
        assert self.__repo_student.size_student_repo() == 0
        self.__repo_student.adauga_student_repo(self.__primul_student)
        assert self.__repo_student.size_student_repo() == 1
        self.__repo_student.adauga_student_repo(self.__al_doilea_student)

        self.__lista_studenti = self.__repo_student.get_list()
        assert self.__lista_studenti[0] == self.__primul_student
        assert self.__lista_studenti[1] == self.__al_doilea_student

        self.__student_gasit = self.__repo_student.cauta_id_student_repo(0)
        assert self.__student_gasit == self.__primul_student

        try:
            self.__student_gasit = self.__repo_student.cauta_id_student_repo(3)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Student inexistent!\n"

        self.__student_modificare = Student(0, "Mircel")
        self.__repo_student.modificare_id_student_repo(self.__student_modificare.get_id(), self.__student_modificare)
        
        self.__student_cautat = self.__repo_student.cauta_id_student_repo(self.__primul_student.get_id())
        assert self.__student_cautat == self.__student_modificare

        self.__student_cautat = self.__repo_student.cauta_id_student_repo(self.__al_doilea_student.get_id())
        assert self.__student_cautat == self.__al_doilea_student

        self.__repo_student.delete_id_student_repo(3)
        assert self.__repo_student.size_student_repo() == 2
        self.__repo_student.delete_id_student_repo(1)
        assert self.__repo_student.size_student_repo() == 1
        
        try:
            self.__repo_student.cauta_id_student_repo(1)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Student inexistent!\n"        
        
        self.__repo_student.delete_id_student_repo(0)
        assert self.__repo_student.size_student_repo() == 0



    def __test_control_nota(self):
        self.__REPO_Nota = NotaRepo()
        self.__REPO_Student = StudentRepo()
        self.__REPO_Disciplina = DisciplinaRepo()
        self.__SERVICE_disciplina = ServiceDisciplina(self.__REPO_Disciplina)
        self.__SERVICE_student = ServiceStudent(self.__REPO_Student)
        self.__SERVICE_nota = ServiceNota(self.__REPO_Student, self.__REPO_Disciplina,self.__REPO_Nota)


        self.__SERVICE_disciplina.adaugare_disciplina_service([0, "Mate", "Cotfas"])
        self.__SERVICE_student.adaugare_student_service([0,"Marcel"])

        self.__nota_control = Nota(0, Student(0, "Marcel"), Disciplina(0, "Mate", "Cotfas"), 8)

        self.__SERVICE_nota.adaugare_nota_service([0, 0, 0,8])

        self.__nota_cautat = self.__REPO_Nota.cauta_id_nota_repo(0)
        assert self.__nota_cautat == self.__nota_control

        try:
            self.__SERVICE_nota.adaugare_nota_service([0, 0, 0,8])
            assert False
        except RepoError as err:
            assert str(err) == "Id deja existent!\n"
        
        try:
            self.__SERVICE_nota.adaugare_nota_service([1, 1, 1,8])
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Student inexistent!\nEroare repo: Disciplina inexistenta!\n"

        try:
            self.__SERVICE_nota.adaugare_nota_service([0, 0, 0,-8])
            assert False
        except ValidationError as err:
            assert str(err) == "Nota invalida!\n"


        self.__SERVICE_disciplina.adaugare_disciplina_service([1, "Romana", "Ghinea"])
        self.__SERVICE_student.adaugare_student_service([1, "Gigel"])
        self.__nota_modificat = Nota(0, Student(1, "Gigel"), Disciplina(1, "Romana", "Ghinea"), 4)

        self.__SERVICE_nota.modifica_nota_service([0, 1, 1, 4])
        self.__nota_cautat = self.__REPO_Nota.cauta_id_nota_repo(0)
        assert self.__nota_cautat == self.__nota_modificat

        try:
            self.__SERVICE_nota.modifica_nota_service([-9,0, 0, 213])
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNota invalida!\n"


        self.__SERVICE_nota.sterge_student_id_service([1])
        self.__SERVICE_nota.sterge_disciplina_id_service([1])
        try:
            self.__REPO_Student.cauta_id_student_repo(1)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Student inexistent!\n"
        try:
            self.__REPO_Disciplina.cauta_id_disciplina_repo(1)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Disciplina inexistenta!\n"

        try:
            self.__REPO_Nota.cauta_id_nota_repo(0)
            assert False
        except RepoError as err:
            assert str(err) == "Eroare repo: Nota inexistenta!\n"



    def __test_control_disciplina(self):
        self.__REPO_Disciplina = DisciplinaRepo()
        self.__SERVICE_disciplina = ServiceDisciplina(self.__REPO_Disciplina)

        self.__disciplina_control = Disciplina(0, "Mate", "Cotfas")
        self.__SERVICE_disciplina.adaugare_disciplina_service([0, "Mate", "Cotfas"])
        self.__disciplina_cautat = self.__REPO_Disciplina.cauta_id_disciplina_repo(0)
        assert self.__disciplina_cautat == self.__disciplina_control

        try:
            self.__SERVICE_disciplina.adaugare_disciplina_service([0, "Marcel", "Cotfas"])
            assert False
        except RepoError as err:
            assert str(err) == "Id deja existent!\n"
        
        try:
            self.__SERVICE_disciplina.adaugare_disciplina_service([-5, "", ""])
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNume invalid!\nProfesor invalid!\n"

        self.__disciplina_modificat = Disciplina(0, "Romana", "Ghinea")
        self.__SERVICE_disciplina.modifica_disciplina_service([0, "Romana", "Ghinea"])
        self.__disciplina_cautat = self.__REPO_Disciplina.cauta_id_disciplina_repo(0)
        assert self.__disciplina_cautat == self.__disciplina_modificat

        try:
            self.__SERVICE_disciplina.modifica_disciplina_service([-9,"", ""])
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNume invalid!\nProfesor invalid!\n"

    def __test_control_student(self):
        self.__REPO_student = StudentRepo()
        self.__SERVICE_student = ServiceStudent(self.__REPO_student)

        self.__student_control = Student(0, "Marcel")
        self.__SERVICE_student.adaugare_student_service([0, "Marcel"])
        self.__student_cautat = self.__REPO_student.cauta_id_student_repo(0)
        assert self.__student_cautat == self.__student_control

        try:
            self.__SERVICE_student.adaugare_student_service([0, "Mirel"])
            assert False
        except RepoError as err:
            assert str(err) == "Id deja existent!\n"
        
        try:
            self.__SERVICE_student.adaugare_student_service([-5, ""])
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNume invalid!\n"

        self.__student_modificat = Student(0, "Yelod")
        self.__SERVICE_student.modifica_student_service([0, "Yelod"])
        self.__student_cautat = self.__REPO_student.cauta_id_student_repo(0)
        assert self.__student_cautat == self.__student_modificat

        try:
            self.__SERVICE_student.modifica_student_service([-9,""])
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNume invalid!\n" 
    def __test_statistici(self):
        """Functia resposnabila pentru a testa crearea de statistici"""

        self.__REPO_Nota = NotaRepo()
        self.__REPO_Student = StudentRepo()
        self.__REPO_Disciplina = DisciplinaRepo()
        self.__SERVICE_disciplina = ServiceDisciplina(self.__REPO_Disciplina)
        self.__SERVICE_student = ServiceStudent(self.__REPO_Student)
        self.__SERVICE_nota = ServiceNota(self.__REPO_Student, self.__REPO_Disciplina,self.__REPO_Nota)    


        student1 = Student(0, "Marc")
        student2 = Student(1, "Alex")
        student3 = Student(2, "Alex")
        disciplina = Disciplina(0, "Mate", "Delia")

        self.__SERVICE_student.adaugare_student_service([0, "Marc"])
        self.__SERVICE_student.adaugare_student_service([1, "Alex"])
        self.__SERVICE_student.adaugare_student_service([2, "Alex"])
        self.__SERVICE_disciplina.adaugare_disciplina_service([0, "Mate", "Delia"])


        nota1 = Nota(0, student1, disciplina, 9)
        nota2 = Nota(1, student2, disciplina, 8)
        nota3 = Nota(2, student3, disciplina, 7)
        self.__SERVICE_nota.adaugare_nota_service([0,student1.get_id(),disciplina.get_id(),9])
        self.__SERVICE_nota.adaugare_nota_service([1,student2.get_id(),disciplina.get_id(),8])
        self.__SERVICE_nota.adaugare_nota_service([2,student3.get_id(),disciplina.get_id(),7])
        lista_ordonata = self.__SERVICE_nota.lista_note_ordonate_service([0])

        # for nota in lista_ordonata:
        #     print(nota.get_student().get_nume() , nota.get_valoare())
        # input()

        # for nota in [nota2, nota3, nota1]:
        #     print(nota.get_student().get_nume() , nota.get_valoare())
        # input()
        assert lista_ordonata == [nota2, nota3, nota1]


        self.__SERVICE_nota.adaugare_nota_service([3,student1.get_id(),disciplina.get_id(),10])
        self.__SERVICE_nota.adaugare_nota_service([4,student2.get_id(),disciplina.get_id(),2])
        self.__SERVICE_nota.adaugare_nota_service([5,student3.get_id(),disciplina.get_id(),1])
        lista = self.__SERVICE_nota.lista_medii_service()
        assert len(lista) == 1
        assert lista[0].get_nume() == "Marc" 



    def __test_domain_medii(self):
        """
        teste domain medii
        """
        medie1 = Medii(0, "Marcel", 7.65)
        medie2= Medii(1, "Marcel", 7.65)

        assert medie1.get_nume() == "Marcel"
        assert medie2.get_medie() == 7.65
        assert medie1 == medie2

    def ruleaza_toate_testele(self):
        """
        Functia responsabila pentru a rula testele, apelata in main
        """
        self.__test_domain_student()
        print("Teste domain student trecute!")
        self.__test_validare_student()
        print("Teste validare student trecute!")
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


        self.__test_domain_nota()
        print("Teste domain disciplina trecute")
        self.__test_validare_nota()
        print("Teste de validare note trecute!")
        self.__test_repo_nota()
        print("Teste repo nota trecute!")
        self.__test_control_nota()
        print("Teste control nota trecute!")

        self.__test_domain_medii
        print("Teste de domain medii trecute!")
        self.__test_statistici()
        print("Teste de statistici trecute!")
        input()

        

