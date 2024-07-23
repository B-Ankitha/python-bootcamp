'''
input: hello123
output:6'''

# str=input()
# convert=int(str)
# print(convert)
# #print(convert)
# s=0
# count=0
# while(convert>0):
#     rem=convert%10
#     s+=rem*10
#     convert//=10
# print(s)

    
    

str=input()
digit="0123456789"
s=0
for i in str:
    if i in digit:
        s+=(int(i))
print(s)        

str=input()
str=input()
sum=0
for i in str:
    if(ord(i)>=48 and ord(i)<=58):
        sum+=int(i)
print(sum)             

