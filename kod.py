x = ("skriv ett heltal :")
y = int(input(x))
print(y)

a = ("skriv ett decimaltal ")
b = float(input(a))
svaret = y + b
print ("svaret på det var:", svaret)
print("detdär var enkelt, ge mig något svårare nu som jag lägger i kvadrat")


c = (":")
output = int(input(c))
svar = output * output
print("talet i kvadrat är:", svar)

print("nu testar vi division,")
tal = float(input("skriv ett tal som du vill dela med 2: "))
print (tal / 2)
repeat = input("vill du göra en ny beräkning? (ja,nej)")
if repeat == "ja":

    print("Vad vill du räkna ut?")

print()
    print("1. Addition (+)")
    print("2. Subtraktion (-)")
    print("3. Multiplikation (*)")
    print("4. Division (/)")
    print("5. Kvadrat (x²)")
