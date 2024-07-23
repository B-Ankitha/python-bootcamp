'''reverse the string'''
str=input()
digit="0123456789"
s=""
for i in str:
    if i in digit:
        s+=i
print(s) 
n=int(s)
print(n)
rem=0
rev=0  
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)    
