import sys
sys.path.append('../')
sys.path.append('./')
from Business.control import ServiceDisciplina, ServiceNota, ServiceStudent

from Infrastructura.Discipline.repo import DisciplinaRepo
from Infrastructura.Note.repo import NotaRepo
from Infrastructura.Studenti.repo import StudentRepo

from Prezentare.ui import UI


from Teste.teste import Teste

def main():
    instanta_testare = Teste()
    instanta_testare.ruleaza_toate_testele()
    student_repo = StudentRepo()
    disciplina_repo = DisciplinaRepo()
    nota_repo = NotaRepo()
    service_student = ServiceStudent(student_repo)
    service_disciplina = ServiceDisciplina(disciplina_repo)
    service_nota = ServiceNota(student_repo, disciplina_repo, nota_repo)
    UI(service_student, service_disciplina, service_nota)

if __name__=="__main__":
    main()

    #THIS IS A TEST
    #TEST NR 2