import sys
#Skriv rabbaten (prosent) her:
rabatt = None
#Rabbaten (nummer) her:
rabattnummer = None
#Skriv gammelpris her:
gammelpris = None
#Skriv nypris her:
nypris = None
#testkode
if 1 + 1 is not 2:
    print("no! >:(")
    print("math is hard. ok.")
    print("error1")
    sys.exit(1)
#Kode
if rabatt is None:
    if gammelpris is not None and nypris is not None:
        rabatt = (gammelpris - nypris) / gammelpris * 100
    elif gammelpris is not None and rabattnummer is not None:
        rabatt = rabattnummer / gammelpris * 100
    elif rabattnummer is not None and nypris is not None:
        rabatt = rabattnummer / (nypris + rabattnummer) * 100

if rabattnummer is None:
    if rabatt is not None and gammelpris is not None:
        rabattnummer = gammelpris * (rabatt / 100)
    elif rabatt is not None and nypris is not None:
        rabattnummer = nypris / (1 - rabatt / 100) * (rabatt / 100)
    elif gammelpris is not None and nypris is not None:
        rabattnummer = gammelpris - nypris

if gammelpris is None:
    if rabatt is not None and rabattnummer is not None:
        gammelpris = rabattnummer / (rabatt / 100)
    elif rabatt is not None and nypris is not None:
        gammelpris = nypris / (1 - rabatt / 100)
    elif rabattnummer is not None and nypris is not None:
        gammelpris = rabattnummer + nypris

if nypris is None:
    if rabatt is not None and rabattnummer is not None:
        nypris = rabattnummer / (rabatt / 100) * (1 - rabatt / 100)
    elif rabatt is not None and gammelpris is not None:
        nypris = (1 - rabatt / 100) * gammelpris
    elif rabattnummer is not None and gammelpris is not None:
        nypris = gammelpris - rabattnummer

if rabatt is not None and rabbatnumber is not None and gammelpris is not None and nypris is not None:
    print("rabatt: " + str(float(rabatt)))
    print("rabattnummer: " + str(float(rabattnummer)))
    print("gammelpris: " + str(float(gammelpris)))
    print("nypris: " + str(float(nypris)))
else:
    print("finnes ingen tall")
    print("error2")
