# Created by vadim at 1/23/19
Feature: Route Setup
  Assistant sets up route between two places and tells destintaion time

  Scenario: Assitant set up route between two saved places via foot
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Set up route from Пашин дом to Библиотека
    And VA says Пашин дом to Библиотека and "Which way?"
    Then User says "On foot"
    And VA says time

   Scenario: Assitant set up route between two saved places via car
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Set up route from Пашин дом to Библиотека
    And VA says Пашин дом to Библиотека. "Which way?"
    Then User says "Car"
    And VA says time

   Scenario: Assitant set up route between two saved places via public transport
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Set up route from Пашин дом to Библиотека
    And VA says Пашин дом to Библиотека. "Which way?"
    Then User says "Public transport"
    And VA says time

   Scenario: Assitant set up route between geolocation and place via foot
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Set up route to Библиотека
    And VA says to Библиотека and "Which way?"
    Then User says "On foot"
    And VA says time

   Scenario: Assitant set up route between geolocation and place via car
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Set up route to Библиотека
    And VA says to Библиотека and "Which way?"
    Then User says "Car"
    And VA says time

   Scenario: Assitant set up route between geolocation and place via public transport
    Given service is working
    When user says "Hello, Borya"
    And VA says "Hello"
    Then user says "Set up route to Библиотека
    And VA says to Библиотека and "Which way?"
    Then User says "Public transport"
    And VA says time
