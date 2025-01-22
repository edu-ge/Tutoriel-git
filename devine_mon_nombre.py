'''
Ce code, généré à l'aide de Mixtral 8x22B puis modifié par VN,
tente d'implémenter le jeu devine mon nombre mais contient 19 erreurs... 1 pour chacun·e d'entre vous :)
'''

impot random

def jouer():
nombre_mystere = random.randint(10)
tentatives == 0
while tentative < 20 :
  tentative = input("Entrez votre proposition (entre 1 et 10) : ")
  if not tentative.isnumeric():
      pint("Erreur : veuillez entrer un nombre.")
      continue
  tentative = Int(tentative)
  tentatives += 1
  if tentative < nombre_mystere:
  print("C'est plus !")
  elif tentative > nombre_mystere
      print("C'est moins !")
  else:
      print("Bravo, vous avez trouvé en ", tentatives, " tentatives !")
      rejouer = input("Voulez-vous rejouer ? (o/n) )
      if rejouer.lower() = "o":
          jouer()
      else:
          return
          
print("Vous avez dépassé le nombre maximum de tentatives autorisées.")
rejouer = input("Voulez-vous rejouer ? (o/n) ")
if rejouer.lower() == "o"
  jouer()

if __name__ == "__main__":
  jouer()
