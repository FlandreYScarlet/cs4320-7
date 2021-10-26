import pytest
import System


#test for ontime assignment
def test_checkOntime(grading_system):
    
    username = "akend3"
    password = "123454321"
    dueDate = "10/23/2021"
    ontimeSubmissionDate = "10/22/2020"
    lateSubmissionDate = "10/24/2020"
   
    grading_system.login(username, password)
    onTimeCheck = grading_system.usr.check_ontime(ontimeSubmissionDate, dueDate)
    lateCheck = grading_system.usr.check_ontime(lateSubmissionDate, dueDate)


    if onTimeCheck:
        assert True
    else:#if lateCheck
    	assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
