n=int(input("enter year="))
if (n%4==0 & n%100==0 & n%400==0):
    print("leap year")
else:
    print("not leap year")