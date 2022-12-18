import sys
sys.path.append('../')
sys.path.append('./')
from Business.control import ServiceDisciplina, ServiceNota, ServiceStudent

from Infrastructura.Discipline.repo import DisciplinaRepoFisiere
from Infrastructura.Note.repo import NotaRepoFisiere
from Infrastructura.Studenti.repo import StudentRepoFisiere
from Prezentare.ui import UI

import unittest
from Teste.teste import Teste
from Teste.teste_unit import TestDomainStudent, TestDomainNotaDTO, TestRepoNotaDTO, TestDomainDisciplina ,TestValidareStudent, TestValidareDisciplina, TestValidareNotaDTO,TestRepoStudent,TestRepoDisciplina, TestControlStudent, TestControlDisciplina, TestDomainMedii, TestControlNota,TestFisier

def main():

    #unittest.main()
    # instanta_testare = Teste()
    # instanta_testare.ruleaza_toate_testele()
    student_repo = StudentRepoFisiere("studenti.txt")
    disciplina_repo = DisciplinaRepoFisiere("discipline.txt")
    nota_repo = NotaRepoFisiere("note.txt")
    service_student = ServiceStudent(student_repo)
    service_disciplina = ServiceDisciplina(disciplina_repo)
    service_nota = ServiceNota(student_repo, disciplina_repo, nota_repo)
    UI(service_student, service_disciplina, service_nota)

if __name__=="__main__":
    main()

    #THIS IS A TEST