#D-3) Applications

# 1)
# Var1 = input("Donner votre prénom ")
# print("Bonjour " + Var1 + " !")

# 2)
# mot = input("Donner un mot ")
# print("la taille du mot", mot, "est de " + str(len(mot)) + " caractères")

# 3)
# Var1 = input("Donner votre prénom ")
# for i in Var1 :
#    print(i) 
# ce programe affiche chaque lettre du prénom sur une ligne différente
# les valeur prise par i sont les lettres du prénom
"""
exemple d'affichage
si le prénom est  Mathias
M
a
t
h
i
a
s
"""

# Var1 = input("Donner votre prénom ")
# for i in Var1 :
#    print(i,end=" / ")    # ce programe affiche chaque lettre du prénom sur la meme ligne avec un / entre chaque lettre

# 4)
# mot = input("Ecrire un mot : ")
# lettre = input("Donner une lettre : ")
# Compteur = 0
# for j in mot:
#    if j == lettre:
#       Compteur = Compteur +1  
# print("Le mot", mot, "contient ", Compteur," lettres ", lettre,".")

# ce programe compte le nombre de fois qu'une lettre est présente dans un mot
# il y a la variable mot qui est le mot et la variable lettre qui est la lettre à compter
# il y a la variable Compteur qui est initialisé à 0 et qui est incrémenté de 1 chaque fois que la lettre est trouvée dans le mot
# la variable j prend la valeur de chaque lettre du mot
# la différence entre = et == est que = est une affectation et == est une comparaison
# exemple d'affichage
"""
Ecrire un mot : Mathias
Donner une lettre : a
Le mot Mathias contient  2  lettres  a .
"""

# 5)
# Nombre1=input("Premier nombre ? ")
# print(Nombre1)
# Nombre2=input("Deuxième nombre ? ")
# print(Nombre2)
# print(Nombre1+Nombre2)

# exemple d'affichage
"""
Premier nombre ? 1
1
Deuxième nombre ? 2
2
12
"""

# si on veut additionner les deux nombres il faut les convertir en entier

# Nombre1=int(input("Premier nombre ? "))
# print(Nombre1)
# Nombre2=int(input("Deuxième nombre ? "))
# print(Nombre2)
# print(Nombre1+Nombre2)

# exemple d'affichage
"""
Premier nombre ? 1
1
Deuxième nombre ? 2
2
3
"""

# Est-ce que cette addition donne maintenant le bon résultat pour des nombres réels ?
# Non, car il faut utiliser la fonction float() pour convertir les nombres en flottants

# Nombre1=float(input("Premier nombre ? "))
# print(Nombre1)
# Nombre2=float(input("Deuxième nombre ? "))
# print(Nombre2)
# print(Nombre1+Nombre2)

# exemple d'affichage
"""
Premier nombre ? 1.2
1.2
Deuxième nombre ? 3.4
3.4
4.6
"""
# c'est le bon résultat pour des nombres réels


# 6)
# la somme, la soustraction, le produit et la division ( arrondi à 6 chiffres ) de ces deux nombres.

# Nombre1=float(input("Premier nombre ? "))
# print(Nombre1)
# Nombre2=float(input("Deuxième nombre ? "))
# print(Nombre2)
# print("La somme est de ", Nombre1+Nombre2)
# print("La soustraction est de ", Nombre1-Nombre2)
# print("Le produit est de ", Nombre1*Nombre2)
# print("La division est de ", round(Nombre1/Nombre2, 6))

# exemple d'affichage
"""
Premier nombre ? 2
2.0
Deuxième nombre ? 3
3.0
La somme est de  5.0
La soustraction est de  -1.0
Le produit est de  6.0
La division est de  0.666667
"""
"""autre exemple d'affichage
Premier nombre ? 12.5
12.5
Deuxième nombre ? 17.8
17.8
La somme est de  30.3
La soustraction est de  -5.300000000000001
Le produit est de  222.5
La division est de  0.702247
"""

# 7)
# deux   nombres   entiers   sont   saisis   dans   deux   boîtes   dedialogue différentes et qui affiche le quotient et le reste de la division de ces deux nombres.

# Nombre1=int(input("Premier nombre ? "))
# print(Nombre1)
# Nombre2=int(input("Deuxième nombre ? "))
# print(Nombre2)
# print("Le quotient est de ", Nombre1//Nombre2)
# print("Le reste est de ", Nombre1%Nombre2)

# exemple d'affichage
"""
Premier nombre ? 51
51
Deuxième nombre ? 10
10
Le quotient est de  5
Le reste est de  1
"""
""" autre exemple d'affichage
Premier nombre ? 17
17
Deuxième nombre ? 4
4
Le quotient est de  4
Le reste est de  1
"""

# 8)
# deviner un nombre entier généré par l'ordinateur.
# from random import *
# for j in range(10):
#    print(randint(0,100), end= " / ")

# exemple d'affichage
"""
43 / 63 / 70 / 40 / 96 / 63 / 64 / 5 / 36 / 71 / 
"""

# ce programme génère 10 nombres aléatoires entre 0 et 100
# la variable j prend la valeur de 0 à 9
# l'instruction print(randint(0,100), end= " / ") est répétée 10 fois
# la fonction randint(0,100) génère un nombre entier aléatoire entre 0 et 100

# from random import *
# Alea = randint(0,100)
# NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
# if NombreDonne == Alea :
#    print("Vous avez gagné !")
# else :
#    print("Vous avez perdu ! Le nombre cherché était ",Alea,".")

# exemple d'affichage
"""
Donner un nombre entier entre 0 et 100 50
Vous avez perdu ! Le nombre cherché était  5 .
"""


# from random import *
# Alea = randint(0,100)
# NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
# while NombreDonne != Alea : # != signifie différent de
#    if NombreDonne > Alea :
#       print(" Plus petit !")
#       NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
#    else :
#       print(" Plus grand !")
#       NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
# print("Vous avez gagné ! Le nombre cherché était bien ",Alea,".")
   
# exemple d'affichage
"""
Donner un nombre entier entre 0 et 100 50
 Plus grand !
Donner un nombre entier entre 0 et 100 75
 Plus grand !
Donner un nombre entier entre 0 et 100 90
 Plus grand !
Donner un nombre entier entre 0 et 100 95
Vous avez gagné ! Le nombre cherché était bien  95 .
"""

# from random import *
# Alea = randint(0,100)
# Compteur = 0
# NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
# while NombreDonne != Alea : # != signifie différent de
#    if NombreDonne > Alea :
#       print(" Plus petit !")
#       Compteur = Compteur + 1
#       NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
#    else :
#       print(" Plus grand !")
#       Compteur = Compteur + 1
#       NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
# print("Vous avez gagné ! Le nombre cherché était bien ",Alea,".")
# print("Vous avez trouvé en ", Compteur," essai(s).")

# exemple d'affichage
"""
Donner un nombre entier entre 0 et 100 50
 Plus grand !
Donner un nombre entier entre 0 et 100 75
 Plus grand !
Donner un nombre entier entre 0 et 100 90
 Plus grand !
Donner un nombre entier entre 0 et 100 95
Vous avez gagné ! Le nombre cherché était bien  95 .
Vous avez trouvé en  3  essai(s).
"""

# c'est faux car quant le conteur est à 0 a a déja fait un essai
# donc il faut initialiser le compteur à 1

# from random import *
# moyenne = []
# for i in range(9):
#    Alea = randint(0,100)
#    Compteur = 1
#    NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
#    while NombreDonne != Alea : # != signifie différent de
#       if NombreDonne > Alea :
#          print(" Plus petit !")
#          Compteur = Compteur + 1
#          NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
#       else :
#          print(" Plus grand !")
#          Compteur = Compteur + 1
#          NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
#    print("Vous avez gagné ! Le nombre cherché était bien ",Alea,".")
#    print("Vous avez trouvé en ", Compteur," essai(s).")
#    # faire un moyenne sur les 10 essais
#    moyenne.append(Compteur)
# print("La moyenne des essais est de ", sum(moyenne)/len(moyenne))

# exemple d'affichage
"""
Donner un nombre entier entre 0 et 100 50
 Plus petit !
Donner un nombre entier entre 0 et 100 25
 Plus grand !
Donner un nombre entier entre 0 et 100 40
 Plus grand !
Donner un nombre entier entre 0 et 100 45
 Plus petit !
Donner un nombre entier entre 0 et 100 44
 Plus petit !
Donner un nombre entier entre 0 et 100 43
Vous avez gagné ! Le nombre cherché était bien  43 .
Vous avez trouvé en  5  essai(s).
Donner un nombre entier entre 0 et 100 50
 Plus petit !
Donner un nombre entier entre 0 et 100 25
 Plus grand !
Donner un nombre entier entre 0 et 100 40
 Plus grand !
Donner un nombre entier entre 0 et 100 45
 Plus grand !
Donner un nombre entier entre 0 et 100 46
 Plus grand !
Donner un nombre entier entre 0 et 100 47
 Plus grand !
Donner un nombre entier entre 0 et 100 48
 Plus grand !
Donner un nombre entier entre 0 et 100 49
Vous avez gagné ! Le nombre cherché était bien  49 .
Vous avez trouvé en  8  essai(s).
Donner un nombre entier entre 0 et 100 50
 Plus petit !
Donner un nombre entier entre 0 et 100 25
 Plus petit !
Donner un nombre entier entre 0 et 100 10
 Plus grand !
Donner un nombre entier entre 0 et 100 15
 Plus grand !
Donner un nombre entier entre 0 et 100 20
 Plus grand !
Donner un nombre entier entre 0 et 100 24
 Plus petit !
Donner un nombre entier entre 0 et 100 23
 Plus petit !
Donner un nombre entier entre 0 et 100 22
Vous avez gagné ! Le nombre cherché était bien  22 .
Vous avez trouvé en  8  essai(s).
Donner un nombre entier entre 0 et 100 50
 Plus grand !
Donner un nombre entier entre 0 et 100 75
 Plus petit !
Donner un nombre entier entre 0 et 100 60
Vous avez gagné ! Le nombre cherché était bien  60 .
Vous avez trouvé en  3  essai(s).
Donner un nombre entier entre 0 et 100 50
 Plus petit !
Donner un nombre entier entre 0 et 100 25
 Plus petit !
Donner un nombre entier entre 0 et 100 20
 Plus petit !
Donner un nombre entier entre 0 et 100 10
 Plus grand !
Donner un nombre entier entre 0 et 100 15
 Plus petit !
Donner un nombre entier entre 0 et 100 12
 Plus grand !
Donner un nombre entier entre 0 et 100 13
Vous avez gagné ! Le nombre cherché était bien  13 .
Vous avez trouvé en  7  essai(s).
Donner un nombre entier entre 0 et 100 50
 Plus petit !
Donner un nombre entier entre 0 et 100 25
 Plus grand !
Donner un nombre entier entre 0 et 100 30
 Plus petit !
Donner un nombre entier entre 0 et 100 22
 Plus grand !
Donner un nombre entier entre 0 et 100 23
 Plus grand !
Donner un nombre entier entre 0 et 100 24
 Plus grand !
Donner un nombre entier entre 0 et 100 25
 Plus grand !
Donner un nombre entier entre 0 et 100 26
Vous avez gagné ! Le nombre cherché était bien  26 .
Vous avez trouvé en  8  essai(s).
Donner un nombre entier entre 0 et 100 50
 Plus grand !
Donner un nombre entier entre 0 et 100 75
 Plus grand !
Donner un nombre entier entre 0 et 100 80
 Plus grand !
Donner un nombre entier entre 0 et 100 90
 Plus grand !
Donner un nombre entier entre 0 et 100 95
 Plus grand !
Donner un nombre entier entre 0 et 100 97
Vous avez gagné ! Le nombre cherché était bien  97 .
Vous avez trouvé en  6  essai(s).
Donner un nombre entier entre 0 et 100 50
 Plus grand !
Donner un nombre entier entre 0 et 100 25
 Plus grand !
Donner un nombre entier entre 0 et 100 75
 Plus grand !
Donner un nombre entier entre 0 et 100 80
 Plus petit !
Donner un nombre entier entre 0 et 100 77
 Plus grand !
Donner un nombre entier entre 0 et 100 78
 Plus grand !
Donner un nombre entier entre 0 et 100 79
Vous avez gagné ! Le nombre cherché était bien  79 .
Vous avez trouvé en  7  essai(s).
Donner un nombre entier entre 0 et 100 50
 Plus petit !
Donner un nombre entier entre 0 et 100 25
 Plus grand !
Donner un nombre entier entre 0 et 100 30
 Plus grand !
Donner un nombre entier entre 0 et 100 35
 Plus grand !
Donner un nombre entier entre 0 et 100 40
 Plus grand !
Donner un nombre entier entre 0 et 100 45
 Plus petit !
Donner un nombre entier entre 0 et 100 44
Vous avez gagné ! Le nombre cherché était bien  44 .
Vous avez trouvé en  7  essai(s).
Donner un nombre entier entre 0 et 100 50
 Plus grand !
Donner un nombre entier entre 0 et 100 75
 Plus petit !
Donner un nombre entier entre 0 et 100 60
 Plus petit !
Donner un nombre entier entre 0 et 100 55
Vous avez gagné ! Le nombre cherché était bien  55 .
Vous avez trouvé en  4  essai(s).
La moyenne des essais est de  6.444444444444445
"""



# from random import *
# from time import time
# 13 / 32
# Alea = randint(0,100)
# Compteur = 0
# NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
# DebutJeu = time()
# while NombreDonne != Alea : # != signifie différent de
#    if NombreDonne > Alea :
#       print(" Plus petit !")
#       Compteur = Compteur + 1
#       NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
#    else :
#       print(" Plus grand !")
#       Compteur = Compteur + 1
#       NombreDonne = int(input("Donner un nombre entier entre 0 et 100 "))
# FinJeu = time()
# TempsJeu = round(FinJeu - DebutJeu,3)
# print("Vous avez gagné ! Le nombre cherché était bien ",Alea,".")
# print("Vous avez trouvé en ", Compteur," essai(s) et en ",TempsJeu," secondes.")


# 9) Graphiques avec la librairie matplotlib.pyplot
   # 9-1) Placer des points de couleur différente
# Programme 1 : Placer un point de couleur bleue
from matplotlib.pyplot import *

# Place un point de couleur bleue aux coordonnées (5,10)
# plot(5, 10, '.', color='#0000FF')
# show()

# for x in range(0,100):
#    plot(x,10,'.',color='#0000FF')   
# show()

# Ce programme trace une ligne horizontale de points bleus à la hauteur y = 10.

# for x in range(0,100):
#    plot(x,10,'.',color='#0000FF')   
#    plot(range(0, 100), [5]*100, '-', color='#FF0000')
#    plot(range(0, 100), [5]*100, '-', color='#FFFF00')   # jaune
#    plot(range(0, 100), [10]*100, '-', color='#FF00FF')   # magenta
#    plot(range(0, 100), [15]*100, '-', color='#00FFFF')   # cyan
# show()

# 9-2) Représentation graphique de fonctions mathématiques
# from matplotlib.pyplot import *
# for x in range(-100,100) :
#    plot(x,x*x,'.',color='#0000FF')
# show()

# Programme 2 : Représentation des fonctions sinus et cosinus
from math import *

# Fonction cosinus en rouge
for x in range(-100, 100):
   plot(x / 10, cos(x / 10), ".", color='#FF0000')

# Fonction sinus en bleu
for x in range(-100, 100):
   plot(x / 10, sin(x / 10), ".", color='#0000FF')

show()
