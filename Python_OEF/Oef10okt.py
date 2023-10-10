getal = []
i=0
j=0
deeltal=int(input("geef je veelvoud getal waar je alle veelvouden van wilt weten::::"))
while i < 5:
    andergetal = int(input("geef getal(1-100) asap: "))
    if 0 < andergetal <= 100:
        getal.append(andergetal)
        i+=1
    else:
        print("getal tussen1-100")
for i in range(len(getal)):
    j=1
    deelbaar = []
    for j in range(getal[i]+1):
        if j % deeltal == 0:
            deelbaar.append(j)
    simpleD = sorted(set(deelbaar))
    print(str(j) + " deelshit " +str(simpleD))
