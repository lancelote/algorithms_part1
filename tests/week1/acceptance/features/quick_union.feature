Feature: Solve Quick Union algorithm problem
  Program should perform union operations and return correct list of objects

  Scenario: Program execution
    When I run quick union program with "10 6-2 0-8 3-2 1-4 3-9 0-4 7-9 8-2 3-5"
    Then I see a result of "6 0 6 6 1 6 6 6 0 6"