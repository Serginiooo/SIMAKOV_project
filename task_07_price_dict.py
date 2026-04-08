# Прайс лист матераилов
# Исходные данные
materials = {
"Кирпич": 432, 
"Бетон": 178, 
"Штукатурка": 6969,
"Металл": 5252,
"Стекло": 7788                                           
}
# Добавление материалов
materials.update({
    "Черепица": 1000,
    "Фарфор": 2000
})
# Измененеие цены
materials["Кирпич"] *= 1.1
materials.pop("Фарфор")
# Расчет средней цены
average = sum(materials.values())/len(materials)
print(materials)
print(average
