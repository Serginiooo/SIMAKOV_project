spisok1 = ["Кирпич", "Бетон", "Гравий", "Арматура"]
spisok2 = ["Бетон", "Доска", "Гравий", "Черепица"]
spisok3 = ["Кирпич", "Гравий", "Цемент", "Бетон"]

set1 = set(spisok1)
set2 = set(spisok2)
set3 = set(spisok3)

all_unique = set1 | set2 | set3
common_all = set1 & set2 & set3
only_first = set1 - set2 - set3
exactly_two = (set1 & set2) | (set2 & set3) | (set1 & set3) - common_all

print("Уникальные:", sorted(all_unique))
print("Общие для всех:", sorted(common_all))
print("Только у первого:", sorted(only_first))
print("Ровно у двух:", sorted(exactly_two))
