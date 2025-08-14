def hesap(x,y,islem):
    if islem == "+":
        return (str(x) + " + " + str(y) + " = " + str(x + y))
    elif islem == "-":
        return (str(x) + " - " + str(y) + " = " + str(x - y))
    elif islem == "*":
        return (str(x) + " * " + str(y) + " = " + str(x * y))
    elif islem == "/":
        return (str(x) + " / " + str(y) + " = " + str(x / y))
    else:
        return "Geçersiz işlem"
    
x = (int(input("ilk sayıyı giriniz: ")))
y = (int(input("ikinci sayıyı giriniz: ")))
islem = (input("işlemi giriniz (+, -, *, /): "))
print(hesap(x, y, islem))