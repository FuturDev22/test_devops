Feature: Login

  Scenario: connexion réussie
    Given L'utilisateur ouvre la page de connexion
    When L'utilisateur saisit le nom d'utilisateur et le mot de passe
    And L'utilisateur clique sur submit
    Then L'utilisateur doit voir URL https://practicetestautomation.com/logged-in-successfully/
    And  L'utilisateur doit voir le message Logged In Successfully
    And  L'utilisateur doit voir le bouton de déconnexion

