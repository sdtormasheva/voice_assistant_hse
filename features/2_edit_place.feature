# Created by vadim at 1/26/19
Feature: Edit place name
  Assistant finds saved place and reassigns name

  Scenario: User asks to edit saved name and VA reassigns old name
    Given service is working
    When user says "Hello, Borya"
    Then VA says "Hello"
    When user says edit Библиотека
    Then VA asks "What would you like to change, name or address?"
    When user says "Change name"
    Then VA asks "What is the new name?"
    When User says new name is Унылое место
    Then VA names updated location and asks "Confirm?"
    When User says "Yes"
    Then VA updates location and says "Location is updated"

  Scenario: User asks to edit saved name and VA reassigns address
    Given service is working
    When user says "Hello, Borya"
    Then VA says "Hello"
    When user says edit Унылое место
    Then VA asks "What would you like to change, name or address?"
    When user says "Change address"
    Then VA asks "What is the new address?"
    When User says new address is улица Седова
    Then VA names updated location and asks "Confirm?"
    When User says "Yes"
    Then VA updates location and says "Location is updated"

  Scenario: User asks to edit saved name, but it does not exist
    Given service is working
    When user says "Hello, Borya"
    Then VA says "Hello"
    When user says edit Работа
    Then VA says "The place is not found"

  Scenario: User asks to edit saved name, but VA can't recognize new name
    Given service is working
    When user says "Hello, Borya"
    Then VA says "Hello"
    When user says edit Унылое место
    Then VA asks "What would you like to change, name or address?"
    When user says "Change name"
    Then VA asks "What is the new name?"
    When User says new name is nothing
    Then VA says 'Can't recognize new name'
