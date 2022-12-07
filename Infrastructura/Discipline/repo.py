from Erori.erori import RepoError
from Infrastructura.Discipline.domain import Disciplina


class DisciplinaRepo():

    def __init__(self):
        """Constructorul clasei disciplinarepo
        params: lista - lista de discipline
        """
        self.__lista = {}

    def get_list(self):
        """
        Functia returneaza lista de discipline
        params: lista - lista de discipline
        """
        lista = []
        for i in self.__lista:
            lista.append(self.__lista[i])
        return lista


    def adauga_disciplina_repo(self, disciplina):
        """Functia adauga o disciplina la lista de discipline
        params: disciplina: disciplina care va fi adaugata la lista de discipline
        """
        if disciplina.get_id() in self.__lista:
            raise RepoError("Id deja existent!\n")        
        self.__lista[disciplina.get_id()] = disciplina

    def size_disciplina_repo(self):
        """
        functia returneaza numarul de discipline din lista
        """
       
        return len(self.__lista)

    def cauta_id_disciplina_repo(self, id):
        """
        Functia returneaza disciplina cu id-ul id
        params: id - id-ul disciplinei pe care o cautam
        raises: RepoError, daca nu gaseste disciplina in lista
        """

       
        if id in self.__lista:
            return self.__lista[id]
        raise RepoError("Eroare repo: Disciplina inexistenta!\n")

    def modificare_id_disciplina_repo(self, id, disciplina_change):
        """
        Functia modifica disciplina cu id-ul dat, in disciplina_change
        params: id - id-ul disciplinei pe care vrem sa o inlocuim
        params: disciplina_change - disciplina cu care vom modifica disciplina originala
        """
        if id in self.__lista:
            self.__lista[id].set_nume(disciplina_change.get_nume())
            self.__lista[id].set_profesor(disciplina_change.get_profesor())


    def delete_id_disciplina_repo(self, id):
        """
        Functia sterge disciplina cu id-ul id
        params: id - id-ul disciplinei pe care vrem sa o stergem
        """

        if id in self.__lista:
            del(self.__lista[id])


class DisciplinaRepoFisiere(DisciplinaRepo):
    def __init__(self,path):
       DisciplinaRepo.__init__(self)

       self.__path =path
       self.__load_from_file()
    
    def get_list(self):
        self.__load_from_file()
        return DisciplinaRepo.get_list(self)

    def adauga_disciplina_repo(self, disciplina):
          self.__load_from_file()
          DisciplinaRepo.adauga_disciplina_repo(self, disciplina)
          self.__store_in_file()

    def size_disciplina_repo(self):
        self.__load_from_file()
        return DisciplinaRepo.size_disciplina_repo(self)

    def cauta_id_disciplina_repo(self, id):
        self.__load_from_file()
        return DisciplinaRepo.cauta_id_disciplina_repo(self, id)

    def modificare_id_disciplina_repo(self, id, disciplina_change):
          self.__load_from_file()
          DisciplinaRepo.modificare_id_disciplina_repo(self, id, disciplina_change)
          self.__store_in_file()

    def delete_id_disciplina_repo(self, id):
          self.__load_from_file()
          DisciplinaRepo.delete_id_disciplina_repo(self, id)
          self.__store_in_file()



    def __load_from_file(self):
        """
        functia resposnabila pentru a adauga in lista de discipline, disciplinele din fisier
        """
        DisciplinaRepo.__init__(self)

        try:
         fisier_discipline = open(self.__path, "r")
        except IOError:
            pass

        disciplina_impachetat = fisier_discipline.readline()
        while disciplina_impachetat != "":
            disciplina_impachetat  =disciplina_impachetat.strip()
            disciplina_params = disciplina_impachetat.split(";")
            DisciplinaRepo.adauga_disciplina_repo(self, Disciplina(int(disciplina_params[0]),disciplina_params[1], disciplina_params[2]))
            disciplina_impachetat = fisier_discipline.readline()
        fisier_discipline.close()


    def __store_in_file(self):
        """
        Functia responsabila pentru a updata fisierul cand apar elemente noi
        """
        try:
         fisier_discipline = open(self.__path, "w")
        except IOError:
            pass
        lista_discipline = DisciplinaRepo.get_list(self)

        for disciplina in lista_discipline:
            fisier_discipline.write(f"{disciplina.get_id()};{disciplina.get_nume()};{disciplina.get_profesor()}\n")
        fisier_discipline.close()