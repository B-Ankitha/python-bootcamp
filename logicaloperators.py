age=int(input())
#age=56
if(age>=18 and age<24):
    print("only 2 wheelers")
elif(age>=24 and age<45):
    print("2 and 4 wheelers")
elif(age>=46):
    print("all")

#x goes to market he will buy 10 apples,2 dozen bananas, 8 oranges,the cost of 1 apple is 15 rupees,the cost of one orange is 5 rupees,the cost of each banana is 4 rupees,the mother of mister    
#10*15=150(apples)
#24*4=96(banasa)
#8*5=40(oranges)
#total=286

apples=10
bananas=24
oranges=8
total=0
total=(10*15+24*4+8*5)
print(total)
if(total>=700):
    print("not got cheated")
else:
    print("got cheated")
 
