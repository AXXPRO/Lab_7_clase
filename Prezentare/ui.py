from os import system
from Business.control import BusinessStudent



from Erori.erori import ParamsError, RepoError, ValidationError
from Prezentare.ui_functions import UI_functions



class UI:

    def __init__(self):
        self.ui_main()

    def __print_ui(self):
        system('cls')
        print(">>>", end="")

    def __validare_comanda(self,__comanda, __comenzi):
        """
        Functie responsabila pentru a decide daca o comanda este acceptata
        return: True, daca comanda este valabila, False altfel
        """
        for i in range(len(__comenzi)):
            if __comanda in __comenzi[i]:
                return i

        return -1

    def ui_main(self):
        """Functie responsabila pentru cererea introducerii de la tastatura a comenzilor, si validarea lor"""
        
        __comenzi_afisare = {
            "afisare_studenti": UI_functions.afisare_student_service,
            "cauta_student" : UI_functions.cauta_student_id_service

        }
        __comenzi_student = {

            "adaugare_student": BusinessStudent.adaugare_student_service,
            "sterge_student" :  BusinessStudent.sterge_student_id_service,
            "modifica_student": BusinessStudent.modifica_student_service,

            

        }
        __lista_studenti = []
        __lista_discipline = []
        __lista_note = []
        __Rulare = True
        while __Rulare:
            self.__print_ui()
            __comanda = input()
            if __comanda.lower() == "exit":
                __Rulare = False
            else:
                __params = __comanda.split()
                if __params == []:
                    __params.append("nan")

    
                __params.append(__lista_studenti)
                __params.append(__lista_discipline)
                __params.append(__lista_note)

                __comenzi =[]
                __comenzi.append(__comenzi_afisare)
                __comenzi.append(__comenzi_student)
                self.__business_choice = self.__validare_comanda(__params[0], __comenzi)


                if self.__business_choice!=-1:
                    try:
                        if self.__business_choice == 0:

                            self.__EXECUTA = UI_functions(__params[1:], __comenzi_afisare[__params[0]])

                        if self.__business_choice == 1:
                            self.__EXECUTA = BusinessStudent(__params[1:], __comenzi_student[__params[0]])                        
                        
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
