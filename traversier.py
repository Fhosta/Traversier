import os.path
import datetime
import xml.etree.ElementTree as ET
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from vues.interface import Ui_MainWindow
from Classe.personne import Personne
from Classe.client import *


class Traversier(QMainWindow):
    def __init__(self):
        super().__init__()

  

        # Création de l'interface utilisateur à partir du fichier .ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        numeroIdentification = self.ui.numClient.text()
        sexe = self.ui.sexeClient.text()

        # Autres initialisations de l'application
        self.setWindowTitle("Traversier")
        self.show()
        self.listeClient = self.ui.listeClient
        self.client = Client(numeroIdentification,sexe)
        self.ui.btnClient.clicked.connect(self.client.ajouterClient)
        
        if os.path.isfile("clients.xml") and os.path.getsize("clients.xml") > 0:
            tree = ET.parse("clients.xml")
            root = tree.getroot()
        else:
            root = ET.Element("clients")
            tree = ET.ElementTree(root)
            tree.write("clients.xml", encoding="utf-8", xml_declaration=True)

        Client.chargerClient(self)

        Client.ajouterClient(self)
    


if __name__ == '__main__':
    app = QApplication([])
    window = Traversier()
    app.exec_()
