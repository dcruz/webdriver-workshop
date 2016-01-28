Feature: Testing SAPO search consistency

    Scenario Outline: Search query is the same on result page
        Given I open SAPO homepage
        When I search for "<query>"
        Then SERP query is the same

    Examples:
        | query         |
        | Portugal      |
        | Aveiro        |
        | Presidente    |
