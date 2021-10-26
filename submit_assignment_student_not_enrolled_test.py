import pytest
import System


#test for submit assignment but student doesn't enrolled
def test_assignmentSubmit(grading_system):

    username= 'akend3'
    password = '123454321'
    assignment = 'assignment1'
    course = 'software_engineering'
    submission = 'Bla Bla Bla'
    submission_date = '01/01/20'

    grading_system.login(username, password)
    assert grading_system.usr.submit_assignment(course, assignment, submission, submission_date)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
