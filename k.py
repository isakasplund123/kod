ålder = int(input("Hur gammal är du?"))
if (ålder > 18):
    print("du är myndig")
elif(ålder < 12):
    print("du är ett barn")
else:
    print("du är tonåring")

print("igen?")
if (input("ja eller nej?") == "ja"):
    ålder = int(input("hur gammal är du?"))
    if (ålder > 18):
        print("du är myndig")
    elif(ålder < 12):
        print("du är ett barn")
    else:
        print("du är tonåring") 
print("igen?")
if (input("ja eller nej?") == "nej"):
    print("okej, hejdå")
if(input("ja eller nej?") == "ja"):
    ålder = int(input("hur gammal är du?"))
    if (ålder > 18):
        print("du är myndig")
    elif(ålder < 12):
        print("du är ett barn")
    else:
        print("du är tonåring")