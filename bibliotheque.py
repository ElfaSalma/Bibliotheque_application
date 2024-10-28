#création du classe livre:
class Livre:
    def __init__(self, titre, auteur, isbn, nb_exemplaires):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.nb_exemplaires = nb_exemplaires
        self.nb_exemplaires_disponibles = nb_exemplaires

    def ajouter_exemplaire(self, nombre=1):
        self.nb_exemplaires += nombre
        self.nb_exemplaires_disponibles += nombre

    def retirer_exemplaire(self, nombre=1):
        if nombre <= self.nb_exemplaires_disponibles:
            self.nb_exemplaires -= nombre
            self.nb_exemplaires_disponibles -= nombre

    def emprunter_exemplaire(self):
        if self.nb_exemplaires_disponibles > 0:
            self.nb_exemplaires_disponibles -= 1
            return True
        return False

    def rendre_exemplaire(self):
        if self.nb_exemplaires_disponibles < self.nb_exemplaires:
            self.nb_exemplaires_disponibles += 1

    def afficher_infos(self):
        print(f"Titre: {self.titre}, Auteur: {self.auteur}, ISBN: {self.isbn}")
        print(f"Exemplaires: {self.nb_exemplaires}, Disponibles: {self.nb_exemplaires_disponibles}")

livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "123456789", 3)
livre2 = Livre("1984", "George Orwell", "987654321", 2)

livre.afficher_infos()

livre.ajouter_exemplaire(3)
livre.afficher_infos()

livre.retirer_exemplaire(1)
livre.afficher_infos()

livre2.emprunter_exemplaire()
livre.afficher_infos()

livre2.rendre_exemplaire()
livre.afficher_infos()


#création du class membre:
class Membre:
    def __init__(self, nom, adresse, numero_membre):
        self.nom = nom
        self.adresse = adresse
        self.numero_membre = numero_membre
        self.livres_empruntes = []  # Liste pour stocker les livres empruntés

    def emprunter_livre(self, livre):
        # 1. Vérifier s'il y a des exemplaires disponibles
        if livre.emprunter_exemplaire():
            # 2. Ajouter le livre à la liste des livres empruntés
            self.livres_empruntes.append(livre)
            print(f"{self.nom} {self.adresse} {self.numero_membre} a emprunté '{livre.titre}'.")
        else:
            print(f"Pas d'exemplaire disponible pour le livre '{livre.titre}'.")

    def rendre_livre(self, indice_livre_emprunte):
        # Vérifier que l'indice est valide
        if 0 <= indice_livre_emprunte < len(self.livres_empruntes):
            print("les livres rendus :")
            livre = self.livres_empruntes.pop(indice_livre_emprunte)
            livre.rendre_exemplaire()  # Incrémenter le compteur pour le livre
            print(f"{self.nom} {self.adresse} {self.numero_membre} a rendu '{livre.titre}'.")
        else:
            print("Indice invalide pour le livre emprunté.")

    def afficher_infos(self):
        # Afficher les informations du membre et ses livres empruntés
        print(f"Membre: {self.nom} {self.adresse} {self.numero_membre}")
        print("Livres empruntés:")
        if self.livres_empruntes:
            for i, livre in enumerate(self.livres_empruntes, start=1):
                print(f" {i}. {livre.titre} par {livre.auteur}")
        else:
            print(" Aucun livre emprunté.")


membre1 = Membre("Alma", "4 Rue de Vanve", "125")
membre2 = Membre("Bob", "6 Rue de CDG", "342")

livre = Livre("Le Petit Pays", "Antoine de Saint-Exupéry", "123456789", 3)
livre2 = Livre("la tresse", "George Orwell", "987654321", 2)
membre1.afficher_infos()

membre1.emprunter_livre(livre)
membre1.afficher_infos()

membre1.rendre_livre(0)
membre1.afficher_infos()


#création du class Emprunt:
#importation de bibliothéque:
from datetime import datetime, timedelta
#class Emprunt:

class Emprunt:
    def __init__(self, membre, livre):
        self.membre = membre
        self.livre = livre
        self.date_emprunt = datetime.now()
        self.date_retour_prevue = self.date_emprunt + timedelta(days=14)

    def calculer_retard(self):
        date_aujourdhui = datetime.now()
        if date_aujourdhui > self.date_retour_prevue:
            return (date_aujourdhui - self.date_retour_prevue).days
        return 0

    def afficher_infos_emprunt(self):
        print(f"Membre: {self.membre.nom}, Livre: {self.livre.titre}")
        print(f"Date d'emprunt: {self.date_emprunt.strftime('%Y-%m-%d')}")
        print(f"Date de retour prévue: {self.date_retour_prevue.strftime('%Y-%m-%d')}")

        retard = self.calculer_retard()
        if retard > 0:
            print(f" Retard de {retard} jours")
        else:
            print(" Pas de retard")

emprunt = Emprunt(membre1, livre)

    
emprunt.calculer_retard()

emprunt.afficher_infos_emprunt()


#création de class Bibliothque:
class Bibliotheque:
    def __init__(self):
        # Initialise des listes vides pour stocker les livres, les membres, et les emprunts
        self.livres = []
        self.membres = []
        self.emprunts = []

    def ajouter_livre(self, livre):
        # Ajouter un livre à la liste des livres
        self.livres.append(livre)
        print(f"Le livre '{livre.titre}' a été ajouté à la bibliothèque.")

    def supprimer_livre(self, livre):
        # Enlever un livre de la liste des livres
        if livre in self.livres:
            self.livres.remove(livre)
            print(f"Le livre '{livre.titre}' a été retiré de la bibliothèque.")
        else:
            print("Erreur : Le livre n'est pas dans la bibliothèque.")

    def ajouter_membre(self, membre):
        # Ajouter un membre à la liste des membres
        self.membres.append(membre)
        print(f"Le membre {membre.nom} {membre.adresse} a été ajouté à la bibliothèque.")

    def supprimer_membre(self, membre):
        # Supprimer un membre de la liste des membres
        if membre in self.membres:
            self.membres.remove(membre)
            print(f"Le membre {membre.prenom} {membre.nom} a été retiré de la bibliothèque.")
        else:
            print("Erreur : Le membre n'est pas dans la bibliothèque.")
    def gerer_emprunt(self, membre, livre):
        # Gérer un emprunt d'un livre
        if livre in self.livres and livre.emprunter_exemplaire():
            emprunt = Emprunt(membre, livre)
            self.emprunts.append(emprunt)
            membre.emprunter_livre(livre)  # Mette à jour les emprunts du membre
            print(f"{membre.nom} {membre.adresse} a emprunté '{livre.titre}'.")
        else:
            print(f"Emprunt impossible : Aucun exemplaire de '{livre.titre}' disponible.")

    def gerer_retour(self, membre, livre):
        # Gérer un retour d'un livre
        emprunt_a_supprimer = None
        for emprunt in self.emprunts:
            if emprunt.membre == membre and emprunt.livre == livre:
                emprunt_a_supprimer = emprunt
                break

        if emprunt_a_supprimer:
            self.emprunts.remove(emprunt_a_supprimer)
            membre.rendre_livre(membre.livres_empruntes.index(livre))
            livre.rendre_exemplaire()
            print(f"{membre.prenom} {membre.nom} a rendu '{livre.titre}'.")
        else:
            print(f"Erreur : Aucun emprunt trouvé pour '{livre.titre}' par {membre.prenom} {membre.nom}.")

    def afficher_livres_disponibles(self):
        # Afficher les livres disponibles
        print("Livres disponibles dans la bibliothèque :")
        livres_dispo = [livre for livre in self.livres if livre.nb_exemplaires_disponibles > 0]
        if livres_dispo:
            for livre in livres_dispo:
                print(f" - {livre.titre} par {livre.auteur} (Disponibles : {livre.nb_exemplaires_disponibles})")
        else:
            print("Aucun livre disponible.")

    def afficher_emprunts(self):
        # Afficher les emprunts
        print("Liste des emprunts :")
        if self.emprunts:
            for emprunt in self.emprunts:
                print(f"{emprunt.membre.prenom} {emprunt.membre.nom} a emprunté '{emprunt.livre.titre}'")
        else:
            print("Aucun emprunt en cours.")

# Création de la bibliothèque
bibliotheque = Bibliotheque()

# Création de quelques livres
livre1 = Livre("Paris", "Antoine de Saint-Exupéry", "123456789", 3)
livre2 = Livre("1984", "George Orwell", "987654321", 2)
livre3 = Livre("Vous revoir", "Paulo Coelho", "456789123", 1)

# Ajout des livres à la bibliothèque
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

# Création de membres
membre1 = Membre("Alice", "Delet", "M001")
membre2 = Membre("Anais", "Elf", "M002")

# Ajout des membres à la bibliothèque
bibliotheque.ajouter_membre(membre1)
bibliotheque.ajouter_membre(membre2)

# Affichage des livres disponibles avant les emprunts
print("\n--- Livres disponibles avant emprunts ---")
bibliotheque.afficher_livres_disponibles()

# Gestion d'emprunts
print("\n--- Emprunts ---")
bibliotheque.gerer_emprunt(membre1, livre1)  # Alice emprunte "Le Petit Prince"
bibliotheque.gerer_emprunt(membre2, livre1)  # Bob emprunte aussi "Le Petit Prince"
bibliotheque.gerer_emprunt(membre1, livre2)  # Alice emprunte "1984"

# Affichage de la liste des emprunts
print("\n--- Liste des emprunts ---")
bibliotheque.afficher_emprunts

# Affichage des livres disponibles après les emprunts
print("\n--- Livres disponibles après emprunts ---")
bibliotheque.afficher_livres_disponibles()


# Affichage de la liste des emprunts après les retours
print("\n--- Liste des emprunts après retours ---")
bibliotheque.afficher_emprunts

# Affichage des livres disponibles après les retours
print("\n--- Livres disponibles après retours ---")
bibliotheque.afficher_livres_disponibles()



