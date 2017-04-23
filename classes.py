#CLASSES & OBJECTS
#__ means Private Variables 

class Person:
    __name = ''
    __email = ''
    
    #Creating Constructor
    def __init__(self,name,email):
        self.__name = name
        self.__email = email
        
    
    def set_name(self,name):
        self.__name = name
        
        
    def get_name(self):
        return self.__name
    
    def set_email(self,email):
        self.__email = email
        
        
    def get_email(self):
        return self.__email
    
    def toString(self):
        return '{} can be contacted at {}'.format(self.__name,self.__email)

#Creating Brad as an object of Person
#brad = Person('Kaveendra Oshan', 'Kaveendra@gmail.com')
#brad.set_name('Kaveendra Oshan')
#brad.set_email('kaveendra.oshan@gmail.com')

#print(brad.get_name())
#print(brad.get_email())
#print(brad.toString())

class Customer(Person):
    __balance = 0
    
    def __init__(self,name,email,balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        #Calling the constructor
        super(Customer,self).__init__(name, email)
        
    def set_balance(self,balance):
            self.__balance = balance
            
    def get_balance(self):
            return self.__balance
        
    def toString(self):
        return '{} has a balance of {} and can be contacted {}'.format(self.__name, self.__balance, self.__email)

john = Customer('John Doe','john@gmail.com',10000)
john.set_balance(5000)
kate = Customer('Kate Smith','oshan@gmail.com',60000000)
print(kate.toString())
print(john.toString())

