lis = []
while len(lis)!=5:
    x = input("Enter number: ")
    if x.isdecimal():
        x = float(x)
    else:
        print("You didn't enter a number, try again (invalid input)")
        continue
    if not(x in lis):
        lis.append(x)
    else:
        print("Number already exists in list. Try again")
print(lis)
