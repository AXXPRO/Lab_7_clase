from Infrastructura.Studenti.domain import *
from Infrastructura.Discipline.domain import *
from Validare.Disciplina import *
from Validare.Student import *
from Infrastructura.Studenti.repo import *
from Infrastructura.Discipline.repo import *
def test_domain_student():
    """
    Testele pentru functiile domain asociate student
    """
    id = 0
    nume = "Carol"
    primul_student = Student(id, nume)

    assert primul_student.get_id() == 0
    assert primul_student.get_nume() == "Carol"

    nume_nou = "Gabi"
    primul_student.set_nume(nume_nou)
    assert primul_student.get_nume()== "Gabi"

def test_domain_disciplina():
    id=0
    nume = "Matematica"
    profesor = "Cotfas"

    disciplina_prima = creaza_disciplina(id, nume, profesor)
    assert get_id_disciplina(disciplina_prima) == 0
    assert get_nume_disciplina(disciplina_prima) == "Matematica"
    assert get_profesor_disciplina(disciplina_prima) == "Cotfas"

    set_nume_disciplina(disciplina_prima, "Engleza")
    set_profesor_disciplina(disciplina_prima, "Vulpe")
    assert get_nume_disciplina(disciplina_prima) == "Engleza"
    assert get_profesor_disciplina(disciplina_prima) == "Vulpe"


def test_validare():
    student = Student(-5, "")
    try:
        valid = ValidareStudent(student)
        valid.is_student_valid()
        assert False
    except ValueError as err:
        assert str(err) == "Id invalid!\nNume invalid!\n"

    disciplina = creaza_disciplina(7.3, "", "")
    try:
        is_disciplina_valid(disciplina)
        assert False
    except ValueError as err:
        assert str(err) == "Id invalid!\nNume invalid!\nProfesor invalid!\n"

        
    student = Student(0, "Marcel")
    valid = ValidareStudent(student)
    valid.is_student_valid()
    disciplina = creaza_disciplina(1, "Mate", "Mircel")
    is_disciplina_valid(disciplina)

def test_repo_student():
    
    lista_studenti = []
    student1 =Student(0, "Marcel")
    student2 = Student(1, "Demian")
    adauga_student_repo(lista_studenti, student1)
    assert lista_studenti == [student1]

    assert size_student_repo(lista_studenti) == 1

    student_lau = Student(0, "wEzio")
    modificare_id_student_repo(lista_studenti, student_lau.get_id(),student_lau)

    print(student_lau.get_id(), student_lau.get_nume())
    
    assert student1.get_id() == student_lau.get_id()
    assert student1.get_nume() == student_lau.get_nume()

    assert lista_studenti == [student1]
    assert lista_studenti[0].get_id() == student_lau.get_id()
    assert lista_studenti[0].get_nume() == student_lau.get_nume()
    adauga_student_repo(lista_studenti, student2)

    assert lista_studenti == [student1,student2]
    assert size_student_repo(lista_studenti) == 2
    student_cautat = cauta_id_student_repo(lista_studenti, 0)

    assert student_cautat.get_id() == student1.get_id()
    assert student_cautat.get_nume() == student1.get_nume()

    try:
        student_cautat = cauta_id_student_repo(lista_studenti, 3)
        assert False
    except TypeError as err:
        assert str(err) == "Nu exista niciun student cu acel id!\n"


    student_modificat = Student(3, "Antonio")
    modificare_id_student_repo(lista_studenti,student_modificat.get_id(),student_modificat)
    assert lista_studenti ==[student1, student2]

    #print(student1.get_nume(), student1.get_id())

    student_modificat2 = Student(0, "Antonio")
    modificare_id_student_repo(lista_studenti,student_modificat2.get_id(),student_modificat)
    
    # for studentt in lista_studenti:
    #     print(studentt.get_nume(), studentt.get_id())

    # print(student_modificat2.get_nume(), student_modificat2.get_id())
    # print(student2.get_nume(), student2.get_id())
    # print(student1.get_nume(), student1.get_id())
    assert student1.get_id() == student_modificat2.get_id()
    assert student1.get_nume() == student_modificat2.get_nume()
    assert lista_studenti == [student1, student2]


    delete_id_student_repo(lista_studenti, 2)
    assert size_student_repo(lista_studenti) == 2

    delete_id_student_repo(lista_studenti, 0)
    assert lista_studenti == [student2]
    delete_id_student_repo(lista_studenti, 1)
    assert lista_studenti == []



def test_repo_disciplina():
    
    lista_disciplina = []
    disciplina1 = creaza_disciplina(0, "Mate", "Cotfas")
    disciplina2 = creaza_disciplina(1, "Romana", "Ghinea")
    adauga_disciplina_repo(lista_disciplina, disciplina1)
    assert lista_disciplina == [disciplina1]

    assert size_disciplina_repo(lista_disciplina) == 1

    adauga_disciplina_repo(lista_disciplina, disciplina2)
    assert lista_disciplina == [disciplina1,disciplina2]
    assert size_disciplina_repo(lista_disciplina) == 2
    disciplina_cautat = cauta_id_disciplina_repo(lista_disciplina, 0)

    assert get_id_disciplina(disciplina_cautat) == get_id_disciplina(disciplina1)
    assert get_nume_disciplina(disciplina_cautat) == get_nume_disciplina(disciplina1)
    assert get_profesor_disciplina(disciplina_cautat) == get_profesor_disciplina(disciplina1)

    try:
        disciplina_cautat = cauta_id_disciplina_repo(lista_disciplina, 3)
        assert False
    except TypeError as err:
        assert str(err) == "Nu exista nicio disciplina cu acel id!\n"


    disciplina_modificat = creaza_disciplina(3, "Info", "Torok")
    modificare_id_disciplina_repo(lista_disciplina,get_id_disciplina(disciplina_modificat),disciplina_modificat)
    assert lista_disciplina ==[disciplina1, disciplina2]

    disciplina_modificat = creaza_disciplina(0, "Info", "Torok")
    modificare_id_disciplina_repo(lista_disciplina,get_id_disciplina(disciplina_modificat),disciplina_modificat)

    assert lista_disciplina ==[disciplina_modificat, disciplina2]

    delete_id_disciplina_repo(lista_disciplina, 2)
    assert size_disciplina_repo(lista_disciplina) == 2

    delete_id_disciplina_repo(lista_disciplina, 0)
    assert lista_disciplina == [disciplina2]
    delete_id_disciplina_repo(lista_disciplina, 1)
    assert lista_disciplina == []    

def test_business_student():
    """"""



def ruleaza_toate_testele():
    """
    Functia responsabila pentru a rula testele, apelata in main
    """
    test_domain_student()
    print("Teste domain student trecute!")
    test_domain_disciplina()
    print("Teste domain disciplina trecute!")
    test_validare()
    print("Teste validare trecute!")
    test_repo_student()
    print("Teste repo student trecute!")
    test_repo_disciplina()
    print("Teste repo disciplina trecute!")
    test_business_student()
    print("Teste business student trecute!")