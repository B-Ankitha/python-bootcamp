'''WAP code to find the no of vowels '''
# str=input()
# c=0
# vowels="aeiouAEIOU"
# for i in str:
#     if i in vowels:
#         c+=1
# print(c)        


'''method-2'''
check=['a','e','i','o','u']
c=0
str=input()
for i in str:
    if i not in check:
        c+=1
print(c)        
