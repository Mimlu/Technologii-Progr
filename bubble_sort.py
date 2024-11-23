def bubble_sort(list_):
  n = len(list_)
  for i in range(n-1):
    for j in range(n-i-1):
      if list_[j] > list_[j+1]:
        list_[j], list_[j+1] = list_[j+1], list_[j]
  return list_

my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print("Отсортированный список:", sorted_list)