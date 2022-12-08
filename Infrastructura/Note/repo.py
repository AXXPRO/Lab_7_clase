from Erori.erori import RepoError
from Infrastructura.Discipline.domain import Disciplina
from Infrastructura.Note.domain import Nota
from Infrastructura.NoteDTO.domain import NotaDTO
from Infrastructura.Studenti.domain import Student


class NotaRepo():

    def __init__(self):
        """Constructorul clasei notelor
        params: lista - lista de note
        """
        self.__lista = {}

    def get_list(self):
        """
        Functia returneaza lista de note
        params: lista - lista de note
        """
        lista = []
        for i in self.__lista:
            lista.append(self.__lista[i])
        return lista


    def adauga_nota_repo(self, nota):
        """Functia adauga o nota la lista de note
        params: nota: nota care va fi adaugata la lista de note
        """
        if nota.get_id() in self.__lista:
            raise RepoError("Id deja existent!\n")        
        self.__lista[nota.get_id()] = nota

    def size_nota_repo(self):
        """
        functia returneaza numarul de note din lista
        """
       
        return len(self.__lista)

    def cauta_id_nota_repo(self, id):
        """
        Functia returneaza nota cu id-ul id
        params: id - id-ul notei pe care o cautam
        raises: RepoError, daca nu gaseste nota in lista
        """

        if id in self.__lista:
            return self.__lista[id]
        raise RepoError("Eroare repo: Nota inexistenta!\n")

    def modificare_id_nota_repo(self, id, nota_change):
        """
        Functia modifica nota cu id-ul dat, in nota_change
        params: id - id-ul notei pe care vrem sa o inlocuim
        params: nota_change - nota cu care vom modifica nota originala
        """
        if id in self.__lista:
            self.__lista[id].set_student(nota_change.get_student())
            self.__lista[id].set_disciplina(nota_change.get_disciplina())
            self.__lista[id].set_valoare(nota_change.get_valoare())



    def delete_id_nota_repo(self, id):
        """
        Functia sterge nota cu id-ul id
        params: id - id-ul notei pe care vrem sa o stergem
        """

        if id in self.__lista:
            del(self.__lista[id])

class NotaRepoFisiere():
    def __init__(self,path):
       self.__lista_note = {}
       self.__path = path
       self.__load_from_file()

    def empty(self):
        self.__lista_note = {}
        self.__store_in_file()
    def get_list(self):
        self.__load_from_file()
        return [x for x in self.__lista_note.values()]


    def adauga_nota_repo(self, nota):
        self.__load_from_file()
        if nota.get_id_nota() in self.__lista_note:
            raise RepoError("Nota deja existenta!\n")
        self.__lista_note[nota.get_id_nota()] = nota
        self.__store_in_file()

    def size_nota_repo(self):
        self.__load_from_file()
        return len(self.__lista_note)

    def cauta_id_nota_repo(self, id):
        self.__load_from_file()
        if id not in self.__lista_note:
            raise RepoError("Nota inexistenta!\n")
        return self.__lista_note[id]

    def modificare_id_nota_repo(self, id, nota_change):
          self.__load_from_file()
          self.__lista_note[id].set_id_student(nota_change.get_id_student())
          self.__lista_note[id].set_id_disciplina(nota_change.get_id_disciplina())
          self.__lista_note[id].set_valoare(nota_change.get_valoare())

          self.__store_in_file()

    def delete_id_nota_repo(self, id):
          self.__load_from_file()
          if id in self.__lista_note:
            del(self.__lista_note[id])
          self.__store_in_file()



    def __load_from_file(self):
        """
        functia resposnabila pentru a adauga in lista de note, notele din fisier
        """
        self.__lista_note = {}

        try:
         fisier_note = open(self.__path, "r")
        except IOError:
            pass

        nota_impachetat = fisier_note.readline()
        while nota_impachetat != "":
            nota_impachetat  =nota_impachetat.strip()
            nota_params = nota_impachetat.split(";")


            self.__lista_note[int(nota_params[0])] = NotaDTO(int(nota_params[0]),int(nota_params[1]),int(nota_params[2]),int(nota_params[3]))


            nota_impachetat = fisier_note.readline()
        fisier_note.close()


    def __store_in_file(self):
        """
        Functia responsabila pentru a updata fisierul cand apar elemente noi
        """
        try:
         fisier_note = open(self.__path, "w")
        except IOError:
            pass
        lista_note = [x for x in self.__lista_note.values()]


        for nota in lista_note:
            fisier_note.write(f"{nota.get_id_nota()};{nota.get_id_student()};{nota.get_id_disciplina()};{nota.get_valoare()}\n")
        fisier_note.close()