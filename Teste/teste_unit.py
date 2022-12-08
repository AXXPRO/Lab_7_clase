import unittest
from Erori.erori import RepoError
from Infrastructura.Discipline.domain import Disciplina
from Infrastructura.Note.domain import Nota
from Infrastructura.Note.repo import NotaRepoFisiere
from Infrastructura.NoteDTO.domain import NotaDTO

from Infrastructura.Studenti.domain import Student

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
        #self.REPO_NotaDTO.adauga_nota_repo(self.__doua_nota_dto)
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


