''' you r given with a comma seperated natural numbers 1 to 10 print only even numbers
'''
# list2=list(map(int,input().split(",")))
# for i in range(1,len(list2)):
#     if(list2[i]%2==0):
#         print(list2[i])


'''another easy method using single line'''
list12=list(map(int,input().split(",")))
for i in range(1,len(list12),2):
    print(list12[i])

''' how many even numbers are there in above seventh.py '''

list12=list(map(int,input().split(" ")))
c=0
for i in range(1,len(list12),2):
   # print(list12[i])
   c=c+1
print(c)   






# list1=[1,2,3,4,5,6,7,8,9,10]
# for i in range(1,11,2):
#     print(list1[i])


''' your given witha space seperated integer list 
find no of even ele and odd elements '''
''' how many even numbers are there in above seventh.py '''

list12=list(map(int,input().split(" ")))
c=0
c1=0
for i in range(0,len(list12)):
   # print(list12[i])
   if(list12[i]%2==0):
      c+=1
   else:
      c1+=1  
print(c,c1)      
#print(" no of even  number is c =" c " no of odd numbers is "c1)   
#c=4
# g=6
# print("even numbers are ",c ,"and no of odd numbers are g",g)