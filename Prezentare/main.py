import sys
sys.path.append('../')
sys.path.append('./')

from Prezentare.ui import UI


from Teste.teste import Teste

def main():
    instanta_testare = Teste()
    instanta_testare.ruleaza_toate_testele()
    UI()

if __name__=="__main__":
    main()