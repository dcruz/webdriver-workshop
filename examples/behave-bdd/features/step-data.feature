Feature: Demo for several types of Step data

    Scenario: Search query is the same on result page
        Given I open SAPO homepage
        When I load text into search box
        """
        Some random text
        """
        Then search box is the same
