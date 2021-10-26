import pytest
import System


#test drop student
def test_studentDrop(grading_system):

    username= 'goggins'
    password = 'augurrox'
    student = 'yted91'
    course = "software_engineering"

    grading_system.login(username, password)
    if grading_system.user.drop_student(student, course) is None:
        assert True
    else:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
