from os import system
from Business.fara_modificare_lista import *

from Business.modificare_liste import *

def print_ui():
    system('cls')
    print(">>>", end="")

def validare_comanda(comanda, comenzi):
    """
    Functie responsabila pentru a decide daca o comanda este acceptata
    return: True, daca comanda este valabila, False altfel
    """
    if comanda =="":
        return False
    if comanda in comenzi:
        return True
    return False


def ui_main():
    """Functie responsabila pentru cererea introducerii de la tastatura a comenzilor, si validarea lor"""
    
    comenzi = {

        "adaugare_student": adaugare_student_service,
        "afisare_studenti": afisare_student_service

    }
    lista_studenti = []
    lista_discipline = []
    note = []
    Rulare = True
    while Rulare:
        print_ui()
        comanda = input()
        if comanda.lower() == "exit":
            Rulare = False
        else:

            params = comanda.split()
            if params == []:
                params.append("nan")
            params.append(lista_studenti)
            params.append(lista_discipline)
            params.append(note)
            if validare_comanda(params[0],comenzi):
                try:
                    comenzi[params[0]](params[1:])
                except ValueError as err:
                    print(str(err))
                    input()
