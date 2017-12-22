#!/usr/bin/env python
#-*- coding: utf-8 -*-
#importer les bibliothèques de PyQt4 pour la fenetre
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#importer les fonctionnalités du système
import os, sys

#importer la fonction de crawler contenu dans tpe.py
from tpe import *

#Création de classe Fenetre pour representer la fenetre
class Fenetre(QWidget):
    #définition du constructeur
    def __init__(self):
        QWidget.__init__(self)
        #fixation des dimensions de la fenetre
        self.resize(500, 500)
        #création d'un bouton servant à lancer le crawl
        self.bouton = QPushButton("lancement",self)
        #liaison du bouton à la fonction lancer
        self.bouton.clicked.connect(self.lancer)
        #Création d'un layout pour l'emplacement des objets
        self.l = QHBoxLayout(self)
        #ajout du bouton au layout
        self.l.addWidget(self.bouton)
        #configuration du layout 
        self.setLayout(self.l)
    #fonction pour lancer le crawl
    def lancer(self):
        #rendre le bouton non visible
        self.bouton.setVisible(False)
        #appelation de la fonction de crawl contenu dan tpe.py
        self.liste = recupere()
        #création d'une variable pour contenir les données obtenues après crawl sous forme de texte
        string = ''
        #transformation des données en texte
        for i in self.liste:
            (x, y, z) = i
            string += x + y + str(z)+"\n\n" 
        #création d'une zone de texte pour afficher les données
        self.t = QTextEdit(self)
        self.t.setText(string)
        self.l.addWidget(self.t)
#fonction principale
if __name__ == '__main__':
    #création d'une instance de la classe QApplication
    a = QApplication(sys.argv)
    #création d'une instance de notre classe Fenetre
    m = Fenetre()
    #rendre la fenetre visible
    m.show()
    #execution de notre application
    a.exec_()