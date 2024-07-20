''' WAP to find the reverse of a number'''


n=int(input())
rem=0
rev=" "
#rev=0
while(n>0):
    rem=n%10
    rev=rev+str(rem)
    #rev=rev*10+rem
    n=n//10
print(rev)    
#print(int(rev))
#type(rev)