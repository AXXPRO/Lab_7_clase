from os import system
from Business.control import Business


from Erori.erori import ParamsError, RepoError, ValidationError



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

        if __comanda in __comenzi:
                return True
        return False

    def ui_main(self):
        """Functie responsabila pentru cererea introducerii de la tastatura a comenzilor, si validarea lor"""
        

        __comenzi = {

            "adaugare_student": Business.adaugare_student_service,
            "sterge_student" :  Business.sterge_student_id_service,
            "modifica_student": Business.modifica_student_service,
            "afisare_studenti": Business.afisare_student_service,
            "cauta_student" : Business.cauta_student_id_service
            

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


            if self.__validare_comanda(__params[0], __comenzi):
                try:
                
                    self.__EXECUTA = Business(__params[1:], __comenzi[__params[0]])                        
                    
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
