from bubble_sort import bubble_sort

# Тестовые данные
test_cases = [
    ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),
    ([7], [7]),
    ([9,9,9], [9,9,9]),
]

# Проверка
for unsorted_list, expected_sorted_list in test_cases:
  sorted_list = bubble_sort(unsorted_list)
  assert sorted_list == expected_sorted_list, f"Неверный результат сортировки для списка: {unsorted_list}. Ожидалось: {expected_sorted_list}, получено: {sorted_list}"
  print(f"Тест пройден для списка: {unsorted_list}")


print("Все тесты пройдены!")