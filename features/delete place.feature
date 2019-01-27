# Created by vadim at 1/23/19
Feature: delete saved place
  Deleting place which was saved

  Scenario: User asks to delete saved place and VA removes it from storage
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Delete Пашин дом"
    And VA says Парусная 17 and Пашин дом and says "Delete?"
    Then User say "Yes"
    And VA says "Deleted"

   Scenario: User asks to delete saved place but changes his mind
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Delete Пашин дом"
    And VA says Парусная 17 and Пашин дом and says "Delete?"
    Then User say "No"
    And VA says "Cancelled"

