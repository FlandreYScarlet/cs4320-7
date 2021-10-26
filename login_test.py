import pytest
import System

#Test login
def test_login(grading_system):
        
        username = 'hdjsr7'
        password = 'pass1234'

        testResult = grading_system.login(username, password) is None

        if testResult:
            assert True
        else:
            assert False
        


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
