import random
#liste de mot sélectionnées pour le pendu
Mots = ["Tets", "Test", "Empereur", "Canard", "Platane", "Blablacar"]

#afficher le mot en fonction des lettres devinées
def afficher_mot(mot,lettres_trouvees):
  print("Mot : ", end = '')
  for i in range(len(mot)):
    if mot[i] in lettres_trouvees:
      print(mot[i],end='')

    else:
      print("  _  ", end='')

  print()
  #print()

#Vérifier si le mot a été entièrement trouvé en comparant les lettres devinées avec le mot
def mot_trouve(mot, lettres_trouvees):
  for i in range(len(mot)):
    if mot[i] not in lettres_trouvees:
      return False
      
    return True

#La fonction principale du jeu pendu
def main(Mots):
  
  mot = random.choice(Mots) #liste des mots disponibles pour le jeu
  #print(mot)
  nombre_tentatives = 6

  #variable qui stocke les lettres trouvées par l'utilisateur
  lettres_trouvees = set()

  while nombre_tentatives > 0:
    afficher_mot(mot, lettres_trouvees)
    print("Nombre de tentatives restant :", nombre_tentatives)
    lettre = input("Entrer une lettre : ")
    if lettre not in mot:
      nombre_tentatives -= 1

    elif lettre in mot and lettre not in lettres_trouvees:
      lettres_trouvees.add(lettre)

    elif mot_trouve(mot, lettres_trouvees):
      print("Le mot a été trouvé !!")
      print(mot)
      break
    
    if nombre_tentatives == 0:
      print("Le mot n'a pas été trouvé")
      break
    print()

main(Mots)
