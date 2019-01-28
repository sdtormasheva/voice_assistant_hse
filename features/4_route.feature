# Created by vadim at 1/23/19
Feature: Route Setup
 Assistant sets up route between two places and tells its duration

 Scenario: Assistant sets up route between two saved places on foot
  Given service is working
  When user says "Hello, Borya"
  Then VA says "Hello"
  When user says Set up route from Пашин дом to Библиотека
  Then VA validates locations
  When VA asks "Which way?"
  And User says go by foot
  Then VA says time
  #  optional
  And user says "Start!"

  Scenario: Assistant sets up route between two saved places, but location(s) does not exist
  Given service is working
  When user says "Hello, Borya"
  Then VA says "Hello"
  When user says Set up route from Пашин дом to Библиотека
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
