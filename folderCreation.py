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
        print("Création du répertoire %s failed" % path)
        print("Un problème est survenu lors de la cration du répertoire.")
    else :
        print("Répertoire %s créé avec succès ! " % path)
    
    return(pathtot)
