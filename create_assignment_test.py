import pytest
import Staff


#Test assignment create
def test_assignmentCreate(staff_system):
        
        assignment_name = 'assignment7'
        course = 'software_engineering'
        due_date = '10/24/2030'

        assert staff_system.create_assignment(assignment_name, due_date, course)


        


@pytest.fixture
def staff_system():
    staffSystem = Staff.Staff()
    #staffSystem.load_data()
    return staffSystem
