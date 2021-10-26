import pytest
import Staff

#Test grade change but student not enrolled
def test_gradeChangeStudentDoesntExist(staff_system):
        
        username = 'akend3'
        course = 'software_engineering'
        assignment = 'assignment1'
        grade = 50

        assert staff_system.change_grade(username,course,assignment,grade)


        


@pytest.fixture
def staff_system():
    staffSystem = Staff.Staff()
    #staffSystem.load_data()
    return staffSystem
