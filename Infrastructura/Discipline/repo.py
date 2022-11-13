from Erori.erori import RepoError


class DisciplinaRepo():

    def __init__(self, lista):
        """Constructorul clasei disciplinarepo
        params: lista - lista de discipline
        """
        self.__lista = lista

    def get_list(self):
        """
        Functia returneaza lista de discipline
        params: lista - lista de discipline
        """
        return self.__lista


    def adauga_disciplina_repo(self, disciplina):
        """Functia adauga o disciplina la lista de discipline
        params: disciplina: disciplina care va fi adaugata la lista de discipline
        """
        self.__lista.append(disciplina)

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

        for __disciplina in self.__lista:
            if __disciplina.get_id() == id:
                return __disciplina
        raise RepoError("Eroare repo: Disciplina inexistenta!\n")

    def modificare_id_disciplina_repo(self, id, disciplina_change):
        """
        Functia modifica disciplina cu id-ul dat, in disciplina_change
        params: id - id-ul disciplinei pe care vrem sa o inlocuim
        params: disciplina_change - disciplina cu care vom modifica disciplina originala
        """
        for __disciplina in self.__lista:
            if __disciplina.get_id() == id:
                __disciplina.set_nume(disciplina_change.get_nume())
                __disciplina.set_profesor(disciplina_change.get_profesor())


    def delete_id_disciplina_repo(self, id):
        """
        Functia sterge disciplina cu id-ul id
        params: id - id-ul disciplinei pe care vrem sa o stergem
        """
        __lista_noua = []

        for __disciplina in self.__lista:
            if __disciplina.get_id() != id:
                __lista_noua.append(__disciplina)
        self.__lista[:] = __lista_noua