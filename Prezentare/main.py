import sys
sys.path.append('../')
sys.path.append('./')
from Business.control import ServiceDisciplina, ServiceNota, ServiceStudent

from Infrastructura.Discipline.repo import DisciplinaRepoFisiere
from Infrastructura.Note.repo import NotaRepoFisiere
from Infrastructura.Studenti.repo import StudentRepoFisiere
from Prezentare.ui import UI


from Teste.teste import Teste

def main():
    instanta_testare = Teste()
    instanta_testare.ruleaza_toate_testele()
    student_repo = StudentRepoFisiere()
    disciplina_repo = DisciplinaRepoFisiere()
    nota_repo = NotaRepoFisiere()
    service_student = ServiceStudent(student_repo)
    service_disciplina = ServiceDisciplina(disciplina_repo)
    service_nota = ServiceNota(student_repo, disciplina_repo, nota_repo)
    UI(service_student, service_disciplina, service_nota)

if __name__=="__main__":
    main()

    #THIS IS A TEST