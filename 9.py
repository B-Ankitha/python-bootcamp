'''  middle (8)th line is very very important(logic)
1 and the 3 line are common for all
sum of the digits '''
n=int(input())
sum=0
while(n>0):
    rem=n%10
    sum+=rem
    n//=10
print(sum)   


''' find the sum of squares of a digit 
123
1*1+2*2+3*3====1+4+9===14'''
n=123
s=0
while(n>0):
    rem=n%10
    s+=rem*rem
    n//=10
print(s)    



'''
1234==2+4===6

'''
n=1234
sum=0
while n>0:
    r=n%10
    if(r%2==0):
        sum+=r
    n//=10
print(sum)   