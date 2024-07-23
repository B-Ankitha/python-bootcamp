'''input ABC skip=4
output: EFG'''
str=input()
for i in str:
    if(ord(i)>=65 and ord(i)<=90):
        print(ord(i)+4)
        print(chr(ord(i)+4))

# skip=int(input())
# for i in str:
#     print(i)

'''input:XYZ
skip:3
output:BCD
'''
str=input()
for i in str:
    if(ord(i)>=65 and ord(i)<=90):
        print(chr(ord(i)+3))

        #print(chr(ord(i)+3))

'''hello ---world
----hello world'''
