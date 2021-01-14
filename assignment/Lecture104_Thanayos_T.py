# Lecture 104 สร้าง class เก็บ ชื่อ นามสกุล อายุ แจ้งการซื้อของลูกค้า สร้างลูกค้า 4 คน
class Customer:
    name = ""
    lastName = ""
    age = 0
    def createCustomer(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = age
    def addCart(self):  
        print( "Added product to %s %s's cart" % (self.name, self.lastName) )

customer1 = Customer() 
customer1.name = "Barry" 
customer1.lastName = "Alen"
customer1.age = 24
customer1.addCart()  

customer2 = Customer()
customer2.createCustomer("Peter","Parker",26)
customer2.addCart()

customer3 = Customer()
customer3.createCustomer("Tony","Stark",35)
customer3.addCart()

customer4 = Customer()
customer4.createCustomer("Bruce","Wayne",37)
customer4.addCart()
