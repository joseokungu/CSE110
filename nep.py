L = int(input("Veuillez saisir le nombre de lignes : "))
for i in range (1,L+1):
    for j in range (1,L-i+1):
        print(" ", end="")
    for j in range(1,i+1):
        print(i-j+1,end="")
    for j in range (2,i+1):
        print(j,end="")
    print("")    