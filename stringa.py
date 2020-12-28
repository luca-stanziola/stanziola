stringa = input("inserisci parola:")
print(stringa)
n = len(stringa)
print("la parola ha" + " " + str(n) + " " + "caratteri:")
i = 0
while i < n : 
    print("L" + str(i) + " " + stringa[i])
    i = i + 1
