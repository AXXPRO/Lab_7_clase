import sys
sys.path.append('../')
sys.path.append('./')

from Prezentare.ui import ui_main


from Teste.teste import ruleaza_toate_testele

def main():
    ruleaza_toate_testele()
    ui_main()

if __name__=="__main__":
    main()