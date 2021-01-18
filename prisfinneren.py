#Denne vasijonen er laget av @BlueLLD

#Skriv rabbaten (prosent) her:
rabatt = 21
#Rabbaten (nummer) her:
rabattnummer = None
#Skriv gammelpris her:
gammelpris = None
#Skriv nypris her:
nypris = 948

if rabatt is None:
    try:
        rabatt = rabattnummer / (nypris + rabattnummer) * 100
    except TypeError:
        try:
            rabatt = (gammelpris - nypris) / gammelpris * 100
        except TypeError:
            rabatt = rabattnummer / gammelpris * 100
            nypris = gammelpris - rabattnummer
        
if rabattnummer is None:
    try:
        rabattnummer = gammelpris - nypris
    except TypeError:
        try:
            rabattnummer = nypris / (1 - rabatt / 100) * (rabatt / 100)
        except TypeError:
            rabattnummer = gammelpris * (rabatt / 100)
            nypris = gammelpris - rabattnummer

gammelpris = rabattnummer / (rabatt / 100)
nypris = rabattnummer / (rabatt / 100) * (1 - rabatt / 100)

print("rabatt: " + str(float(rabatt)))
print("rabattnummer: " + str(float(rabattnummer)))
print("gammelpris: " + str(gammelpris))
print("nypris: " + str(float(nypris)))
