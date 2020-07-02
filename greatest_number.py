value1 = int(input("enter first value: "))
value2 = int(input("enter second value: "))
value3 = int(input("enter third value: "))
if value1 > value2 and value1 >value3:
    print("value 1 is greatest among all")
    if value1 < value3:
        print("value 3 is greatest")
elif value2 >value3:
    print("value 2 is greatest among all")
    if value2 < value3:
        print("value 3 is greatest among all")
else:
    if value1 == value2 or value1 == value3 or value2 == value3:
        if value1 == value2 and value1 == value3:
            print("all values are same")
        elif value1==value2:
            print("value 1 and 2 are same and greatest")        
        elif value2 == value3:
            print("value 2 and 3 are same and greatest")        
        elif value1 == value3:
            print("value 1 and 3 are same and greatest")

