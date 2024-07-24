'''constructor===execution starts from here
default exection starts without the declaration of variables
self===good practise'''
'''destructor====it manages like garbage collectors'''
class Myclass:
    #def --init-- is used for dynamic
    cla_var="Iam class variable"
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(a,b):
        return a+b
    def sub(a,b):
        return abs(a-b)
    def mul(a,b):
        return a*b
    def mod(a,b):
        return a%b
    def divide(a,b):
        return a//b
    
    
obj1=Myclass
obj2=Myclass
print(obj1.add(5,10))
print(obj2.divide(50,2))  
print(obj1.mul(6,5))  
print(obj2.sub(67,9))
print(obj1.mod(55,10))
print(obj1.sub(4,8))
print(obj2.mul(5.9,93))
    