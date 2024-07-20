#4 peek ele in array
list1=list(map(int,input().split(" ")))
peek=0
a=len(list1)
mid=a//2
for i in range(a):
    if(list1[mid]>list[i]):
        print(list1[mid])


