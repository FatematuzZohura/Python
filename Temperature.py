"""Write a program to convert Fahrenheit to Celsius or vice versa using functions."""
def Fahrenhiet():
    f = float(input("Enter the temperature Fahrenhiet: "))
    c = (f-32)*5/9
    print("Celsius:",c)
def Celsius():
    d = float(input("Enter the temperature Celsius: "))
    e = (d*(9/5))+32
    print("Fahrenhiet:",e)


T=int(input("Enter 1 foe F to C,Otherwise 0:"))
if T==1:
    Fahrenhiet()

else:
    Celsius()


