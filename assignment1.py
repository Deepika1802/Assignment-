#ques1
print("Hello World")

#ques2, ques3
name = "Deepika Yadav" #stores name in name variable
age = 22 #stores 22 in age variable
hobby = "Reading"  #stores reading in hobby variable
print(name, age, hobby) 

#ques4
a = int(input("Enter your number: "))
if(a>0):
    print("a is positive")
elif(a<0):
    print("a is negative")
else:
    print("a is zero")

#ques5
yr = int(input("Enter a year: "))

if yr % 400 == 0:
    print(f"{yr} is a leap year.")
elif yr % 100 == 0:
    print(f"{yr} is not a leap year.")
elif yr % 4 == 0:
    print(f"{yr} is a leap year.")
else:
    print(f"{yr} is not a leap year.")

#ques6
for x in range(1, 11):
    print(x)

#ques7
n = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i = i+1

#ques8
for x in range(1, 11):
    if x % 3 == 0:
        continue
    print(x)
#ques10
def greet(name):
    print(f"Hello, {name}!")
    greet("Deepika")

#ques11
def add(n1, n2):
    return n1 + n2

result = add(5, 7)
print(result) 

#ques9
for number in range(1, 11):
    print(number)
    if number > 5:
        break

