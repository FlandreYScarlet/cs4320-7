import pytest
import Staff

#Test grade change
def test_gradeChange(staff_system):
        
        username = 'yy9p4'
        course = 'software_engineering'
        assignment = 'assignment7'
        grade = 50

        assert staff_system.change_grade(username,course,assignment,grade)


        


@pytest.fixture
def staff_system():
    staffSystem = Staff.Staff()
    #staffSystem.load_data()
    return staffSystem
