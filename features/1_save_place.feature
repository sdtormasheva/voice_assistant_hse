Feature: Save particular place
  Assistant saves certain location point from user and assigns a name

  Scenario: User asks to save current point and VA saves it with name and location
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Save my location"
    And VA names location and asks "Confirm?"
    When User says "Yes"
    And VA asks "How to name?"
    Then User says Библиотека
    Then VA says "Location is saved"

  Scenario: User asks to save current point, but VA determines incorrect location
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Save my location"
    And VA names location and asks "Confirm?"
    Then User says "No"

  Scenario: User asks to save current point, but the point with this name already exists
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Save my location"
    And VA names location and asks "Confirm?"
    Then User says "Yes"
    And VA asks "How to name?"
    Then User says Библиотека
    Then VA says "Location already exists"

  Scenario: User asks to save current location and VA cannot determine location
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Save my location"
    And VA says 'Can't determine location'

  Scenario: User asks to save current location and VA cannot determine name
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Save my location"
    And VA names location and asks "Confirm?"
    Then User says "Yes"
    And VA asks "How to name?"
    Then User says nothing
    And VA says 'Can't recognize name'
