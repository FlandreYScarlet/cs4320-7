import pytest
import System


def test_studentAdd(grading_system):

    username= 'goggins'
    password = 'augurrox'
    student = 'akend3'
    course = "software_engineering"

    grading_system.login(username, password)
    if grading_system.user.add_student(student, course) is None:
        assert True
    else:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
