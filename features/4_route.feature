# Created by vadim at 1/23/19
Feature: Route Setup
 Assistant sets up route between two places and tells its duration

 Scenario: Assistant sets up route between two saved places on foot
  Given service is working
  And locations Пашин дом and Библиотека are saved
  When user says "Hello, Borya"
  Then VA says "Hello"
  When user says Set up route from Пашин дом to Библиотека
  Then VA validates locations
  When VA asks "Which way?"
  And User says go by foot
  Then VA says time
  #  optional
  When user gives command to start the route
  Then VA follows the route

  Scenario: Assistant sets up route between two saved places, but location(s) does not exist
  Given service is working
  When user says "Hello, Borya"
  Then VA says "Hello"
  When user says Set up route from Университет to Дом
  Then VA validates locations
  And VA says "Invalid location(s)"

#   Scenario: Assitant set up route between two saved places via car
#    Given service is working
#    When user says "Hello, Borya"
#    Then VA says "Hello"
#    When user says "Set up route from Пашин дом to Библиотека
#    Then VA says Пашин дом to Библиотека. "Which way?"
#    When User says "Car"
#    Then VA says time
#
#   Scenario: Assitant set up route between two saved places via public transport
#    Given service is working
#    When user says "Hello, Borya"
#    Then VA says "Hello"
#    When user says "Set up route from Пашин дом to Библиотека
#    Then VA says Пашин дом to Библиотека. "Which way?"
#    When User says "Public transport"
#    Then VA says time
#
#   Scenario: Assitant set up route between geolocation and place via foot
#    Given service is working
#    When user says "Hello, Borya"
#    Then VA says "Hello"
#    When user says "Set up route to Библиотека
#    Then VA says to Библиотека and "Which way?"
#    When User says "On foot"
#    Then VA says time
#
#   Scenario: Assitant set up route between geolocation and place via car
#    Given service is working
#    When user says "Hello, Borya"
#    Then VA says "Hello"
#    When user says "Set up route to Библиотека
#    Then VA says to Библиотека and "Which way?"
#    When User says "Car"
#    Then VA says time
#
#   Scenario: Assitant set up route between geolocation and place via public transport
#    Given service is working
#    When user says "Hello, Borya"
#    Then VA says "Hello"
#    When user says "Set up route to Библиотека
#    Then VA says to Библиотека and "Which way?"
#    When User says "Public transport"
#    Then VA says time
