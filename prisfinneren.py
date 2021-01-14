#Skriv rabbaten (prosent) her:
rabbat = 0
#Rabbaten (nummer) her:
rabbatnumber = 100
#Skriv gammelpris her:
gammelpris = 1000
#Skriv nypris her:
nypris = 900
#Skriv hva du vil regne ut
#1 = Gammelpris + Rabbat = Nypris
#2 = Gammelpris + Nypris = Rabbat
#3 = Nypris + Rabbat = Gammelpris
#4 = Rabbatnumber + Gammelpris = Nypris
regnetype = 2
#Kode / Formel:
print("Hello World")
if regnetype == 1:
    print("Den nye prisen er:")
    print((1 - rabbat * .01) * gammelpris)

elif regnetype == 2:
    print("Rabbaten på produktet er:")
    print((gammelpris - nypris) / gammelpris * 100)

elif regnetype == 3:
    print("Den gamle prisen er:")
    print(nypris / (1 - rabbat * .01))

elif regnetype == 4:
    print("Den nye prisen er:")
    print(gammelpris - rabbatnumber)

else:
    print ("velg et bedre tall >:(")
