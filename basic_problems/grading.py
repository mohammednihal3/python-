marks = int(input("enter your marks:"))
if 90 <= marks <= 100:
    print("A grade")
elif 75 <= marks <= 89:
    print("B grade")
elif 60 <= marks <= 74:
    print("C grade")
elif 40 <= marks <= 59:
    print("D grade")
else:
    print("F")
