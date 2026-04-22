year=int(input("Enter year"))
if year%100==0:
    if year%400==0:
        print("leap year")
    else:
        print("Non Leap Year")
else:
    if year%4==0:
        print("Leap Year")
    else:
        print("Non Leap Year")
