age = int(input("tu as quel age: "))

if age>18 and age<30:
    print("tu es jeune")
    probleme = input("tu fais quoi dans ta vie?")
    if probleme == ("je travaille"):
        reponse = input("tu fais quoi comme travail?")
        if reponse == ("je suis designer"):
            print("c’est bien continue ainsi")
        else:
            print("tu devrais te trouver un travail")
            probleme = int(input("Depuis combien de mois tu ne travailles plus (en mois) ? "))

            if 2 < probleme < 12:
                print("Je suis désolé d’apprendre cela.")
            elif probleme == 1:
                print("Ce n’est pas grave, tu en trouveras bientôt.")
            else:
                print("je ne vois pas quel mois")

    else:
        print("pareusseux")
        print("les pareusseux n’iront nul part")
        print("je te conseille de trouver quoi faire de ta vie")


if age>30:
    print("tu es adulte")
elif age<18 and age>=12:
    print("tu es adolescent")

if age<12:
    print("tu es bébé")
    probleme = input("Ou sont tes parents?")
    if probleme ==("je ne sais pas"):
        print("tu devrais savoir")
    elif probleme==("ils sont la"):
        print("vas les rechercher et depose le telephone")
