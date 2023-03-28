import os.path
import datetime
import xml.etree.ElementTree as ET
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from vues.interface import Ui_MainWindow
from Classe.personne import Personne
from Classe.client import Client


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
        
        if os.path.isfile("clients.xml") and os.path.getsize("clients.xml") > 0:
            tree = ET.parse("clients.xml")
            root = tree.getroot()
        else:
            root = ET.Element("clients")
            tree = ET.ElementTree(root)
            tree.write("clients.xml", encoding="utf-8", xml_declaration=True)

        self.chargerClient()

    def ajouterClient(self):
        nom = self.ui.nomClient.text()
        adresse = self.ui.adresseClient.text()
        ville = self.ui.villeClient.text()
        province = self.ui.provienceClient.text()
        codePostal = self.ui.codePostalClient.text()
        telephone = self.ui.telephoneClient.text()
        courriel = self.ui.courrielClient.text()
        numeroIdentification = self.ui.numClient.text()
        sexe = self.ui.sexeClient.text()


        unePersonne = Personne(nom, adresse, ville, province, codePostal, telephone, courriel)
        unClient = Client(numeroIdentification,sexe)

        # Enregistrement du client dans un dossier xml
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
        sexeElement =  ET.SubElement(client,"sexe")
        sexeElement.text = sexe
        dateCreationElement = ET.SubElement(client, "dateCreation")
        dateCreationElement.text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if os.path.isfile("clients.xml") and os.path.getsize("clients.xml") > 0:
            tree = ET.parse("clients.xml")
            root = tree.getroot()
        else:
            root = ET.Element("clients")
            tree = ET.ElementTree(root)

        root.append(client)
        tree.write("clients.xml", encoding="utf-8", xml_declaration=True)

        self.listeClient.addItem(unePersonne.nom +"-"+ unClient.sexe)

        # Effacer les champs du formulaire
        self.ui.nomClient.setText('')
        self.ui.adresseClient.setText('')
        self.ui.villeClient.setText('')
        self.ui.provienceClient.setText('')
        self.ui.codePostalClient.setText('')
        self.ui.telephoneClient.setText('')
        self.ui.courrielClient.setText('')

    def chargerClient(self):

        # Effacer la liste actuelle
        self.listeClient.clear()
    
        # Charger les clients existants depuis le fichier XML
        tree = ET.parse("clients.xml")
        root = tree.getroot()  
        for client in root.findall('client'):
            nom = client.find('nom').text
            ville = client.find('ville').text
            sexe = client.find('sexe').text
            leClient = nom + " - " + ville + "-"+ sexe
            self.listeClient.addItem(leClient)
            
if __name__ == '__main__':
    app = QApplication([])
    window = Traversier()
    app.exec_()
