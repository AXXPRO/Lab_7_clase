from Erori.erori import ParamsError, RepoError
from Infrastructura.Discipline.domain import Disciplina
from Infrastructura.Discipline.repo import DisciplinaRepo
from Infrastructura.Medii.domain import Medii
from Infrastructura.Note.domain import Nota
from Infrastructura.Note.repo import NotaRepo
from Infrastructura.Studenti.domain import *
from Infrastructura.Studenti.repo import StudentRepo
from Validare.Disciplina import ValidareDisciplina
from Validare.Note import ValidareNota
from Validare.Student import ValidareStudent
import random
import string


class ServiceStudent:
    def __init__(self,repo_studenti):
        """
        Constructorul functiilor Service
        param: params- listele + parametrii specifici fiecarei functii
        param: COMANDA- metoda clasei ce va fi executata
        
        """
        self.REPO_Studenti = repo_studenti

    def __get_max_id_student_service(self):
        """
        Functia va returna cel mai mare id al unui student din lista
        """
        __lista = self.REPO_Studenti.get_list()
        if __lista == []:
            return -1
        __max_id = max(__lista, key = lambda x: int(x.get_id())) 
        return __max_id.get_id()  
    def __creaza_student_random_service(self):
        """
        Functia va crea un student cu nume random si id random, si il va returna
        """

        __id_student = str(int(self.__get_max_id_student_service()) + 1)
        __nume = ""

        for i in range(random.randint(5,16)):
            __nume+=random.choice(string.ascii_lowercase)
        return Student(__id_student, __nume)
    def adauga_studenti_random(self, params):
        """
        Functia va adauga un numar dat de studenti random in lista
        """
        __numar_studenti = int(params[0])
        for i in range(0, __numar_studenti):
            __student_random = self.__creaza_student_random_service()
            self.adaugare_student_service([__student_random.get_id(), __student_random.get_nume()])



    def adaugare_student_service(self, params):
        """
        Functie responsabila pentru validare, si introducerea unui student in lista
        raises ValueError if element is not a student, or if id exists
        param1: id student
        param2: nume student
        """

        self.__id = params[0]
        self.__nume = params[1]
        self.__student = Student(self.__id, self.__nume)
        self.__VALID = ValidareStudent(self.__student)
        self.__VALID.is_student_valid()
        
        self.REPO_Studenti.adauga_student_repo(self.__student)


    def modifica_student_service(self, params):
        """
        Funcita va modifca studentul cu id-ul id, cu un student dat de utilizator
        param1: id-ul
        param2: numele
        """

        self.__id = params[0]
        self.__nume = params[1]
        self.__student = Student(self.__id, self.__nume)
        self.__VALID = ValidareStudent(self.__student)
        self.__VALID.is_student_valid()
        
        self.REPO_Studenti.modificare_id_student_repo(self.__id, self.__student)


class ServiceDisciplina:
    def __init__(self,repo_disciplina):
        """
        Constructorul functiilor Service
        param: params- listele + parametrii specifici fiecarei functii
        param: COMANDA- metoda clasei ce va fi executata
        
        """
        self.REPO_Disciplina = repo_disciplina
    def __get_max_id_disciplina_service(self):
        """
        Functia va returna cel mai mare id al unui disciplina din lista
        """
        __lista = self.REPO_Disciplina.get_list()
        if __lista == []:
            return -1
        __max_id = max(__lista, key = lambda x: int(x.get_id())) 
        return __max_id.get_id()  
    def __creaza_disciplina_random_service(self):
        """
        Functia va crea o disciplina cu nume random si id random, si il va returna
        """

        __id_disciplina= str(int(self.__get_max_id_disciplina_service()) + 1)
        __nume = ""
        __profesor = ""

        for i in range(random.randint(5,16)):
            __nume+=random.choice(string.ascii_lowercase)
        for i in range(random.randint(5,16)):
            __profesor+=random.choice(string.ascii_lowercase)
        return Disciplina(__id_disciplina, __nume, __profesor)
    def adauga_discipline_random(self, params):
        """
        Functia va adauga un numar dat de discipline random in lista
        """
        __numar_discipline = int(params[0])
        for i in range(0, __numar_discipline):
            __disciplina_random = self.__creaza_disciplina_random_service()
            self.adaugare_disciplina_service([__disciplina_random.get_id(), __disciplina_random.get_nume(), __disciplina_random.get_profesor()])

    def adaugare_disciplina_service(self,params):
        """
        Functie responsabila pentru validare, si introducerea unei discipline in lista
        raises ValueError if element is not a disciplina, or if id exists
        param1: id Disciplina
        param2: nume Disciplina
        param3: profesor Disciplina
        """

        self.__id = params[0]
        self.__nume = params[1]
        self.__profesor = params[2]

        self.__disciplina = Disciplina(self.__id, self.__nume, self.__profesor)
        self.__VALID = ValidareDisciplina(self.__disciplina)
        self.__VALID.is_disciplina_valid()
        
        
        self.REPO_Disciplina.adauga_disciplina_repo(self.__disciplina)


    def modifica_disciplina_service(self,params):
        """
        Funcita va modifca disciplina cu id-ul id, cu o disciplina data de utilizator
        """

        self.__id = params[0]
        self.__nume = params[1]
        self.__profesor = params[2]

        self.__disciplina = Disciplina(self.__id, self.__nume, self.__profesor)
        self.__VALID = ValidareDisciplina(self.__disciplina)
        self.__VALID.is_disciplina_valid()

        self.REPO_Disciplina.modificare_id_disciplina_repo(self.__id, self.__disciplina)



class ServiceNota:



    def __init__(self,student_repo, disciplina_repo, nota_repo):
        """
        Constructorul functiilor Service
        param: params- listele + parametrii specifici fiecarei functii
        param: COMANDA- metoda clasei ce va fi executata
        
        """
        self.REPO_Note = nota_repo
        self.REPO_Studenti = student_repo
        self.REPO_Discipline = disciplina_repo


        
    def medie_litera_service(self, litera):
        """
        Functia de service ce se va afisa media studentilor al caror nume incepe cu o litera
        VA INTOARCE o LISTA cu UN FLOAT CA SI MEDIA NOTELOR TUTUROR STUDENTILOR CARE INCEP CU O LITERA
        """
        lista_note = self.REPO_Note.get_list()
        note = []
        for nota in lista_note:
            numele_student = nota.get_student().get_nume()
            if numele_student[0].lower() == litera:
                note.append(int(nota.get_valoare()))
        if note == []:
            return []
        else:
            medie = sum(note) / len(note)
            return [medie]
            



    def __lista_note_neordonate_service(self, id):
        """
        Functia va returna o lista cu toate notele la disciplina cu id-ul dat
        """
        lista_originala = self.REPO_Note.get_list()

        lista_de_returnat = []

        for nota in lista_originala:
            if nota.get_disciplina().get_id() == id:
                lista_de_returnat.append(nota)
        return lista_de_returnat

    def __douza_zeci(self):
        """
        returneaza cat inseamna 20% din toti studentii
        """

        numar_studenti = self.REPO_Studenti.size_student_repo()
        return round((20 * numar_studenti)/100)


    def lista_medii_service(self):
        """
        Functia responsabila pentru a intoarce o lista cu top 20% studenti
        """
        lista_note = self.REPO_Note.get_list()
        situatie_studenti = {}
        for nota in lista_note:
            id_student = nota.get_student().get_id()
            if id_student not in situatie_studenti:
                    situatie_studenti[id_student] = []
            situatie_studenti[id_student].append(int(nota.get_valoare()))
        rez =[]
        for id_student in situatie_studenti:
            nume_student = self.REPO_Studenti.cauta_id_student_repo(id_student).get_nume()
            medie = sum(situatie_studenti[id_student] ) / len(situatie_studenti[id_student])
            rez.append(Medii(id_student, nume_student, medie))
        rez.sort(key = lambda x: x.get_medie() ,reverse = True)
        
        return rez[:self.__douza_zeci()]


    def lista_note_ordonate_service(self, params):
        """
        Functia va ordona studentii dupa nume, note, la o disciplina data de utilizator
        params1: id-ul disciplinei
        """
        self.__id = params[0]
        self.REPO_Discipline.cauta_id_disciplina_repo(self.__id)

        lista_neordonata = self.__lista_note_neordonate_service(self.__id)

        ###aici o ordonezi
        lista_neordonata.sort(key = lambda x:(x.get_student().get_nume(), -int(x.get_valoare())))

        return lista_neordonata


    def sterge_disciplina_id_service(self, params):
        """
        Sterge disciplina cu id-ul dat, si notele aferente acestei discipline
        param1: id-ul disciplinei
        """
        self.__id = params[0]
        self.__lista_note = self.REPO_Note.get_list()

        for __nota in self.__lista_note:
            if __nota.get_disciplina().get_id() == self.__id:
                self.sterge_nota_id_service([__nota.get_id()]) 

        self.REPO_Discipline.delete_id_disciplina_repo(self.__id)
        

    def sterge_student_id_service(self, params):
        """
        Sterge Studentul cu id-ul dat, si notele aferente acesteui student
        param1: id-ul studentului
        """
        self.__id = params[0]

        self.__lista_note = self.REPO_Note.get_list()

        for __nota in self.__lista_note:
            if __nota.get_student().get_id() == self.__id:
                self.sterge_nota_id_service([__nota.get_id()]) 

        self.REPO_Studenti.delete_id_student_repo(self.__id)

    def sterge_nota_id_service(self,params):
        """
        Functia sterge din lista de notele cu cu id-ul id
        param1: id-ul
        """

        self.__id_de_sters = params[0]
        self.REPO_Note.delete_id_nota_repo(self.__id_de_sters)


    def __check_ids(self, __student_id, __disciplina_id):
        """
        Functia verifica daca exista sau nu student si disciplina cu id-ul dat
        """
        self.__err = ""
        self.__student_id = __student_id
        self.__disciplina_id = __disciplina_id

        try:
            self.REPO_Studenti.cauta_id_student_repo(self.__student_id)
        except RepoError as err:
            self.__err += str(err)
        try:
            self.REPO_Discipline.cauta_id_disciplina_repo(self.__disciplina_id)
        except RepoError as err:
            self.__err += str(err)
        
        if len(self.__err) > 0:
            raise RepoError(self.__err)
             
            
        
    def adaugare_nota_service(self,params):
        """
        Functie responsabila pentru validare, si introducerea unei note in lista
        raises ValueError if element is not a nota, or if id exists
        param1: id Nota
        param2: id Student
        param3: id Disciplina
        param4: id Valoare
        """

        self.__id = params[0]
        self.__student_id = params[1]
        self.__disciplina_id = params[2]
        self.__valoare = params[3]

        self.__check_ids(self.__student_id, self.__disciplina_id)

        self.__nota = Nota(self.__id,  self.REPO_Studenti.cauta_id_student_repo(self.__student_id), self.REPO_Discipline.cauta_id_disciplina_repo(self.__disciplina_id), self.__valoare )
        
        
        self.__VALID = ValidareNota(self.__nota)
        self.__VALID.is_nota_valid()
        

        
        self.REPO_Note.adauga_nota_repo(self.__nota)


    def modifica_nota_service(self,params):
        """
        Funcita va modifca nota cu id-ul id, cu o nota data de utilizator
        param1: id-ul notei
        param2: id-ul studentului
        param3: id-ul disciplinei
        param4: valoare notei
        """


        self.__id = params[0]
        self.__student_id = params[1]
        self.__disciplina_id = params[2]
        self.__valoare = params[3]



        self.__check_ids(self.__student_id, self.__disciplina_id)

        self.__nota = Nota(self.__id,  self.REPO_Studenti.cauta_id_student_repo(self.__student_id), self.REPO_Discipline.cauta_id_disciplina_repo(self.__disciplina_id), self.__valoare )
        self.__VALID = ValidareNota(self.__nota)
        self.__VALID.is_nota_valid()

        self.REPO_Note.modificare_id_nota_repo(self.__id, Nota(self.__id, self.REPO_Studenti.cauta_id_student_repo(self.__student_id), self.REPO_Discipline.cauta_id_disciplina_repo(self.__disciplina_id), self.__valoare))