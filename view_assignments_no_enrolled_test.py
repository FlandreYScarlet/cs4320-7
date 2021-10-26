import pytest
import System


#test for view assignments but student not enrolled
def test_viewAssignmentsNoEnrolled(grading_system):

    username = "akend3"
    password  = "123454321"
    course = "software_engineering"

    
    grading_system.login(username, password)
    assert grading_system.usr.view_assignments(course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
