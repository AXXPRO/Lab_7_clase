import unittest
from Infrastructura.Discipline.domain import Disciplina
from Infrastructura.Note.domain import Nota

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


