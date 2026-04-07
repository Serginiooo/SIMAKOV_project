# Очистка адресов
# Исходные данные
import re

addresses = [
    "  г. Москва, ул. Ленина, д. 10  ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100  "
]
# Создание пустого списка
good_addresses = []
# Редактируем адреса
for address in addresses:
  address_1=address.strip().replace(" ","").replace(".",". ").replace(",",", ")
  good_addresses.append(address_1)
print(f'#1\nДо: {addresses[0]} \nПосле: {good_addresses[0]}')
print(f'#1\nДо: {addresses[0]} \nПосле: {good_addresses[1]}')
print(f'#1\nДо: {addresses[0]} \nПосле: {good_addresses[2]}')
