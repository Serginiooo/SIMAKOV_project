warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

print("Материал    Кол-во  Цена     Мин.   Стоимость")
total = 0
max_cost = 0
max_name = ""
critical = []

for name, data in warehouse.items():
    q = data["quantity"]
    p = data["price"]
    m = data["min_quantity"]
    cost = q * p
    total += cost
    if cost > max_cost:
        max_cost = cost
        max_name = name
    if q < m:
        critical.append(name)
    print(f"{name:<10} {q:<6} {p:<8.2f} {m:<6} {cost:<10.2f}")

print(f"\nОбщая стоимость: {total:.2f} руб")
print(f"Самый дорогой: {max_name} ({max_cost:.2f} руб)")
print("Критические остатки:", critical)

material = "Цемент"
amount = 25
if warehouse[material]["quantity"] >= amount:
    warehouse[material]["quantity"] -= amount
    print(f"\nВыдано {amount} {material}")
    print(f"Остаток: {warehouse[material]['quantity']}")
else:
    print("Недостаточно материала")
