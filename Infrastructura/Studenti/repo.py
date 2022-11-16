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
        lista = []
        for i in self.__lista:
            lista.append(self.__lista[i])
        return lista


    def adauga_student_repo(self, student):
        """Functia adauga un student la lista de studenti
        params: student - studentul ce va fi adaugat la lista de studenti"""
        self.__lista[student.get_id()] = student

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

        if id in self.__lista:
            return self.__lista[id]
        raise RepoError("Eroare repo: Student inexistent!\n")

    def modificare_id_student_repo(self, id, student_change):
        """
        Functia modifica studentul cu id-ul dat, in student_change
        params: id - id-ul studentului pe care vrem sa il inlocuim
        params: student_chamge - studentul cu care vom modifica studentul original
        """
        if id in self.__lista:
            self.__lista[id].set_nume(student_change.get_nume())


    def delete_id_student_repo(self, id):
        """
        Functia sterge studentul cu id-ul id
        params: id - id-ul studentului pe care vrem sa il stergem
        """

        if id in self.__lista:
            del(self.__lista[id])