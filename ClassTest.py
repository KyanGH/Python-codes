class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
        
def main():
    emp1 = Employee('Arthur','Morgan',10000)
    print(emp1.email)
    print(emp1.fullname())
main()