class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = self.first + '.' + self.last + '@email.com'
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter 
    def full_name(self):
        print('Delete Name!')
        self.first = None
        self.last = None

#emp_1 = Employee('John', 'Lu')

#print(emp_1.full_name())
#print(emp_1.email)