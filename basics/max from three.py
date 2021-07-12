def maximum(a,b,c):
    if(a>=b and a>=c):
        print("a is max")
    elif(b>=a and b>=c):
        print("b is max")
    else:
        print("c is max")

x = int(input())
y = int(input())
z = int(input())

maximum(x,y,z)

# if x>y:
#     if x>z:
#         print("x is max")
# elif y>x:
#     if y>z:
#         print("y is max")
# else:
#     print("z is max")

