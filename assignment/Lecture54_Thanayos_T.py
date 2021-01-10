# homework lecture 54 login+price calculator
def login():
    usernameInput = input("username: ")
    passwordInput = input("password: ")
    if usernameInput == "admin" and passwordInput == "password":
        showMenu()
        selectMenu()
    else:
        print("username or password incorrect\n"+"please try again")
        login()
def showMenu():
    print( "Done!!" )
    print("--Welcome to Gunpla ABC shop--")
    print("selected menu")
    print("1 Vat Calculator")
    print("2 Price Calculator")
def selectMenu():
    userSelected = int(input(">>"))
    if userSelected == 1:
        vatCalculator(int(input("product price: ")))
    elif userSelected == 2:
        priceCalculator()
    else:
        print("chosen error, please try again")
        selectMenu()
def vatCalculator(totalPrice):
    vat = 7 / 100
    result = totalPrice + (vat * totalPrice)
    print("Net price =",result)
    return result
def priceCalculator():
    n = int(input("ระบุจำนวนสินค้าที่ต้องการคำนวน: "))
    sum = 0
    for i in range(n):
        priceProduct = int(input(f"product number {i + 1}: "))
        sum += priceProduct
    return vatCalculator(sum)
login()