'''its the no of parameters
self===dynamic inputs

in python polymorphism is the not there
to overcome ===to that we will us method overloading,ridding
static ==runtime==
dynamic===compile time=='''


# class Cal:
#     def add(self,args):
#         return sum(args)
# obj=Cal
# print(obj.add())    

#Cal.add() missing 2 required positional arguments: 'self' and 'args'

# class Cal:
#     def add(a,b,c):
#         return a+b+c
#     def add1(a,b,e,d,f):
#         return a+b+e+d+f
# obj=Cal
# print(obj.add(1,2,3))
# obj1=Cal
# print(obj.add(1,2,3,4,5))  
#same methods cant be  thereCal.add() missing 2 required positional arguments: 'd' and 'f'


class Cal:
    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        return(sum)
obj=Cal
print(obj.add(1,2,3,4,5))    