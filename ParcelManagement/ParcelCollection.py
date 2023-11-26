#creating parcel class
class parcel():
    def __init__(self, height, length, width, weight, sign, track):
        self.height = height
        self.length = length
        self.width = width
        self.weight = weight
        self.sign = sign
        self.track = track

#calculating size of package
        size = length * width * height

#calculating cost
        if weight > 40 | size > 1000:
            cost = 30
        elif weight > 20 | size > 500:
            cost = 20
        else:
            cost = 10
        if sign:
            cost += 2
        if track:
            cost += 5
        self.cost = cost
    
#creating menu
def menu():
    print("1. collect parcel\n2. Exit")
    choice = input()
    while not choice == "1" and not choice == "2":
        choice = input("Please choose either 1 or 2\n")
    return choice

#creating option for sign and track
def yesno():
    print("1. Yes\n2. No\n")
    choice = input()
    while not choice == "1" and not choice == "2":
        choice = input("Please enter either 1 or 2\n")
    if choice == "1":
        return True
    else:
        return False

#menu choice
choice = menu()
while choice == "1":

#input user name
    name = input("Please enter your name\n")
    while len(name) == 0 or name.isspace():
        name = input("You cannot enter blank\n")
#input user address       
    address = input("Please enter your address\n")
    while len(address) == 0 or address.isspace():
        adress = input("You cannot enter blank\n")
#input user phone       
    phone = input("Please enter your phone\n")
    while not phone.isnumeric() or not len(phone) in range(11,16):
        phone = input("Phone must be numeric and between 11 and 16 digits\n")
        
#input number of parcels maximum number is 6
    numParcels = input("Howmany parcels do you wish to collect\n")
    while not numParcels.isnumeric() or not len(numParcels) in range(1,7):
        numParcels = input("It must be between 1 and 6\n")
    numParcels = int(numParcels)

#array of parcels to be stored
    parcels = []

#collecting dimensions for each parcel
    for i in range(numParcels):
        height = 1
        length = 1
        width = 10001
        print("Insert details for parcel",i+1)
        if (height * length * width) < 10000:
            height = input("Please input the height of the parcel\n")
            while not height.isnumeric() or int(height) <= 0:
                height = input("Please only input numbers\n")
            height = int(height)
            length = input("Please input the length of the parcel\n")
            while not length.isnumeric() or int(length)<= 0:
                length = input("Please only input numbers\n")
            length = int(length)
            
            width = input("Please input the width of the parcel\n")
            while not width.isnumeric() or int(width) > length or int(width) <= 0:
                width = input("Width must be smaller than length\n")
            width = int(width)
        
        #calculating parcl dimensions
        size = height * length * width

        #collecting parcel weight
        weight = input("Please enter weight of parcel in kg\n")
        while not weight.isnumeric() or int(weight) > 40:
            weight = input("Please enter a number between 1 and 40\n")
        weight = int(weight)

        #asking if user wishes to sign parcel
        print("Do you want the parcel to be signed for")
        sign = yesno()

        #asking if user wishes to track parcel
        print("Do you want the parcel to be tracked")
        track = yesno()
        parcels.append(parcel(height, length, width, weight, sign, track))

    #print receipt details    
    print("Customer name",name)
    print("Customer address",address)
    print("Customer phone",phone)
    print("Number of parcels",numParcels)
    temp = i 
    total = 0
    
    for el in parcels:
        if el.sign and el.track:
            addCost = 7
        elif el.sign:
            addCost = 2
        elif el.track:
            addCost = 5
        else:
            addCost = 0
        
        #print parcel costs
        print("Parcel",temp,"costs",el.cost,"with",addCost,"for signature and tracking")
        total += el.cost
    print("Your total cost is",total)

    #asking if user wishes to add more parcels
    choice = menu()
        
