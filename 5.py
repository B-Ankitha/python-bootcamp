''''1 find the missing number in an array
stmt: sequence of numbers 1 to 50 
it will work only for continuous not for the sub elements like 5 4 7 2 we can find it '''
list1=list(map(int,input().split(" ")))
sum1=0
missing=0
a=len(list1)+1
sum=a*(a+1)//2
print(sum)
for i in range(a-1):
   sum1+=list1[i]
print(sum1)
missing=sum-sum1
print(missing)


''' find the dublicants in array
 '''
#dublicants
# 8 7 7 8 5 4 4 8 9-------8 7 4
list1=list(map(int,input().split(" ")))
list12=[]
for i in list1:
    if(i not in list12):
        list12.append(i)
print(*list12)        


#dublicants
# 8 7 7 8 5 4 4 8 9-------8 7 4
list1=list(map(int,input().split(" ")))
list12=[]
for i in list1:
    if(i not in list12):
        list12.append(i)
print(*list12)        



#dublicants
# 8 7 7 8 5 4 4 8 9-------8 7 4
list1=list(map(int,input().split(" ")))
list12=[]
for i in list1:
    if(i in list12):
        list12.append(i)
print(*list12)        


