# Created by vadim at 1/26/19
Feature: Edit place name
  Assistant finds saved place and reassigns name

  Scenario: User asks to edit saved name and VA reassigns old name
    Given service is working
    When user says "Hello, Borya"
    Then VA says "Hello"
    When user says edit Библиотека
    Then VA repeats place name and address
    And VA asks "Confirm?"
#    When User says "Yes"
#    Then VA says "How to name place?"
#    When User says Свободный дом
#    Then VA says Свободный дом and says "Confirm?"
#    When User says "Yes"
#    Then VA says Парусная 17 says Свободный дом
#    And VA says "Done"

#   Scenario: User asks to edit saved name and VA can't determine new name
#    Given service is working
#    When user says "Hello, Borya"
#    Then VA says "Hello"
#    When user says "Edit Пашин дом"
#    Then VA says Парусная 17 and says "Confirm?"
#    When User says "Yes"
#    Then VA says "How to name place?"
#    When User says Абра Кадабра
#    Then VA says "Can't define name"
