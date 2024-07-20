'''1   find the sum of squares of given number 
2 find sum of squares of even and odd digits
3  check whether given number is palindrome or not
4 write a program to print first nth fibonaaci series'''
#1
n=int(input())
list1=list(map(int,input().split(" ")))
s=0
for i in range(n):
    s+=list1[i]*list1[i]
print(s) 


#2
#2 find sum of squares of even and odd digits
#2 find sum of squares of even and odd digits
list1=list(map(int,input().split(" ")))
s=0
s1=0
s2=0
for i in range(len(list1)):
    if(list1[i]%2==0):
        s+=list1[i]*list1[i]
        print(s)
    else:
        s1+=list1[i]*list1[i]
        print(s1)
s2=s+s1
print(s2)       

  #3  check whether given number is palindrome or not
n=int(input())
r=0
p=0
while(n>0):
    r=n%10
    p=p*10+r
    n//=10
print(p)
if n==p:
    print("palindrome")
else:
    print("not")    













