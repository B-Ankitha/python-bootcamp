''' product based company question
suppose to print the element in particualr index condition is cyclic printing
TC-1
k=20
70 54 36 72 76 99 89
length=7
output:6

TC-2
k=18
80 70 54 36 77
length=5
output:3

TC-3
k=38
70 54 36 72 59
length=5
output:3




cyclic rotation of a array in leetcode





we have another method to solve this (-) subtraction method 
k=20
70 54 36 72 76 99 89
length=7

k-length===(20-7=13)
mod operation must to be used
which is time consuming processs and run time error(time limit exceed)

output:6'''

k=11
list1=list(map(int,input().split(" ")))
a=len(list1)
m=k%a
print(list1[m-1])


