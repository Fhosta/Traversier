from Classe.personne import *
import xml.etree.ElementTree as ET
import datetime
import os.path


class Client(Personne):
    def __init__(self, numeroIdentification: str, sexe: str):
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe

    
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

        unePersonne = Personne(nom, adresse, ville, province, codePostal, telephone, courriel)
        unClient = Client(numeroIdentification,sexe)

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