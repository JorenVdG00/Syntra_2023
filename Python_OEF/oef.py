def oppDriehoek(basis, hoogte):
    return (basis*hoogte)/2
def volKubus(zijde):
    return zijde**3
def tweelaatste(nr):
    return nr%100
print(tweelaatste(793257))
print(volKubus(25))
print(oppDriehoek(15,36))

def som(getal1,getal2):
    som = getal1+getal2
    return som
print(som(1,6))

def gemiddelde(lijstgetallen):
    som=0
    for getallen in lijstgetallen:
        som+=getallen
    return som/len(lijstgetallen)
print(gemiddelde([1,2,3,7,9,5,4,6,8]))

def tweelaatsteB(tekst):
    tekstB = str(tekst)
    return tekstB[(len(tekstB)-2):len(tekstB)]
print(tweelaatsteB(793257))

getal=123
print(tweelaatsteB(str(getal)))
