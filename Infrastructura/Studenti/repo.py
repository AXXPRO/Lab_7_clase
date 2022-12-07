from Erori.erori import RepoError
from Infrastructura.Studenti.domain import *


class StudentRepo():

    def __init__(self):
        """Constructorul clasei studentrepo
        params: lista - lista de studenti
        """
        self.__lista = {}

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

        if student.get_id() in self.__lista:
            raise RepoError("Id deja existent!\n")
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


class StudentRepoFisiere(StudentRepo):
    def __init__(self, path):
       StudentRepo.__init__(self)

       self.__path = path
       self.__load_from_file()
    
    def get_list(self):
        self.__load_from_file()
        return StudentRepo.get_list(self)

    def adauga_student_repo(self, student):
          self.__load_from_file()
          StudentRepo.adauga_student_repo(self, student)
          self.__store_in_file()

    def size_student_repo(self):
        self.__load_from_file()
        return StudentRepo.size_student_repo(self)

    def cauta_id_student_repo(self, id):
        self.__load_from_file()
        return StudentRepo.cauta_id_student_repo(self, id)

    def modificare_id_student_repo(self, id, student_change):
          self.__load_from_file()
          StudentRepo.modificare_id_student_repo(self, id, student_change)
          self.__store_in_file()

    def delete_id_student_repo(self, id):
          self.__load_from_file()
          StudentRepo.delete_id_student_repo(self, id)
          self.__store_in_file()



    def __load_from_file(self):
        """
        functia resposnabila pentru a adauga in lista de studenti, studentii din fisier
        """
        StudentRepo.__init__(self)

        try:
         fisier_studenti = open(self.__path, "r")
        except IOError:
            pass

        studentul_impachetat = fisier_studenti.readline()
        while studentul_impachetat != "":
            studentul_impachetat  =studentul_impachetat.strip()
            studentul_params = studentul_impachetat.split(";")
            StudentRepo.adauga_student_repo(self, Student(int(studentul_params[0]),studentul_params[1]))
            studentul_impachetat = fisier_studenti.readline()
        fisier_studenti.close()


    def __store_in_file(self):
        """
        Functia responsabila pentru a updata fisierul cand apar elemente noi
        """
        try:
         fisier_studenti = open(self.__path, "w")
        except IOError:
            pass
        lista_studenti = StudentRepo.get_list(self)

        for student in lista_studenti:
            fisier_studenti.write(f"{student.get_id()};{student.get_nume()}\n")
        fisier_studenti.close()