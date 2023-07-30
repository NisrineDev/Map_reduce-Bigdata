#!/usr/bin/env python

import sys

# sauter l'entête du fichier
next(sys.stdin)

for line in sys.stdin:
    columns = line.strip().split('\t') #diviser les colonnes
    for i in range(3, len(columns)): #boucle sur les colonnes de dates
        country = columns[1] #définir la colonne du pays
        deaths = [int(c) for c in columns[i].split('\t') if c != ''] #sauter les valeurs manquantes
        death = sum(deaths) if deaths else 0 
        print(f"{country}\t{death}") #le couple clé-valeur du map
