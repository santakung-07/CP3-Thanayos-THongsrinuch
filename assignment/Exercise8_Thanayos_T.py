# Exercise 8 program ขายของ
print("Sign in")
username_01 = "customer01"
password_01 = "0101"
userInput = input("username: ")
passInput = input("password: ")
vat = 7/100
if userInput == username_01 and passInput == password_01:
    print("--Welcome to Gunpla ABC shop--")
    print("Our product:")
    print("1 HG GN-000 0 Gundam          2000.00 THB per piece")
    print("2 HG GNY-001 Gundam Astraea   2500.00 THB per piece")
    print("3 HG GNY-002 Gundam Sadalsuud 2700.00 THB per piece")
    print("4 HG GNY-003 Gundam Abulhool  2400.00 THB per piece")
    print("5 HG GNY-004 Gundam Plutone   2300.00 THB per piece")
    addToCart = int(input("please select a product you need(1-5): "))
    quantity = int(input("quantity: "))
    if addToCart not in range(1,6):
        print("error")
    else:
        if addToCart == 1:
            price = (2000.00*quantity)
        elif addToCart == 2:
            price = 2500.00*quantity
        elif addToCart == 3:
            price = 2700.00*quantity
        elif addToCart == 4:
            price = 2400.00*quantity
        elif addToCart == 5:
            price = 2300.00*quantity
        VAT = price*vat
        VAT = format(VAT,".2f")
        price_2f = price.__format__(".2f")
        totalPrice = price+(price*vat)
        totalPrice = format(totalPrice,".2f")
        print(f"\tSUBTOTAL {price_2f} \tTHB")
        print(f"\tVAT\t {VAT} \tTHB")
        print(f"\tTOTAL\t {totalPrice} \tTHB")
        print("\t\tTHANK YOU")
else:
    print("username or password incorrect")
