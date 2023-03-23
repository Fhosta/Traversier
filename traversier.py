import datetime
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from vues.interface import Ui_MainWindow


class Traversier(QMainWindow):
    def __init__(self):
        super().__init__()

        # Création de l'interface utilisateur à partir du fichier .ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Autres initialisations de l'application
        self.setWindowTitle("Traversier")
        self.show()
        self.listClient = QStandardItemModel(self)
        self.ui.btnClient.clicked.connect(self.obtenirResultatClient)

    def obtenirResultatClient(self):
        nom = self.ui.nomClient.text()
        adresse = self.ui.adresseClient.text()
        ville = self.ui.villeClient.text()
        province = self.ui.provienceClient.text()
        codePostal = self.ui.codePostalClient.text()
        telephone = self.ui.telephoneClient.text()
        courriel = self.ui.courrielClient.text()
        resultat = f"Nom: {nom}, Adresse: {adresse}, Ville: {ville}, Province: {province}, Code postal: {codePostal}, Téléphone: {telephone}, Courriel: {courriel}"
        item = QStandardItem(resultat)
        print(resultat)
        self.listClient.appendRow(item)
        # print(nom)

if __name__ == '__main__':
    app = QApplication([])
    window = Traversier()
    app.exec_()
