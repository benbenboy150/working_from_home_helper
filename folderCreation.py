import os

def jaimeleschevres():
    path = os.getcwd()
    numerodedossier = 0
    strnumerodedossier = str(numerodedossier)
    print("le dossier courant est : ",path)
    pathtot = path + "/coursnumero" + strnumerodedossier + "/"

    # créer un moyen de créer un nouveau dossier à chaque fois

    while os.path.exists(pathtot):
        numerodedossier += 1
        strnumerodedossier = str(numerodedossier)
        pathtot = path + "/coursnumero" + strnumerodedossier + "/"
        if numerodedossier > 100 :
            print("problemedossier")
            break


    #___________________________________

    try :
        os.mkdir(pathtot)
    except OSError:
        print("création du répertoire %s failed" % path)
        print("bah ça marche pas sorry soit j'ai fais de la merde soit c'est toi hihi")
    else :
        print("répertoire %s créé avec succès ! tu peux aller prendre ton café avec la voisine le programme prend les notes à ta place ;)" % path)
    
    return(pathtot)