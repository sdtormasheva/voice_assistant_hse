# Created by vadim at 1/23/19
Feature: delete saved place
  Deleting place which was saved

  Scenario: User asks to delete saved place, but changes his mind
    Given service is working
    When user says "Hello, Borya"
    Then VA says "Hello"
    When user says delete Библиотека
    Then VA repeats place name and address
    And VA Asks "Delete?"
    When User says "No"
    Then VA says "Cancelled"

  Scenario: User asks to delete saved place and VA removes it from storage
    Given service is working
    When user says "Hello, Borya"
    Then VA says "Hello"
    When user says delete Библиотека
    Then VA repeats place name and address
    And VA Asks "Delete?"
    When User says "Yes"
    Then VA deletes place and says "Deleted"

  Scenario: User asks to delete saved place, but it does not exist
    Given service is working
    When user says "Hello, Borya"
    Then VA says "Hello"
    When user says delete Библиотека
    Then VA says "The place is not found"
