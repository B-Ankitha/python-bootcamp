'''WAPP find area of circle 
WAP to find perimeter of a circle
WAp to find area of a triangle
WAP to find perimeter of a triangle
WAP to find area and perimeter of a rectangle 
WAP to find the sqrt method for the prime number'''


#1
radius=int(input())
print("Area of circle",3.14*radius*radius)

#2
r=int(input())
print("Perimeter of circle is",2*3.14*r)

#3
l,b=map(int,input().split(" "))
print("Area of triangle is",0.5*(l*b))

#4
l,b,h=map(int,input().split(" "))
print("Perimeter of a triangle is ",l+b+h)

#5
l,b=map(int,input().split(" "))
print("Area of a rectangle is ",l*b)
print("perimeter of a rectangle is ",2*(l+b))


