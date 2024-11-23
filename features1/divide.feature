Feature: Division

  Scenario: Divide by a non-zero number
    Given I have a number 25
    And I have a divisor 5
    When I divide the number by the divisor
    Then the result should be 5.0

  Scenario: Divide by zero
    Given I have a number 25
    And I have a divisor 0
    When I divide the number by the divisor
    Then an error should be raised
