Feature: Demo for several types of Step data

    Background: Go to homepage
        Given I open SAPO homepage

    Scenario: Search query is the same on result page
        When I search for "Portugal"

    Scenario: Title is "SAPO"
        Then Title is SAPO
