# Created by vadim at 1/26/19
Feature: Edit place location
  Assistant finds saved place and reassigns location point

  Scenario: User asks to edit saved location and VA reassigns old location
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Измени Парусная 17"
    And VA says Парусная 17 and Пашин дом and "Confirm?"
    Then User says "Yes"
    And VA says "Say new location"
    Then User says Парусная 2
    And VA says Парусная 2 and says "Confirm?"
    Then User says "Yes"
    And VA says Парусная 2 and says Пашин дом
    And VA says "Done"

   Scenario: User asks to edit saved location and VA can't determine new location
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Edit Парусная 17"
    And VA says Парусная 17 Пашин дом and "Confirm?"
    Then User says "Yes"
    And VA says "Say new location"
    Then User says Абра Кадабра
    And VA says "Can't define location"