from threading import Thread
from time import sleep
from tkinter import Button, Label, Tk
import numpy as np
import cv2
import pyautogui
import os
import folderCreation
 
 
class App(Tk):
 
    def __init__(self):
        Tk.__init__(self)
        self.label = Label(self, text="Programme en pause.")
        self.label.pack()
        self.play_button = Button(self, text="commencer les screenshots", command=self.play)
        self.play_button.pack(side="left", padx=2, pady=2)
        self.stop_button = Button(self, text="arrêter les screenshots", command=self.stop)
        self.stop_button.pack(side="left", padx=2, pady=2)
        self._thread, self._pause, self._stop = None, False, True
 
    def action(self):
        print("Lancement du programme !")
        compteurtemps = 0
        numeroimage = 0
        strnumeroimage = str(numeroimage)
        tempsattentescreenshot = 5

        screen1 = pyautogui.screenshot()
        screen1 = cv2.cvtColor(np.array(screen1),cv2.COLOR_RGB2BGR)

        pathtot = folderCreation.jaimeleschevres()
        print(pathtot)
        photodirection = pathtot + "image" + strnumeroimage + ".png"
        cv2.imwrite(photodirection,screen1)

        sleep(tempsattentescreenshot)

        #boucle infinie______________________________________________________________________________________________


        while True :
            print("t'es là ?")
            #__ je tente de comparer 2 images

            screen0 = screen1
            screen1 = pyautogui.screenshot()
            screen1 = cv2.cvtColor(np.array(screen1),cv2.COLOR_RGB2BGR)

            #screen0 = cv2.imread(photodirection)

            image1 = screen0.shape
            image2 = screen1.shape

            nbrdepixels1 = image1[0]*image1[1]
            nbrdepixels2 = image2[0]*image2[1]

            def testpixels():
                if nbrdepixels2 != nbrdepixels1 :
                    print("la comparaison ne peut pas fonctinner les image n'ont pas le même size")
                else :
                    print("ça rouuuuule !")

            testpixels()

            if screen0.shape == screen1.shape:
                print("les images font la même taille")
                difference = cv2.subtract(screen0,screen1)
                b, g, r = cv2.split(difference)
                nonZero = abs(cv2.countNonZero(b)) + abs(cv2.countNonZero(g)) + abs(cv2.countNonZero(r))
                nonZero = nonZero/3
                print(nonZero)


            pourcentage = (nbrdepixels1 - nonZero)/nbrdepixels1 * 100
            print(pourcentage," pourcent de similarité")

            #comparaison photo actuelle et dernière photo enregistrée__________________________

            derniereimage = cv2.imread(photodirection)

            difference = cv2.subtract(derniereimage,screen1)
            b, g, r = cv2.split(difference)
            nonZero = abs(cv2.countNonZero(b)) + abs(cv2.countNonZero(g)) + abs(cv2.countNonZero(r))
            nonZero = nonZero/3
            print(nonZero,"le deuxième nonZero")

            if nonZero == 0 :
                print("les images sont totalement les mêmes.")

            pourcentage1 = (nbrdepixels1 - nonZero)/nbrdepixels1 * 100
            print(pourcentage1," pourcent de similarité")
            #__________________________________________________________________________________
            
            compteurtemps += 1

            # définir le nom de l'image à enregistrer
            if pourcentage < 92 or pourcentage1 < 92: 
                compteurtemps = 0
                print("tes sensé la créer là")
                while os.path.exists(photodirection):
                    numeroimage += 1
                    strnumeroimage = str(numeroimage)
                    photodirection = pathtot + "image" + strnumeroimage + ".png"
                    if numeroimage > 100:
                        print("problème image")
                        break
                


                photodirection = pathtot + "image" + strnumeroimage + ".png"
                cv2.imwrite(photodirection,screen1)
            
            if compteurtemps >= 48 :
                numeroimage += 1
                strnumeroimage = str(numeroimage)
                photodirection = pathtot + "image" + strnumeroimage + ".png"
                cv2.imwrite(photodirection,screen1)


            sleep(tempsattentescreenshot)

            if self._stop:
                self.label["text"] = "arrêté"
                break
            while self._pause:
                sleep(0.1)
            self.label["text"] = "en cours d'acquisition"
            sleep(0.1)
            self.play_button["text"] = "screenshots en cours"

 
    def play(self):
        if self._thread is None:
            self._stop = False
            self._thread = Thread(target=self.action)
            self._thread.start()
        self._pause = False
        # self.play_button.configure(text="Pause", command=self.pause)
 
    def pause(self):
        self._pause = True
        self.play_button.configure(text="Play", command=self.play)
 
    def stop(self):
        if self._thread is not None:
            self._thread, self._pause, self._stop = None, False, True
        self.play_button.configure(text="commencer les screenshots", command=self.play)
 
 
App().mainloop()