class Animal:
    def Speak():
        return "ANIMAL IS SPEAKING"
class Dog(Animal):
    def Bark():
        return "dog is barking"    
class Puppy(Dog):
    def P_Speak():
        return "puppy is speaking"
obj1=Puppy
print(obj1.P_Speak())   
obj1=Animal 
print(obj1.Speak())
