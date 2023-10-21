money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
tek_sum = money_capital
counter = -1
while (tek_sum > 0):
    counter += 1
    tek_sum = tek_sum - spend + salary
    spend = spend * (1 + increase)
print("Количество месяцев, которое можно протянуть без долгов:", counter)
