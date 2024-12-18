Feature: Сортировка пузырьком

  Scenario Outline: Сортировка различных списков
    Given список чисел: <list>
    When я сортирую список пузырьком
    Then отсортированный список должен быть: <sorted_list>

    Examples:
      | list                  | sorted_list           |
      | []                    | []                    |
      | [9]                   | [9]                   |
      | [3, 4, 5, 6, 7]       | [3, 4, 5, 6, 7]        |
      | [5, 1, 3, 2, 8]       | [1, 2, 3, 5, 8]       |
      | [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] | [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9] |
      | [-5, 2, -1, 0, 3]     | [-5, -1, 0, 2, 3]     |