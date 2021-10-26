import pytest
import System

#Tests if the password right
def test_checkPassword:
    username = 'yy9p4'
    password = 'flandrescarlet'
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
