'''WAP GIVEN A  SPACE SEPERATED INTEGER LIST 
FIND THE AVG OF ELEMETS PRESENT IN THE EVEN INDEX  
'''

list11=list(map(int,input().split(" ")))
avg=0
sum=0
count=0
a=len(list11)
print(a)
for i in range(0,len(list11)):
    if(i%2==0):
        sum+=list11[i]
        count+=1
avg=sum/count
print(avg)        

