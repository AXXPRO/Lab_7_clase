from os import system




from Erori.erori import ParamsError, RepoError, ValidationError




class UI:

    def __init__(self,service_student, service_disciplina, service_nota):
        self.__ServiceStudent = service_student
        self.__ServiceDisciplina = service_disciplina
        self.__ServiceNota = service_nota
        self.ui_main()

    def __print_ui(self):
        """
        Printeaza >>> pentru a semnifica asteptarea unei comenzi
        """
        system('cls')
        print(">>>", end="")

    def __validare_comanda(self,__comanda, __comenzi):
        """
        Functia returneaza True daca __comanda este valida, False altfel

        """
    
        if __comanda in __comenzi:
             return True



    def ui_main(self):
        """Functie responsabila pentru cererea introducerii de la tastatura a comenzilor, si validarea lor"""
        
        __comenzi = {
            "afisare_studenti": self.afisare_student_ui,
            "cauta_student" : self.cauta_student_id_ui,
            "afisare_discipline": self.afisare_disciplina_ui,
            "cauta_disciplina" :self.cauta_disciplina_id_ui,
             "afisare_note": self.afisare_nota_ui,
             "cauta_nota": self.cauta_nota_id_ui,

            "adaugare_studenti_random": self.adauga_x_studenti_ui,
            "adaugare_discipline_random": self.adauga_x_discipline_ui,
            "adaugare_student": self.adaugare_student_ui,
            "sterge_student" :  self.sterge_student_id_ui,
             "modifica_student": self.modifica_student_ui,

             "adaugare_disciplina": self.adaugare_disciplina_ui,
            "sterge_disciplina" :  self.sterge_disciplina_id_ui,
             "modifica_disciplina": self.modifica_disciplina_ui,

             "adaugare_nota": self.adaugare_nota_ui,
             "sterge_nota" :  self.sterge_nota_id_ui,
            "modifica_nota":self.modifica_nota_ui,

            "statistici_disciplina": self.lista_note_ordonate_ui,
            "statistici_medii" : self.lista_medii_ui,
            "statistici_studenti": self.medie_litera_ui
        }
        
        __Rulare = True
        while __Rulare:
            self.__print_ui()
            __comanda = input()
            if __comanda.lower() == "exit" or __comanda == "":
                __Rulare = False
            else:
                self.__params = __comanda.split()

                __comanda = self.__params[0]
                self.__params.pop(0)


                if self.__validare_comanda(__comanda, __comenzi):
                    try:
                         __comenzi[__comanda]()                                                                 
                        
                    except ParamsError as err:
                        print(str(err))
                        input()
                    except RepoError as err:
                        print(str(err))
                        input()
                    except ValidationError as err:
                        print(str(err))
                        input()
                else: 
                    print("Comanda inexistenta!")
                    input()

    def medie_litera_ui(self):
        """
        Functia de ui ce se va afisa media studentilor al caror nume incepe cu o litera
        """
        if len(self.__params) !=1 :
            raise ParamsError("Numar de parametrii invalid!")
        self.__params[0] = self.__params[0].lower()
        if self.__params[0] <"a" or self.__params[0] > "z":
            raise ParamsError("Litera invalida!")

        lista_medii = self.__ServiceNota.medie_litera_service(self.__params[0])
        if lista_medii == []:
            print("Niciun element in lista!")
            input()
        else:
                print(lista_medii[0])
                input()

    def lista_medii_ui(self):
        """
        Functia va afisa top 20% studenti cu cele mai mari medii
        """
        studenti_top = self.__ServiceNota.lista_medii_service()

        if studenti_top == []:
            print("Niciun student adaugat momentan!")
            input()
        else:
            for medie in studenti_top:
                print(str(medie))
            input()

    def lista_note_ordonate_ui(self):
        """
        Functia va afisa statisticile legate de o disciplina data de utilizator ordonate
        """
        if len(self.__params) !=1 :
            raise ParamsError("Numar de parametrii invalid!")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")   
        self.__params[0] = int(self.__params[0])     

        lista = self.__ServiceNota.lista_note_ordonate_service(self.__params)

        
        if lista == []:
            print("Nicio nota in lista!")
            input()
        else:
            for __nota in lista:
                print(__nota.get_id(), __nota.get_student().get_nume(), __nota.get_disciplina().get_nume(), __nota.get_valoare())

            input()        

    def adauga_x_discipline_ui(self):
        """
        Functia va crea un numar dat de utilizator de discipline, si ii va adauga in aplicatie
        """
        if len(self.__params) !=1 :
            raise ParamsError("Numar de parametrii invalid!")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")
        self.__params[0] = int(self.__params[0])
        self.__ServiceDisciplina.adauga_discipline_random(self.__params)
    def adauga_x_studenti_ui(self):
        """
        Functia va crea un numar dat de utilizator de studenti, si ii va adauga in aplicatie
        """
        if len(self.__params) !=1 :
            raise ParamsError("Numar de parametrii invalid!")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")
        self.__params[0] = int(self.__params[0])
        
        self.__ServiceStudent.adauga_studenti_random(self.__params)


    def sterge_student_id_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul stundetului
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor
        """
        if len(self.__params) !=1 :
            raise ParamsError("Numar de parametrii invalid!")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")  
        self.__params[0] = int(self.__params[0])
        self.__ServiceNota.sterge_student_id_service(self.__params) 


    def sterge_disciplina_id_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul disciplinei
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor
        """
        if len(self.__params) !=1 :
            raise ParamsError("Numar de parametrii invalid!")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")  
        self.__params[0] = int(self.__params[0])
        self.__ServiceNota.sterge_disciplina_id_service(self.__params) 


    def afisare_student_ui(self):
        """
        Functie de ui ce afiseaza lista de studenti

        """
        lista = self.__ServiceStudent.REPO_Studenti.get_list()
        if lista == []:
            print("Niciun student in lista!")
            input()
        else:
            for __student in lista:
                print(__student.get_id(), __student.get_nume())
            input()
    def cauta_student_id_ui(self):
        """
        Functie de ui ce afiseaza studentul caruia ii corespunde un id
        Valideaza: id-ul stundetului
        Raise: RepoError daca studentul nu exista
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor
        """
        if len(self.__params) !=1:
            raise ParamsError("Numar de parametrii invalid!\n")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")
        self.__params[0] = int(self.__params[0])

        Student = self.__ServiceStudent.REPO_Studenti.cauta_id_student_repo(self.__params[0])
        print("Studentul cu id-ul",Student.get_id(), "este", Student.get_nume())
        input()

    def adaugare_student_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul studentului
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor sau ValidationError
        """        
        if len(self.__params) !=2:
            raise ParamsError("Numar de parametrii invalid!\n")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")
        self.__params[0] = int(self.__params[0])
        self.__ServiceStudent.adaugare_student_service(self.__params)

    def modifica_student_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul studentului
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor
        """    
        if len(self.__params) != 2:
            raise ParamsError("Numar de parametrii invalid!")        
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")
        self.__params[0] = int(self.__params[0])
        self.__ServiceStudent.modifica_student_service(self.__params)    

    def adaugare_disciplina_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul disciplinei
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor
        """    
        if len(self.__params) !=3:
            raise ParamsError("Numar de parametrii invalid!\n")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")
        self.__params[0] = int(self.__params[0])
        self.__ServiceDisciplina.adaugare_disciplina_service(self.__params)


    def afisare_disciplina_ui(self):
        """
        Functie ce printeaza lista de discipline
        """
        lista = self.__ServiceDisciplina.REPO_Disciplina.get_list()
        if lista == []:
            print("Nicio disciplina in lista!")
            input()
        else:
            for __disciplina in lista:
                print(__disciplina.get_id(), __disciplina.get_nume(), __disciplina.get_profesor())
            input()

    def cauta_disciplina_id_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul disciplinei
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor si RepoError daca studentul nu exista
        """    
        if len(self.__params) !=1:
            raise ParamsError("Numar de parametrii invalid!\n")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")
        self.__params[0] = int(self.__params[0])
        Disciplina = self.__ServiceDisciplina.REPO_Disciplina.cauta_id_disciplina_repo(self.__params[0])
        print("Disciplina cu id-ul",Disciplina.get_id(), "este", Disciplina.get_nume(), "si il are profesor:",Disciplina.get_profesor())
        input()

    def modifica_disciplina_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul disciplinei
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor
        """    
        if len(self.__params) != 3:
            raise ParamsError("Numar de parametrii invalid!")        
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")
        self.__params[0] = int(self.__params[0])
        self.__ServiceDisciplina.modifica_disciplina_service(self.__params)   
    
    def adaugare_nota_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul notei, studentului, disciplinei
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor
        """    
        if len(self.__params) != 4:
            raise ParamsError("Numar de parametrii invalid!")
        try:
            int(self.__params[0])
            int(self.__params[1])
            int(self.__params[2])
            float(self.__params[3])
        except ValueError:
            raise ParamsError("Id invalid!\n")
        self.__params[0] = int(self.__params[0])
        self.__params[1] = int(self.__params[1])
        self.__params[2] = int(self.__params[2])
        self.__params[3] = float(self.__params[3])
        self.__ServiceNota.adaugare_nota_service(self.__params)

    def sterge_nota_id_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul notei, studentului, disciplinei
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor
        """    
        if len(self.__params) !=1 :
            raise ParamsError("Numar de parametrii invalid!")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")  
        self.__params[0] = int(self.__params[0])
        self.__ServiceNota.sterge_nota_id_service(self.__params)      
        
    def modifica_nota_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul notei, studentului, disciplinei
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor
        """    
        if len(self.__params) != 4:
            raise ParamsError("Numar de parametrii invalid!")
        try:
            int(self.__params[0])
            int(self.__params[1])
            int(self.__params[2])
        except ValueError:
            raise ParamsError("Id invalid!\n")
        self.__params[0] = int(self.__params[0])
        self.__params[1] = int(self.__params[1])
        self.__params[2] = int(self.__params[2])
        self.__ServiceNota.modifica_nota_service(self.__params)
        

    def afisare_nota_ui(self):
        """
        Functie ce printeaza notele din lista
        """
        #lista = self.__ServiceNota.REPO_Note.get_list()
        lista = self.__ServiceNota.afisare_nota_service()
        if lista == []:
            print("Nicio nota in lista!")
            input()
        else:
            for __nota in lista:
                print(__nota.get_id(), __nota.get_student().get_nume(), __nota.get_disciplina().get_nume(), __nota.get_valoare())

            input()
    def cauta_nota_id_ui(self):
        """
        Functie de ui ce apeleaza o functie din service
        Valideaza: id-ul notei, studentului, disciplinei
        Raises: ParamsError pentru orice eroare legata de numarul de parametrii sau validarea lor si RepoError daca nu exista nota
        """    
        if len(self.__params) !=1:
            raise ParamsError("Numar de parametrii invalid!")
        try:
            int(self.__params[0])
        except ValueError:
            raise ParamsError("Id invalid!\n")    
        self.__params[0] = int(self.__params[0]) 
        #CHECK
        Nota = self.__ServiceNota.cauta_nota_id_service(self.__params[0])


        print("Studentul",Nota.get_student().get_nume(), "are nota", Nota.get_valoare(),"la", Nota.get_disciplina().get_nume())
        input()         