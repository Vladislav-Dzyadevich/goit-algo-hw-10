from pulp import LpMaximize, LpProblem, LpVariable

# Ініціалізація моделі
model = LpProblem(name="maximize_production", sense=LpMaximize)

# Визначення змінних рішення
lemonade = LpVariable(name="Lemonade_units", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_juice_units", lowBound=0, cat="Integer")

# Визначення обмежень
# Обмеження ресурсів
water_constraint = 2 * lemonade + fruit_juice <= 100
sugar_constraint = lemonade <= 50
lemon_juice_constraint = lemonade <= 30
fruit_puree_constraint = 2 * fruit_juice <= 40

# Додавання обмежень до моделі
model += water_constraint, "Water_constraint"
model += sugar_constraint, "Sugar_constraint"
model += lemon_juice_constraint, "Lemon_juice_constraint"
model += fruit_puree_constraint, "Fruit_puree_constraint"

# Визначення функції максимізації
model += lemonade + fruit_juice

# Вирішення моделі
model.solve()

# Виведення результатів
print("Status:", model.status)
print("Maximum units of Lemonade to produce:", lemonade.varValue)
print("Maximum units of Fruit Juice to produce:", fruit_juice.varValue)
print("Maximum total units produced:", lemonade.varValue + fruit_juice.varValue)
