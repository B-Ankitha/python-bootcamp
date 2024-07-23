'''hello ---world
output: --- hello world'''
'''hint: print("-"*30)'''
# str=input()
# print(str+"-"*30)

str=input()
c=0
ans=""
for i in str:
    if(i=="-"):
        c+=1
    else:
        ans+=i
print("-"*c+ans)