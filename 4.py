''''min element in list'''


# list1=list(map(int,input().split(" ")))
# a=len(list1)
# for i in range(a):
#     min1=list1[0]
#     if(min1>list1[i]):
#         min1=list1[i]
# print(min1)    

''''replace the elements in array with average of maximum and minimum elements 
tc-1
13 2 67 20 68
68+2=70===35
output==35 35 35 35 35


'''
list1=list(map(int,input().split(" ")))
a=len(list1)
sum=0
avg=0
max1=list1[0]
min1=list1[0]
for i in range(a):
    if(max1<list1[i]):
        max1=list1[i]
print(max1)    
for i in range(a):
 if(min1>list1[i]):
       min1=list1[i] 
print(min1)       
sum=min1+max1
print(sum)
avg=sum//2
for i in range(a):
    list1=avg
#list1=avg
    print(list1,end=" ")       