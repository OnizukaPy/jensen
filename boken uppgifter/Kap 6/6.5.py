# Kontantkort, lägsta pris

namn = []
pris = []

while True:
    s = input("Namnoch pris för ett kort: ")
    if s == "":
        break
    
    s = s.rpartition(" ")
    namn.append(s[0])
    pris.append(float(s[2]))
    #s = s.strip()
    #i = s.rfind(" ")
    #namn.append(s[0:i])
    #pris.append(float(s[i+1:]))

m = min(pris)
k = pris.index(m)
print(namn[k] + " är billigast")
print(f"Kostan: {m:.2f} kr/månad")