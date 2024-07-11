Feature: Fonctionnalités de collaborateur
  As a Collaborateur
  I want to perform various actions in the application
  So that I can manage my personal information and requests efficiently

  Background:
    Given le collaborateur est connecté

  Scenario: Modifier Etat Civil
    When le collaborateur navigue vers "Mes données individuelles"
    And le collaborateur clique sur "Mon état civil"
    And le collaborateur modifie la date d'effet de son état civil "Mariée" du "05/10/2014" à "06/10/2014"
    Then le collaborateur envoie la demande de modification d'état civil

  Scenario: Annuler Demande modification Etat civil
    When le collaborateur navigue vers "Mes demandes"
    And le collaborateur sélectionne la demande de modification à annuler
    Then le collaborateur clique sur "Annuler"

  Scenario: Ajouter demande d'ajout d'une nouvelle adresse de résidence et adresse email
    When le collaborateur navigue vers "Mon adresse et mon téléphone"
    Then le collaborateur ajoute une nouvelle adresse de résidence
    And le collaborateur ajoute une nouvelle adresse émail "adélaide.ouattara@soprahr.com"

  Scenario: Ajouter Personnes à Charge
    When le collaborateur navigue vers "Personnes à charge"
    Then le collaborateur ajoute une nouvelle personne à charge

  Scenario: Modifier Contacts d'Urgence
    When le collaborateur navigue vers "Personnes à contacter"
    Then le collaborateur modifie les informations du contact d'urgence

  Scenario: Modifier Coordonnées Bancaires
    When le collaborateur navigue vers "Mes coordonnées bancaires"
    Then le collaborateur modifie ses coordonnées bancaires

  Scenario: Absences Collaborateur
    When le collaborateur navigue vers "Mes absences"
    And  le collaborateur navigue vers "Demande d'absence"
    Then le collaborateur ajoute une demande une absence
    When le collaborateur navigue vers "mon planning des absences"
    Then  le collaborateur voit son planning des absences en vue annuelle
    When le collaborateur navigue vers "calendrier d'équipe"
    Then le collaborateur navigue vers "historique des absences"

    Scenario: Update Compétence
    When le collaborateur navigue vers "Mes compétences"
    And le collaborateur ajoute une nouvelle compétence "Adaptabilité"
    Then le collaborateur navigue vers "Graphe des compétences"

  Scenario: Voir Documents
    When le collaborateur navigue vers "Mes documents"
    And le collaborateur voit document "Bulletin de Paie"
    Then le collaborateur clique sur bouton "Télécharger"

  Scenario: Recherche Formation
    When le collaborateur navigue vers "Ma formation"
    And le collaborateur recherche une  formation avec le domaine "Langues étrangères", un nom de stage "Anglais débutants", et un id de stage "ATS001"
    Then le collaborateur voit les détails de la résultat
    And le collaborateur ferme modal résultat