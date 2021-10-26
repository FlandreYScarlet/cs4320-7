import pytest
import System

#Tests if the password right
def test_checkPassword:
    username = 'akend3'
    password = '123454321'
    result = grading_system.check_password(username, password)


    if result:
        assert True, "password correct!"
    else:
        assert False, "wrong password!"
        

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
