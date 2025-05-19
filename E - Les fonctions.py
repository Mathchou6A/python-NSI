# E ) Les fonctions :
# E-1) Fonctions sans paramètres :

# 1) Afficher une ligne de caractère:

def AfficheCaractere() :
   for i in range(0,21) :
      print("#", end= " ")

# AfficheCaractere()

# 2) Une fonction simple qui appelle une autre fonction simple :
def AfficheCaractere() :
   for i in range(0,21) :
      print("#",end=" ")

def AfficheTripleCaractere() :
   AfficheCaractere()
   AfficheCaractere()
   AfficheCaractere()

# AfficheTripleCaractere()

# renvoie :
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""

# 3) Calculer le volume d'une sphère de rayon R :
from math import pi
def VolumeSphere():
   rayon=float(input("Donner un rayon en cm "))
   print("Le volume de cette sphère est de ",4*1/3*rayon*rayon*rayon*pi,"cm3.")
# VolumeSphere()
# renvoie :
"""
Donner un rayon en cm 3
Le volume de cette sphère est de  113.09733552923255 cm3.
"""


# E-2) Fonctions avec paramètres :

# 1) Calculer le volume d'une sphère de rayon R :
from math import pi
# rayon =float(input("Donner un rayon en cm"))
def VolumeSphere(rayon) :
   print("Le volume de cette shère est de ",4*1/3*rayon*rayon*rayon*pi,"cm3.")
# VolumeSphere(rayon)

# 2) Calculer le volume d'une sphère de rayon de 1,2,3,4 à 10 cm:
from math import pi
def VolumeSphere(rayon):
   print(round(4*1/3*rayon*rayon*rayon*pi,4),"cm^3")
# for i in range(1,11) :
#    print("Le volume de la sphère de rayon ",i,"cm est ")
   # VolumeSphere(i)

# renvoie :
"""
Le volume de la sphère de rayon  1 cm est 
4.1888 cm^3
Le volume de la sphère de rayon  2 cm est 
33.5103 cm^3
Le volume de la sphère de rayon  3 cm est 
113.0973 cm^3
Le volume de la sphère de rayon  4 cm est 
268.0826 cm^3
Le volume de la sphère de rayon  5 cm est
523.5988 cm^3
Le volume de la sphère de rayon  6 cm est
904.7787 cm^3
Le volume de la sphère de rayon  7 cm est
1436.755 cm^3
Le volume de la sphère de rayon  8 cm est
2144.6606 cm^3
Le volume de la sphère de rayon  9 cm est
3053.6281 cm^3
Le volume de la sphère de rayon  10 cm est
4188.7902 cm^3
"""

# 3) Calculer l'aire d'un triangle de hauteur h et de base b :
# a=float(input("Donner la base en cm"))
# b=float(input("Donner la hauteur en cm"))

# def AireTriangle(base,hauteur) :
#    print(round(base*hauteur/2,4),"cm².")
   
# print("L'aire d'un triangle de base",a,"cm et de hauteur",b,"cm est ")
# AireTriangle(a,b)

# renvoie :
"""
Donner la base en cm10
Donner la hauteur en cm5
L'aire d'un triangle de base 10.0 cm et de hauteur 5.0 cm est 
25.0 cm².
"""

# 4) Définir la fonction g(x) = 4x³ – 2x² +3 et calculer g(0), g(1),...,g(10) :
def g(x) :
   return 4*x**3 -2*x**2 + 3
for i in range (0,11) :
   print("g(",i,") = ",g(i),end="  ;  ")

# renvoie :
"""
g( 0 ) =  3  ;  g( 1 ) =  5  ;  g( 2 ) =  27  ;  g( 3 ) =  93  ;  g( 4 ) =  227  ;  g( 5 ) =  453  ;  g( 6 ) =  795  ;  g( 7 ) =  1277  ;  g( 8 ) =  1923  ;  g( 9 ) =  2757  ;  g( 10 ) =  3803  ;
"""

