import unittest
from Business.control import ServiceDisciplina, ServiceNota, ServiceStudent
from Erori.erori import RepoError, ValidationError
from Infrastructura.Discipline.domain import Disciplina
from Infrastructura.Discipline.repo import DisciplinaRepo
from Infrastructura.Medii.domain import Medii
from Infrastructura.Note.domain import Nota
from Infrastructura.Note.repo import NotaRepo, NotaRepoFisiere
from Infrastructura.NoteDTO.domain import NotaDTO

from Infrastructura.Studenti.domain import Student
from Infrastructura.Studenti.repo import StudentRepo
from Validare.Disciplina import ValidareDisciplina
from Validare.Note import ValidareNota
from Validare.Student import ValidareStudent
class TestDomainMedii(unittest.TestCase):
    def setUp(self):
        self.__medie1 = Medii(0, "Marcel", 7.65)
        self.__medie2= Medii(1, "Marcel", 7.65)     
    def tearDown(self):
        pass
    def testGetMedie(self):
        self.assertEqual(self.__medie1.get_nume() , "Marcel")
        self.assertEqual( self.__medie2.get_medie() , 7.65)
        self.assertEqual( self.__medie1 , self.__medie2)
class TestDomainStudent(unittest.TestCase):
    def setUp(self):
        self.__id = 0
        self.__nume = "Carol"
        self.__primul_student = Student(self.__id, self.__nume)

    def tearDown(self):
        pass
    def testGetStudent(self):
        self.assertEqual(self.__primul_student.get_id() , 0)
        self.assertEqual(self.__primul_student.get_nume() ,"Carol")
    def testSetStudent(self):
        self.__nume_nou = "Gabi"
        self.__primul_student.set_nume(self.__nume_nou)
        self.assertEqual( self.__primul_student.get_nume(), "Gabi")    


    def testEgalitateStudent(self):
        self.__al_doilea_student = Student(self.__primul_student.get_id(), self.__primul_student.get_nume())
        self.assertEqual(self.__primul_student ,self.__al_doilea_student)
        self.__al_doilea_student = Student(self.__primul_student.get_id()+1, self.__primul_student.get_nume())
        self.assertNotEqual (self.__primul_student, self.__al_doilea_student)
class TestDomainNotaDTO(unittest.TestCase):
    def setUp(self):
        self.__id_nota = 0
        self.__id_student = 1
        self.__id_dsiciplina = 2
        self.__valoare = 7
        self.__prima_nota_dto = NotaDTO(self.__id_nota,self.__id_student, self.__id_dsiciplina,self.__valoare)
        self.__doua_nota_dto = NotaDTO(0,1,2,7)
        self.__treia_nota_dto = NotaDTO(1,7,3,1)

    def tearDown(self):
        pass
    def testGetNotaDTO(self):
        self.assertEqual(self.__prima_nota_dto.get_id_nota(), 0)
        self.assertEqual(self.__prima_nota_dto.get_id_student(), 1)
        self.assertEqual(self.__prima_nota_dto.get_id_disciplina(), 2)
        self.assertEqual(self.__prima_nota_dto.get_valoare(), 7)
    def testSetNotaDTO(self):
        self.__prima_nota_dto.set_id_student(2)
        self.__prima_nota_dto.set_id_disciplina(3)
        self.__prima_nota_dto.set_valoare(4)

        self.assertEqual(self.__prima_nota_dto.get_id_nota(), 0)
        self.assertEqual(self.__prima_nota_dto.get_id_student(), 2)
        self.assertEqual(self.__prima_nota_dto.get_id_disciplina(), 3)
        self.assertEqual(self.__prima_nota_dto.get_valoare(), 4)

    def testEqualNotaDTO(self):
        self.assertEqual(self.__prima_nota_dto, self.__doua_nota_dto)
        self.assertNotEqual(self.__prima_nota_dto, self.__treia_nota_dto)
class TestDomainDisciplina(unittest.TestCase):
    def setUp(self):
        self.__id = 0
        self.__nume = "Mate"
        self.__profesor = "Cotfas"
        self.__prima_materie = Disciplina(self.__id, self.__nume, self.__profesor)
        self.__nume_nou = "Romana"
        self.__profesor_nou = "Ghinea"
    def tearDown(self):
        pass
    def testGetter(self):
        assert self.__prima_materie.get_id() == 0
        assert self.__prima_materie.get_nume() == "Mate"
        assert self.__prima_materie.get_profesor() == "Cotfas"
    def testSetter(self):

        self.__prima_materie.set_nume(self.__nume_nou)
        self.__prima_materie.set_profesor(self.__profesor_nou)
        assert self.__prima_materie.get_nume() == "Romana"
        assert self.__prima_materie.get_profesor() == "Ghinea"

        self.__prima_materie = Disciplina(self.__id, self.__nume, self.__profesor)
        self.__a_doua_materie = Disciplina(self.__prima_materie.get_id(),self.__prima_materie.get_nume(),self.__prima_materie.get_profesor())
        assert self.__prima_materie == self.__a_doua_materie

        self.__a_doua_materie = Disciplina(self.__prima_materie.get_id()+1,self.__prima_materie.get_nume(),self.__prima_materie.get_profesor())
        assert (self.__prima_materie == self.__a_doua_materie) == False

class TestValidareStudent(unittest.TestCase):
    def setUp(self):
        self.__id_valid = 0
        self.__nume_valid = "Cram"
        self.__primul_student_valid = Student(self.__id_valid, self.__nume_valid)

        self.__id_gresit = -5
        self.__nume_gresit = ""
        self.__student_gresit = Student(self.__id_gresit, self.__nume_gresit)
    def tearDown(self):
        pass
    def testValdiare(self):
        self.__valid = ValidareStudent(self.__primul_student_valid)
        self.__valid.is_student_valid()
        try:
            self.__valid = ValidareStudent(self.__student_gresit)
            self.__valid.is_student_valid()
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNume invalid!\n"       
class TestValidareDisciplina(unittest.TestCase):
    def setUp(self):
        self.__id_gresit = -5
        self.__nume_gresit = ""
        self.__profesor_gresit = ""
        self.__disciplina_gresita = Disciplina(self.__id_gresit, self.__nume_gresit, self.__profesor_gresit)

        self.__id= 0
        self.__nume = "Mate"
        self.__profesor = "Delia"
        self.__disciplina = Disciplina(0, "Mate", "Delia")
    def tearDown(self):
        pass
    def testValdiare(self):
        try:
            self.__valid = ValidareDisciplina(self.__disciplina_gresita)
            self.__valid.is_disciplina_valid()
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNume invalid!\nProfesor invalid!\n"
        self.__valid = ValidareDisciplina(self.__disciplina)
        self.__valid.is_disciplina_valid()
class TestValidareNotaDTO(unittest.TestCase):
    def setUp(self):
        self.__id_gresit = -5
        self.__id_student = 0
        self.__id_disciplina = 0
        self.__valoare_gresita = -6.5
        self.__nota_gresita = NotaDTO(self.__id_gresit,self.__id_student,self.__id_disciplina,self.__valoare_gresita)

        self.__id = 0
        self.__valoare = 10
        self.__nota = NotaDTO(self.__id,self.__id_student,self.__id_disciplina,self.__valoare)
    def tearDown(self):
        pass
    def testValdiare(self):
        try:
            self.__valid = ValidareNota(self.__nota_gresita)
            self.__valid.is_nota_valid()
            assert False
        except ValidationError as err:
            assert str(err) == "Id invalid!\nNota invalida!\n"
        self.__valid = ValidareNota(self.__nota)
        self.__valid.is_nota_valid()

class TestRepoNotaDTO(unittest.TestCase):
    def setUp(self):
        self.__path = r'notedto_test.txt'
        self.__prima_nota_dto = NotaDTO(0, 0, 0, 7)
        self.__doua_nota_dto = NotaDTO(0, 1, 1, 9)
        self.__treia_nota_dto = NotaDTO(2,1, 1, 10)
        self.REPO_NotaDTO = NotaRepoFisiere(self.__path)

    def tearDown(self):
        self.REPO_NotaDTO.empty()
    def testAdaugaNotaDTO(self):
        self.REPO_NotaDTO.adauga_nota_repo(self.__prima_nota_dto)
        self.assertRaises(RepoError, self.REPO_NotaDTO.adauga_nota_repo ,self.__doua_nota_dto)

        self.REPO_NotaDTO.adauga_nota_repo(self.__treia_nota_dto)
        self.assertEqual(self.REPO_NotaDTO.size_nota_repo(), 2)
    def testStergeNotaDTO(self):
        self.REPO_NotaDTO.adauga_nota_repo(self.__prima_nota_dto)
        self.REPO_NotaDTO.delete_id_nota_repo(self.__prima_nota_dto.get_id_nota())
        self.assertEqual(self.REPO_NotaDTO.size_nota_repo(), 0)
    def testCautaNotaDTO(self):
        self.REPO_NotaDTO.adauga_nota_repo(self.__prima_nota_dto)
        nota_gasita = self.REPO_NotaDTO.cauta_id_nota_repo(self.__prima_nota_dto.get_id_nota())
        self.assertEqual(nota_gasita, self.__prima_nota_dto)
    def testModificaNotaDTO(self):
        self.REPO_NotaDTO.adauga_nota_repo(self.__prima_nota_dto)
        self.REPO_NotaDTO.modificare_id_nota_repo(self.__prima_nota_dto.get_id_nota(), self.__doua_nota_dto)
        self.assertEqual(self.__doua_nota_dto, self.REPO_NotaDTO.cauta_id_nota_repo(self.__prima_nota_dto.get_id_nota()))


class TestRepoStudent(unittest.TestCase):
    
    
    def setUp(self):
        self.__repo_student = StudentRepo()
        self.__primul_student = Student(0, "Marc")
        self.__al_doilea_student = Student(1, "Ionel")

    def tearDown(self):
        pass
    def testAdaugareStudent(self):
        self.assertEqual( self.__repo_student.size_student_repo() ,0 )
        self.__repo_student.adauga_student_repo(self.__primul_student)
        self.assertEqual( self.__repo_student.size_student_repo(),1)
        self.__repo_student.adauga_student_repo(self.__al_doilea_student)
        self.__lista_studenti = self.__repo_student.get_list()
        self.assertEqual(self.__lista_studenti[0] ,self.__primul_student)
        self.assertEqual(self.__lista_studenti[1] , self.__al_doilea_student)

    def testCautaStudent(self):
        self.__repo_student.adauga_student_repo(self.__primul_student)  
        self.__repo_student.adauga_student_repo(self.__al_doilea_student)      
        self.__student_gasit = self.__repo_student.cauta_id_student_repo(0)
        self.assertEqual(self.__student_gasit, self.__primul_student)
        self.assertRaises(RepoError, self.__repo_student.cauta_id_student_repo, 3)
    def testModificaStudent(self):
        self.__repo_student.adauga_student_repo(self.__primul_student)  
        self.__repo_student.adauga_student_repo(self.__al_doilea_student)   
        self.__student_modificare = Student(0, "Mircel")
        self.__repo_student.modificare_id_student_repo(self.__student_modificare.get_id(), self.__student_modificare)
        
        self.__student_cautat = self.__repo_student.cauta_id_student_repo(self.__primul_student.get_id())
        self.assertEqual( self.__student_cautat, self.__student_modificare)

        self.__student_cautat = self.__repo_student.cauta_id_student_repo(self.__al_doilea_student.get_id())
        self.assertEqual (self.__student_cautat, self.__al_doilea_student)
    def testStergeStudent(self):

        self.__repo_student.adauga_student_repo(self.__primul_student)  
        self.__repo_student.adauga_student_repo(self.__al_doilea_student)   

        self.__repo_student.delete_id_student_repo(3)
        self.assertEqual( self.__repo_student.size_student_repo() , 2)
        self.__repo_student.delete_id_student_repo(1)
        self.assertEqual( self.__repo_student.size_student_repo() , 1)
        self.__repo_student.delete_id_student_repo(0)
        self.assertEqual( self.__repo_student.size_student_repo() , 0)


class TestRepoDisciplina(unittest.TestCase):
    def setUp(self):
        self.__repo_disciplina = DisciplinaRepo()
        self.__prima_disciplina = Disciplina(0, "Mate", "Cotfas")
        self.__a_doua_disciplina = Disciplina(1, "Romana", "Ghinea")

    def tearDown(self):
        pass     
    def testAdaugareDisciplina(self):
        self.assertEqual( self.__repo_disciplina.size_disciplina_repo() ,0 )
        self.__repo_disciplina.adauga_disciplina_repo(self.__prima_disciplina)
        self.assertEqual( self.__repo_disciplina.size_disciplina_repo(),1)
        self.__repo_disciplina.adauga_disciplina_repo(self.__a_doua_disciplina)
        self.__lista_discipline = self.__repo_disciplina.get_list()
        self.assertEqual (self.__lista_discipline[0] , self.__prima_disciplina)
        self.assertEqual (self.__lista_discipline[1] , self.__a_doua_disciplina)

    def testCautaDisciplina(self):
        self.__repo_disciplina.adauga_disciplina_repo(self.__prima_disciplina)
        self.__repo_disciplina.adauga_disciplina_repo(self.__a_doua_disciplina)

        self.__disciplina_gasit = self.__repo_disciplina.cauta_id_disciplina_repo(0)
        self.assertEqual(self.__disciplina_gasit, self.__prima_disciplina)
        self.assertRaises(RepoError,self.__repo_disciplina.cauta_id_disciplina_repo, 3)
    def testModificaDisciplina(self):
        self.__repo_disciplina.adauga_disciplina_repo(self.__prima_disciplina)
        self.__repo_disciplina.adauga_disciplina_repo(self.__a_doua_disciplina)  
        self.__disciplina_modificare = Disciplina(0, "Muzica", "Grosar")

        self.__repo_disciplina.modificare_id_disciplina_repo(self.__disciplina_modificare.get_id(), self.__disciplina_modificare)
        
        self.__disciplina_cautata = self.__repo_disciplina.cauta_id_disciplina_repo(self.__prima_disciplina.get_id())
        self.assertEqual (self.__disciplina_cautata, self.__disciplina_modificare)


        self.__disciplina_cautata = self.__repo_disciplina.cauta_id_disciplina_repo(self.__a_doua_disciplina.get_id())
        self.assertEqual( self.__disciplina_cautata , self.__a_doua_disciplina)
    def testStergeDisciplina(self):
        self.__repo_disciplina.adauga_disciplina_repo(self.__prima_disciplina)
        self.__repo_disciplina.adauga_disciplina_repo(self.__a_doua_disciplina)  
        self.__repo_disciplina.delete_id_disciplina_repo(3)
        self.assertEqual (self.__repo_disciplina.size_disciplina_repo() , 2)
        self.__repo_disciplina.delete_id_disciplina_repo(1)
        self.assertEqual (self.__repo_disciplina.size_disciplina_repo() , 1)
        self.__repo_disciplina.delete_id_disciplina_repo(0)
        self.assertEqual (self.__repo_disciplina.size_disciplina_repo() , 0)

class TestControlStudent(unittest.TestCase):
    def setUp(self):
        self.__REPO_student = StudentRepo()
        self.__SERVICE_student = ServiceStudent(self.__REPO_student)

        self.__student_control = Student(0, "Marcel")
        self.__SERVICE_student.adaugare_student_service([0, "Marcel"])

    def tearDown(self):
        pass
    
    def testCautareStudent(self):
        self.__student_cautat = self.__REPO_student.cauta_id_student_repo(0)
        self.assertEqual (self.__student_cautat , self.__student_control)
    def testAdaugareStudent(self):
        self.assertRaises(RepoError, self.__SERVICE_student.adaugare_student_service, [0, "Mirel"])
        self.assertRaises(ValidationError, self.__SERVICE_student.adaugare_student_service,[-5, ""])
    def testModificareStudent(self):
        self.__student_modificat = Student(0, "Yelod")
        self.__SERVICE_student.modifica_student_service([0, "Yelod"])
        self.__student_cautat = self.__REPO_student.cauta_id_student_repo(0)
        self.assertEqual( self.__student_cautat , self.__student_modificat)
        self.assertRaises(ValidationError, self.__SERVICE_student.modifica_student_service, [-9,""])


class TestControlDisciplina(unittest.TestCase):
    def setUp(self):
        self.__REPO_Disciplina = DisciplinaRepo()
        self.__SERVICE_disciplina = ServiceDisciplina(self.__REPO_Disciplina)

        self.__disciplina_control = Disciplina(0, "Mate", "Cotfas")
        self.__SERVICE_disciplina.adaugare_disciplina_service([0, "Mate", "Cotfas"])
    def tearDown(self):
        pass
    def testCautareDisciplina(self):
        self.__disciplina_cautat = self.__REPO_Disciplina.cauta_id_disciplina_repo(0)
        self.assertEqual (self.__disciplina_cautat , self.__disciplina_control)
    def testAdaugareDisciplina(self):
        self.assertRaises(RepoError, self.__SERVICE_disciplina.adaugare_disciplina_service, [0, "Marcel", "Cotfas"])
        self.assertRaises(ValidationError,  self.__SERVICE_disciplina.adaugare_disciplina_service, [-5, "", ""])
    def testModificareDisciplina(self):
        self.__disciplina_modificat = Disciplina(0, "Romana", "Ghinea")
        self.__SERVICE_disciplina.modifica_disciplina_service([0, "Romana", "Ghinea"])
        self.__disciplina_cautat = self.__REPO_Disciplina.cauta_id_disciplina_repo(0)
        self.assertEqual( self.__disciplina_cautat , self.__disciplina_modificat)
        self.assertRaises(ValidationError, self.__SERVICE_disciplina.modifica_disciplina_service, [-9,"", ""])

class TestControlNota(unittest.TestCase):
    def setUp(self):
        self.__REPO_Nota = NotaRepoFisiere("notedto_test.txt")
        self.__REPO_Student = StudentRepo()
        self.__REPO_Disciplina = DisciplinaRepo()
        self.__SERVICE_disciplina = ServiceDisciplina(self.__REPO_Disciplina)
        self.__SERVICE_student = ServiceStudent(self.__REPO_Student)
        self.__SERVICE_nota = ServiceNota(self.__REPO_Student, self.__REPO_Disciplina,self.__REPO_Nota)
        self.__SERVICE_disciplina.adaugare_disciplina_service([0, "Mate", "Cotfas"])
        self.__SERVICE_student.adaugare_student_service([0,"Marcel"])
        self.__nota_control = NotaDTO(0, 0,0, 8)

        self.__SERVICE_disciplina.adaugare_disciplina_service([1, "Romana", "Ghinea"])
        self.__SERVICE_student.adaugare_student_service([1, "Gigel"])
        self.__nota_modificat = NotaDTO(0, 1,1, 4)
    def tearDown(self):
        self.__REPO_Nota.empty()

    def testAdaugareNota(self):
        self.__SERVICE_nota.adaugare_nota_service([0, 0, 0,8])
        self.assertRaises(RepoError, self.__SERVICE_nota.adaugare_nota_service, [0, 0, 0,8])
        self.assertRaises(RepoError,self.__SERVICE_nota.adaugare_nota_service, [0,99,99,8] )
        self.assertRaises(ValidationError, self.__SERVICE_nota.adaugare_nota_service   , [0, 0, 0,-8])
    def testCautareNota(self):
        self.__SERVICE_nota.adaugare_nota_service([0, 0, 0,8])
        self.__nota_cautat = self.__REPO_Nota.cauta_id_nota_repo(0)
        self.assertEqual( self.__nota_cautat , self.__nota_control)
    def testModificareNota(self):
        self.__SERVICE_nota.adaugare_nota_service([0, 0, 0,8])
        self.__SERVICE_nota.modifica_nota_service([0, 1, 1, 4])
        self.__nota_cautat = self.__REPO_Nota.cauta_id_nota_repo(0)
        self.assertEqual( self.__nota_cautat , self.__nota_modificat)
        self.assertRaises(ValidationError, self.__SERVICE_nota.modifica_nota_service, [-9,0, 0, 213])
    def testStergeNota(self):
        self.__SERVICE_nota.adaugare_nota_service([0, 1, 1,8])
        self.__SERVICE_nota.sterge_student_id_service([1])
        self.__SERVICE_nota.sterge_disciplina_id_service([1])
        self.assertRaises(RepoError, self.__REPO_Student.cauta_id_student_repo,1)
        self.assertRaises (RepoError, self.__REPO_Disciplina.cauta_id_disciplina_repo,1)
        self.assertRaises(RepoError, self.__REPO_Nota.cauta_id_nota_repo,0)