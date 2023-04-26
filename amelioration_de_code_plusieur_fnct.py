
#on va utiliser une fonction et on va l'appeler par la suite 
def afficher_information_personne(nom ,age):
    # afficher le resultat 
    print( "vous vous appelez "+nom +", vous avez " + str(age)+ " ans .")
    print("l'an prochain  vous aurez "+ str(age+1)+" ans")

def demander_age():
    age=0
    while age== 0 :
        age_str=input ("quel est votre age ?")
            # input retoune tjr une chaine de carctére
        try:
            age=int(age_str) 
            # on converti le resultat en entier avec int()
        except:
            # gestion d'une exception
            print("erreur !! vous devez rentrer un nombre pour l'age")
    return age

# demander le nom
def demander_nom():
    reponse_nom=""
    while reponse_nom== "":
        reponse_nom= input("quel est votre nom ?")
    return reponse_nom

# appel a la fonction demander l'age
nom1=demander_nom()
age1=demander_age()
afficher_information_personne(nom1,age1)
nom2=demander_nom()
age2=demander_age()
afficher_information_personne(nom2,age2)