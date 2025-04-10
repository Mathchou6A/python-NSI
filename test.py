# a, b = 7.3, 12
# y = 3*a + b/5
# print(y)

# r , pi = 12, 3.14159
# s = pi * r**2 
# print(s)
# print(type(r), type(pi), type(s))

# a, b = 3, 7
# a = b
# b = a
# print(a, b)


# a = 0
# if a > 0:
#    print("a est positif")
# elif a < 0:
#    print("a est négatif")
# else:
#    print("a est nul")



# x, y = 1, 2
# if x == y:
#    print("x et y sont égaux")
# if x != y:
#    print("x et y sont différents")
# if x < y:
#    print("x est inférieur à y")
# if x > y:
#    print("x est supérieur à y")
# if x >= y:
#    print("x est supérieur ou égal à y")
# if x <= y:
#    print("x est inférieur ou égal à y")
# else:
#    print("x et y ne sont pas comparables")


# a = 7
# if (a % 2 == 0):
#    print("a est pair")
#    print("parce que le reste de sa division par 2 est nul")
# else:
#    print("a est impair")


# altitude = 320
# print(altitude)
# altitude = 375
# print(altitude)


# a = 0
# while (a < 12):
#    a = a + 1
#    print(a, a**2, a**3)


# a, b, c = 1, 1, 1
# while (c < 110):
#    print(b, end =" ")
#    a, b, c = b, a+b, c+1



# a, b, d = 1, 13, 1
# while (d <= 50):
#    c = a*b
#    if (c % 3 == 0):
#       print(c, end=" ")
#       d = d + 1
#    a = a+1





# 4.3
# euro, dollar = 1, 1.65
# while (euro < 1616384):
#    print(euro,"euro =",dollar,"dollar",)
#    euro = euro * 2
#    dollar = euro * 1.65 / 1

#4.4
# i = 1
# n = 1
# while n <= 12:
#    print(i, end=" / ")
#    i = i*3
#    n += 1

# 4.9
# programme qui affiche la suite de symboles
# i = 1
# var1 = "*"
# while (i <= 10):
#    print(var1*i,)
#    i = i + 1






# i, sept = 1, 7
# while (i <= 20):
#    print(i*sept, end=" ")
#    i = i + 1


# phrase1 = 'Petit poisson'
# phrase2 = 'deviendra grand'
# phrase3 = "j'aime bien"
# nombre_text = '6790'
# nombre_textavirgule = '3.50'
# print(phrase2, phrase3, phrase1) 
# print(phrase1[0], phrase2[0:5])
# print(phrase1 + phrase2 + phrase3[6] + phrase3[0] + phrase3[5])
# print(len(phrase3))
# nombre = int(nombre_text)
# print(nombre + 1)
# nombre = float(nombre_textavirgule)
# print(nombre)



# text = "savoir si il y a un e ou un E dans une chaîne de caractères"
# n_text = len(text)
# i = 1
# print("la longueur de la chaîne est", n_text)
# while (i < n_text):
#    if (text[i] == "e" or text[i] == "E"):
#       print("il y a un e")
#       break
#    i = i + 1
# else:
#    print("il n'y a pas de e")



# text = "savoir combien il y a de e ou de E dans une chaîne de caractères"
# i = 1
# nombre_de_e = 0
# print("la longueur de la chaîne est de", len(text), "caractères")
# while (i < len(text)):
#    if (text[i] == "e" or text[i] == "E"):
#       print("il y a un \"e\" a la lettre", i)
#       nombre_de_e = nombre_de_e + 1
#    i = i + 1
# if (nombre_de_e == 0):
#    print("il n'y a pas de e")
# else:
#    print("il y a", nombre_de_e, "\"e\" dans la chaîne")



# i = 0
# text = "écrire le texte à l'envers"
# text = text[::-1]
# while i < len(text):
#    print(text[i], end="")
#    i = i + 1


# i = 0
# n_palindrome = 0
# text_palindrome = "radare"
# text_palindrome_invers = text_palindrome[::-1]
# while i < len(text_palindrome):
#    print(text_palindrome_invers[i], end="")
#    if text_palindrome == text_palindrome_invers:
#       n_palindrome = n_palindrome + 1
#    else:
#       n_palindrome = 0
#    i = i + 1
# if n_palindrome == 0:
#    print("\nle text_palindromee n'est pas un palindrome")
# else:
#    print("\nle text_palindromee est un palindrome")




# Les listes (première approche)

# jour = ['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']
# print(jour)
# print(jour[0], jour[3])
# print(jour[0:3])
# jour[3] = jour[3] +47
# print(jour)
# print(len(jour))  
# del(jour[0])
# print(jour)
# print(len(jour))
# jour.append('samedi')
# print(jour)
# print(jour[len(jour) - 1])
# jour[3] = 87
# print(jour)
# jour.insert(3, "inserter")
# print(jour)
# jour[len(jour)-3 : len(jour)-1] = ["samdi", "dimanche"]
# print(jour)

# jour = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']
# a, b = 0, 0
# while (a < 25):
#    a = a + 1
#    b = a % 7
#    print(a, jour[b])


# ex 5.11
# t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
# i = 1
# t3 = [t2[0], t1[0]]
# while i < len(t1):
#    t3.append(t2[i])
#    t3.append(t1[i])
#    i = i + 1
# print(t3)


# ex 5.12
# t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
# i1 = 1
# t3 = [t2[0], t1[0]]
# while i1 < len(t1):
#    t3.append(t2[i1])
#    t3.append(t1[i1])
#    i1 = i1 + 1
# print(t3)

# i2 = 0
# while i2 < len(t2):
#    print(t2[i2], end=" ")
#    i2 = i2 + 1



# ex 5.13 recherche le plus grand élément présent dans une liste donnée
# l = [32, 5, 12, 8, 3, 75, 2, 15]
# i = 0
# max = 0
# while i < len(l):
#    if l[i] > max:
#       max = l[i]
#    i = i + 1
# print(" le plus grand élément de cette liste a la valeurt", max)



#  5.14 séparer les éléments d'une liste en deux listes, une liste de nombres pairs et une liste de nombres impairs
# l = [32, 5, 12, 8, 3, 75, 2, 15]
# l_pair = []
# l_impair = []
# i = 0
# while i < len(l):
#    if l[i] % 2 == 0:
#       l_pair.append(l[i])
#    else:
#       l_impair.append(l[i])
#    i = i + 1
# print("la liste des nombres pairs est", l_pair)
# print("la liste des nombres impairs est", l_impair)



# 5.15 
# l = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
# i = 0
# l1 = []
# l2 = []
# while i < len(l):
#    if len(l[i]) < 6:
#       l1.append(l[i])
#    else:
#       l2.append(l[i])
#    i = i + 1

# print(l1)
# print(l2)


# 6 Fonctions prédéfinies

# la fonction print()
# print("Bonjour", "à", "tous", sep ="*")
# print("Bonjour", "à", "tous", sep ="")
# print("Bonjour", "à", "tous", sep =" test")
# print("bonjour", "à", "tous")


#  Interaction avec l’utilisateur : la fonction input()
# prenom = input("Entrez votre prénom : ")
# print("bonjour,", prenom)

# print("Veuillez entrer un nombre positif quelconque : ", end=" ")
# ch = input()
# nn = float(ch)
# ou
# nn = int(ch)
# print("le carré de", nn, "vaut", nn**2)


from math import *
# nombre = 121
# angle = pi / 6

# print("racine carrée de", nombre, "=", sqrt(nombre))
# print("sinus de", angle, "radians", "=", sin(angle))




# 6.1
# miles_s = input("Veuillez entrer un nombre de miles : ")
# miles_n = int(miles_s)
# print(miles_n, "miles est égale a : ", miles_n*1609/1, "mètres/h et :", (miles_n*1609/1)*3.5, "km/h")
# c'est faux pas envie de faire les bon calcul

# 6.4


# Un peu de détente avec le module turtle 
# from turtle import * 
# reset()
# a = 0
# while a <12:
#    a = a +1
#    forward(150)
#    left(150)


# Véracité/fausseté d’une expression
# print("Ce script recherche le plus grand de trois nombres")
# print("Veuillez entrer trois nombres séparés par des virgules : ")
# ch =input()
# nn = list(eval(ch))
# print(nn)
# max, index = nn[0], 'premier'
# if nn[1] > max: 
#    max = nn[1]
#    index = 'second'
# if nn[2] > max:
#    max = nn[2]
#    index = 'troisième'
# print("le plus grand de ces nombres est", max)
# print("ce nombre est le", index, "de votre liste")



# Instructions composées <while> - <if> - <elif> - <else>

# print('Choisissez un nombre de 1 à 3 (ou 0 pour terminer) ', end=' ')
# a = float(input())         # conversion de la chaîne entrée en entier
# while a:                # équivalent à : < while a != 0: >
#    if a == 1:
#       print("Vous avez choisi un :")
#       print("le premier, l'unique, l'unité ...")
#    elif a == 2:
#       print("Vous préférez le deux :")
#       print("la paire, le couple, le duo ...")
#    elif a == 3:
#       print("Vous optez pour le plus grand des trois :")
#       print("le trio, la trinité, le triplet ...")
#    else :
#       print("Un nombre entre UN et TROIS, s.v.p.")
#    print('Choisissez un nombre de 1 à 3 (ou 0 pour terminer) ', end =' ')
#    a = float(input())
# print("Vous avez entré zéro :")
# print("L’exercice est donc terminé.")



# a = 0 
# while a < 16:
#    a = a + 1
#    if a !=2:
#       print('perdu', a)
#    elif a == 3:
#       print('un instant, s.v.p.', a)
#    else :
#       print('gagné', a)


# a = 5
# b = 2
# if (a==5) & (b<=2):
#    print('"&" signifie "et"; on peut aussi utiliser le mot "and"')


# a, b = 2, 4
# if (a==4) or (b!=4):
#    print('gagné')
# elif (a==4) or (b==4):
#    print('presque gagné')


# a = 1
# if not a:
#    print('gagné')
# elif a:
#    print('perdu')

# 6.10
# nom = input("quelle est votre nom : " )
# sexe = input("quelle est votre sexe : ")
# if sexe == "M":
#    print("Cher Monsieur", nom)
# else:
#    print("Chère Mademoiselle", nom)


# 6.11 
# from math import *
# a = float(input("longuers a : "))
# b = float(input("longuers b : "))
# c = float(input("longuers c : "))
# if a + b > c and a + c > b and b + c > a:
#    if a == b == c:
#       print("C'est un triangle équilatéral.")
#    elif (a**2 == b**2 + c**2 or b**2 == c**2 + a**2 or c**2 == a**2 + b**2):
#       print("ce triangle est rectangle.")
#    elif(a == b or a == c or b == c):
#       print("ce triangle est isocèle.")
#    else:
#       print("ce triangle est quelconque.")
# else: 
#    print("ce n'est pas un triangle")




# Fonctions originales
# def table7():
#    n = 1
#    while n < 20 :
#       print(n * 7, end =' ')
#       n = n + 1

# table7()

# table7()

# def table7triple():
#    print('La table par 7 en triple exemplaire :')
#    table7()
#    table7()
#    table7()


# table7triple()


# def table(base):
#    n = 0
#    while n <= 10 :
#       n = n +1
#       print(n * base, end =' ')

# table(10)
# print()
# table(4)

# def table(base):
#    resultat = []             # resultat est d’abord une liste vide
#    n = 1
#    while n < 11:
#       b = n * base
#       resultat.append(b)     # ajout d’un terme à la liste
#       n = n +1               # (voir explications ci-dessous)
#    return resultat

# ta9 = table(9)
# print(ta9)


# def oiseau(voltage=100, etat='allumé', action='danser la java'):
#    print('Ce perroquet ne pourra pas', action)
#    print('si vous le branchez sur', voltage, 'volts !')
#    print("L'auteur de ceci est complètement", etat)

# oiseau(etat='givré', voltage=250, action='vous approuver')
# print()
# oiseau()


# Utilisation de fenêtres et de graphismes p99
# from tkinter import *

# fen1 = Tk()
# tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
# tex1.pack()
# bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
# bou1.pack()
# fen1.mainloop()

# def valeur_max(valeur1, valeur2):
#    if valeur1 > valeur2:
#       print(valeur1, "est le plus grand")
#    else:
#       print(valeur2, "est le plus grand")


# valeur_max(int(input("entrer la valeur 1 : ")), int(input("entrer la valeur 2 : ")))

# def achat_place_de_cinema():
#    age = int(input("quel est votre age ? : "))
#    if age < 0:
#       age = int(input("votre vrai age ? : "))
#    pop_corn = input("souhaitez-vous du pop corn ? : ")
#    if age < 18: 
#       prix = 7
#    else:
#       prix = 12
#    if pop_corn == "oui":
#       prix += 5
#    print("le prix est de", prix, "€")


# achat_place_de_cinema()


# D1
# a1 = 3
# print(type(a1))

# a2 = 3,1415
# print(type(a2))


#D2
# n = "a" 
# print(type(n))

# lettre='b' 
# print(type(lettre))

# n1 = "Bonjour"
# n2 = " à tous !"
# print(n1 + n2)

# mot = "Informatique"
# print(mot[0])
# print(mot[1])
# print(mot[2])
# print(mot[11])

# print(len(mot))

# print(len(n1 + n2)) #les espace sont aussi compté


# l = [[12, 14, 120, "text", "text2"], [13, 15, 121, "textliste2"], ["liste", 13, 45, 134554]]
# print(len(l[0]))

# 4.5
# calcule le volume d’un parallélépipède rectangle dont sont fournis au départ la largeur, la hauteur et la profondeur.
# def volume():
#    largeur = float(input("largeur : "))
#    hauteur = float(input("hauteur : "))
#    profondeur = float(input("profondeur : "))
#    print(largeur * hauteur * profondeur)

# volume()


# 4.6
# convertit un nombre entier de secondes fourni au départ en un nombre d’années, de mois, de jours, de minutes et de secondes (utilisez l’opérateur modulo : %)

# def convertisseur_secondes():
#    secondes = int(input("entrer le nombre de secondes : "))
#    annee = secondes // 31536000
#    mois = (secondes % 31536000) // 2592000
#    jours = (secondes % 2592000) // 86400
#    heures = (secondes % 86400) // 3600
#    minutes = (secondes % 3600) // 60
#    secondes = secondes % 60
#    print(annee, "années", mois, "mois", jours, "jours", heures, "heures", minutes, "minutes", secondes, "secondes")

# convertisseur_secondes()


# 4.7
# affiche les 20 premiers termes de la table de multiplication par 7, en signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de 3
# def table_de_7_avec_3():
#    i = 0
#    while i <= 20:
#       i = i + 1
#       if i % 3 == 0:
#          print(i * 7, "*", end=" ")
#       else:
#          print(i * 7, end=" ")

# table_de_7_avec_3()


# 4.8
# programme qui calcule les 50 premiers termes de la table de multiplication par 13, mais n’affiche que ceux qui sont des multiples de 7
# def table_de_13_avec_7():
#    i = 0
#    while i <= 50:
#       i = i + 1
#       if i % 7 == 0:
#          print(i * 13, end=" ")

# table_de_13_avec_7()































































