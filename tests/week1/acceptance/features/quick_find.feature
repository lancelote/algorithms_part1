Feature: Solve algorithm problem
  Program should perform union operations and return correct list of objects

  Scenario: Program execution
    When I run quick union program with "10 9-0 5-6 2-1 2-9 7-9 1-5"
    Then I see a result of "6 6 6 3 4 6 6 6 8 6"