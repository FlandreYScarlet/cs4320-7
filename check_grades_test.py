import pytest
import System


#test for check grade
def test_checkGrades(grading_system):
    username = "hdjsr7"
    password  = "pass1234"
    course = "databases"

    grading_system.login(username, password)
    assert grading_system.usr.check_grades(course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
