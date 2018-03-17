Feature: Dashboard

    Scenario Outline: Components
        Given I load the website
        When I go to "Dashboard" page
        Then I see this component "<rows>"
        Examples:
            | rows              |
            | Status            |
            | Detector Settings |
            | Battery           |
            | GPS               |

    Scenario Outline: Status
        Given I load the website
        When I go to "Dashboard" page
        Then Dashboard Status shows correct values for row "<rows>"
        Examples:
            | rows                    |
            | Status                  |
            | White Reference Count   |
            | Collect Reference Count |
            | Dark Reference Count    |
            | Last White Reference    |
            | Last Optimize           |
            | Last Dark Reference     |
            | Last Wavelength Check   |

    Scenario: Status Refresh
        Given I load the website
        When I go to "Dashboard" page
        Then Clicking on Status Refresh should refresh status component

    Scenario: Battery
        Given I load the website
        When I go to "Dashboard" page
        Then Dashboard Battery shows Battery or AC Power with correct icon.

    Scenario: Battery Refresh
        Given I load the website
        When I go to "Dashboard" page
        Then Clicking on Battery Refresh should refresh battery component

    Scenario Outline: Detector Settings
        Given I load the website
        When I go to "Dashboard" page
        Then Dashboard Detector Settings shows correct values for row "<rows>"
        Examples:
            | rows  |
            | VNIR  |
            | SWIR1 |
            | SWIR2 |

    Scenario Outline: GPS
        Given I load the website
        When I go to "Dashboard" page
        Then Dashboard GPS shows correct values for row "<rows>"
        Examples:
            | rows     |
            | Fix      |
            | Location |
            | Altitude |
            | Format   |

