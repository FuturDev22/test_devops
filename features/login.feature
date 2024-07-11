Feature: Facebook Login

  Scenario: Connexion échouée avec des informations d'identification invalides
    Given l'utilisateur est sur la page de connexion Facebook
    When l'utilisateur saisit des informations d'identification non valides
    And l'utilisateur clique sur le bouton de connexion
    Then l'utilisateur devrait voir un message d'erreur

