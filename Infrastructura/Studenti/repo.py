from Erori.erori import RepoError
from Infrastructura.Studenti.domain import *


class StudentRepo():

    def __init__(self, lista):
        self.__lista = lista

    def get_list(self):
        return self.__lista


    def adauga_student_repo(self, student):

        self.__lista.append(student)

    def size_student_repo(self):
       
        return len(self.__lista)

    def cauta_id_student_repo(self, id):

        for __student in self.__lista:
            if __student.get_id() == id:
                return __student
        raise RepoError("Eroare repo!\n")

    def modificare_id_student_repo(self, id, student_change):

        for __student in self.__lista:
            if __student.get_id() == id:
                __student.set_nume(student_change.get_nume())


    def delete_id_student_repo(self, id):
 
        __lista_noua = []

        for __student in self.__lista:
            if __student.get_id() != id:
                __lista_noua.append(__student)
        self.__lista[:] = __lista_noua