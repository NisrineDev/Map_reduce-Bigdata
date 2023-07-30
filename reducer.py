#!/usr/bin/env python

import sys

current_country = None #initialisation du valeur contient le pays 
total_deaths = 0 #inistialisation du valeur contient le total des décès

for line in sys.stdin:
    country, death = line.strip().split('\t') #prenant comme entrées le couple clé-valeur de chez le map
    death = int(death)

    if current_country != country:
        if current_country is not None:
            print(f"{current_country}\t{total_deaths}") 
        current_country = country 
        total_deaths = 0

    total_deaths += death #on calcule la somme des décès

if current_country is not None:
    print(f"{current_country}\t{total_deaths}")
