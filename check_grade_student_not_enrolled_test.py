import pytest
import System


#test for check grade but sutdent not enrolled
def test_checkGrades(grading_system):
    username = "akend3"
    password  = "123454321"
    course = "software_engineering"

    grading_system.login(username, password)
    assert grading_system.usr.check_grades(course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
