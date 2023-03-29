import os.path
import datetime
import xml.etree.ElementTree as ET
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from vues.interface import Ui_MainWindow
from Classe.personne import Personne
from Classe.vehicule import Vehicule


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
        self.listeEmploye = self.ui.listeEmploye
        self.listeVehicule = self.ui.listeVoiture
        self.ui.btnClient.clicked.connect(self.ajouterClient)
        self.ui.btnEmploye.clicked.connect(self.ajouterEmployer)
        self.ui.btnVoiture.clicked.connect(self.ajouterVoiture)


        
        if os.path.isfile("TransStLaurent.xml ") and os.path.getsize("TransStLaurent.xml ") > 0:
            tree = ET.parse("TransStLaurent.xml ")
            root = tree.getroot()
        else:
            root = ET.Element("clients")
            tree = ET.ElementTree(root)
            tree.write("TransStLaurent.xml ", encoding="utf-8", xml_declaration=True)

        self.chargerClient()
        self.chargerEmployer()
        self.chargerVoiture()


    def ajouterClient(self):
        nom = self.ui.nomClient.text()
        prenom = self.ui.prenomClient.text()
        adresse = self.ui.adresseClient.text()
        ville = self.ui.villeClient.text()
        province = self.ui.provienceClient.text()
        codePostal = self.ui.codePostalClient.text()
        telephone = self.ui.telephoneClient.text()
        courriel = self.ui.courrielClient.text()
        numeroIdentification = self.ui.numClient.text()
        sexe = self.ui.sexeClient.text()


        unePersonne = Personne(nom,prenom, adresse, ville, province, codePostal, telephone, courriel)
        

        # Enregistrement du client dans un dossier xml
        client = ET.Element("client")
        nomElement = ET.SubElement(client, "nom")
        nomElement.text = nom
        prenomElement = ET.SubElement(client, "prenom")
        prenomElement.text = prenom
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
        numClientElement =  ET.SubElement(client,"numClient")
        numClientElement.text = numeroIdentification
        dateCreationElement = ET.SubElement(client, "dateCreation")
        dateCreationElement.text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if os.path.isfile("TransStLaurent.xml ") and os.path.getsize("TransStLaurent.xml ") > 0:
            tree = ET.parse("TransStLaurent.xml ")
            root = tree.getroot()
        else:
            root = ET.Element("clients")
            tree = ET.ElementTree(root)

        root.append(client)
        tree.write("TransStLaurent.xml ", encoding="utf-8", xml_declaration=True)

        self.listeClient.addItem(unePersonne.nom +"-"+ unePersonne.prenom+"-"+unePersonne.adresse)

        # Effacer les champs du formulaire
        self.ui.nomClient.setText('')
        self.ui.prenomClient.setText('')
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
        tree = ET.parse("TransStLaurent.xml ")
        root = tree.getroot()  
        for client in root.findall('client'):
            nom = client.find('nom').text
            prenom = client.find('prenom').text
            adresse = client.find('adresse').text
            leClient = nom + " - " + prenom + "-"+ adresse
            self.listeClient.addItem(leClient)


###################################################################################################################################
                                                    #Employés
###################################################################################################################################

    def ajouterEmployer(self):
            nom = self.ui.nomEmploye.text()
            prenom = self.ui.prenomEmploye.text()
            adresse = self.ui.adresseEmploye.text()
            ville = self.ui.villeEmploye.text()
            province = self.ui.provinceEmploye.text()
            codePostal = self.ui.codePostalEmploye.text()
            telephone = self.ui.telephoneEmploye.text()
            courriel = self.ui.courrielEmploye.text()



            unePersonne = Personne(nom,prenom, adresse, ville, province, codePostal, telephone, courriel)
            

            # Enregistrement de l'employe dans un dossier xml
            employe = ET.Element("employe")
            nomElement = ET.SubElement(employe, "nom")
            nomElement.text = nom
            prenomElement = ET.SubElement(employe, "prenom")
            prenomElement.text = prenom
            adresseElement = ET.SubElement(employe, "adresse")
            adresseElement.text = adresse
            villeElement = ET.SubElement(employe, "ville")
            villeElement.text = ville
            provinceElement = ET.SubElement(employe, "province")
            provinceElement.text = province
            codePostalElement = ET.SubElement(employe, "codePostal")
            codePostalElement.text = codePostal
            telephoneElement = ET.SubElement(employe, "telephone")
            telephoneElement.text = telephone
            courrielElement = ET.SubElement(employe, "courriel")
            courrielElement.text = courriel
            dateCreationElement = ET.SubElement(employe, "dateCreation")
            dateCreationElement.text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if os.path.isfile("TransStLaurent.xml ") and os.path.getsize("TransStLaurent.xml ") > 0:
                tree = ET.parse("TransStLaurent.xml ")
                root = tree.getroot()
            else:
                root = ET.Element("employes")
                tree = ET.ElementTree(root)

            root.append(employe)
            tree.write("TransStLaurent.xml ", encoding="utf-8", xml_declaration=True)

            self.listeEmploye.addItem(unePersonne.nom +"-"+ unePersonne.prenom+"-"+unePersonne.adresse)

            # Effacer les champs du formulaire
            self.ui.nomClient.setText('')
            self.ui.prenomClient.setText('')
            self.ui.adresseClient.setText('')
            self.ui.villeClient.setText('')
            self.ui.provienceClient.setText('')
            self.ui.codePostalClient.setText('')
            self.ui.telephoneClient.setText('')
            self.ui.courrielClient.setText('')

    def chargerEmployer(self):

        # Effacer la liste actuelle
        self.listeEmploye.clear()
        
        # Charger les clients existants depuis le fichier XML
        tree = ET.parse("TransStLaurent.xml ")
        root = tree.getroot()  
        for employe in root.findall('employe'):
            nom = employe.find('nom').text
            prenom = employe.find('prenom').text
            adresse = employe.find('adresse').text
            lEmploye = nom + " - " + prenom + "-"+ adresse
            self.listeEmploye.addItem(lEmploye)


###################################################################################################################################
                                                    #Véhicule
###################################################################################################################################

    def ajouterVoiture(self):
            marque = self.ui.marqueVoiture.text()
            modele = self.ui.modeleVoiture.text()
            couleur = self.ui.couleurVoiture.text()
            annee = ''
            noIdentification = ''
            immatriculation = self.ui.immatriculationVoiture.text()
            typeVoiture = self.ui.typeVoiture.text()
            nombreRoue = self.ui.nbRoueVoiture.text()
            PrixTraverse = self.ui.prixTraverseVoiture.text()
            
            uneVoiture = Vehicule(noIdentification,marque,modele,couleur,annee,immatriculation)

            # Enregistrement de l'employe dans un dossier xml
            voiture = ET.Element("voiture")
            marqueElement = ET.SubElement(voiture, "marque")
            marqueElement.text = marque
            modeleElement = ET.SubElement(voiture, "modele")
            modeleElement.text = modele
            couleurElement = ET.SubElement(voiture, "couleur")
            couleurElement.text = couleur
            # anneeElement = ET.SubElement(voiture, "annee")
            # anneeElement.text = annee
            immatriculationElement = ET.SubElement(voiture, "immatriculation")
            immatriculationElement.text = immatriculation
            typeVoitureElement = ET.SubElement(voiture, "typeVoiture")
            typeVoitureElement.text = typeVoiture
            nombreRoueElement = ET.SubElement(voiture, "nombreRoue")
            nombreRoueElement.text = nombreRoue
            PrixElement = ET.SubElement(voiture, "prix")
            PrixElement.text = PrixTraverse
            dateCreationElement = ET.SubElement(voiture, "dateCreation")
            dateCreationElement.text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if os.path.isfile("TransStLaurent.xml ") and os.path.getsize("TransStLaurent.xml ") > 0:
                tree = ET.parse("TransStLaurent.xml ")
                root = tree.getroot()
            else:
                root = ET.Element("voitures")
                tree = ET.ElementTree(root)

            root.append(voiture)
            tree.write("TransStLaurent.xml ", encoding="utf-8", xml_declaration=True)

            self.listeEmploye.addItem(uneVoiture.marque+"-"+ uneVoiture.modèle+"-"+uneVoiture.immatriculation)

            # Effacer les champs du formulaire
            self.ui.marqueVoiture.setText('')
            self.ui.modeleVoiture.setText('')
            self.ui.couleurVoiture.setText('')
            self.ui.immatriculationVoiture.setText('')
            self.ui.nbRoueVoiture.setText('')
            self.ui.typeVoiture.setText('')
            self.ui.prixTraverseVoiture.setText('')

    def chargerVoiture(self):

        # Effacer la liste actuelle
        self.listeVehicule.clear()
        
        # Charger les clients existants depuis le fichier XML
        tree = ET.parse("TransStLaurent.xml ")
        root = tree.getroot()  
        for voiture in root.findall('voiture'):
            marque = voiture.find('marque').text
            modele = voiture.find('modele').text
            immatriculation = voiture.find('immatriculation').text
            uneVoiture = marque + " - " + modele + "-"+ immatriculation
            self.listeVehicule.addItem(uneVoiture)
            
if __name__ == '__main__':
    app = QApplication([])
    window = Traversier()
    app.exec_()
