aantal = int(input('Hoeveel niet-negatieve getallen wil je invoeren?'))
antwoord = 1
for x in range(aantal):
    antwoord *= x + 1
    
print(antwoord)
    
