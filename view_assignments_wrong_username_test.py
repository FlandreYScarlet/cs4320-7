import pytest
import System


#test for view assignments but student get wrong username
def test_viewAssignmentsWrongName(grading_system):

    username = "flandre"
    password  = "123454321"
    course = "comp_sci"

    
    grading_system.login(username, password)
    assert grading_system.usr.view_assignments(course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
