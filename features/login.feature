Feature: Fonctionnalité de connexion pour GP4YOU

  Scenario: L'employé se connecte au portail GP4YOU
    Given l'utilisateur est sur la page de connexion de GP4YOU
    When l'utilisateur saisit le nom d'utilisateur "SBCEE"
    And l'utilisateur saisit le mot de passe "HRHR"
    And l'utilisateur sélectionne la langue "French"
    And l'utilisateur clique sur le bouton "Connexion"
    Then l'utilisateur devrait être redirigé vers la page d'accueil de GP4YOU
    And l'URL devrait être "https://tnhldapp0144.interpresales.mysoprahronline.com/GP4You/"