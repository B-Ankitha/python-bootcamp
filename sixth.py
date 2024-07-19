'''WAPP list of elemets count how many 
take a input space seperated input from user and print alernate elements '''
list1=list(map(int,input().split(" ")))
a=len(list1)#this the number of ele present in list
print(a)
for i  in range(0,a,2):#in range we can take only the length cant take all the list and place in it 
    print(list1[i])