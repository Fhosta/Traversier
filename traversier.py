# Auteur : Florian Hostachy
# Date : 3/29/2023
# Fonction : Permet une gestion complète d'un traversier 


import os.path
import datetime
import xml.etree.ElementTree as ET
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from vues.interface import Ui_MainWindow
from Classe.personne import Personne
from Classe.vehicule import Vehicule
from Classe.traversier import TraversierC
from Classe.traverse import Traverse
import re

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
        self.listeEmployeTraversier = self.ui.listeEmployerTraversier
        self.listeTraversier = self.ui.listeTraversier
        self.cbClient = self.ui.cbClient
        self.cbEmployer = self.ui.cbEmploye
        self.cbVehicule = self.ui.cbVehicule
        self.listeTraverse = self.ui.listeTraverse



        self.ui.btnClient.clicked.connect(self.ajouterClient)
        self.ui.btnEmploye.clicked.connect(self.ajouterEmployer)
        self.ui.btnVoiture.clicked.connect(self.ajouterVoiture)
        self.ui.btnTraversier.clicked.connect(self.ajouterTraversier)
        self.ui.btnTraverse.clicked.connect(self.ajouterTraverse)



        if os.path.isfile("TransStLaurent.xml ") and os.path.getsize("TransStLaurent.xml ") > 0:
            tree = ET.parse("TransStLaurent.xml ")
            root = tree.getroot()
        else:
            root = ET.Element("clients")
            tree = ET.ElementTree(root)
            tree.write("TransStLaurent.xml ",
                       encoding="utf-8", xml_declaration=True)

        self.chargerClient()
        self.chargerEmployer()
        self.chargerVoiture()
        self.chargerEmployerTraversier()
        self.chargerTraversier()
        self.chargerEmployerTraverse()
        self.chargerClientTraverse()
        self.chargerVehiculeTraverse()
        self.chargerTraverse()


###################################################################################################################################
                                           # Clients
###################################################################################################################################

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

        unePersonne = Personne(nom, prenom, adresse, ville,
                               province, codePostal, telephone, courriel)

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
        sexeElement = ET.SubElement(client, "sexe")
        sexeElement.text = sexe
        numClientElement = ET.SubElement(client, "numClient")
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
        tree.write("TransStLaurent.xml ",
                   encoding="utf-8", xml_declaration=True)

        self.listeClient.addItem(
            unePersonne.nom + "-" + unePersonne.prenom+"-"+unePersonne.adresse)
        
        self.cbClient.addItem(
            unePersonne.nom + "-" + unePersonne.prenom+"-"+unePersonne.adresse)

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
            leClient = nom + " - " + prenom + "-" + adresse
            self.listeClient.addItem(leClient)


###################################################################################################################################
                                           # Employés
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

        unePersonne = Personne(nom, prenom, adresse, ville,
                               province, codePostal, telephone, courriel)

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
        tree.write("TransStLaurent.xml ",
                   encoding="utf-8", xml_declaration=True)

        self.listeEmploye.addItem(
            unePersonne.nom + "-" + unePersonne.prenom+"-"+unePersonne.adresse)
        
        self.listeEmployeTraversier.addItem(
            unePersonne.nom + "-" + unePersonne.prenom+"-"+unePersonne.adresse)
        
        self.cbEmployer.addItem(
            unePersonne.nom + "-" + unePersonne.prenom+"-"+unePersonne.adresse)

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
            lEmploye = nom + " - " + prenom + "-" + adresse
            self.listeEmploye.addItem(lEmploye)


###################################################################################################################################
                                           # Véhicule
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

        uneVoiture = Vehicule(noIdentification, marque,
                              modele, couleur, annee, immatriculation)

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
        tree.write("TransStLaurent.xml ",
                   encoding="utf-8", xml_declaration=True)

        self.listeVehicule.addItem(
            uneVoiture.marque+"-" + uneVoiture.modèle+"-"+uneVoiture.immatriculation)
        
        self.cbVehicule.addItem(
            uneVoiture.marque+"-" + uneVoiture.modèle+"-"+uneVoiture.immatriculation)

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
            uneVoiture = marque + " - " + modele + "-" + immatriculation
            self.listeVehicule.addItem(uneVoiture)

###################################################################################################################################
                                           # Traversier
###################################################################################################################################

    def ajouterTraversier(self):
        nom = self.ui.nomTraversier.text()
        capaciteVehicule = self.ui.capaVehiculeTraversier.text()
        capacitePersonne = self.ui.capaPersonneTraversier.text()
        dateFabri = ''
        dateService = ''

        unTraversier = TraversierC(nom, capaciteVehicule,
                              capacitePersonne, dateService,dateFabri)

        # Enregistrement du traversier dans un dossier xml
        traversier = ET.Element("traversier")
        nomElement = ET.SubElement(traversier, "nom")
        nomElement.text = nom
        capaVehiElement = ET.SubElement(traversier, "capaVehi")
        capaVehiElement.text = capaciteVehicule
        capacitePersonneElement = ET.SubElement(traversier, "capacitePersonne")
        capacitePersonneElement.text = capacitePersonne
        # anneeElement = ET.SubElement(voiture, "annee")
        # anneeElement.text = annee
        dateCreationElement = ET.SubElement(traversier, "dateCreation")
        dateCreationElement.text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if os.path.isfile("TransStLaurent.xml ") and os.path.getsize("TransStLaurent.xml ") > 0:
            tree = ET.parse("TransStLaurent.xml ")
            root = tree.getroot()
        else:
            root = ET.Element("traversiers")
            tree = ET.ElementTree(root)

            
        root.append(traversier)
        tree.write("TransStLaurent.xml ",
            encoding="utf-8", xml_declaration=True)

        self.listeTraversier.addItem(
            unTraversier.nom+"-" + unTraversier.capaciteVehicule+"-"+unTraversier.capacitePersonne)
        

            # Effacer les champs du formulaire
        self.ui.nomTraversier.setText('')
        self.ui.capaVehiculeTraversier.setText('')
        self.ui.capaPersonneTraversier.setText('')
        self.ui.immatriculationVoiture.setText('')

    def chargerTraversier(self):

        # Effacer la liste actuelle
        self.listeTraversier.clear()

        # Charger les traversier existants depuis le fichier XML
        tree = ET.parse("TransStLaurent.xml ")
        root = tree.getroot()
        for traversier in root.findall('traversier'):
            nom = traversier.find('nom').text
            capaVehi = traversier.find('capaVehi').text
            capacitePersonne = traversier.find('capacitePersonne').text
            unTraversier = nom + " - " + capaVehi + "-" + capacitePersonne
            self.listeTraversier.addItem(unTraversier)

    def chargerEmployerTraversier(self):

        # Effacer la liste actuelle
        self.listeEmployeTraversier.clear()

        # Charger les clients existants depuis le fichier XML
        tree = ET.parse("TransStLaurent.xml ")
        root = tree.getroot()
        for employe in root.findall('employe'):
            nom = employe.find('nom').text
            prenom = employe.find('prenom').text
            adresse = employe.find('adresse').text
            lEmploye = nom + " - " + prenom + "-" + adresse
            self.listeEmployeTraversier.addItem(lEmploye)

###################################################################################################################################
                                           # Traverse
###################################################################################################################################

    def ajouterTraverse(self):
        date = ''
        villeDepart = self.ui.villeTraverse.text()
        client = self.cbClient.currentText()
        employe = self.cbEmployer.currentText()
        voiture = self.cbVehicule.currentText()
        
        voiture_str = voiture

        prix_pattern = r"\d+"

        prix_match = re.search(prix_pattern, voiture_str)

        if prix_match:
            # Convertit le prix en un nombre entier
            prix = int(prix_match.group(0))
            
            # Calcul du prix total avec les taxes
            print(prix)
            prix_tps = prix * 0.05
            prix_tvq = prix * 0.0975
            prix_total = prix + prix_tps + prix_tvq

            print("Prix total avec taxes : ", prix_total)
        else:
            print("Impossible de trouver le prix dans la chaîne de caractères de la voiture.")

        uneTraverse = Traverse(date,villeDepart,employe,client,voiture)

        # Enregistrement de l'employe dans un dossier xml
        traverse = ET.Element("traverse")
        dateElement = ET.SubElement(traverse, "date")
        dateElement.text = date
        villeDepartElement = ET.SubElement(traverse, "villeDepart")
        villeDepartElement.text = villeDepart
        clientElement = ET.SubElement(traverse, "client")
        clientElement.text = client
        employeElement = ET.SubElement(traverse, "employe")
        employeElement.text = employe
        voitureElement = ET.SubElement(traverse, "typeVoiture")
        voitureElement.text = voiture
        prixElement = ET.SubElement(traverse, "prix")
        prixElement.text = prix
        dateCreationElement = ET.SubElement(traverse, "dateCreation")
        dateCreationElement.text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if os.path.isfile("TransStLaurent.xml ") and os.path.getsize("TransStLaurent.xml ") > 0:
            tree = ET.parse("TransStLaurent.xml ")
            root = tree.getroot()
        else:
            root = ET.Element("traverses")
            tree = ET.ElementTree(root)

        root.append(traverse)
        tree.write("TransStLaurent.xml ",
                   encoding="utf-8", xml_declaration=True)

        self.listeTraverse.addItem(
            uneTraverse.villeDepart+" - " + uneTraverse.client+" - "+uneTraverse.employe+" - "+uneTraverse.voiture +" - "+prix_total)

        # Effacer les champs du formulaire
  
        self.ui.villeTraverse.setText('')
    
    def chargerClientTraverse(self):

         # Effacer la liste actuelle
        self.cbClient.clear()

        # Charger les clients existants depuis le fichier XML
        tree = ET.parse("TransStLaurent.xml ")
        root = tree.getroot()
        for client in root.findall('client'):
            nom = client.find('nom').text
            prenom = client.find('prenom').text
            adresse = client.find('adresse').text
            leClient = nom + " - " + prenom + "-" + adresse
            self.cbClient.addItem(leClient)

        
    def chargerTraverse(self):

         # Effacer la liste actuelle
        self.listeTraverse.clear()

        # Charger les clients existants depuis le fichier XML
        tree = ET.parse("TransStLaurent.xml ")
        root = tree.getroot()
        for traverse in root.findall('traverse'):
            villeDepart = traverse.find('villeDepart').text
            client = traverse.find('client').text
            employe = traverse.find('employe').text
            voiture = traverse.find('typeVoiture').text
            prix= traverse.find('prix').text

            laTraverse = villeDepart + " - " + client + "-" + employe +" - "+voiture+" Prix total :" + prix
            self.listeTraverse.addItem(laTraverse)

    def chargerEmployerTraverse(self):

        # Effacer la liste actuelle
        self.cbEmployer.clear()

        # Charger les clients existants depuis le fichier XML
        tree = ET.parse("TransStLaurent.xml ")
        root = tree.getroot()
        for employe in root.findall('employe'):
            nom = employe.find('nom').text
            prenom = employe.find('prenom').text
            adresse = employe.find('adresse').text
            lEmploye = nom + " - " + prenom + "-" + adresse
            self.cbEmployer.addItem(lEmploye)
    
    def chargerVehiculeTraverse(self):

        # Effacer la liste actuelle
        self.cbVehicule.clear()

        # Charger les clients existants depuis le fichier XML
        tree = ET.parse("TransStLaurent.xml ")
        root = tree.getroot()
        for voiture in root.findall('voiture'):
            marque = voiture.find('marque').text
            modele = voiture.find('modele').text
            immatriculation = voiture.find('immatriculation').text
            prix = voiture.find('prix').text
            uneVoiture = marque + " - " + modele + " - " + immatriculation +" - "+prix
            self.cbVehicule.addItem(uneVoiture)
            self.cbVehicule.addItem(prix)


if __name__ == '__main__':
    app = QApplication([])
    window = Traversier()
    app.exec_()
