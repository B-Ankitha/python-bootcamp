# class Animal:
#     def Speak():
#         return "animal is speaking"
# class Dog(Animal):
#     def Bark():
#         return "BOW"  
# obj1=Animal
# obj2=Dog
# print(obj1.Speak())  
# print(obj2.Bark())



'''multi-level'''

# class Animal:
#     def Speak():
#         return "animal is speaking"
# class Dog(Animal):
#     def Bark():
#         return "BOW"  
# class Puppy(Dog):
#     def Puppy_Bark():
#           return "bow bow "  
# obj1=Animal
# obj2=Dog
# obj3=Puppy
# print(obj1.Speak())  
# print(obj2.Bark())
# print(obj3.Puppy_Bark())
    
'''MULTIPLE inheritence'''
class Father:
    def Father_speak():
        return "Father is speaking"
class Mother(Father):
    def Mother_speak():
        return "Mother is speaking" 
class Kid(Father,Mother):
    def Kid_speak():
         return "kid is speaking"    
obj1=Father
obj2=Mother
obj3=Kid
print(obj1.Father_speak()) 
print(obj2.Mother_speak())
print(obj3.Kid_speak())


    
    