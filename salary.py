"""Write a Python program that accepts an employee's ID, total worked hours of a month and the amount ' \
S/he received per hour. Print the employee's ID and salary (with two decimal places) of a ' \
particular month. S/he has day off on Friday and Saturday. """
n=int(input("Number of Employee:"))
i=0
for i in range (n):
    Id = int(input("Enter employee Id:"))
    h= float(input("Enter hour:"))
    s = float(input("Enter salary:"))
    salary = h*s
    print ("Id = ",Id)
    print("Salary =  %.2lf" %salary)

