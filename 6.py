''''1    find ven or odd for list
2  find greatest of 3 
3 find sum of all elemets in array
4*** find peek element in the array 
5 find max elemet in array
6 find the 2 nd maximum element in array
7 reverse an array without using built in functions
 '''

#1
list1=list(map(int,input().split(" ")))
for i in range(len(list1)):
    if(list1[i]%2==0):
        print(list1[i])

#2
#list1=list(map(int,input().split(" ")))  
a,b,c=map(int,input().split(" "))
if(a>b and b>c and a>c):
    print(a)
elif(b>a and c>a and b>c):
    print(b)
else:
    print(c)    


#3
list1=list(map(int,input().split(" ")))
sum=0
for i in list1:
    sum+=i
print(sum)   

#4 peek ele in array
list1=list(map(int,input().split(" ")))
peek=0
a=len(list1)
mid=a//2
for i in range(a):
    if(list1[mid]>list[i]):
        print(list1[mid])




