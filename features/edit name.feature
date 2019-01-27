# Created by vadim at 1/26/19
Feature: Edit place name
  Assistant finds saved place and reassigns name

  Scenario: User asks to edit saved name and VA reassigns old name
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Edit Пашин дом"
    And VA says Парусная 17 and Пашин дом and says "Confirm?"
    Then User says "Yes"
    And VA says "How to name place?"
    Then User says Свободный дом
    And VA says Свободный дом and says "Confirm?"
    Then User says "Yes"
    And VA says Парусная 17 says Свободный дом
    And VA says "Done"

   Scenario: User asks to edit saved name and VA can't determine new name
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Edit Пашин дом"
    And VA says Парусная 17 and says "Confirm?"
    Then User says "Yes"
    And VA says "How to name place?"
    Then User says Абра Кадабра
    And VA says "Can't define name"