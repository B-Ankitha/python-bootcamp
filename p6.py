''''WAP tp print the vowels and consonents'''
str=input()
vowels="aeiou"
cv=""
cc=""
consonents="bcdfghjklmnpqrstvwxyz"
for i in str:
    if i in vowels:
        cv+=i
        #print(cv)
for j in str:
    if j in consonents:
        cc+=j
print(cv+cc)        
        
'''WAP print the unique characters in string'''

str=input()
a=len(str)
ans=""
#c=0
for i in str:
    if i not in ans:
        ans+=i
print(ans)        

    