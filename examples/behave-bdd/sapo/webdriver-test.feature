Feature: showing off behave

    Scenario: Open SAPO homepage
        Given I open SAPO homepage
        When I search for "minuscode"
        Then Title is SAPO
