# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
money_capital -= spend - salary
while money_capital > 0:
    spend += spend * increase
    money_capital -= spend - salary
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
