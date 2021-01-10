# Homework lecture53 vatCalculator
totalPrice = 0
def vatCalculate(totalPrice):
    totalPrice = int(input("insert total price>> "))
    result = totalPrice+(totalPrice*(7/100))
    return result


print("Net price =",vatCalculate(totalPrice))