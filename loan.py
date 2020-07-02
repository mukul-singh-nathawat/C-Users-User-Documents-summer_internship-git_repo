occupation = ['government','business']
ocup = input("enter occupation : ")
if ocup not in occupation:
    print("bhag gareeb")
else:
    if ocup == 'government':
        print("submit your documentation")
        name = input("enter name")
        ammount = input("enter ammount")
        loan = { 'name ' : name,'ammount':ammount}
        print("details",loan)
        print("loan granted")
    elif ocup =='business':
        turnover = int(input("enter turnover"))
        if turnover < 5000000:
                print("bhag gareeb")
        else:
                print("enter details:")
                name = input("enter name")
                ammount = input("enter ammount")
                loan = { 'name ' : name,'ammount':ammount}
                print("details:",loan)
                print("loan granted")
