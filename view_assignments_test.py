import pytest
import System


#test for view assignments
def test_viewAssignments(grading_system):

    username = "hdjsr7"
    password  = "pass1234"
    course = "databases"

    
    grading_system.login(username, password)
    assert grading_system.usr.view_assignments(course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
