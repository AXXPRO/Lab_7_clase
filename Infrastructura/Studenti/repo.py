from Erori.erori import RepoError
from Infrastructura.Studenti.domain import *


class StudentRepo():

    def __init__(self, lista):
        """Constructorul clasei studentrepo
        params: lista - lista de studenti
        """
        self.__lista = lista

    def get_list(self):
        """
        Functia returneaza lista de studenti
        params: lista - lista de studenti
        """
        return self.__lista


    def adauga_student_repo(self, student):
        """Functia adauga un student la lista de studenti
        params: student - studentul ce va fi adaugat la lista de studenti"""
        self.__lista.append(student)

    def size_student_repo(self):
        """
        functia returneaza numarul de studenti din lista
        """
       
        return len(self.__lista)

    def cauta_id_student_repo(self, id):
        """
        Functia returneaza studentul cu id-ul id
        params: id - id-ul studentului pe care il cautam
        raises: RepoError, daca nu gaseste studentul in lista
        """

        for __student in self.__lista:
            if __student.get_id() == id:
                return __student
        raise RepoError("Eroare repo: Student inexistent!\n")

    def modificare_id_student_repo(self, id, student_change):
        """
        Functia modifica studentul cu id-ul dat, in student_change
        params: id - id-ul studentului pe care vrem sa il inlocuim
        params: student_chamge - studentul cu care vom modifica studentul original
        """
        for __student in self.__lista:
            if __student.get_id() == id:
                __student.set_nume(student_change.get_nume())


    def delete_id_student_repo(self, id):
        """
        Functia sterge studentul cu id-ul id
        params: id - id-ul studentului pe care vrem sa il stergem
        """
        __lista_noua = []

        for __student in self.__lista:
            if __student.get_id() != id:
                __lista_noua.append(__student)
        self.__lista[:] = __lista_noua