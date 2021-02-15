# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0):
        self.name = name
        self.gpa = gpa
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)