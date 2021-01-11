"""
    โปรแกรมแสดงบิล
    กรอก menu และ ราคาเรื่อยๆจนกรอก exit
    แสดงราคารวมสินค้า
"""
menuList = []
priceList = []
totals = 0
while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":      # ให้ check โดยแปลงเป็น lower ให้หมดถ้ากรอก exit ก็ออก loop เลย
        break
    else:
        menuPrize = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrize)
def showBill():
    global totals
    for i in range(len(priceList)):
        totals += priceList[i]
    print("---My food---")
    for x in range(len(menuList)):      # ทำแบบนี้ได้เลยเพราะสมาชิก ทั้ง 2 list เท่ากันและกรอกมาคู่กัน
        print(f"{menuList[x]} = {priceList[x]}")
    print("total =", totals)
showBill()
