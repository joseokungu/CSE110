S = 0
for i in range(1,9):
    print("Entrez N",i,":", end="")
    N = int(input())
    if N < 0 :
        continue
    S = S+N
print("La somme est :",S)    