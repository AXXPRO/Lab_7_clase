from Erori.erori import RepoError


class NotaRepo():

    def __init__(self, lista):
        """Constructorul clasei notelor
        params: lista - lista de note
        """
        self.__lista = lista

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