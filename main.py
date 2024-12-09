data = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'Анаконда']

# Функція видалення дублікатів
def def_lst_unique(lst):
    lst_unique = []
    lst_in_set = set()
    for item in lst:
        item_lower = item.lower() if isinstance(item, str) else item
        if item_lower not in lst_in_set:
            lst_unique.append(item)
            lst_in_set.add(item_lower)
    return lst_unique

# Функція сортування списку
def def_lst_sort(lst):
    lst_str = sorted([k for k in lst if isinstance(k, str)])
    lst_int = sorted([k for k in lst if isinstance(k, int)])
    return lst_int + lst_str

# Видаляємо дублікати та сортуємо
unique_list = def_lst_unique(data)
sorted_list = def_lst_sort(unique_list)

print(sorted_list)  # Вивід результату






