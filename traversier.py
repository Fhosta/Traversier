import datetime
import xml.etree.ElementTree as ET
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from vues.interface import Ui_MainWindow
from Classe.personne import *


class Traversier(QMainWindow):
    def __init__(self):
        super().__init__()

        # Création de l'interface utilisateur à partir du fichier .ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Autres initialisations de l'application
        self.setWindowTitle("Traversier")
        self.show()
        self.listeClient = self.ui.listeClient
        self.ui.btnClient.clicked.connect(self.ajouterClient)



    def ajouterClient(self):
        nom = self.ui.nomClient.text()
        adresse = self.ui.adresseClient.text()
        ville = self.ui.villeClient.text()
        province = self.ui.provienceClient.text()
        codePostal = self.ui.codePostalClient.text()
        telephone = self.ui.telephoneClient.text()
        courriel = self.ui.courrielClient.text()

        unePersonne = Personne(nom, adresse, ville, province, codePostal, telephone, courriel)

        
        # Enregistrement du client dans le un dossier xml 
        client = ET.Element("client")
        nomElement = ET.SubElement(client, "nom")
        nomElement.text = nom
        adresseElement = ET.SubElement(client, "adresse")
        adresseElement.text = adresse
        villeElement = ET.SubElement(client, "ville")
        villeElement.text = ville
        provinceElement = ET.SubElement(client, "province")
        provinceElement.text = province
        codePostalElement = ET.SubElement(client, "codePostal")
        codePostalElement.text = codePostal
        telephoneElement = ET.SubElement(client, "telephone")
        telephoneElement.text = telephone
        courrielElement = ET.SubElement(client, "courriel")
        courrielElement.text = courriel
        dateCreationElement = ET.SubElement(client, "dateCreation")
        dateCreationElement.text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        tree = ET.ElementTree(client)
        tree.write("clients.xml", encoding="utf-8", xml_declaration=True)

        self.listeClient.addItem(unePersonne.nom)

    def chargerClient(self):
        root = ET.tree.getroot()
        clients = root.findall('./client')
        for client in clients:
            self.model.ajouter(
                client(client.find('nom').text, client.find('adresse').text, client.find('ville').text,
                        client.find('province').text, client.find('codePostal').text, client.find('telephone').text,
                        client.find('courriel').text))
        self.model.layoutChanged.emit()
        
if __name__ == '__main__':
    app = QApplication([])
    window = Traversier()
    app.exec_()
