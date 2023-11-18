a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))
if (a>b & a>c):
    print("a is greatest")
elif (b>c & b>a):
    print("b is greatest")
else:
    print("c is greatest")