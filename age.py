first = int(input("Enter the First Age: "))
second = int(input("Enter the Second Age: "))
third = int(input("Enter the Third Age: "))
if first>second:
    print("Oldest Age is : ",first)
elif second>third:
    print("Oldest Age is : ",second)
elif third > first:
    print("Oldest Age is : ",third)